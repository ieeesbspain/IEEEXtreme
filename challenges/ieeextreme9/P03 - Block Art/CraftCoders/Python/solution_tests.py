#!/bin/python
# -*- coding: utf-8 -*-
############################################################################
#  Copyright (C) 2015 Benito Palacios Sánchez                              #
#                                                                          #
#  This program is free software: you can redistribute it and/or modcify   #
#  it under the terms of the GNU General Public License as published by    #
#  the Free Software Foundation, either version 2 of the License, or       #
#  (at your option) any later version.                                     #
#                                                                          #
#  This program is distributed in the hope that it will be useful,         #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the            #
#  GNU General Public License for more details.                            #
#                                                                          #
#  You should have received a copy of the GNU General Public License       #
#  along with this program. If not, see <http://www.gnu.org/licenses/>.    #
############################################################################
import unittest

# Import IEEEXtreme test framework
from importlib.machinery import SourceFileLoader
xtremetests = SourceFileLoader(
    "xtremetests", "../../../TestProblem/Python/xtremetests.py").load_module()


class SolutionTest(xtremetests.ProgramTest):
    pass


if __name__ == '__main__':
    # Set the program path
    xtremetests.PROGRAM = 'solution.py'

    unittest.main()
