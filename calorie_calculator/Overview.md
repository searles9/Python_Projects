# Calorie Calculator

## Important Notes
* The basic logic of this is complete but there are still some changes that need to be made. See the "things to add" section below.

# What is this:
Being in a caloric deficit is the only way to lose fat. This is a program that can calculate your caloric needs based on a goal weight that you provide.

In practice you wouldnt want to change your calories until your body stops losing the desired amount of  weight per week. This just gives a blueprint that you can use as a refrence.

# How to use this:
```
$ python calorie-calc.py 
How tall are you (feet): 6
How tall are you (inches): 2
How much do you weigh? (lbs): 195
How old are you? (years): 21
What is your gender? (Male or Female): m
What weight would you like to get to? (lbs): 185


1 - Sedentary / little or no exercise, desk job
2 - Lightly active / light exercise/ sports 1-3 days/week
3 - Moderately active / moderate exercise/ sports 6-7 days/week
4 - Very active / hard exercise every day, or exercising 2 xs/day
5 - Extra active / hard exercise 2 or more times per day, or training for marathon, or triathlon, etc.


Please enter the number associated with your activity level: 1
How many lbs would you like to lose per week? (years): 1


* Your starting weight is: 195 lbs
* Your starting activity level is: sedentary
Week 1: 1851 | Weight at the end of the week: 194
Week 2: 1846 | Weight at the end of the week: 193
Week 3: 1840 | Weight at the end of the week: 192
Week 4: 1835 | Weight at the end of the week: 191
Week 5: 1829 | Weight at the end of the week: 190
Week 6: 1824 | Weight at the end of the week: 189
Week 7: 1818 | Weight at the end of the week: 188
Week 8: 1814 | Weight at the end of the week: 187
Week 9: 1808 | Weight at the end of the week: 186
Week 10: 1802 | Weight at the end of the week: 185
```
* Once you run the script it asks you for some information and then proceeds to calculate the info.

# Things to add:
* Females should not eat less than 1,200 calories per day and a Male should not eat less than 1,500. I need to add logic that makes adjustments to the "change per week" and the "activity level" when the program sees the calories being below the minimum levels.... Might have to make some large adjustments for this

# Some of the related Python Documentation: