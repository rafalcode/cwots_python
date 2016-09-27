#!/usr/bin/env python2.7
# as well as playing aroudn with envvars, this script also tests a restful api from Kyoto Genome Databank
import os, sys, urllib2

if os.environ.get('http_proxy') is None:
        os.environ['http_proxy']="http://172.25.64.1:3128"

        resp0=urllib2.urlopen("http://rest.kegg.jp/link/ko/ec:3.1.11.1")
        output=resp0.read()
        print output,
