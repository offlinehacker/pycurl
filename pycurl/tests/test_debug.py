# $Id$

import pycurl

def test(t, b):
    print "debug(%d): %s" % (t, b)

c = pycurl.Curl()
c.setopt(pycurl.URL, 'http://curl.haxx.se/')
c.setopt(pycurl.VERBOSE, 1)
c.setopt(pycurl.DEBUGFUNCTION, test)
c.perform()
c.close()
