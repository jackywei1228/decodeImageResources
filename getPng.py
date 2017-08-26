# -*- coding: utf-8 -*-
#!/usr/bin/env python
from struct import *

from pprint import pprint

import json
import os
import os.path
import zlib

def load(myfile):
    with open(myfile) as json_file:
        data = json.load(json_file)
        return data

#"/home/jackywei/myGreatWork/photo/fusion.mbn"
def readmbn(filename,curdir):
    mbndirname = filename.split(".")[-2].split(os.sep)[-1]
    subdir = curdir+os.sep+mbndirname
    print subdir
    try:
        os.mkdir(subdir)
    except OSError,e:
        print e.message
    mbnfile = open(filename, "rb")
    (notuseData,myoffset) = unpack("II",mbnfile.read(4+4))
    print ("myoffset is %08x "%(myoffset))
    fjsonname = subdir+os.sep+mbndirname+'.json'
    print "fjsonname = %s" % fjsonname
    fjson = open(fjsonname,'wb')
    filedata = mbnfile.read(myoffset)
    fjson.write(filedata)
    fjson.close()
    data = load(fjsonname)
    offsetstart = mbnfile.tell()
    for i in range(len(data)):
        #print i,data[i]
        print "================================"
        print data[i]['name'],data[i]['size']
        print (subdir+os.sep+"%s" % (data[i]['name']))
        productname = subdir+os.sep+"%s" % (data[i]['name'])
        fmap = open(productname,'wb')
        print ("offset = %08x,json offset = %08x,logic offset = %08x"%(mbnfile.tell(),data[i]['offset'],(mbnfile.tell() - offsetstart)))
        filedata = mbnfile.read(data[i]['size'])
        if data[i]['name'].split(".")[-1] == 'dds':
            fmap.write(zlib.decompress(filedata))
        else:
            fmap.write(filedata)
        fmap.close()
    mbnfile.close()

if __name__ == '__main__':
    print os.path.realpath(__file__)
    print "os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__))
    curdir = os.path.dirname(os.path.realpath(__file__))
    for parent,dirnames,filenames in os.walk(os.path.dirname(os.path.realpath(__file__))):
        #print "========================"
        #for dirname in  dirnames: 
        #    print "parent is:" + parent
        #    print  "dirname is" + dirname

        for filename in filenames:
            #print "parent is" + parent
            #print "filename is:" + filename
            #print "the full name of the file is:" + os.path.join(parent,filename)
            tempfilename = os.path.join(parent,filename)
            if tempfilename.split(".")[-1] == "mbn":
                print tempfilename
                readmbn(tempfilename,curdir)

