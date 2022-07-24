# < Mavi Ruh Bakým Tablosu >
#-------------------------------------------------------------------------------|
# NOT : Kodlama > Karakter Takimi > Turkce > ISO 8859-9 yapmadan editlemeyin!!! |
#-------------------------------------------------------------------------------|
import ui, wndMgr, serverInfo
class Bar(ui.Window):
	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterBar(self, layer)
	def SetColor(self, color):
		wndMgr.SetColor(self.hWnd, color)
class Mavi_Ruh_Bakim_Tablosu(ui.BoardWithTitleBar):
	satirsayisi = 5
	maviruh = 0
	servername = serverInfo.SERVER_NAME
	yesilrenkkodu = '|cff00ff00'
	sarirenkkodu = '|cffffff00'
	beyazrenkkodu = '|cFFFFFFFF'

	#------------------------------------------------------ editlenecek alan

	tarih = '01.07.2022'

	gamemaster = '<<{*MaviRuh*}>>'

	text = [
			'Droplar arttýrýldý.',
			'Mavi Ejder aktif edildi.',
			'Metinlerden düþen gereksiz yanglar kaldýrýldý.',
			'Satýcýya cesaret pelerini eklendi.',
			'Temmuz ayý boyunca nesne market ürünlerinde %20 indirim.',
			'Oyma taþý etkinliði sonra erdi.',
			'Depocudan yanglarýnýzý külçe altýnlara dönüþtürebilirsiniz.',
		 ]

	#------------------------------------------------------ editlenecek alan son

	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.isLoaded = FALSE
		if FALSE == self.isLoaded:
			self.__LoadMe()
	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)
	def __LoadMe(self):
		self.SetSize(480, 170)
		self.SetCenterPosition()
		self.AddFlag('movable')
		self.SetTitleName(Mavi_Ruh_Bakim_Tablosu.beyazrenkkodu+"Bakým Notlarý")
		self.SetCloseEvent(self.Close)
		self.isLoaded = TRUE
		self.tarihlar()
		self.aciklamalar()
		self.cubuklar()
#------------------------------------------------------------------------------------------#
	def tarihlar(self):
		self.Tarih_BG = Bar()
		self.Tarih_BG.SetParent(self)
		self.Tarih_BG.SetSize(113, 15)
		self.Tarih_BG.SetPosition(20,40)
		self.Tarih_BG.Show()
#--------------------------------------#
		self.ServerName_BG = Bar()
		self.ServerName_BG.SetParent(self)
		self.ServerName_BG.SetSize(113, 15)
		self.ServerName_BG.SetPosition(160,40)
		self.ServerName_BG.Show()
#--------------------------------------#
		self.GameMaster_BG = Bar()
		self.GameMaster_BG.SetParent(self)
		self.GameMaster_BG.SetSize(116, 15)
		self.GameMaster_BG.SetPosition(300,40)
		self.GameMaster_BG.Show()
#--------------------------------------#
		Tarih = ui.TextLine()
		Tarih.SetParent(self)
		Tarih.SetPosition(23, 40)
		Tarih.SetText(Mavi_Ruh_Bakim_Tablosu.yesilrenkkodu+'Bakým Tarihi: ' +Mavi_Ruh_Bakim_Tablosu.sarirenkkodu+self.tarih)
		Tarih.Show()
		self.Tarih = Tarih
		Tarih.SetWindowHorizontalAlignLeft()
#--------------------------------------#
		ServerName = ui.TextLine()
		ServerName.SetParent(self)
		ServerName.SetPosition(0-76, 40)
		ServerName.SetText(Mavi_Ruh_Bakim_Tablosu.yesilrenkkodu+'Server: '+Mavi_Ruh_Bakim_Tablosu.sarirenkkodu+self.servername)
		ServerName.Show()
		self.ServerName = ServerName
		ServerName.SetWindowHorizontalAlignCenter()
#--------------------------------------#
		GameMaster = ui.TextLine()
		GameMaster.SetParent(self)
		GameMaster.SetPosition(63, 40)
		GameMaster.SetText(Mavi_Ruh_Bakim_Tablosu.yesilrenkkodu+'GM: '+Mavi_Ruh_Bakim_Tablosu.sarirenkkodu+self.gamemaster)
		GameMaster.Show()
		self.GameMaster = GameMaster
		GameMaster.SetWindowHorizontalAlignCenter()
#------------------------------------------------------------------------------------------#
	def aciklamalar(self):
		self.textLines = []
		self.Aciklama_1_BG = Bar()
		self.Aciklama_1_BG.SetColor(0x77000000)
		self.Aciklama_1_BG.SetParent(self)
		self.Aciklama_1_BG.SetSize(420, 85)
		self.Aciklama_1_BG.SetPosition(20,58)
		self.Aciklama_1_BG.Show()
#--------------------------------------#
		for i in range(Mavi_Ruh_Bakim_Tablosu.satirsayisi):
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(23, 63+15*i)
			textLine.SetText(Mavi_Ruh_Bakim_Tablosu.beyazrenkkodu+'- '+self.text[i])
			textLine.Show()
			self.textLines.append(textLine)
#------------------------------------------------------------------------------------------#
	def cubuklar(self):
		scrollBar = ui.ScrollBar()
		scrollBar.SetParent(self)
		scrollBar.SetScrollBarSize(120)
		scrollBar.SetPosition(445,40)
		scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar = scrollBar
		if len(self.text) <= Mavi_Ruh_Bakim_Tablosu.satirsayisi:
			self.scrollBar.Hide()
		else:
			self.scrollBar.Show()
#------------------------------------------------------------------------------------------#
	def __OnScroll(self):
		pos = int(self.scrollBar.GetPos() * (len(self.text) - Mavi_Ruh_Bakim_Tablosu.satirsayisi))
		for i in xrange(Mavi_Ruh_Bakim_Tablosu.satirsayisi):
			self.textLines[i].SetText(Mavi_Ruh_Bakim_Tablosu.beyazrenkkodu+'- '+self.text[i+pos])
#------------------------------------------------------------------------------------------#
	def Open(self):
		self.maviruh = 1
		self.Show()
	def Close(self):
		self.maviruh = 0
		self.Hide()
	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
	def OnPressExitKey(self):
		self.Close()
		return TRUE
