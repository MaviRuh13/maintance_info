''' Arat '''

import musicInfo

# Ekle

import bakim_tablosu

''' Arat '''

		self.__ProcessPreservedServerCommand()

# Ekle

		self.bakim_tablosu = bakim_tablosu.Mavi_Ruh_Bakim_Tablosu()
		self.bakim_tablosu.Close()

''' Arat '''

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())

# Ekle

		self.bakim_tablosu = bakim_tablosu.Mavi_Ruh_Bakim_Tablosu()
		self.bakim_tablosu.Close()

''' Arat '''

		onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)

# Ekle

		onPressKeyDict[app.DIK_F5] 	= lambda : self.__bakim()

# En alta ekle

	def __bakim(self):
		if self.bakim_tablosu.maviruh == 1:
			self.bakim_tablosu.Close()
		else:
			self.bakim_tablosu.Show()

