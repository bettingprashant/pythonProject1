from abc import ABC, abstractmethod


class ExcelReader(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(Browser):

    def startBrowser(self):
        print("Started")

    def stopBrowser(self):
        print("stopped")

    def readFromExcel(self):
        print("readfromexcel is ready")
    def runTC(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()


tc1 = TC1()
tc1.runTC()