#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import hivex
import hashlib
from Type import Type

'''
	Třída pro komunikaci s knihovnou hivex
'''
class HivexManager:

	

	def __init__(self, hive, debug = False):

		self.h = hivex.Hivex(hive.path, write=True, debug=debug)

	'''
		Vrácení prvního levelu root klíčů hive
	'''
	def getRootKeys(self):
			
		root = self.h.root()
		return self.getKeyChildren(root)
	
	'''
		Vrácení dětí daného klíče
	'''
	def getKeyChildren(self, key):
	
		root = key
		children = self.h.node_children(root);

		keys = []
		
		for child in children:

			name = self.h.node_name(child)
			subChildren = 0
			#self.h.node_get_child(child, name)
			subChildren = self.h.node_children(child)
			
			hasChildren = False
			if(len(subChildren) > 0):
				hasChildren = True

			keys.append([name, hasChildren, child])

		return keys		
				
	def getValues(self, key):

		typ = Type()
		
		res = []
	
		values = self.h.node_values(key)
		for value in values:
			
			keyName = self.h.value_key(value)

			#print h.node_name(value)
			val = self.h.node_get_value(key, keyName)
			valType = self.h.value_type(val)[0]

			value2 = self.getIntepretation(valType, val)
			stringType = typ.getStringType(valType)

			res.append([keyName, stringType, value2])
			#print "\t %s --> %s" % (keyName, value2)

		return res
	
	def addChild(self, key, new_node):
		
		return self.h.node_add_child(key, new_node)

	def removeChild(self, key):

		return self.h.node_delete_child(key)

	def close(self):

		return self.h.close()

	'''
		Display format for others
	'''
	def getIntepretation(self, val_type, val):

		if val_type == Type.STRING:
			res = self.h.value_string(val)
		elif val_type == Type.SYS_STRING:
			res = self.h.value_string(val)
		elif val_type == Type.BINARY:
			res = hex(self.h.value_value(val)[1])
		elif val_type == Type.INTEGER:
			res = self.h.value_dword(val)
		elif val_type == Type.INTEGER_BIG_ENDIAN:
			res = self.h.value_value(val)[1].decode('utf-16be').encode('utf-8') # no nevím
		elif val_type == Type.LINK:
			res = self.h.value_string(val)
		elif val_type == Type.LIST_STRING:
			res = self.h.value_multiple_strings(val)
		else:
			res = self.h.value_value(val)[1].decode('utf-16be').encode('utf-8') # no nevím
		
		return str(res)
