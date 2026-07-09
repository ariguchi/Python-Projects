
ch = 0

print('=== === CALCULATOR === ===\n')
first_int = int(input('Enter First no: '))
second_int = int(input('Enter Second no: '))

try:
    while True:
        print('\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Floor Division\n 6. Exit')
        ch = int(input('Enter your choice: '))

        if ch == 1:
            print(first_int+second_int)

        elif ch == 2:
            print(first_int-second_int)

        elif ch == 3:
            print(first_int*second_int)

        elif ch == 4:
            try:
                print(first_int/second_int)
            except Exception:
                print('Number is not divisible by 0')

        elif ch == 5:
            try:
                print(first_int//second_int)
            except Exception:
                print('Number is not divisible by 0')

        elif ch == 6:
            break

        else:
            print('Invalid Choice')

except ValueError:
    print('Invalid Response')