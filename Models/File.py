#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

'''
	Třída pro práci se soubory, s hive
'''
class File:

	def __init__(self, path):
		self.path = path

	def existsFile(self):

		if os.path.isfile(self.path):
			return True
		else:
			return False	
	'''
		Is this file a regular hive?
	'''
	def isFileHive(self):

		f = open(self.path, "rb")
		try:
			string = f.read(4)
			# first 4 bytes have to be "regf"
			if(string == "regf"):
				return True
			else:
				return False
			
		finally:
			f.close()

			

		
		
