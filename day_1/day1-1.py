
# Import data
with open(r'day_1/raw_data.txt') as data:
    # Set sum variable for later (sum of all lines)
    sum = 0
    # Go through each line in data
    for line in data:
        # Strip away \n to be able to work with data
        line = line.strip('\n')
        # Remove all letters
        no_letters = (line.translate(
            {ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'}))
        # Add first number index 0
        firstnum = no_letters[0]
        # Add last number index -1
        lastnum = no_letters[-1]
        # Add first number and last number (strings) to variable number
        number = firstnum + lastnum
        # Add integer version of number to sum variable
        sum += int(number)
    # Print sum to get final result
    print(sum)
