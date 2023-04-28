#1
def midpoint(x1, y1, x2, y2):
    import turtle
    import math

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Calculate the mid-point between the two points
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    # Set up the turtle window
    wn = turtle.Screen()
    wn.setup(600 , 600) # Set the window size
    wn.setworldcoordinates(-10, -10, 10, 10)  # Set the coordinate system
    wn.title("Cartesian Plane")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Draw the x-axis
    t.goto(-10, 0)
    t.pendown()
    t.goto(10, 0)
    t.penup()

    for i in range(-10, 11):
        t.goto(i, 0)
        t.dot(5)
        t.write(i, align="center", font=("Arial", 8, "normal"))

    # Draw the y-axis
    t.goto(0, -10)
    t.pendown()
    t.goto(0, 10)
    t.penup()
    t.setheading(90) #used to change the orientation of the turtle (direction in which it will  start drawing )
    for i in range(-10, 11):
        t.goto(0, i)
        t.dot(5)
        t.write(i, align="center", font=("Arial", 8, "normal"))
    t.setheading(0)

    # Draw the first point
    t.goto(x1, y1)
    t.pendown()
    t.dot(10, "blue")
    t.write(f"({x1}, {y1})", align="left")

    # Draw the second point
    t.penup()
    t.goto(x2, y2)
    t.pendown()
    t.dot(10, "blue")
    t.write(f"({x2}, {y2})", align="left")

    # Draw the line between the two points
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

    # Draw the mid-point
    t.penup()
    t.goto(mid_x, mid_y)
    t.pendown()
    t.dot(10, "red")
    t.write(f"({mid_x}, {mid_y})", align="left")

    # Write the distance between the two points
    t.penup()
    t.goto(mid_x, mid_y + 1)
    t.pendown()
    t.write(f"Distance: {distance:.2f}", align="center", font=("Arial", 16, "normal"))

    # Keep the turtle window open
    turtle.mainloop()

# midpoint(2,2,4,4)

#2
def cocentric_circles():
    import turtle

    # Define center point
    center = (0, 0)

    no_of_circle=5

    # Define radii of the circles
    radii = [20, 40, 60, 80, 100]

    # Define colors for the circles
    colors = ['red', 'orange', 'yellow', 'green', 'blue']

    # Create turtle object
    t = turtle.Turtle()

    # Move turtle to center point
    t.penup()
    t.goto(center)
    t.pendown()
    t.pensize(3)

    # Draw circles using turtle
    for r in range(no_of_circle):
        t.penup()
        t.pencolor(colors[r])
        t.goto(center[0], center[1] - radii[r])
        t.pendown()
        t.circle(radii[r])

    # Hide turtle when finished drawing
    t.hideturtle()

    # Keep window open until closed by user
    turtle.done()

# cocentric_circles()

#3
def colored_hexagon():
    import turtle

    # Initialize turtle and set the background color
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    turtle.bgcolor("white")

    # Set the size of the hexagon
    size = 200

    # Set the colors
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # Draw the hexagon made up of six equilateral triangles
    for i in range(6):

        # Move to the center of the hexagon
        t.penup()
        t.goto(0, 0)
        t.pendown()

        # Set the color of the current section
        t.fillcolor(colors[i])

        # Draw the current section
        t.begin_fill()
        for j in range(2):
            t.forward(size)
            t.left(120)
        t.end_fill()

        # Rotate to the next section
        t.left(60)

    # Hide turtle and exit the turtle graphics window
    t.hideturtle()
    turtle.done()

colored_hexagon()

#4

# the fundamental type of digital imagesd are : 

# grascale images -
    # no color component, 
    # monochromatic images
    # refers to the range of shades between white and black 
    # 8 bits are enough to  represent gray scale images 2^8=256 levels 
    #  examples : ct scan, MRI images , ultra sound images    
# binary images  -
    # pixel assumes either 0 or 1
    # one bit is sufficient to represent pixel value 
    # also called bit level images 
    # created from gray scale image using threshold process 
    # used to represent basic shapes and line drawings
    # can be used as masks 
    # in image processing , these images produced at intermediate levels

# true color images 
    # pixel has a color that is obtained by mixing primary colors 
    # each component is represented using 8 bit like a gray scale 
    # most true color images use 24 bits to represent all colors 
    # hence called three band images 
    # no. of possible colors are: 256^3
# psuedo color images 
    # colors are added artificially based on the interpretation of data rather actual object color 
    #  popular in medical domain 
    # example: doppler color image 

def grayscale_to_binary_image():
    import cv2

    # Read the gray image
    gray_image = cv2.imread('grayscale_cat.jpg', cv2.IMREAD_GRAYSCALE)

    # Convert to binary image using a threshold value of 127
    ret, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow("original image (grayscale)", gray_image)
    cv2.imshow("processed image (binary)", gray_image)

    # Wait indefinitely for a key press event
    cv2.waitKey(0)

# grayscale_to_binary_image() 
#5
def extract_rgb():
    import cv2

    # Read the color image
    image = cv2.imread('grayscale_cat.jpg')

    # Check if image was loaded successfully
    if image is None:
        print("Error: Could not read image file")
        return
    
    # Extract pixel values in the red, green, and blue dimension
    b, g, r = cv2.split(image)

    # Print the pixel values
    print(f"Red pixels: {r}", end="\n")
    print(f"Green pixels: {g}", end="\n")
    print(f"Blue pixels: {b}", end="\n")

extract_rgb()






























