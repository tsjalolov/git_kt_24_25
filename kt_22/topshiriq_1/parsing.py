print('salom')
import requests as re
respons = re.get('https://google.com')
html = respons.text
#print(html)
from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, gsc_a_t):
#         print("Encountered a start tag:", tag)
#
#     # def handle_endtag(self, tag):
#     #     print("Encountered an end tag :", tag)
#     #
#     # def handle_data(self, data):
#     #     print("Encountered some data  :", data)
#
# parser = MyHTMLParser()
# parser.feed(html)


from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = chr(int(name[1:], 16))
    #     else:
    #         c = chr(int(name))
    #     print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser(html)