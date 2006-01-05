#!/usr/bin/python

"""
  Author:     Martin Matusiak <numerodix@gmail.com>
  Program:    Creates static HTML album pages and images pages recursively
  Date:       Dec. 19, 2005

  This file is subject to the GNU General Public License (GPL)
  (http://www.gnu.org/copyleft/gpl.html)
"""


import sys
import imagetest
import blackboxtest

verbose = 1
if len(sys.argv) > 1 and sys.argv[1] == "-v":
	verbose = 2
sys.argv = sys.argv[:1]

imagetest.run(verbose)
blackboxtest.run(verbose)