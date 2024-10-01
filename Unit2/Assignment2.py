sideA = float(input("Enter side A: "))
sideB = float(input("Enter side B: "))
sideC = float(input("Enter side C: "))
sideD = float(input("Enter side D: "))
sideE = float(input("Enter side E: "))

rect1 = (sideA * sideB)

rect2 = (sideD - sideB - sideE) * (sideA - sideC)

tri = (sideA - sideC) * sideE * 0.5

print("Room Area: " + str(rect1+ rect2+tri))
