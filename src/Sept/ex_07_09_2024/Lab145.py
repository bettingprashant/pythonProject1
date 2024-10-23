class ExcelReader:
    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class MySQLDBConnection:
    @staticmethod
    def readMYSQLfile():
        print("Reading from MYSQL")

class TC1():
    def runTC(self):
        ExcelReader().readExcelFile()
        MySQLDBConnection().readMYSQLfile()

tc1 = TC1()
tc1.runTC()