# django-bootstrap-daterangepicker

This is Django form field wrapper for [bootstrap-daterangepicker](http://www.daterangepicker.com/), for use with Bootstrap 3 and 4.

This module allows for: single date pickers, date range selectors and datetime range selectors.

Ranges are returned as tuples of format `(start, end)`, where `start` and `end` are datetime.date or datetime.datetime objects depending on the field type.

The DateField is a replacement for Django's built-in `forms.DateField`, with the only difference being that it accepts an optional `clearable` parameter, and the default widget is the DatePickerWidget specified in this module. 

# Installation
1. `pip install django-bootstrap-daterangepicker`
2. Add `'bootstrap_daterangepicker'` to your `INSTALLED_APPS`
3. Add the resource links required for [bootstrap-daterangepicker](http://www.daterangepicker.com/) into the `<head>`  of the relevant HTML files

## Example usage
```python
from django import forms
from bootstrap_daterangepicker import widgets, fields


class DemoForm(forms.Form):
    # Date Picker Fields
    date_single_normal = fields.DateField()
    date_single_with_format = fields.DateField(
        input_formats=['%d/%m/%Y'],
        widget=widgets.DatePickerWidget(
            format='%d/%m/%Y'
        )
    )
    date_single_clearable = fields.DateField(clearable=True)

    # Date Range Fields
    date_range_normal = fields.DateRangeField()
    date_range_with_format = fields.DateRangeField(
        input_formats=['%d/%m/%Y'],
        widget=widgets.DateRangeWidget(
            format='%d/%m/%Y'
        )
    )
    date_range_clearable = fields.DateRangeField(clearable=True)

    # DateTime Range Fields
    datetime_range_normal = fields.DateTimeRangeField()
    datetime_range_with_format = fields.DateTimeRangeField(
        input_formats=['%d/%m/%Y (%I:%M:%S)'],
        widget=widgets.DateTimeRangeWidget(
            format='%d/%m/%Y (%I:%M:%S)'
        )
    )
    datetime_range_clearable = fields.DateTimeRangeField(clearable=True)
```

### Requirements
* [Bootstrap](http://getbootstrap.com/) >= 3
* [jQuery](http://www.jquery.com/) >= 1
* [Moment.js](http://momentjs.com/) >= 2.10.6
* [bootstrap-daterangepicker](http://www.daterangepicker.com/) >= 2
* [Django](https://www.djangoproject.com/) >= 1.8

