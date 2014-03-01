#!/usr/bin/python

import sys
import os
import wx

sys.path.append(os.path.abspath("Models"))
sys.path.append(os.path.abspath("Views"))

from Models import File
from Models import HivexManager

from Views import MainFrame


'''file = File("DEFAULT")
file.existsFile()
file.isFileHive()


hivex = HivexManager(file)
print hivex.getRootKeys()'''


app = wx.PySimpleApp(0)
frame = MainFrame(None, wx.ID_ANY, "")
app.SetTopWindow(frame)
frame.Show()
app.MainLoop()

print "done"

