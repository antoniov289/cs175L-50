#expensePieChart.py
#Antonio Vinagre
#CS 175L

import matplotlib.pyplot as plt

def main():
    expenses_file = open('expenses.txt', 'r')

    #put the info into a list seperated by tabs
    expenses = [line.split('\t') for line in expenses_file]
    
    #pull out the expense labels
    expense_labels = [item[0] for item in expenses]
    
    #pull out the expense values and remove the newline
    expense_values = [item[1] for item in expenses]
    expense_values = [int(item[:-1]) for item in expense_values]

    #plot the info
    plt.pie(expense_values, labels = expense_labels)
    plt.title('Monthly Expenses')
    plt.show()

if __name__ == '__main__':
    main()
