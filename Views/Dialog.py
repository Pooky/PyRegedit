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

