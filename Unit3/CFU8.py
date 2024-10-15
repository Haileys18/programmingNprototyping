#V1
#Hailey Sooknanan
#5-6
#10/15
#Grubhub deliveries asking user the order
word = input("Did you order delivery?")

if word == "yes":
    print("Great!")
else:
    print("NO?! So who is cooking?")

#V2
#Hailey Sooknanan
#5-6
#10/15
#Grubhub deliveries asking user the order
word = input("Did you order delivery?")

if word == "yes":
    cost = int(input("What is the cost?"))
    people = int(input("How many people"))
    total = cost/people
    print("total per person: " + str(total) )
else:
    print("NO?! So who is cooking?")
