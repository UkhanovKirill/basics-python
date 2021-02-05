my_str = input("введите предложение ")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    print(f" {num} {my_word [el] [0:10]}")
    num += 1