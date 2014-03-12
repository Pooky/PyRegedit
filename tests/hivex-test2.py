#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import struct
import hivex

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
		alias 32 bit, little endian integer
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

'''
	Return format for save string -> value
'''
def transform(val_type, val):

	val = val.strip() # remove whitespace
	if val_type == Type.BINARY:
		res = hextobin(val)
	elif val_type == Type.INTEGER_BIG_ENDIAN:
		res = struct.pack(">I", int(val))
	elif val_type == Type.INTEGER:
		res = struct.pack("<I", int(val))
	elif val_type == Type.LIST_STRING:

		res = ""
		for x in val.split('\n'):
			res += x.decode('utf-8').encode('utf-16le')
			res += "\x00\x00"
		res += "\x00\x00"
	elif val_type == Type.NONE:
		res = val
	else:
		res = val.decode("utf-8").encode("utf-16le")

	return res
	
def hextobin(value):

	try:
		res = int(value, 16)
		res = res.decode('hex')
	except Exception:
		res = value # its a string

	return res

h = hivex.Hivex ("NTUSER.DAT", write=True)

root = h.root ()
node = h.node_get_child (root, "Keys")

values = [
    { "key": "TEST_BINARY(ABC)", "t": Type.BINARY, "value": transform(Type.BINARY,"ABC") }, # How transform this to save it as Binary value?
    { "key": "TEST_BINARY(A5C5)", "t": Type.BINARY, "value": transform(Type.BINARY, "a5c5") }, # How transform this to save it as Binary value?
    #{ "key": "TEST_NONE(00001)", "t": Type.NONE, "value":  transform(Type.NONE, "00001")},
    { "key": "TEST_DWORD(15)", "t": Type.INTEGER, "value":  transform(Type.INTEGER, "15")},
    { "key": "TEST_MULTISTRING", "t": Type.LIST_STRING, "value": transform(Type.LIST_STRING, "IT\nIS\nGOOD")},
]
h.node_set_values(node, values)
h.commit("KEYS_TEST")


