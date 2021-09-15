# Function goes here

age = ""
count = 0
MAX_TICKETS = 5


# checks for an integer between two values
def int_check(question):
    error = "Please enter a whole number between 12 and 130"

    valid = False
    while not valid:

        # ask user for number and check if its valid
        try:
            response = int(input(question))
            return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)

while age != "xxx" and count < MAX_TICKETS:

     # end the loop if the exit code is entered
    if age == "xxx":
        break
    # Get age (between 12, 130)
    age = int_check("Age: ")

    if age <= 12:
        print("You are too young for this movie")
        continue
    elif age >= 130:
        print("This is old, are you sure it's not and error")
        continue
    else:
        print("You are the correct age")
        break

    count += 1
