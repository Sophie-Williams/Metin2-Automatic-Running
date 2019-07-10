## 1.) Find this:
		onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)

## 2.) Add after this:
		if (app.ENABLE_AUTO_RUNING):
			onPressKeyDict[app.DIK_F5]			= lambda : self.PressAutoRun()

## 1.) Find this:
	def __PressNumKey(self,num):

## 2.) Add before this:
	if (app.ENABLE_AUTO_RUNING):
		def PressAutoRun(self):
			if constInfo.AUTO_RUNING == 0:
				constInfo.AUTO_RUNING = 1
				player.SetSingleDIKKeyState(app.DIK_UP, True)
				self.SendSystemChat(localeInfo.AUTO_RUNING_ACTIVE)
			else:
				constInfo.AUTO_RUNING = 0
				player.SetSingleDIKKeyState(app.DIK_UP, False)
				self.SendSystemChat(localeInfo.AUTO_RUNING_DEACTIVE)

		def SendSystemChat(self, text):
			ColorAndText = "|cffffcc00|H|h[Auto Runing]:|cFF6BD2FF|H|h"
			chat.AppendChat(chat.CHAT_TYPE_INFO, ColorAndText+str(text))