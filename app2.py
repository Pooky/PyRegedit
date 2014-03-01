#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import wx

sys.path.append(os.path.abspath("Models"))
sys.path.append(os.path.abspath("Views"))

from Models import File
from Models import HivexManager
from Views import *

class Controller:
	
	def initApp(self):

		self.app = wx.PySimpleApp(0)
		self.frame = MainFrame(None, wx.ID_ANY, "")
		self.app.SetTopWindow(self.frame)

		# Init menu bar
		self.menuBar = MenuBar()
		self.frame.SetMenuBar(self.menuBar)
		self.initMenuBar()

		self.hivex = None
		self.ef = None
		self.openHive("NTUSER.DAT_CHANGED")

		# Init handle for TreeView
		self.treeView = self.frame.TreeView
		self.initTreeView()

		# Init handle for ListCtrl
		self.lc = self.frame.lc
		self.frame.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClick, self.lc)

		self.frame.Show()
		self.app.MainLoop()

	def getFrame(self):
		
		return self.frame;

	def setStatusBarText(self, text):
		self.frame.sb.SetStatusText(text)

	def openHive(self, path):
		
		self.hive = File(path)
		if(not self.hive.existsFile()):
			 wx.MessageBox('File not found!', 'Error', wx.OK | wx.ICON_ERROR)
			 return False			
		if(not self.hive.isFileHive()):
			 wx.MessageBox('File is not valid hive!', 'Error', wx.OK | wx.ICON_ERROR)
			 return False
			 
		self.hivex = HivexManager(self.hive);
		self.setStatusBarText("Hive opened: " + path)
		
	'''
		Click on selected key -> value
	'''
	def OnClick(self, event):
		
		if self.ef != None: 
			return False
			
		item = event.GetItem()
		node = item.GetData() # parent node of this key
		keyName = item.GetText() # name of key

		value = self.hivex.getValue(node, keyName)

		# Create frame for editing value
		self.ef = EditFrame()

		self.ef.Bind(wx.EVT_BUTTON, self.OnSaveClick, self.ef.btn_save)
		self.ef.Bind(wx.EVT_BUTTON, self.OnCancelClick, self.ef.btn_cancel)

		self.ef.key_name.SetValue(keyName)
		self.ef.key_value.SetValue(value[0])

		self.ef.Show()

		# save values for saving
		self.editingValue = { "key" : keyName, "t": value[1], "value" : value[0] }
		self.editingNode = node
		
	'''
		Saving value back to key
	'''
	def OnSaveClick(self, event):

		value = self.editingValue
		new_value = self.ef.key_value.GetValue()
		
		# reconvert
		value["value"] = self.hivex.getIntepretationBack(value["t"], new_value)
		print "saving", value
		self.hivex.setValue(self.editingNode, value)

		self.reloadKeyView(self.editingNode)
		self.ef.Destroy()
		self.ef = None
		self.editingNode = None
		self.editingValue = None

		self.setStatusBarText("Key was saved")

	def OnCancelClick(self, event):
		self.ef.Destroy()
		self.ef = None
	
	'''
		Menu Bar
	'''
	def initMenuBar(self):
		
		self.frame.Bind(wx.EVT_MENU, self.menuOpen, id=self.menuBar.ID_OPEN)
		self.frame.Bind(wx.EVT_MENU, self.menuClose, id=self.menuBar.ID_CLOSE)
		self.frame.Bind(wx.EVT_MENU, self.menuSave, id=self.menuBar.ID_SAVE)
		self.frame.Bind(wx.EVT_MENU, self.menuReload, id=self.menuBar.ID_RELOAD)
		self.frame.Bind(wx.EVT_MENU, self.menuAddNode, id=self.menuBar.ID_ADD_NODE)
		self.frame.Bind(wx.EVT_MENU, self.menuDeleteNode, id=self.menuBar.ID_DELETE_NODE)

	def menuOpen(self, event):
		
		self.dirname = ""
			
		dlg = wx.FileDialog(self.frame, "Choose a hive", self.dirname, "", "*", wx.OPEN)
		
		if dlg.ShowModal() == wx.ID_OK:
			
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			self.full_path = os.path.join(self.dirname, self.filename)
			print self.full_path # test
			self.openHive(self.full_path)
			self.reloadTreeView()

		dlg.Destroy()
		
	def menuReload(self, event):
		self.reloadTreeView()
		
	def menuClose(self, event):
		self.treeView.DeleteAllItems()
		del self.hivex
		self.hivex = None
		
	def menuSave(self, event):
		 #self.hivex.commit()
		 event.Skip()
	'''
		Add new node to hive
	'''
	def menuAddNode(self, event):

		dlg = AddNodeDialog()
		if dlg.ShowModal() == wx.ID_OK:
			
			new_node = dlg.txt.GetValue()
			item = self.treeView.GetSelection()
			keyId = self.treeView.GetItemData(item).GetData()[0]
			newId =  self.hivex.addChild(keyId, new_node)

			self.treeView.SetItemData(item, wx.TreeItemData([keyId, True]))  # update expand
			self.treeView.AppendItem(item, new_node, data=wx.TreeItemData([newId, False])) 

			self.setStatusBarText("Node was added")
			
		dlg.Destroy()
		
	def menuDeleteNode(self, event):

		dlg = wx.MessageDialog(None, 'Are you sure to delete this node? And all his subnodes!', 'Are you sure?', 
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		if dlg.ShowModal() == wx.ID_YES:

			item = self.treeView.GetSelection()
			keyId = self.treeView.GetItemData(item).GetData()[0]

			self.hivex.removeChild(keyId)
			self.treeView.Delete(item)

			self.setStatusBarText("Node was deleted")

	'''
		Tree View
	'''
	def initTreeView(self):

		# Bind for collapse and uncollapse
		self.treeView.Bind(wx.EVT_TREE_ITEM_EXPANDING, self.OnExpandItem)
		self.treeView.Bind(wx.EVT_TREE_ITEM_COLLAPSING, self.OnCollapseItem)	
		self.treeView.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivatedItem)

		self.reloadTreeView()
	
	def reloadTreeView(self):

		self.treeView.DeleteAllItems()
		root = self.treeView.AddRoot("My Computer", data=wx.TreeItemData([0, True]))

		if(self.hivex != None):
			# Top levels keys
			for key in self.hivex.getRootKeys():
				temp = self.treeView.AppendItem(root, key[0], data=wx.TreeItemData([key[2], False]))
				if(key[1] == True):
					self.treeView.SetItemHasChildren(temp)		
		
	
	def OnExpandItem(self, event):
		
		item = event.GetItem()
		if not item.IsOk():
			item = self.treeView.GetSelection()
		
		itemData = self.treeView.GetItemData(item).GetData()

		keyId = itemData[0]
		expand = itemData[1]

		name = self.treeView.GetItemText(item)

		# Byl už tento klíč rozbalen? 
		if(expand == False):
			# Top levels keys
			for key in self.hivex.getKeyChildren(keyId):
				temp = self.treeView.AppendItem(item, key[0], data=wx.TreeItemData([key[2], False]))
				if(key[1] == True):
					self.treeView.SetItemHasChildren(temp)

			# Expand -> TRUE
			self.treeView.SetItemData(item, wx.TreeItemData([keyId, True])) 
			
	
		
		#print "data: %i, name: %" % (data, name)
		
	def OnCollapseItem(self, event):
		print "collapse"

	'''
		Click on item and write his key -> values
	'''
	def OnActivatedItem(self, event):

		self.setStatusBarText("Item Activated")
		
		item = event.GetItem()
		if not item.IsOk():
			item = self.treeView.GetSelection()
		
		keyId = self.treeView.GetItemData(item).GetData()[0]
		if not keyId:
			return False

		self.reloadKeyView(keyId)
			
	'''
		Reload view of values
	'''
	def reloadKeyView(self, keyId):

		self.lc.DeleteAllItems()
		rows = self.hivex.getValues(keyId)
		
		for i, val in enumerate(rows):
			
			index = self.lc.InsertStringItem(i, val[0])
			self.lc.SetStringItem(index, 1, val[1])
			self.lc.SetStringItem(index, 2, val[2])

			self.lc.SetItemData(index, keyId)
		

controller = Controller()
controller.initApp() # Init app

