# Calorie Calculator
class Person:
     activitymultiplier={
            'sedentary':1.2, # Sedentary = BMR x 1.2 (little or no exercise, desk job) 
            'lightly_active':1.375,  # Lightly active = BMR x 1.375 (light exercise/ sports 1-3 days/week) 
            'moderately_active':1.55, # Moderately active = BMR x 1.55 (moderate exercise/ sports 6-7 days/week) 
            'very_active':1.725, # Very active = BMR x 1.725 (hard exercise every day, or exercising 2 xs/day)  
            'extra_active':1.9 # Extra active = BMR x 1.9 (hard exercise 2 or more times per day, or training for marathon, or triathlon, etc.
        }
     activityrank={
             1:'sedentary',
             2:'lightly_active',
             3:'moderately_active',
             4:'very_active',
             5:'extra_active'
         }
      

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
         #print('- {ammount} lbs'.format(ammount = ammount))

     def gain_weight(self, ammount):
         self.weight += (0.453592 * ammount) # 0.453592 kg is 1lb 
         #print('+ {ammount} lbs'.format(ammount = ammount))

     def calculate_cals(self):
         return int(round((self.get_bmr() * self.activitymultiplier[self.activitylvl])))

     def weight_in_lbs(self):
         return convert_unit(self.weightkg,'kg','lb')

     def goal_weight_in_lbs(self):
         return convert_unit(self.goalweightkg,'kg','lb')

     def cals_to_low(self):
         if self.gender == 'Male':
             # 1,500 minimum to stay healthy 
             if self.calculate_cals() <= 1500:
                 return True
             else:
                 return False
         elif self.gender == 'Female':
             # 1,200 minimum to stay healthy
             if self.calculate_cals() <= 1200:
                 return True
             else:
                 return False

     def increase_activitylvl(self):
         currentlevel = [k for k, v in self.activityrank.items() if v == self.activitylvl][0]
         if int(currentlevel) <= 4:
             self.activitylvl = self.activityrank[(int(currentlevel)+1)]


         

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
    elif fromunit == "kg" and tounit == "lb":
        return float(fromvalue)/0.45359237
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

    
if __name__ == "__main__":
   # make instance of person - gets info
   donovan = Person.get_user_input()
   # get starter values
   thegoalweight = int(donovan.goal_weight_in_lbs())
   thestartweight = int(donovan.weight_in_lbs())
   weightperweek = 2
   # logic
   counter = 0
   print("\n")
   print(f"* Your starting weight is: {thestartweight} lbs")
   print(f"* Your starting activity level is: {str(donovan.activitylvl.replace('_',' '))}")
   if thestartweight == thegoalweight:
       print(f"Congrats you have reached your goal weight of {thegoalweight} lbs")
   elif thestartweight < thegoalweight:
       # gain weight 
       for weight in range(thegoalweight ,thestartweight,weightperweek):
           counter += 1
           weightendofweek = (int(donovan.weight_in_lbs())+weightperweek)
           print(f"Week {counter}: {donovan.calculate_cals()} | Weight at the end of the week: {weightendofweek}")
           donovan.gain_weight(weightperweek)
   elif thestartweight > thegoalweight:
       # lose weight
        for weight in range(thegoalweight ,thestartweight,weightperweek):
               if donovan.cals_to_low() == True:
                   while donovan.cals_to_low() == True:
                       if donovan.activitylvl == donovan.activityrank[5]:
                           print("Your calories have gotten to low and you are already extra active. Please see a specialist as you may have a metabolic issue.")
                           break
                       else:
                           donovan.increase_activitylvl()
                           print(f"Your calories have gotten to low. To prevent eating to little you activity level has changed to {str(donovan.activitylvl.replace('_',' '))}")
                           print("You will now need to do additional exercise to continue losing weight")
               else:
                   counter += 1
                   weightendofweek = (int(donovan.weight_in_lbs())-weightperweek)
                   print(f"Week {counter}: {donovan.calculate_cals()} | Weight at the end of the week: {weightendofweek}")
                   donovan.lose_weight(weightperweek)

