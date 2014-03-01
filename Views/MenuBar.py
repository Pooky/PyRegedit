import wx

class MenuBar(wx.MenuBar):

	ID_OPEN = 101
	ID_SAVE = 102
	ID_RELOAD = 99
	ID_CLOSE = 103

	ID_ADD_NODE = 104
	ID_DELETE_NODE = 105
	
	
	def __init__(self, *args, **kwds):
		# begin wxGlade: MenuBar.__init__
		wx.MenuBar.__init__(self, *args, **kwds)

		self.File = wx.Menu()

		self.File.Append(self.ID_OPEN, "Open", "", wx.ITEM_NORMAL)
		self.File.Append(self.ID_SAVE, "Save", "", wx.ITEM_NORMAL)
		self.File.Append(self.ID_RELOAD, "Reload", "", wx.ITEM_NORMAL)
		self.File.Append(self.ID_CLOSE, "Close", "", wx.ITEM_NORMAL)
		
		self.Append(self.File, "Hive")

		self.Node = wx.Menu()

		self.Node.Append(self.ID_ADD_NODE, "Add node", "", wx.ITEM_NORMAL)
		self.Node.Append(self.ID_DELETE_NODE, "Remove node", "", wx.ITEM_NORMAL)
		self.Append(self.Node, "Node")
		
		self.About = wx.Menu()
		self.Append(self.About, "About")

		self.FaQ = wx.Menu()
		self.Append(self.FaQ, "FaQ")

		self.__set_properties()
		self.__do_layout()
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: MenuBar.__set_properties
		pass
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: MenuBar.__do_layout
		pass
		# end wxGlade
	
