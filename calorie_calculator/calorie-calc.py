# Calorie Calculator
class Person:
     def __init__(self, weightkg, heightcm, age, gender):
         self.weightkg = weightkg
         self.heightcm = heightcm
         self.age = age
         self.gender = gender
    
     def __str__(self):
         return "This individual is a {age} year old {gender}. They are {heightcm:.2f} cm tall and weigh {weight:.2f} kg".format(age=self.age,gender=self.gender,heightcm=self.heightcm,weight=self.weightkg)

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
         print('Lost {ammount} lbs'.format(ammount = ammount))

     def gain_weight(self, ammount):
         self.weight += (0.453592 * ammount) # 0.453592 kg is 1lb 
         print('Gained {ammount} lbs'.format(ammount = ammount))

     @classmethod
     def get_user_input(self):
         heightcm = get_heightcm()
         weightkg = get_weightkg()
         age = get_age()
         gender = get_gender()
         return self(weightkg,heightcm,age,gender)

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

# get goal weight    

    
if __name__ == "__main__":
    pass
    person1 = Person.get_user_input()
    print(person1)
    print(person1.get_bmr())
    person1.lose_weight(10) 
    print(person1.get_bmr())

    
   # make instance of person - gets info

   # get goal weight

   # for loop to get the calories needed at each weight (per week)



