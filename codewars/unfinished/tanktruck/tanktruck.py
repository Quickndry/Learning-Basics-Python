import math

def tankvol(h, d, vt):
    # Identify the area of the circle and use it to find the length of the tank
    # then find the measurements of the triangle inside the circle using the 
    # height given. Use these to find the area of the segment of the circle i.e.
    # the midsection of the leftover liquid. Use this and the length to find the
    # volume of the leftover liquid.

    # find area of circle
    radius_of_circle = d * 0.5
    area_of_circle = math.pi * (radius_of_circle ** 2)
    print("Radius: ", radius_of_circle, "\nArea: ", area_of_circle)

    # find length of tank
    length_of_tank = vt / radius_of_circle
    print("Length: ", length_of_tank)

    # finding the lengths of the triangle inside the circle
    # using pythagoras theorem
    a = abs(radius_of_circle - h) # depending on if its negative or positive, find area of segment or major segment
    a_squared = a ** 2
    r_squared = radius_of_circle ** 2
    if a_squared > r_squared:
        squared_diff = a_squared - r_squared
    elif r_squared > a_squared:
        squared_diff = r_squared - a_squared
    b = math.sqrt(squared_diff)
    print("A: ", a, "\nB: ", b, "\nC: ", radius_of_circle)

    # finding target angle
    temp_total = a + b
    a_ratio = a / temp_total
    a_angle = 2 * (a_ratio * 90)
    target_angle = a_angle / 360
    print("Angle: ", target_angle)

    # find area of circle sector
    area_of_segment = 0.5 * (target_angle * math.sin(target_angle)) * r_squared
    print("Area of Segment: ", area_of_segment)

    # find volume of rest liquid in tank
    volume_of_segment = area_of_segment * length_of_tank
    return volume_of_segment

