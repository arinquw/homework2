
print('задание 1')
print('"Don`t compare yourself with anyone in this world...if you do so, you are insulting\n'
      'yourself."\n'
      '\n'
      'Bill Gates')

print('задание 2')

def get_even_numbers(num1, num2):
    start = min(num1, num2)
    end = max(num1, num2)
    even_numbers = []
    for number in range(start, end + 1):
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
result = get_even_numbers(3, 12)
print(f"четные числа: {result}")

print('задание 3')

def xz(side_length, symbol, is_filled):
    for row in range(side_length):
        line = ""
        for col in range(side_length):
            if is_filled:
                line += symbol + " "
            else:
                if row == 0 or row == side_length - 1 or col == 0 or col == side_length - 1:
                    line += symbol + " "
                else:
                    line += "  "
        print(line)
print("заполненный квадрат 6x6:")
xz(6, '#', True)

print("\nпустой квадрат 6x6:")
xz(6, '#', False)
