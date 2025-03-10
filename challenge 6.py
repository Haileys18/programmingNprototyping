#Hailey Sooknanan
#Period 5-6
#3/10
#Challenge 6

def is_triangle(a, b, c):
    # Check the triangle inequality theorem
    if a + b > c and a + c > b and b + c > a:
        print("Yes")
    else:
        print("No")

def main():
    # Prompt the user to input three stick lengths
    stick_1 = int(input("Enter the first stick length: "))
    stick_2 = int(input("Enter the second stick length: "))
    stick_3 = int(input("Enter the third stick length: "))
    
    # Check if the three lengths can form a triangle
    is_triangle(stick_1, stick_2, stick_3)

# Call the main function to execute
main()
