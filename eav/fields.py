# -*- coding: utf-8 -*-
#
#    EAV-Django is a reusable Django application which implements EAV data model
#    Copyright © 2009—2010  Andrey Mikhaylenko
#
#    This file is part of EAV-Django.
#
#    EAV-Django is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    EAV-Django is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with EAV-Django.  If not, see <http://gnu.org/licenses/>.
"""
Fields
~~~~~~
"""

# django
from django import forms

# this app
from widgets import RangeWidget


__all__ = ['RangeField']


class RangeField(forms.MultiValueField):
    "A multi-value field which consists of tho float fields."
    widget = RangeWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.FloatField(),
            forms.FloatField(),
        )
        super(RangeField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        return tuple(data_list) or None
