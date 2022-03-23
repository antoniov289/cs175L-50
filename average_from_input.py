# Antonio Vinagre, s1303334
#CS 175 L
#Spring 2022
#average_from_input.py

def get_values():
    try:
        nums_file = open('numbers.txt', 'r')
    except IOError:
        print('Error: Make sure the file is in the correct folder with the correct name.')
        tot = 0
        count = -1
    else:
        tot = 0
        count = 0
        for line in nums_file:
            try:
                num = float(line)
            except ValueError:
                print('Error: Some data was not in the form of a valid number and it was skipped.')
            else:
                tot += num
                count += 1
                print(f"I've read in {count} number(s). Current number is: {num}. Total is: {tot}.")
        nums_file.close()
    return tot, count

def calc_avg(total, count):
    avg = total/count
    return avg

def print_avg(average):
    print(f"Average: {average}")

def main():
    tot, count = get_values()
    average = calc_avg(tot, count)
    if count != -1:
        print_avg(average)

if __name__ == '__main__':
    main()
