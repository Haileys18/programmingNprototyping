#Hailey Sooknanan
#2/27
#Period 5-6
#Python Practice

# Volume of a sphere
import math  # Importing the math module to use mathematical functions like pi

def volume(radius):  # Defining a function 'volume' that takes 'radius' as input
    x = (4/3)*math.pi*(radius**3)  # Calculating the volume of the sphere using the formula (4/3)*pi*r^3
    return x  # Returning the calculated volume

r = volume(5)  # Calling the 'volume' function with a radius of 5 and storing the result in 'r'
print(f"1. The volume of the sphere is {r:.2f}")  # Printing the volume of the sphere rounded to two decimal places

# Whole sale Book Cost
def W_cost(copies):  # Defining a function 'W_cost' that takes 'copies' as input
    bookPrice = 24.95  # Defining the price of one book
    shipFirst = 3  # Defining the shipping cost for the first book
    Shipafter = 0.75  # Defining the shipping cost for each additional book
    discount = 0.40  # Defining the discount percentage (40%)

    books_Total = (bookPrice * (1 - discount) * copies)  # Calculating the total price for the books after applying the discount
    shipcost = shipFirst + (Shipafter * (copies - 1))  # Calculating the total shipping cost (first book and additional books)
    Total = books_Total + shipcost  # Calculating the total cost (book price + shipping cost)

    print(f"2. The total wholesale price is ${Total:.2f}")  # Printing the total wholesale price rounded to two decimal places

W_cost(60)  # Calling the 'W_cost' function with 60 copies to calculate and print the total cost

# Running time Calculation
def running_time(s_h, s_m):  # Defining a function 'running_time' that takes start hour ('s_h') and start minute ('s_m') as inputs
    easy_pace = 8 * 60 + 15  # Defining the easy pace in seconds (8 minutes and 15 seconds per mile)
    tempo_pace = 7 * 60 + 12  # Defining the tempo pace in seconds (7 minutes and 12 seconds per mile)

    total_time_sec = (2 * easy_pace) + (3 * tempo_pace)  # Calculating total time for the run (2 miles at easy pace + 3 miles at tempo pace)
    total_min = total_time_sec // 60  # Converting total time in seconds to total minutes (integer division)
    total_sec = total_time_sec % 60  # Finding the remaining seconds after converting to minutes

    end_time_min = s_m + total_min  # Adding the total minutes to the starting minutes to get the end minutes
    end_hour = s_h  # Initializing the end hour to the starting hour

    if end_time_min >= 60:  # Checking if the total minutes exceed 60
        end_hour += end_time_min // 60  # Adding the number of hours to the end hour
        total_min += total_min // 60  # Adding the number of hours to total minutes (to account for overflow)

    return end_hour, total_min  # Returning the final hour and minute

end_h, end_m = running_time(6, 52)  # Calling the 'running_time' function with a start time of 6:52 AM and storing the result in 'end_h' and 'end_m'
print(f"3. you'll have breakfast at {end_h}:{end_m} AM.")  # Printing the time you will have breakfast at (end hour and end minute)
