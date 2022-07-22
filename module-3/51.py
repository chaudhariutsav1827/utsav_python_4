a = int(input('Enter number: '))


def fact(a1):
        if a1 > 0:
            fac = 1
            for i in range(a1):
                fac = fac * a1
                a1 -= 1
        else:
            print('Please enter positive number.')
            return
        print(fac)


fact(a)
