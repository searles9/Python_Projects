# Calorie Calculator
class Person:
     def __init__(self, weightkg, heightcm, age, gender,goalweightkg,activitylvl):
         self.weightkg = weightkg
         self.heightcm = heightcm
         self.age = age
         self.gender = gender
         self.goalweightkg = goalweightkg
         self.activitylvl = activitylvl
    
     def __str__(self):
         return "{age} year old {gender} who is {heightcm:.2f} cm's tall and weighs {weight:.2f} kg".format(age=self.age,gender=self.gender,heightcm=self.heightcm,weight=self.weightkg)

     def get_bmr(self):
         if self.gender == 'Male':
             # Mifflin-St Jeor Equation:
             bmr = (10*self.weightkg) + (6.25*self.heightcm) - (5*self.age) + 5
             return round(bmr)
         elif self.gender == 'Female':
             # Mifflin-St Jeor Equation:
             bmr = (10*self.weightkg) + (6.25*self.heightcm) - (5*self.age) - 161
             return round(bmr)

     def lose_weight(self, ammount):
         self.weightkg -= (0.453592 * ammount) # 0.453592 kg is 1lb 
         print('- {ammount} lbs'.format(ammount = ammount))

     def gain_weight(self, ammount):
         self.weight += (0.453592 * ammount) # 0.453592 kg is 1lb 
         print('+ {ammount} lbs'.format(ammount = ammount))

     def calculate_cals(self):
         activity={
            'sedentary':1.2, # Sedentary = BMR x 1.2 (little or no exercise, desk job) 
            'lightly_active':1.375,  # Lightly active = BMR x 1.375 (light exercise/ sports 1-3 days/week) 
            'moderately_active':1.55, # Moderately active = BMR x 1.55 (moderate exercise/ sports 6-7 days/week) 
            'very_active':1.725, # Very active = BMR x 1.725 (hard exercise every day, or exercising 2 xs/day)  
            'extra_active':1.9 # Extra active = BMR x 1.9 (hard exercise 2 or more times per day, or training for marathon, or triathlon, etc.
        }
         return int(round((self.get_bmr() * activity[self.activitylvl])))


     @classmethod
     def get_user_input(self):
         heightcm = get_heightcm()
         weightkg = get_weightkg()
         age = get_age()
         gender = get_gender()
         goalweightkg = get_goal_weight()
         activitylvl = get_activity_level()
         return self(weightkg,heightcm,age,gender,goalweightkg,activitylvl)
#----------------------------------------------------------------
# UNIT CONVERTER
def convert_unit(fromvalue,fromunit,tounit):
    # Height
    if fromunit == "ft" and tounit == "cm":
        return float(fromvalue)*30.48
    elif fromunit == "ft" and tounit == "inch":
        return float(fromvalue)*12
    elif fromunit == "inch" and tounit == "cm":
        return float(fromvalue)*2.54
    # Weight
    elif fromunit == "lb" and tounit == "kg":
        return float(fromvalue)/2.2046
#----------------------------------------------------------------
# GET INPUT FOR CLASS OBJECT
def get_heightcm():
    heightft = ''
    while heightft not in range(0,10):
        heightft = int(input('How tall are you (feet): '))
    heightin = ''  
    while heightin not in range(0,12):
        heightin = int(input('How tall are you (inches): '))
    return (convert_unit(heightft,'ft','cm')) + (convert_unit(heightin,'inch','cm'))

def get_weightkg():
    weightlbs = input('How much do you weigh? (lbs): ')
    return convert_unit(weightlbs,'lb','kg')

def get_age():
    age = ''
    while age not in range(1,101):
        age = int(input('How old are you? (years): '))
    return age


def get_gender():
    while True:
        gender = input('What is your gender? (Male or Female): ')
        if gender.lower()[0] == 'm':
            return 'Male'
            break
        elif gender.lower()[0] == 'f':
            return 'Female'
            break
        else: 
            continue

def get_goal_weight():
    # returns weight in kg
    while True:
        try:
            goal_weight = int(input('What weight would you like to get to? (lbs): '))
            goal_weight = convert_unit(goal_weight,'lb','kg')
            return goal_weight #in kg
        except:
            print("Please enter a valid weight: example...140 ")
            continue

def get_activity_level():
    activity={
             1:'sedentary',
             2:'lightly_active',
             3:'moderately_active',
             4:'very_active',
             5:'extra_active'
    }
    print("\n")
    print("1 - Sedentary / little or no exercise, desk job")
    print("2 - Lightly active / light exercise/ sports 1-3 days/week")
    print("3 - Moderately active / moderate exercise/ sports 6-7 days/week")
    print("4 - Very active / hard exercise every day, or exercising 2 xs/day")
    print("5 - Extra active / hard exercise 2 or more times per day, or training for marathon, or triathlon, etc.")
    print("\n")
    number = 0
    while number not in range(1,6):
        number = int(input("Please enter the number associated with your activity level: "))
    return activity[number]


#----------------------------------------------------------------  
# GET INPUT - GENERAL FUNCTION


#----------------------------------------------------------------  

    
if __name__ == "__main__":
   # make instance of person - gets info
   donovan = Person.get_user_input()
   # get goal weight
   print(donovan.goalweightkg)
   cals = donovan.calculate_cals()
   print(cals)
   # for loop to get the calories needed at each weight (per week)


