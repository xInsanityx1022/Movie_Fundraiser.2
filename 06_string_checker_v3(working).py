

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

    if is_valid != "yes":
        return "Invalid choice"
    # if the snack is not OK - ask question again
    else:
        return chosen


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
snack_list = ["Popcorn ( p, corn, a)",
              "M&M's (m&m's, m, b)",
              "Pita chips (chips, pc, pita, c)",
              "Water (w, d)"
]
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]


snack_order = []

# ask user if they would want a snack
check_snack = "Invalid choice"
while check_snack == "Invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

# If they say yes ask what snacks they want
if check_snack == "Yes":

    desired_snack = ""
    print(snack_list)
    while desired_snack != "xxx":

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

        snack_choice = string_check(desired_snack, valid_snacks)
        print("Snack Choice: ", snack_choice)

        if snack_choice != "xxx" and snack_choice != "Invalid Choice":
            snack_order.append(snack_choice)

print()
if len(snack_order) == 0:
    print("Snack Ordered: None")

else:
    print("Snacks Ordered: ")

    for item in snack_order:
        print(item)
