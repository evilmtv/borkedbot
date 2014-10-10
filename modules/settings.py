import sys
sys.dont_write_bytecode = True

import os, cPickle

LOAD_ORDER = 50

datafilename = 'settings.data'
data = {}

if not os.path.isfile(datafilename):
    with open(datafilename, 'w') as f:
        cPickle.dump(dict(), f)


def loadsettings():
    global data
    with open(datafilename, 'r') as f:
        data = cPickle.load(f)


def savesettings():
    with open(datafilename, 'w') as f:
        cPickle.dump(data, f)

def getdata(key):
    loadsettings()
    return data[key]

def setdata(key, value, announce=True):
    loadsettings()
    global data

    if key in data.keys():
        if data[key] != value and announce:
            print "[Settings] Key %s changed: %s -> %s" % (key, data[key], value)
    
    if key not in data.keys():
        print "[Settings] Key added: %s (%s)" % (key, value)

    data[key] = value
    
    savesettings()

def trygetset(key, value, announce=True):
    loadsettings()
    try:
        return data[key]
    except:
        setdata(key, value, announce)
        return data[key] 


def setup(bot):
    return

def alert(event):
    return


loadsettings()