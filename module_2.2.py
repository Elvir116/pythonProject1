first = int(input('first: '))
second = int(input('second: '))
third = int(input('third: '))
if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)