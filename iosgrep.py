import sys, os, hashlib, re

def Search_in_Data(keywordInData, pgname):
        print("# grep -ril -e '%s'  %s :" %(keywordInData, pgname))
        recvAll = os.popen("grep -ril -e '%s' %s  ; echo echo:$?" %(keywordInData, pgname)).read()
        recvCode = re.search('(?<=echo:)\d+', recvAll)
        print("Find" if recvCode.group(0)=='0' else "Not Found")
        print("------")
if __name__=="__main__":
    packagename = sys.argv[1]
    keywordFile = open('name.txt', 'r')
    for keyword in keywordFile.readlines():
        print("---use plaintext to search---\n")
        Search_in_Data(keyword[:-1], packagename)
        Search_in_SystemCatch(keyword[:-1])
        print("---use hex to search---\n")
        Search_in_Data(keyword[:-1].encode("hex"), packagename)
        Search_in_SystemCatch(keyword[:-1].encode("hex"))
        print("---use base64 to search---\n")
        Search_in_Data(keyword[:-1].encode("base64").replace('\n', ''), packagename)
        Search_in_SystemCatch(keyword[:-1].encode("base64").replace('\n', ''))
        print("---use md5 to search---\n")
        Search_in_Data(hashlib.md5(keyword[:-1]).hexdigest(), packagename)
        Search_in_SystemCatch(hashlib.md5(keyword[:-1]).hexdigest())
        print("---use sha1 to search---\n")
        Search_in_Data(hashlib.sha1(keyword[:-1]).hexdigest(), packagename)
        Search_in_SystemCatch(hashlib.sha1(keyword[:-1]).hexdigest())
        print("---use utf-8 to search---\n")
        Search_in_Data(keyword[:-1].decode("utf-8").encode("utf-8"), packagename)
        Search_in_SystemCatch(keyword[:-1].decode("utf-8").encode("utf-8"))
        print("---use binary to search---\n")
        Search_in_Data(''.join(map(bin,bytearray(keyword[:-1]))), packagename)
        Search_in_SystemCatch(''.join(map(bin,bytearray(keyword[:-1]))))
