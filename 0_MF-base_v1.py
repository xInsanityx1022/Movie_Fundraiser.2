# Import statements


# functions go here:

# checks that ticket name is not blank


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # if name is not blank, program continues
        if response != "":
            return response

        # if name is blank, show error (& repeat loop)
        else:
            print("Sorry this can't be blank, Please enter your name")


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

# ------------ Main Routine ------------

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if they haven't

# Loop to get ticket details
# start of loop

# initialise loop so that it runs at least once

MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_value = 0

while name != "xxx" and ticket_count < MAX_TICKETS:

    # tell user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))
        print()

    # Warns user that only one is left
    else:
        print("-=* There is only ONE seat left!! *=-")
        print()

    # Get details...

    # Get name (can't be blank)
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # Get age (between 12, 130)
    age = int_check("Age: ")

    if age < 12:
        print("You are too young for this movie")
        continue
    elif age > 130:
        print("This is old, are you sure it's not and error")
        continue

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    ticket_count += 1
    ticket_value += ticket_price

# End ticket loop

# calculate profit made
ticket_profit = ticket_value - {5 * ticket_count}
print("Ticket profit: ${:2.f}".format(ticket_profit))

# tell user if they have sold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all available tickets!")
else:
    print("You have sold {} tickets. Seats remaining {} ".format(ticket_count, MAX_TICKETS - ticket_count))

    # Get age (can't be blank)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # ask for payment method (cash or credit, add surcharge in necessary)


# Calculate total sales and profit

# Output data to text file
