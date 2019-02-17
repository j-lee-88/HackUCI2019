'''NOTE TO PROGRAMMER: PUT THE NAME OF THE SUBFOLDER WHERE THE USER PRICE DATA WILL BE STORED IN THE CONSTANT BELOW (SUBFOLDER)'''

SUBFOLDER = './Named_Files'



def get_name():
    name = input("What is your name?: ")
    budget = input("How much do you pay in yearly tuition?: ")
    return (name, budget)

def make_file(nb:tuple):
    name = nb[0]
    budget = nb[1]
    pfile = open(SUBFOLDER + name + '.txt', 'w')
    pfile.write(budget)


name_and_budget = get_name()
make_file(name_and_budget)
