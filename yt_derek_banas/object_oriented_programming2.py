class Square:
    def __init__(self,height = "0",weight = "0"):
        self.height = height
        self.weight = weight
        
    @property
    def height(self):
        print("Retrieving the height")
        return self.__height

    @height.setter
    def height(self,value):
        if value.isdigit():
            self.__height = value
        else:
            print("The height is not a number. Please enter only numbers for height")

    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("The width is not a number. Please enter only numbers for width")

    def get_area(self):
        return int(self.__height) * int(self.__width)

def main():
    aSquare = Square()
    height = input("Enter the height: ")
    width = input("Enter the width: ")

    aSquare.height = height
    aSquare.width = width

    print("Height: ",aSquare.height)
    print("Width: ", aSquare.width)
    print("The area is: ", aSquare.get_area())

main()