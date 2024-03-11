def filter_short_strings(input_arr):
    output_arr = []
    for string in input_arr:
        if len(string) <= 3:
            output_arr.append(string)
    return output_arr

# Ввод массива строк с клавиатуры
n = int(input("Введите количество строк в массиве: "))
input_arr = []
for i in range(n):
    input_arr.append(input(f"Введите строку {i + 1}: "))

result_arr = filter_short_strings(input_arr)

print("Новый массив из строк, длина которых меньше или равна 3 символам:")
for string in result_arr:
    print(string)
