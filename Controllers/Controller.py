#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx


class Controller:

	def initApp(self):
		
		self.app = wx.PySimpleApp(0)
		self.frame = MainFrame(None, wx.ID_ANY, "")
		self.app.SetTopWindow(frame)
		self.frame.Show()
		app.MainLoop()


		
