#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import hivex
from Models import Type
import struct


'''
# Use hivex to pull out a registry key.
h = hivex.Hivex("ntuser.dat")


root = h.root()
children = h.node_children(root);
for child in children:

	name = h.node_name(child);
	print "Name :", name

	key = h.node_get_child(child, name)
	values = h.node_values(child)
	print values
'''	
	
h = hivex.Hivex ("Data/NTUSER.DAT_CHANGED", write=True)
#h = hivex.Hivex ("DEFAULT")

typ = Type()
root = h.root ()
key = h.node_get_child (root, "Environment")

#for child in h.node_children(root):
	
#name = h.node_name(child);
#print name
'''
	Test string
'''
value = "čeština"
value = value.decode("utf-8").encode("utf-16le")

value1 = { "key": "Key3", "t": Type.STRING, "value": value }
h.node_set_value(key, value1)

'''
	Test int
'''
#value = 150
value = struct.unpack("<h", "150")

value1 = { "key": "Key3", "t": Type.INTEGER, "value": value }
h.node_set_value(key, value1)

for value in h.node_values(key):
	keyName =  h.value_key(value)
	
	#print h.node_name(value)
	val = h.node_get_value(key, keyName)
	valType = h.value_type(val)[0]

	#print valType
	if(valType == Type.STRING):
		value2 = h.value_string(val)
		
	else:
		print typ.getStringType(valType)
		value2 = h.value_value(val)[1]
		value2 = value2.decode('utf-16le').encode('utf-8')


	print "\t %s --> %s" % (keyName, value2)

'''
h.node_add_child (root, "D")
b = h.node_get_child (root, "D")

values = [
    { "key": "Key1", "t": 3, "value": "ABC" },
    { "key": "Key2", "t": 3, "value": "DEF" }
]
h.node_set_values (b, values)

value1 = { "key": "Key3", "t": 3, "value": "GHI" }
h.node_set_value (b, value1)
string = "JKL".decode('utf-8').encode('utf-16le')

value1 = { "key": "Key1", "t": 1, "value": string } ## T = typ záznamu t: 1 = string, t: 3 = binary
h.node_set_value (b, value1)

h.commit("NTUSER.DAT_CHANGED2")


		
#children = h.node_children(key)
#key = h.node_get_child (key, "Microsoft")
#key = h.node_get_child (key, "Internet Explorer")
#key = h.node_get_child (key, "MenuExt")

#for child in h.node_children(key):
#	print h.node_name(child)

#values = h.node_values(key)
#print values

for child in children:

	
	name = h.node_name(child);
	print "ID: %s, Name: %s" % (child, name)

	key = h.node_get_child(child, name)
	values = h.node_values(child)
	print values

val = h.node_get_value (key, "Start Page")
start_page = h.value_value (val)
#print start_page

# The registry key is encoded as UTF-16LE, so reencode it.
start_page = start_page[1].decode ('utf-16le').encode ('utf-8')

print "User %s's IE home page is %s" % (username, start_page)
'''
