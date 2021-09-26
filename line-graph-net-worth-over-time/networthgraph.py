import matplotlib.pyplot as plt
#import numpy as np

class Person:
    def __init__(self,bank,investments,monthlynet,monthlyinvestments,monthlyexpenses):
        self.bank = bank 
        self.investments = investments
        self.monthlynet = monthlynet
        self.monthlyinvestments = monthlyinvestments
        self.monthlyexpenses = monthlyexpenses


    def oneyearbank(self):
        self.bank += ((self.monthlynet - (self.monthlyexpenses + self.monthlyinvestments)) * 12)

    def oneyearinvestments(self):
        self.investments = (self.investments + (self.monthlyinvestments * 12) )* 1.08 # standard 8% return

    def __str__(self):
        return f"Bank:{self.bank}\nInvestments:{self.investments}\nNet Worth:{self.bank + self.investments}\nMonthly Net:{self.monthlynet}\nMonthly Investments:{self.monthlyinvestments}\nMonthly Expenses:{self.monthlyexpenses}"
    

def makeplots(person,x,y):
    plt.plot(x, y, linewidth = 3, marker='o', markerfacecolor='blue', markersize=5,label = f"Monthly Net:{person.monthlynet}|Monthly Investments:{person.monthlyinvestments}|Expenses:{person.monthlyexpenses}")

def getplotvals(person,years):
    xitem = [0] # years
    yitem = [person.bank + person.investments] # networth
    yearcount = 1
    while yearcount <= years:
        person.oneyearbank()
        person.oneyearinvestments() # standard 8% return
        yitem.append(person.bank + person.investments)
        xitem.append(yearcount)
        yearcount += 1
    return (xitem,yitem)

if __name__ == "__main__":
    # make people objects and people list
    person1 = Person(0,0,3664,0,2000) # 65k after tax GA - investing 0 a month
    person2 = Person(0,0,3664,800,2000) # 65k after tax GA - investing 800 a month
    person3 = Person(0,0,4410,0,2800) # 80k after tax ga - investing 0 a month
    person4 = Person(0,0,4410,1000,2800) # 80k after tax ga - investing 1000 a month
    peoplelist = [person1,person2,person3,person4]
    # get plot values
    for person in peoplelist:
        (xlist,ylist) = getplotvals(person,40)
        makeplots(person,xlist,ylist)
        
    # Make Graph
    #plt.xticks(np.arange(0, 60, 1)) 
    #plt.yticks(np.arange(0, 500000, 10000)) 
    plt.xlabel('Years')
    plt.ylabel('Net Worth')
    plt.title('Net Worth Over Time')
    plt.legend()
    plt.show()
