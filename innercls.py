#inner class

class Students:

    def __int__(self,sname,rollno):
        self.sname = sname
        self.rollno = rollno
        self.lap = self.Asset()

    def show(self):
        print(self.sname,self.rollno)
        self.lap.show()

    class Asset:
        def __init__(self):
            self.assetname = "Lenoovo thinkpad"

        def show(self):
            print(self.assetname)

x = Students("Mahesh",101)

x.show()