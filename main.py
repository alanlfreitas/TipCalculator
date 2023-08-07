##### Data Types #####

# STRING #
  # print("Hello"[0])
  # print("123" + "456")

# INTERGER #
  # print(123 + 456)
  # 123_456_789

# FLOAT #
  # 3.14159

# BOOLEAN #
  # True
  # False

  #num_char = len(input("What is your name? "))
  #new_num_char = str(num_char)
  #print("Your name has " + new_num_char + " characters.")

  #a = float(123)
  #print(type(a))
  #print(70 + float(100.5))  #does the math operation
  #print(str(70) + str(100)) #prints the number together

  #two_digit_number = input("Type a two digit number: ")
  #a = two_digit_number[0]
  #b = two_digit_number[1]
  #x = int(a) + int(b)
  #print(x)

## Math operations ##
#3 + 3   #addition
#7 - 4   #subtraction
#3 * 2   #multiplication
#6 / 3   #division
#2 ** 3  #exponents

##### BMI Calculator #####
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")

#new_height = float(height)
#new_weight = float(weight)

#bmi = int(new_weight / (new_height ** 2))
#print(bmi)

##### NUMBER MANIPULATION #####
#print(round(8/3, 2)) # 2 is defining the number of decimal places
#print(8 // 3) # floor division show the result as interger

#score = 0
# User scores a point
#score += 1 # adds 1
#print(score)

#score = 0
#height = 1.8
#isWinning = True
#f-String
#print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

##### Challenge - Life in days, weeks, months #####
# 🚨 Don't change the code below 👇
#age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#age_int = int(age)

#yearsleft = 90 - age_int
#daysleft = yearsleft * 365
#weeksleft = yearsleft * 52
#monthsleft = yearsleft * 12

#message = f"You have {daysleft} days, {weeksleft} weeks, and {monthsleft} months left."
#print(message)

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the TIP CALCULATOR")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to tip? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100 #calculating tip percentage
totaltip = bill * tip_percent 
totalbill = bill + totaltip #adding the tip to the bill
billperson = totalbill / people #dividing bill among consumers
finalbill = round(billperson, 2) #rounding to 2 decimal places
finalbill = "{:.2f}".format(billperson) #fixing the 2 decimal places problem
print(f"Each person should pay: ${finalbill}.")