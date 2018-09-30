from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print('Encountered comment: ', data)
        pos = self.getpos()
        print('\tAt line: ', pos[0], ' position ', pos[1])

    def handle_starttag(self, tag, attr):
        print('Encountered tag: ', tag)
        pos = self.getpos()
        print('\tAt line: ', pos[0], ' position ', pos[1])

    def handle_endtag(self, tag):
        print('Encountered tag: ', tag)
        pos = self.getpos()
        print('\tAt line: ', pos[0], ' position ', pos[1])

    def handle_data(self, data):
        if (data.isspace())
            return
        print('Encountered data: ', data)
        pos = self.getpos()
        print('\tAt line: ', pos[0], ' position ', pos[1])



def main():
    parser = MyHTMLParser()
    f = open('samplehtml.html')
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)


if __name__ == '__main__':
    main()
