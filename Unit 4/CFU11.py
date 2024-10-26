#hailey sooknanan
#period 5-6
#10/25
#Using FOR LOOP to create loops and asking the user to input which one 
#they want to play


def ten_loop():
    for i in range (10,71,10):
        print(i)

def half_loop():
    for i in range (0, 21):
        print(i*21)
        

def beer_song():
    for i in range (99,-1,-1):
        if i >1:
            print(f"{i} bottles of beer on the wall,\n{i} bottles of beer!\n")
            print(f"Takes one down pass it around.\n{i-1} bottles of beer on the wall.\n")
        elif i == 1:
            print(f"{i} bottle of beer on the wall,\n{i} bottle of beer!\n")
            print("Take one down, pass it around.\nNo more bottles of beer on the wall.\n")
        else:
            print("No more bottles of beer on the wall,\nNo more bottles of beer!\n")
#puts these underneath or else it would not run because to the computer
#it does not exist yet(top --> bottom)
user_input = int(input("Which loop would you like to play?: 1, 2, or 3"))

if user_input == 1:
    ten_loop()
elif user_input == 2:
    half_loop()
else:
    beer_song()
            
           
       
                 
