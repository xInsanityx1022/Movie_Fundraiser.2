import re

# Function goes here

def string_check(choice, options):

    for var_list in options:

        # if the snack is in the list, return the full
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"

number_regex = "^[1-9]"

# valid snacks holds list of all snacks
# Each item in valid snacks is a list with
# valid options for each snack <full name, letter code (a - e)
# , and possible abbreviations etc>
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "m", "b"],
    ["Pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]


snack_order = []

# ask user if they would want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

# If they say yes ask what snacks they want
if check_snack == "Yes":
    print("Popcorn ( p, corn, a) | M&M's (m&m's, m, b) | Pita chips (chips, pc, pita, c) | Water (w, d)")

    desired_snack = ""
    while desired_snack != "xxx":

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        desired_snack = desired_snack.strip()

        snack_choice = string_check(desired_snack, valid_snacks)

        if amount >= 5:
            print("Sorry - We have four snacks maximum")
            snack_choice = "invalid choice"

        amount_snack = "{} {}".format(amount, snack_choice)

        if snack_choice != "xxx" and snack_choice != "invalid hoice":
            snack_order.append(snack_choice)

print()
if len(snack_order) == 0:
    print("Snack Ordered: None")

else:
    print("Snacks Ordered: ")

    for item in snack_order:
        print(item)

