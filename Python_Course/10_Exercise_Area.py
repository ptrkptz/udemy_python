import math
radius=float( input("Input radius of the circle: ") );
area = math.pi * (radius ** 2)
circum = 2 * math.pi * radius


print("my OG - Circle area: ", 3.14*(radius*radius));
print("my OG - Circumferance: ",round(2*3.14*radius,3));

print("Area: ", round(area, 2));
print("Circum:", round(circum,2));
