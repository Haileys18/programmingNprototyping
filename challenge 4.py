#Hailey Sooknanan
#Period 5-6
#3/4
#Challenge 4

def draw_grid():
    def print_row():
        print("+", "- " * 2, "+", "- " * 2, "+")

    def print_column():
        for i in range(4):
            print("|", " " * 4, "|", " " * 4, "|")

    print_row()
    print_column()
    print_row()
    print_column()
    print_row()

draw_grid()
