import re
import os
import time

SLEEP_SEC = 2
FIN = open('list-quyu.txt')
for l in FIN:
    target_url = 'http://bj.lianjia.com/zufang/'+l.strip()
    os.system("wget "+target_url+" -O index/"+re.sub('/', '_', l.strip()))
    time.sleep(SLEEP_SEC)
    file_index_page_1 = open("index/"+re.sub('/', '_', l.strip())).read()
    try:
        totalPage = int(re.findall('{"totalPage":(.*?),"', file_index_page_1)[0])
    except:
        totalPage = 0
    for i in range(2, totalPage+1):
        target_url = 'http://bj.lianjia.com/zufang/'+l.strip()+'/pg'+str(i)
        os.system("wget "+target_url+" -O index/"+re.sub('/', '_', l.strip())+'_pg'+str(i))
        time.sleep(SLEEP_SEC)

print 'Done!'
