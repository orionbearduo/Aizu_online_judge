#Write a program which reads an integer and prints sum of its digits.

while True:
    table = str(input())
    if(table[0] == '0'):
        break
    print(sum(int(num) for num in(table)))
