from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request



class MyHTMLParser(HTMLParser):


    def __init__(self):
          HTMLParser.__init__(self)
          self.event_info = []
          self.temp_dict = {}
          self.flag = 0

    def handle_starttag(self, tag, attrs):
        #print('<%s>' % tag)
        #print('attrs1:%s' % attrs)
        #print('type!!!!!!!!!!!!!!!%s'% type(attrs))
        if ('class', 'event-title') in attrs:
            self.flag = 1
        if 'time' == tag:
            self.flag = 2
        if ('class', 'event-location') in attrs:
            self.flag = 3


    def handle_endtag(self, tag):
        #print('</%s>' % tag)
        pass

    def handle_startendtag(self, tag, attrs):
           #print('<%s/>' % tag)
        #print('attrs2:%s' % str(attrs))
        pass

    def handle_data(self, data):
        #print('data:+++++++++++++++:%s' % data)
        if self.flag == 1:
            self.temp_dict['name'] = data
            self.flag = 0

        if self.flag == 2:
            self.temp_dict['date'] = data
            self.flag = 0

        if self.flag == 3:
            self.temp_dict['address'] = data
            self.flag = 0
            self.event_info.append(self.temp_dict)
            self.temp_dict = {}
            #print("add a new info : %s" % self.event_info)

    def handle_comment(self, data):
        #print('<!--', data, '-->')
        pass

    def handle_entityref(self, name):
        #print('&%s;' % name)
        pass

    def handle_charref(self, name):
        #print('&#%s;' % name)
        pass

    def print_info(self):
        for n in self.event_info:
            print('events: %s' % n['name'])
            print('date: %s' % n['date'])
            print('address: %s' % n['address'])
            print('-----------------------------------------------------')

if __name__ == '__main__':
    with request.urlopen('https://www.python.org/events/python-events/') as f:
        data = f.read()
        parser = MyHTMLParser()
        parser.feed(data.decode('utf-8'))
        parser.print_info()