import wx

class MenuBar(wx.MenuBar):

	ID_OPEN = 101
	ID_SAVE = 102
	ID_RELOAD = 99
	ID_CLOSE = 103

	ID_ADD_NODE = 104
	ID_DELETE_NODE = 105

	ID_ADD_KEY = 156
	ID_REMOVE_KEY = 160

	ID_ABOUT = 200
	ID_FAQ = 201
	
	
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

		self.Key = wx.Menu()
		self.Key.Append(self.ID_ADD_KEY, "Add new key", "", wx.ITEM_NORMAL)
		self.Key.Append(self.ID_REMOVE_KEY, "Remove key", "", wx.ITEM_NORMAL)
		self.Append(self.Key, "Key")
		
		self.About = wx.Menu()
		self.Append(self.About, "About")
		self.About.Append(self.ID_ABOUT, "About", "", wx.ITEM_NORMAL)
		self.About.Append(self.ID_FAQ, "FaQ", "", wx.ITEM_NORMAL)

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
	
