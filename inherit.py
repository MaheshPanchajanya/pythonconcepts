
#### single inheritance ########

class Iphone:

    def feautre1(self):
        print("Display")

    def feature2(self):
        print("body")

class Apps(Iphone):

    def settings(self):
        print("setting")
    
    def iplanet(self):
        print("apple store")

mac = Apps()

mac.feautre1()

###### multi level inheritance #####

class Pixel:

    def googleaccount(self):
        print("gmail")

class Camera(Pixel):

    def focal(self):
        print("108 mega pixel")

class Boxpiece(Camera):

    def charger(self):
        print("charger 1 piece")

android = Boxpiece()

android.googleaccount()

