numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
len_of_numbers = len(numbers)
index_none = numbers.index(None)
sum_of_numbers = sum(numbers[0:index_none])+sum(numbers[(index_none+1)::])
average = sum_of_numbers/len_of_numbers
numbers[index_none]=average
print("Измененный список:", numbers )
