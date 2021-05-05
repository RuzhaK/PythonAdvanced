import math
import exceptions
radius ="nanana"


def find_circle_are(radius):

    if type(radius) not in [int,float]:
        raise exceptions.BadRequestError(f"Radius cannot be of type {type(radius)}")
    return math.pi*radius*radius

print(find_circle_are(radius))


try:
    print(find_circle_are(radius))
except exceptions.Error:
    print("Please enter valid input")