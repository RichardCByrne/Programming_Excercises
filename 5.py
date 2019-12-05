'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''



class Stringy:

    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter your text: ")

    def printString(self):
        print(self.text)

obj = Stringy()

obj.getString()
obj.printString()