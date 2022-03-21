# Antonio Vinagre, s1303334
#CS 175 L
#Spring 2022
#average_from_input.py

def main():
    nums_file = open('numbers.txt', 'r')
    line = nums_file.readline()
    tot = 0
    count = 0
    for line in nums_file:
        num = float(line)
        tot += num
        count += 1
        print(f"I've read in {count} number(s). Current number is: {num}. Total is: {tot}.")

    print(f"Average: {tot/count}")
        
    nums_file.close()

if __name__ == '__main__':
    main()
