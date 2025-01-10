groceries = ["Eggs","Apples","Milk","Bread"]
print(groceries)
print(groceries[1])
print(groceries[0:3])



names=["Hailey","Malachi","Nafisa","Amelia","Nibrus","Evelyn","Cesar","Sharena","Aarya","Farhan","Edwin","Syeda","Romina","Neelam","Arafath","Fahim","Emirah","Mia","Harbans","Sarika","Angel","Willian"]
ages = [16.11,16.5,16.7,16.3,16.1,16.4,16.11,16.4,16.7,16.8,16.6,16.6,17.7,16.11,16.5,16.5,16.7,17.4,16.7,16.2,16.1,16.11]
print(names[4:7])

print("my friend "+ str(names[3:8]) + " is age "+ str(ages[3:8]) + " years old")

for dog in groceries:
    print("I need to buy "+dog)
#len counts the number of items in a list
for i in range(len(ages)):
    print("my friend "+ names[i] + " is age "+ str(ages[i]) + " years old")
   
#Append adds an item to the end of the list
groceries.append("Carrot")
print(groceries)

#Insert needs 2 arguemnts the first one is where you want to put it and the second is what it is
groceries.insert(6,"lolipop")
print(groceries)

groceries.remove("Bread")
print(groceries)
