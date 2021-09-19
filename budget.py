#
# budget.py
# dlane
#

print()
print("Please enter your monthly expenses")
print("(in dollars and cents) for the following categories:")
# use the float(input()) function instead of input() to get numeric results
movies  = input("  Movie tickets: ")
itunes  = input("  iTune downloads: ")
clothes = input("  Clothing: ")
food    = input("  Food: ")

print()
total_expenses = movies + itunes + clothes + food
print("Your total monthly expenses are", total_expenses)
print()
