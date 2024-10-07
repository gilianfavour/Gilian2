# The volume of a sphere with radius r is (4/3)* pie * r**2. 
# What is the volume of the sphere with radius 5. 
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places

#ANSWERS
pie=(22/7)
r =float(input("Enter the radius of the sphere: "))
formula = (4/3)*pie * r**2
#basic = float(input("Enter the radius of the sphere: "))
volume_of_a_sphere= f"The volume of a sphere: {formula:.2f}"
print(volume_of_a_sphere)