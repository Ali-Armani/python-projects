"""
______---------______---------______--------_____----
Recieving The Applicant's Personal Info
______---------______--------______---------______
"""
age=input("How Old Are You?")
age_to_int=int(age)
if age_to_int<=17:
	print("You are under age, sorry!")
else:
	print("Welcome to Our Company!")
