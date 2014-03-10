#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Type:

	NONE = 0  # REG_NONE
	STRING = 1 # REG_SZ
	SYS_STRING = 2 # REG_EXPAND_SZ
	BINARY = 3 # REG_BINARY
	'''
		32 bit, little endian integer
	'''
	INTEGER = 4 # REG_DWORD
	'''
		Integer with big endian
	'''
	INTEGER_BIG_ENDIAN = 5 # REG_DWORD_BIG_ENDIAN
	'''
		A symbolic link, stored as a UTF-16 little endian string
	'''
	LINK = 6 # REG_LINK
	'''
		A list of UTF-16 little endian strings. Each string is NUL (“ \x00\x00 ”) terminated,
		and the list itself is NUL terminated as well (resulting in a total of four 0-bytes at the end ofthe data).
	'''
	LIST_STRING = 7 # REG_MULTI_SZ
	'''
		64 bit, little endian integer
	'''
	INTEGER_64 = 8 # REG_QWORD 
	TYPES = ["REG_NONE", "REG_SZ", "REG_EXPAND_SZ", "REG_BINARY", "REG_DWORD", "REG_DWORD_BIG_ENDIAN", "REG_LINK", "REG_MULTI_SZ", "REG_QWORD"]

	def getStringType(self, x):

		if x == self.NONE:
			res = "REG_NONE"
		elif x == self.STRING:
			res = "REG_SZ"
		elif x == self.SYS_STRING:
			res = "REG_EXPAND_SZ"
		elif x == self.BINARY:
			res = "REG_BINARY"
		elif x == self.INTEGER:
			res = "REG_DWORD"
		elif x == self.INTEGER_BIG_ENDIAN:
			res = "REG_DWORD_BIG_ENDIAN"
		elif x == self.LINK:
			res = "REG_LINK"
		elif x == self.LIST_STRING:
			res = "REG_MULTI_SZ"
		else:
			res = "Unknow"

		return res

		 

