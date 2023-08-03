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

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_height = float(height)
new_weight = float(weight)

bmi = int(new_weight / (new_height ** 2))
print(bmi)

