"""Take a person's age and whether they have a valid ID (True/False)
can enter a venue only if they are 18 or older AND have a valid ID. Print the
appropriate message."""
age=int(input("Enter your Age"))
id_input=input("Do you have a Valid ID ? (yes/no):").strip().lower()
has_valid_id=id_input in ['yes','y','true']
if age>=18 and has_valid_id:
    print("Welcome to the Venue.")
else:
    print("Access Denied")