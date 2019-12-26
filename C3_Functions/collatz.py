def validate_user_input():
    while True:
        try:
            number = int(input("Enter a positive integer (minimum 2): "))
        except KeyboardInterrupt:
            print('\nSee you next time!')
            break
        except ValueError:
            print("That was not even a valid integer!")
        else:
            if number < 0:
                print("Positive integer, please!")
            elif number < 2:
                print("Integer should be at least equal to 2 !")
            else:
                return number


def collatz(n):
    if n == 1:
        return
    else:
        new_number = n // 2 if n % 2 == 0 else n * 3 + 1
        print(new_number)
        collatz(new_number)


if __name__ == '__main__':
    print('Collatz Conjecture Collatz Conjecture')
    number = validate_user_input()
    collatz(number)
