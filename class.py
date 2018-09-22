class myClass:
    def method1(self):
        print('myClass method1')

    def method2(self, someStrings):
        print('myClass method2 ' + someStrings)

class anotherClass:
    def method1(self):
        print('anotherClass method1')

    def method2(self, someStrings):
        print('anotherClass method2 ' + someStrings)

def main():
    c = myClass()
    c.method1()
    c.method2('This is a string')

    d = anotherClass()
    d.method1()
    d.method2('Wow this is anoter string')

if __name__ == '__main__':
    main()
