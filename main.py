import math

print("Hello, world!!")


def circle_perimeter_and_area(radius):
    """

    :param radius: real number representing the radius of the circle
    :return: tuple with the perimeter and area of the circle
    """
    return math.pi * 2 * radius, math.pi * (radius ** 2)


perimeter, area = circle_perimeter_and_area(5)
print("Given a circle of radius {}, its perimeter is {} and its area is {}".format(5, perimeter, area))
