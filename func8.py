#  write a function which take password as input and its validate as per the following conditions:
# 1. password has to be 8 characters 
# 2. should contain alphabets and numbers
# 3. should contain one special character
# 4. it should not have spaces

import string

def validate_password(password):
	if len(password) != 8:
		return False, "Password must be 8 characters long."
	if ' ' in password:
		return False, "Password should not contain spaces."
	has_alpha = (
		password.lower() != password.upper()
	)
	has_digit = any( password in '0123456789')
	
	has_special = any( password in string.punctuation)
	if not has_alpha:
		return False, "Password must contain alphabet."
	if not has_digit:
		return False, "Password must contain  number."
	if not has_special:
		return False, "Password must contain  special character."
	return True, "Password is valid."

password = input("Enter your password: ")
is_valid, message = validate_password(password)
print(message)
