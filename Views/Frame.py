#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import sys

'''
	Hlavní frame celé aplikace
'''
class MainFrame(wx.Frame):
	
	def __init__(self, *args, **kwds):
		# begin wxGlade: MyFrame2.__init__
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		
		self.TreeView = wx.TreeCtrl(self, wx.ID_ANY, style = wx.TR_HAS_BUTTONS | wx.TR_DEFAULT_STYLE | wx.SUNKEN_BORDER)

		self.lc = wx.ListCtrl(self, -1, style=wx.LC_REPORT)

		self.lc.InsertColumn(0, 'Key name')
		self.lc.InsertColumn(1, 'Type')
		self.lc.InsertColumn(2, 'Value')

		# status bar
		self.sb = self.CreateStatusBar() 
		
		self.__set_properties()
		self.__do_layout()
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: MyFrame2.__set_properties
		self.SetTitle("PyRegedit")
		self.SetSize((800, 600))

		self.lc.SetColumnWidth(0, 130)
		self.lc.SetColumnWidth(1, 130)
		self.lc.SetColumnWidth(2, 260)

		#self.TreeView.SetSize((250, 400))
		
		#self.panel_3.SetMinSize((700, 600))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: MyFrame2.__do_layout
		sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_4.Add(self.TreeView, 1, wx.EXPAND, 0)
		sizer_4.Add(self.lc, 2, wx.EXPAND, 0)
		self.SetSizer(sizer_4)
		self.Layout()
		# end wxGlade
'''
	Editace zvoleného klíče
'''
class EditFrame(wx.Frame):
	
	def __init__(self):
		# begin wxGlade: EditFrame.__init__
		
		wx.Frame.__init__(self, None)
		
		self.label_1 = wx.StaticText(self, wx.ID_ANY, "Key name:")
		self.key_name = wx.TextCtrl(self, wx.ID_ANY, "")
		self.key_value = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE)
		self.btn_save = wx.Button(self, wx.ID_ANY, "Save")
		self.btn_cancel = wx.Button(self, wx.ID_ANY, "Cancel")

		self.key_name.Enable(False)
		self.key_value.SetValue(hex(2500))

		self.__set_properties()
		self.__do_layout()
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: EditFrame.__set_properties
		self.SetTitle("Editing...")
		self.key_value.SetMinSize((400, 200))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: EditFrame.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.BoxSizer(wx.VERTICAL)
		sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_3.Add(self.label_1, 0, wx.TOP, 8)
		sizer_3.Add(self.key_name, 1, wx.LEFT | wx.EXPAND, 15)
		sizer_2.Add(sizer_3, 1, wx.BOTTOM | wx.EXPAND, 20)
		sizer_2.Add(self.key_value, 0, 0, 0)
		sizer_4.Add(self.btn_save, 0, 0, 0)
		sizer_4.Add(self.btn_cancel, 0, 0, 0)
		sizer_2.Add(sizer_4, 1, wx.TOP | wx.ALIGN_RIGHT, 20)
		sizer_1.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 50)
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)
		self.Layout()
		# end wxGlade

