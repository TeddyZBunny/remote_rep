def calc(x,y):
    try:
        return x/y
    except (ZeroDivisionError, ValueError) as err:
        print(x,y)
        raise err
        # print(err)
        # print('На ноль делить нельзя')
        
print(calc(int(input('first number ')),int(input('second number '))))