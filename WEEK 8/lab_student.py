# import turtle
# import turtle

# def main():
#     sipi = turtle.Turtle()
#     sipi.shape("turtle")
#     # ... other turtle code ...
#     turtle_screen = turtle.Screen()
#     turtle_screen.exitonclick()

# if __name__ == '__main__':
#     main()

class LABStudent:
    # Constructor method to initialize attributes
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    # Method to introduce the object
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, STUDYING IN IIT"
    
    # Method
    def study(self):
        return f"{self.name} is now studying BSIT"





