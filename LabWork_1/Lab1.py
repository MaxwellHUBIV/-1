numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missed_number = 4

numbers_summ = sum(numbers[:missed_number]) + sum(numbers[missed_number+1:])
amount_of_numbers = len(numbers)
average_number = numbers_summ / amount_of_numbers

numbers[missed_number] = average_number

print("Измененный список:", numbers)
