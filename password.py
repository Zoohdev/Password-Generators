#user inputs password
pass_word= input("Enter your password:") 

pass_word = False

have_length = False

up_case = False

low_case = False

have_num = False

#checks length of user's password
lengthcheck = input("Does the password have at least 6 characters? (Yes or No)")
if have_length == "Yes":
	have_length = True
#checks for upper case letter	
upcase = input("Does your password have an upper case character?(Yes or No)")
if up_case == "Yes":
	up_case = True

#checks for lower case letter
lowcase = input("Does your password have a lower case character?(Yes or No)")
if low_case == "Yes":
	low_case = True
#checks if password has number
num = input("Does your password contain a number?(Yes or No)")
if have_num == "Yes":
	have_num = True
#counts number of Yes answers
count = int(input("How many answers above are a Yes?"))
if count > 2:                  
 print("Password is valid")
                   
else:
                   print("Password is invalid")






