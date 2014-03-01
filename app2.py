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
		self.openHive("NTUSER.DAT_CHANGED")
	
		# Init handle for TreeView
		self.treeView = self.frame.TreeView
		self.initTreeView()

		# Init handle for ListCtrl
		self.lc = self.frame.lc
		self.frame.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, self.lc)

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
		Kliknutí na sloupec
	'''
	def OnColClick(self, event):
		event.Skip()
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

		dlg = wx.MessageDialog(None, 'Are you sure to delete this node? And all his subnodes!', 'Are you shure?', 
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
			event.Skip()
		
	def OnActivatedItem(self, event):

		self.setStatusBarText("Item Activated")
		self.lc.DeleteAllItems()
		
		item = event.GetItem()
		if not item.IsOk():
			item = self.treeView.GetSelection()
		
		keyId = self.treeView.GetItemData(item).GetData()[0]
		rows = self.hivex.getValues(keyId)
		
		for i, val in enumerate(rows):
			index = self.lc.InsertStringItem(i, val[0])
			self.lc.SetStringItem(index, 1, val[1])
			self.lc.SetStringItem(index, 2, val[2])
			
		
		

controller = Controller()
controller.initApp() # Init app

