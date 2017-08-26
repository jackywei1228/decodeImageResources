# -*- coding: utf-8 -*-
#!/usr/bin/env python
from struct import *

from pprint import pprint

import json

jsonfile = '/home/jackywei/myGreatWork/photo/map.json'

def load():
    with open(jsonfile) as json_file:
        data = json.load(json_file)
        return data

file = open("/home/jackywei/myGreatWork/photo/fusion.mbn", "rb")

(notuseData,myoffset) = unpack("II",file.read(4+4))

print ("myoffset is %08x "%(myoffset))


fjson = open(jsonfile,'wb')


filedata = file.read(myoffset)

fjson.write(filedata)
fjson.close()

data = load()

offsetstart = file.tell()

for i in range(len(data)):
    #print i,data[i]
    print "================================"
    print data[i]['name'],data[i]['size']
    fmap = open('/home/jackywei/myGreatWork/photo/%s'%(data[i]['name']),'wb')
    print ("offset = %08x,json offset = %08x,logic offset = %08x"%(file.tell(),data[i]['offset'],(file.tell() - offsetstart)))
    filedata = file.read(data[i]['size'])
    fmap.write(filedata)
    fmap.close()

file.close()
