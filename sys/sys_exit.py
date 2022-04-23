import sys
 
age = int(input("What's your age?\n"))

if age < 18:
    sys.exit("You are a Teenager.")   
else:
    print("You are an adult.")