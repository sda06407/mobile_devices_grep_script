#!/usr/bin/env python
import sys, os, hashlib, re

def Search_in_Data(keywordInData, pgname):
        print("# grep -ril -e '%s'  %s :" %(keywordInData, pgname))
        recvAll = os.popen("grep -ril -e '%s' %s  ; echo echo:$?" %(keywordInData, pgname)).read()
        recvCode = re.search('(?<=echo:)\d+', recvAll)
        print("Find" if recvCode.group(0)=='0' else "Not Found")
        print("------")
if __name__=="__main__":
    packagename = sys.argv[2]
    keywordFile = open(sys.argv[1], 'r')
    for keyword in keywordFile.readlines():
        print("---use plaintext to search---\n")
        Search_in_Data(keyword[:-1], packagename)
        print("---use hex to search---\n")
        Search_in_Data(keyword[:-1].encode("hex"), packagename)
        print("---use base64 to search---\n")
        Search_in_Data(keyword[:-1].encode("base64").replace('\n', ''), packagename)
        print("---use md5 to search---\n")
        Search_in_Data(hashlib.md5(keyword[:-1]).hexdigest(), packagename)
        print("---use sha1 to search---\n")
        Search_in_Data(hashlib.sha1(keyword[:-1]).hexdigest(), packagename)
        print("---use utf-8 to search---\n")
        Search_in_Data(repr(keyword[:-1]).replace("'",""), packagename)
        print("---use binary to search---\n")
        Search_in_Data((' '.join(format(ord(x), 'b')for x in keyword[:-1]).replace(' ','\s')), packagename)
        print("---use unicode to search---")
        Search_in_Data(repr(keyword[:-1].decode("utf-8")).replace("u", "", 1).replace("'", ""), packagename)
