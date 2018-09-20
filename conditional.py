
def main():
    x, y = 100, 100
    print('x: ', x, 'y: ', y)

    if (x < y):
        st = 'x is less than y'
    elif(x > y):
        st = 'x is greater than y'
    elif(x == y):
        st = 'x is same with y'
    else:
        st = 'It is damm status'

    print(st)


if __name__ == '__main__':
    main()
