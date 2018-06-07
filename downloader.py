#!/usr/bin/env python

import requests;
import sys;
import os;

PY3 = sys.version_info[0] == 3
if PY3:
    from urllib.request import urlretrieve
    from urllib.parse import urlparse
else:
    from urllib import urlretrieve
    from urlparse import urlparse


links = sys.argv[1:];
downloadlink = "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=47.0&x=id%3D{}%26installsource%3Dondemand%26uc"
extensionids = [];
for link in links:
    urlinfo = urlparse(link)
    extensionids.append(os.path.basename(urlinfo.path))

for extensionid in extensionids:
    link = downloadlink.format(extensionid);
    extensiondownload = requests.get(link,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"}).url;
    urlretrieve(extensiondownload,"/tmp/{}.crx".format(extensionid));

