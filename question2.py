# Create a program to calculate the area of a triangle (1/2 * base * height). 
# Base and height should be entered using the keyboard. 

#ANSWER 2

base = int(input("Enter the base of the traingle: "))
height = int(input("Enter the height of the triangle: "))
area_of_a_trangle = (1/2 * base * height)
area = f"The the area of a triangle is : {area_of_a_trangle : 2}"
print(area)