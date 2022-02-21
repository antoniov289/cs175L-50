#CS175
#Antonio Vinagre
#rainfall.py

NUM_MONTHS = 12
num_years = int(input("How many years are you entering (1, 2, or 3)? "))
total_months = 0
total_rain = 0

while num_years != 1 and num_years != 2 and num_years != 3:
    print('Invalid number of years, please enter again.')
    num_years = int(input("How many years are you entering (1, 2, or 3)? "))

for years in range(num_years):
    print(f'For year {years+1}:')
    for months in range(NUM_MONTHS):
        total_months += 1
        rainfall = float(input('Enter the rainfall amount for the month: '))
        total_rain += rainfall

print(f'For {total_months} months')
print(f'Total rainfall: {total_rain:.2f} inches')
print(f'Average monthly rainfall: {total_rain/total_months:.2f} inches')
