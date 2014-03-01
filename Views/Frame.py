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

		index = self.lc.InsertStringItem(2, "test")
		self.lc.SetStringItem(index, 1, "test2")
		self.lc.SetStringItem(index, 2, "test3")
		
		# status bar
		self.sb = self.CreateStatusBar() 
		
		self.__set_properties()
		self.__do_layout()
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: MyFrame2.__set_properties
		self.SetTitle("PyRegEdit")
		self.SetSize((800, 600))

		self.lc.SetColumnWidth(0, 130)
		self.lc.SetColumnWidth(1, 130)
		self.lc.SetColumnWidth(2, 140)

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
