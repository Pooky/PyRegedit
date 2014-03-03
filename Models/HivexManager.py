#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import hivex
import hashlib
import binascii
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
				
	def getValues(self, node):

		typ = Type()
		
		res = []
	
		values = self.h.node_values(node)
		for value in values:
			
			keyName = self.h.value_key(value)

			#print h.node_name(value)
			val = self.h.node_get_value(node, keyName)
			valType = self.h.value_type(val)[0]

			value2 = self.getStringIntepretation(valType, val)
			stringType = typ.getStringType(valType)

			res.append([keyName, stringType, value2])
			#print "\t %s --> %s" % (keyName, value2)

		res = sorted(res, key=lambda x: x[0])
		return res
	'''
		Delete one key
		- we have to get all and exclude only the one and then save it again.
	'''
	def deleteKey(self, node, key):

		values = self.h.node_values(node)
		new_values = []

		for value in values:
			keyName = self.h.value_key(value)

			if(keyName == key):
				continue

			val = self.h.node_get_value(node, keyName)
			valType = self.h.value_type(val)[0]

			value2 = self.h.value_value(val)[1]
			
			valObject = { "key": keyName, "t": int(valType), "value": value2 }
			new_values.append(valObject)

		print node, new_values
		self.h.node_set_values(node, new_values)
	
	def saveChanges(self, path):
		self.h.commit(path)
		
		
	def getValue(self, node, keyName):
		
		val = self.h.node_get_value(node, keyName)
		valType = self.h.value_type(val)[0]

		editableValue = self.getStringIntepretation(valType, val, True)
			
		#print valType, val
		return [editableValue, valType]
		
	def setValue(self, node, value):

		print value
		return self.h.node_set_value(node, value)
		
	def addChild(self, key, new_node):
		
		return self.h.node_add_child(key, new_node)

	def removeChild(self, key):

		return self.h.node_delete_child(key)
		
	def getRoot(self):
		return self.h.root()
	
	def close(self):

		return self.h.close()

	'''
		Display format value -> readable string
	'''
	def getStringIntepretation(self, val_type, val, edit = False):

		if val_type == Type.STRING:
			result = str(self.h.value_string(val))
		elif val_type == Type.INTEGER:
			result = str(self.h.value_dword(val))
		elif val_type == Type.INTEGER_64:
			result = str(self.h.value_dword(val))
		elif val_type == Type.SYS_STRING:
			result = str(self.h.value_string(val))
		elif val_type == Type.LIST_STRING:
			
			result = self.h.value_multiple_strings(val)
			if not edit:
				result = str(result)
			else:
				result = '\n'.join(result)
			
		elif val_type == Type.BINARY:
			result = self.h.value_value(val)[1] # Result is in hexadecimal
			if not edit:
				result = '0x' + ''.join(['%x' % ord(x) for x in result]) # překodování
			else:
				result = ''.join(['%x' % ord(x) for x in result]) # překodování
		else:
			#print typ.getStringType(val_type)
			result = self.h.value_value(val)[1]
			result = result.decode('utf-16le').encode('utf-8')
		
		return result
	'''
		Interpreatce v realnem formatu pro python
	'''
	def getRealIntepretation(self, val_type, val):

		if val_type == Type.STRING:
			result = str(self.h.value_string(val))
		elif val_type == Type.INTEGER:
			result = int(self.h.value_dword(val))
		elif val_type == Type.INTEGER_64:
			result = int(self.h.value_dword(val))
		elif val_type == Type.SYS_STRING:
			result = str(self.h.value_string(val))
		elif val_type == Type.LIST_STRING:
			result = self.h.value_multiple_strings(val)
		elif val_type == Type.BINARY:
			result = self.h.value_value(val)[1] # Result is in hexadecimal
			#result = ' '.join(['%x' % ord(x) for x in result]) # překodování
		else:
			#print typ.getStringType(val_type)
			result = self.h.value_value(val)[1]
		
		return result

	'''
		Return format for save string -> value
	'''
	def getIntepretationBack(self, val_type, val):

		if val_type == Type.BINARY:
			res = self.hextobin(val)
		elif val_type == Type.INTEGER_BIG_ENDIAN:
			res = long(val)
		elif val_type == Type.INTEGER:
			res = long(val)
		else:
			res = val.decode("utf-8").encode("utf-16le")

		print res
		
		return res

	def hextobin(self, hexval):
		'''
		Takes a string representation of hex data with
		arbitrary length and converts to string representation
		of binary.  Includes padding 0s
		author: hbdgaf
		'''
		thelen = len(hexval)*4
		binval = bin(int(hexval, 16))[2:]
		while ((len(binval)) < thelen):
			binval = '0' + binval
		return binval
