from collections import namedtuple


plane_1 = ("Boeing 747", 1989, 200, "USA")
plane_2 = ("Airbus A380", 2005, 300, "France")
plane_3 = ("Concorde", 1999, 100, "UK")
plane_4 = ("Cessna 172", 2010, 4, "USA")
planes = [plane_1, plane_2, plane_3, plane_4]

for plane in planes:
    if plane[1] > 190:
        print(f"{plane[0]} is a large plane.")

print("-------------")
plane = namedtuple("Plane", ["name", "year", "capacity", "country"])
plane_1 = plane("Boeing 747", 1989, 200, "USA")
plane_2 = plane("Airbus A380", 2005, 300, "France")
plane_3 = plane("Concorde", 1999, 100, "UK")
plane_4 = plane("Cessna 172", 2010, 4, "USA")
planes = [plane_1, plane_2, plane_3, plane_4]

for plane in planes:
    if plane.capacity > 190:
        print(f"{plane.name} is a large plane.")
