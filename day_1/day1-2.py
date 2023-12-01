
# Calibration

with open(r'day_1/raw_data.txt') as data:
    sum = 0
    for line in data:
        # print("ny rad\n\n")
        line = line.strip('\n')
        no_letters = (line.translate(
            {ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'}))
        first_letter = no_letters[0]
        # print(first_letter)
        last_letter = no_letters[-1]
        # print(last_letter)
        number = first_letter + last_letter
        sum += int(number)
    print(sum)


# with open(r'day_1/calibrationdata.txt') as calibration_data:
#     no_letters = ''
#     for line in calibration_data:
#         no_letters = (line.translate(
#             {ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'}))
#         rangeob = len(no_letters)
#         print(rangeob)
#         # print(no_letters[0, -1, rangeob - 1])

#     print(no_letters)

# with open(r'day_1/calibrationdata.txt') as calibration_data:
#     clean_string = ''
#     temp_list = ''
#     final_list = []
#     for line in calibration_data:
#         temp_string = (line.translate(
#             {ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'}))
#         temp_list += (temp_string.split('\n'))
#     print(temp_list)

# clean_string = clean_string.split('\n')


# for i in clean_string:

#    print(i[0], i[-1])
