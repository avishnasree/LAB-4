# 6. Write lambda functions to find the area of square, rectangle and triangle.


area_square=lambda x: x*x
side=int(input('Enter a side value of square : '))
print(area_square(side))

area_rectangle=lambda x,y:x*y
Length=int(input('Enter a Length value of rectangle : '))
Width=int(input('Enter a Width value of rectangle : '))
print(area_rectangle(Length,Width))

area_triangle =lambda x,y:(x*y)/2
base=int(input('Enter a base value of triangle : '))
height=int(input('Enter a height value of triangle : '))
print(area_triangle(base,height))