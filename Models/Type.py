class Type:

	NONE = 0  # REG_NONE
	STRING = 1 # REG_SZ
	SYS_STRING = 2 # REG_EXPAND_SZ
	BINARY = 3 # REG_BINARY
	INTEGER = 4 # REG_DWORD
	INTEGER_BIG_ENDIAN = 5 # REG_DWORD_BIG_ENDIAN
	LINK = 6 # REG_LINK
	LIST_STRING = 7 # REG_MULTI_SZ

	def getStringType(self, x):

		if x == self.NONE:
			res = "REG_NONE"
		elif x == self.STRING:
			res = "REG_SZ"
		elif x == self.SYS_STRING:
			res = "REG_EXPAND_SZ"
		elif x == self.BINARY:
			res = "REG_BINARY"
		elif x == self.INTEGER:
			res = "REG_DWORD"
		elif x == self.INTEGER_BIG_ENDIAN:
			res = "REG_DWORD_BIG_ENDIAN"
		elif x == self.LINK:
			res = "REG_LINK"
		elif x == self.LINK:
			res = "LIST_STRING"
		else:
			res = "Unknow"

		return res
	
	
	
