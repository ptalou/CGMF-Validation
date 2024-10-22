##
# 
# @mainpage V&V routines for CGMF 
#
#
#



import numpy as numpy
import sys
from CGMFtk import histories as fh

class VV:


	def __init__ (self, fh):


		self.A = fh.A