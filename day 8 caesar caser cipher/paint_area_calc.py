import math

height = int(input("Enter the height of the wall"))
width = int(input("Enter the width of the wall"))
coverage = 6

def area(height , width , coverage):
    areaa = ((height*width)/coverage)
    ceilded_area = math.ceil(areaa)
    print(f'the required area is {ceilded_area}')

area(height , width , coverage)