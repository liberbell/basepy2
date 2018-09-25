def main():
    f = open('textfile.txt', 'w+')

    for i in range(10):
        f.write('This is line ' + str(i) + '\r\n')

    f.close()

if __name__ == '__main__':
    main()
