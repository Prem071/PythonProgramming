# 1. take a user name and the password from user and store it in dictonary
# store some 3 user name and passwords in a dictonary manually
# when the user enters the password if the user name does not exist in the dict, 
# ask the user to sign up ...else print the message that user exists.

users = {"prem": "prem123",
	"siddu": "siddu456",
	"anisetti": "anisetti789"}

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in users : 
	print("User exists.")
else:
	print("Username not found. Please sign up.")
	signup = input("Do you want to sign up? (yes/no): ").strip().lower()
	if signup == "yes":
		users[username] = password
		
		print("User '{username}' signed up successfully!")
	else:
		print("Sign up cancelled.")































































