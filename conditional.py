
def main():
    x, y = 10, 100
    print('x: ', x, 'y: ', y)

    # if (x < y):
    #     st = 'x is less than y'
    # elif(x > y):
    #     st = 'x is greater than y'
    # elif(x == y):
    #     st = 'x is same with y'
    # else:
    #     st = 'It is damm status'

    st = 'x is less than y' if (x<y) else 'x is greater than or the same as y'

    print(st)


if __name__ == '__main__':
    main()
