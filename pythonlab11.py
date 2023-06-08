# # https://docs.google.com/document/d/1kr_pn9wtBC9CEivOP525sreC1Tl74oFlwcVg_CJuZBY/edit

# I. Write a Python class to convert a roman numeral to an integer.
# II. Write a Python class to find validity of a string of parentheses, &#39;(&#39;, &#39;)&#39;, &#39;{&#39;, &#39;}&#39;, &#39;[&#39; and &#39;].
# These brackets must be close in the correct order, for example &quot;()&quot; and &quot;()[]{}&quot; are valid
# but &quot;[)&quot;, &quot;({[)]&quot; and &quot;{{{&quot; are invalid.

# III. Write a Python class which has two methods get_String and print_String. get_String
# accept a string from the user and print_String print the string in upper case.
# IV. Write a Python class named Circle constructed by a radius and two methods which will
# compute the area and the perimeter of a circle.

# V. Design a class named triangle that extends the GeometricObject class. The Tringle class
# contains:
#  Three float fields named side1, side2, and side3 to denote the three sides of the
# triangle.
#  A constructor that creates a tringle with the specified side1, side2, and side3, with
# default value 1.0.
#  The accessor methods for all three data fields.
#  A method named getArea() that returns the perimeter of this triangle.
#  A method named __str__() that returns a string description for the triangle.

#1
class RomanNumeralConverter:
    def __init__(self):
        self.roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def convert(self, roman_numeral):
        result = 0
        previous_value = 0

        for char in roman_numeral[::-1]:
            value = self.roman_map[char]

            if value < previous_value:
                result -= value
            else:
                result += value

            previous_value = value

        return result

converter = RomanNumeralConverter()
result = converter.convert("XIV")
print(result)  # Output: 14

#2
class BracketValidator:
    def __init__(self):
        self.open_brackets = ["(", "{", "["]
        self.close_brackets = [")", "}", "]"]

    def is_valid(self, s):
        stack = []
        for bracket in s:
            if bracket in self.open_brackets:
                stack.append(bracket)
            elif bracket in self.close_brackets:
                if not stack:
                    return False
                current_open = stack.pop()
                if self.open_brackets.index(current_open) != self.close_brackets.index(bracket):
                    return False
        return not stack

validator = BracketValidator()
result1 = validator.is_valid("()[]{}")
result2 = validator.is_valid("[)")
result3 = validator.is_valid("({[)]")
result4 = validator.is_valid("{{{}}}")
print(result1, result2, result3, result4)  # Output: True False False True

#3
class StringManipulator:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Enter a string: ")

    def print_String(self):
        print(self.string.upper())

manipulator = StringManipulator()
manipulator.get_String()
manipulator.print_String()

#4
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

#5
class GeometricObject:
    def __init__(self, color="green", filled=True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def isFilled(self):
        return self.filled

    def setFilled(self, filled):
        self.filled = filled


class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0, color="green", filled=True):
        super().__init__(color, filled)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getSide1(self):
        return self.side1

    def setSide1(self, side1):
        self.side1 = side1

    def getSide2(self):
        return self.side2

    def setSide2(self, side2):
        self.side2 = side2

    def getSide3(self):
        return self.side3

    def setSide3(self, side3):
        self.side3 = side3

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def __str__(self):
        return f"A triangle with sides {self.side1}, {self.side2}, and {self.side3}, and area {self.getArea()}."

t = Triangle(3, 4, 5, "red", True)
print(t)

