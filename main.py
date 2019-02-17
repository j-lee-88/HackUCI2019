from first_trial import return_average




    

def getInput():
    

    print("Which type of student are you?")
    print("1) Public Two-Year In-State Commuter")
    print("2) Public Four-Year In-State On-Campus")
    print("3) Public Four-Year Out-Of State On-Campus")
    print("4) Private Nonprofit Four-Year On-Campus")

    option = int(input())
    expenses = getExpenses()
    
    if option == 1:    
        print_output(expenses, total_1)
    elif option == 2:
        print_output(expenses, total_2)
    elif option == 3:
        print_output(expenses, total_3)
    elif option == 4:
        print_output(expenses, total_4)

def print_output(average, total):
    if average < total:
        print("You're paying less than the average!")
    else:
        print("You're paying more than the average!")
        
def getExpenses():
    print("Please estimate how much your total expenses per year are:")

    expenses = int(input())

    return expenses


avg_tuition_1 = 3660
avg_tuition_2 = 10230
avg_tuition_3 = 26290
avg_tuition_4 = 35830

avg_rnb_1 = 8660
avg_rnb_2 = 11140
avg_rnb_3 = 11140
avg_rnb_4 = 12680

avg_supplies_1 = 1440
avg_supplies_2_4 = 1240

transportation_1 = 1800
transportation_2 = 1160
transportation_3 = 1160
transportation_4 = 1050

other_expenses_1 = 2370
other_expenses_2 = 2120
other_expenses_3 = 2120
other_expenses_4 = 1700

total_1 = 17930
total_2 = 25890
total_3 = 41950
total_4 = 52500

total_avg_costs = return_average()

getInput()
