def vol(l=1,w=1,h=1):
    return(l*w*h)

length = int(input("Enter the length : "))
width = int(input("Enter the width : "))
height = int(input("Enter the height : "))

print("volume of box = ", vol( length , width , height ))

