import json

import urllib
import urllib.request

def read_more(file_name):
    with open(file_name, 'r') as f:
        temp = json.loads(f.read())
        contents = temp['blocks']
        i = 1
        for item in contents.get('items'):
            print('***',i)
            print(item.get('title'))
            print(item.get('description'))
            print(item.get('author')['name'])
            print(item.get('url'))
            print(item['id'])
            # timestamp
            i += 1



def read_page(url):
    file = urllib.request.urlopen(url)
    data = json.load(file)
    # data = file.read()

    return data

def extract_more_article():
    url = 'https://www.forbes.com/simple-data/chansec/stream/?'
    i = 56
    ids="content_607f2f787bb57e000687cd87"
    while True:
        url = url+"date=1618958253669&start="+str(i)+"&ids="+ids+"&limit=25&sourceValue=channel_1&swimLane=&specialSlot=&streamSourceType=channelsection"

        data = read_page(url)

        write_file(data, i)

        ids = data['blocks'].get('items')[9]['id']

        i += 10
        if i > 56:
            break

def write_file(data, i):
    f = open(str(i) + '.json', 'w')
    json.dump(data, f)
    f.close()

# extract_more_article()
# read_more(str(46)+'.json')

