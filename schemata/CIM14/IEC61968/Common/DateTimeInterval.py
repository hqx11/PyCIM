# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.Element import Element

class DateTimeInterval(Element):
    """Interval of date and time.
    """

    def __init__(self, end='', start='', **kw_args):
        """Initializes a new 'DateTimeInterval' instance.

        @param end: Date and time that this interval ended. 
        @param start: Date and time that this interval started. 
        """
        #: Date and time that this interval ended.
        self.end = end

        #: Date and time that this interval started.
        self.start = start

        super(DateTimeInterval, self).__init__(**kw_args)
