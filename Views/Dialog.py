# -*- coding: UTF-8 -*-
import wx

class AddNodeDialog(wx.Dialog):

    def __init__(self):

		wx.Dialog.__init__(self, None, title="Specify node name", size=(290, 40))

		self.txt = wx.TextCtrl(self)
		btn = wx.Button(self, id=wx.ID_OK, label="Add node")

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(self.txt, 4, wx.LEFT | wx.EXPAND, 0)
		sizer.Add(btn, 2, wx.RIGHT | wx.EXPAND, 0)
		self.SetSizer(sizer)

class AboutDialog():

	description = """PyRegedit is GUI tool which allows users to manipulate with Windows Registry hives.
	This program should be open-source replacement for Windows Regedit32.

	!!! Always carefully make backup before you change in production hive !!!
	"""

	license = """
	PyRegedit opensource alternative for Windows Regedit
    Copyright (C) 2014 Martin Klíma

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    """

	

	def __init__(self):
				
		info = wx.AboutDialogInfo()

		info.SetIcon(wx.Icon('registry-icon.png', wx.BITMAP_TYPE_PNG))
		info.SetName('PyRegedit')
		info.SetLicence(self.license)
		info.SetDescription(self.description)
		info.SetVersion('0.1Beta')
		info.SetCopyright('(C) 2014 Pooky')
		info.SetWebSite('https://github.com/Pooky/PyRegedit')

		wx.AboutBox(info)
