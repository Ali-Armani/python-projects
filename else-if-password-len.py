password=input("Password:")
if len(password)<8:
	print("Too weak!")
elif len(password)==8:
	print("Good but still vulnerable!")
elif len(password)>8 and len(password)<12:
	print("Strong but could be better!")
else:
	print("Strong and Impossible to Decipher!")
	first_name=input("First Name:")
	last_name=input("Last Name:")
	print("Birth Date:")
	yy=input("Year:")
	yy_to_int=int(yy)
	if len(yy)<4:
		print("Please enter a valid year.")
	else:
		mm=input("Month:")
		mm_to_int=int(mm)
	if len(mm)<2:
		print("Please enter a valid month.")
	else:
		dd=input("Day:")
		dd_to_date=int(dd)
	if len(dd)<2:
		print("Please enter a valid day.")
	else:
		email=input("Your Email:")
		print("Welcome to Our Company, " + first_name + "♡")
		
