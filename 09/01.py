def calculate_area(radius: int, a: str) -> str:
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :return: The area of the circle.
    """
    # b = a + 67
    area = 3.14 * radius ** 2
    return str(area) + a


print(calculate_area(67, " cm²"))
print(calculate_area.__doc__)
print(calculate_area.__annotations__)
