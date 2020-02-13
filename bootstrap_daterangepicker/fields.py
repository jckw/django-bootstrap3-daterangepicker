import six

from datetime import date, datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.encoding import force_text
from django.utils.text import format_lazy, gettext_lazy as _

from .widgets import DateRangeWidget, DateTimeRangeWidget, DatePickerWidget


class DateRangeMixin(object):
    # These values, if given to validate(), will trigger the self.required check.
    empty_values = (None, '', [], (), {}, (None, None), [None, None])

    def __init__(self, type_, *args, **kwargs):
        super(DateRangeMixin, self).__init__(*args, **kwargs)
        self.type_ = type_

    def to_python(self, value):
        if value is None:
            return None, None

        # if we already have a tuple/list of dates just return them
        try:
            beginning, end = value
            if isinstance(beginning, self.type_) and isinstance(end, self.type_):
                return beginning, end
        except (ValueError, TypeError):
            pass

        # Try to coerce the value to unicode.
        unicode_value = force_text(value, strings_only=True)
        if isinstance(unicode_value, six.text_type):
            value = unicode_value.strip()
        else:
            raise ValidationError(_("Date range value: " + str(value) + " was not able to be converted to unicode."))

        if self.widget.clearable():
            if value.strip() == '':
                return None, None

        if self.widget.separator in value:
            str_dates = value.split(self.widget.separator, 2)

            try:
                beginning = super().to_python(str_dates[0])
            except ValidationError as e:
                raise ValidationError(format_lazy('Error in period beginning: {}', e.message), e.code)

            try:
                end = super().to_python(str_dates[1])
            except ValidationError as e:
                raise ValidationError(format_lazy('Error in period end: {}', e.message), e.code)

            return beginning, end
        else:
            raise ValidationError(_("Invalid date range format."), code='invalid')


class DateRangeField(DateRangeMixin, forms.DateField):
    widget = DateRangeWidget

    def __init__(self, clearable=False, *args, **kwargs):
        super().__init__(type_=date, *args, **kwargs)
        self.widget.clearable_override = clearable


class DateTimeRangeField(DateRangeMixin, forms.DateTimeField):
    widget = DateTimeRangeWidget

    def __init__(self, clearable=False, *args, **kwargs):
        super().__init__(type_=datetime, *args, **kwargs)
        self.widget.clearable_override = clearable


class DateField(forms.DateField):
    widget = DatePickerWidget

    def __init__(self, clearable=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget.clearable_override = clearable
