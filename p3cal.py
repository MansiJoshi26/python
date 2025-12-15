# calculator
# Taking input

first= input("enter 1st no. ")
operator=input("enter the operator ")
second= input("enter 2nd no. ")

# performing operations

if operator=='+':
  print(int(first)+int(second))
elif operator=='*':
  print(int(first)*int(second))
elif operator=='/':
  print(int(first)/int(second))
elif operator=='-':
  print(int(first)-int(second))
elif operator=='%':
  print(int(first)%int(second))
else :
  print('enter valid input')