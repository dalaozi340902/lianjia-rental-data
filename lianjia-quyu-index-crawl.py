import urllib2
import re
import time

send_headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language':'en-US,en;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'lianjia_uuid=c3f9bf73-a7c6-4335-9505-6e7a0d3cd14b; all-lj=78917a1433741fe7067e3641b5c01569; UM_distinctid=15c16234ef866f-026242b6620246-3060750a-384000-15c16234ef97de; sample_traffic_test=test_66; select_city=110000; _jzqx=1.1495020032.1495104547.3.jzqsr=bj%2Elianjia%2Ecom|jzqct=/zufang/101101081549%2Ehtml.jzqsr=bj%2Elianjia%2Ecom|jzqct=/zufang/xicheng/rp5/; _jzqckmp=1; _smt_uid=591c252a.1ff07a8e; CNZZDATA1253477573=2006911211-1495018952-http%253A%252F%252Fbj.lianjia.com%252F%7C1495105384; CNZZDATA1254525948=1357100158-1495015654-http%253A%252F%252Fbj.lianjia.com%252F%7C1495108236; CNZZDATA1255633284=1307601192-1495015498-http%253A%252F%252Fbj.lianjia.com%252F%7C1495106533; CNZZDATA1255604082=1440600964-1495015105-http%253A%252F%252Fbj.lianjia.com%252F%7C1495106958; _qzja=1.314032439.1495020031782.1495023683575.1495104547049.1495109903111.1495109904522.0.0.0.88.3; _qzjb=1.1495104547049.34.0.0.0; _qzjc=1; _qzjto=34.1.0; _jzqa=1.3139688295267249000.1495020032.1495023683.1495104547.3; _jzqc=1; _jzqb=1.34.10.1495104547.1; _ga=GA1.2.497642741.1495020034; _gid=GA1.2.1514393581.1495109906; lianjia_ssid=69be2811-497b-af22-e9c6-6c3f9dfaa141',
'Host':'bj.lianjia.com',
'Pragma':'no-cache',
'Referer':'http://bj.lianjia.com/zufang/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

SLEEP_SEC = 5
FIN = open('list-quyu.txt')
for l in FIN:
    target_url = 'http://bj.lianjia.com/zufang/'+l.strip()
    req = urllib2.Request(target_url, headers=send_headers)
    r = urllib2.urlopen(req).read()
    FOUT = open('index/' + re.sub('/', '_', l.strip()), 'w')
    FOUT.write(r)
    FOUT.close()
    #os.system("wget "+target_url+" -O index/"+re.sub('/', '_', l.strip()))
    time.sleep(SLEEP_SEC)
    file_index_page_1 = open("index/"+re.sub('/', '_', l.strip())).read()
    try:
        totalPage = int(re.findall('{"totalPage":(.*?),"', file_index_page_1)[0])
    except:
        totalPage = 0
    for i in range(2, totalPage+1):
        target_url = 'http://bj.lianjia.com/zufang/'+l.strip()+'/pg'+str(i)
        req = urllib2.Request(target_url, headers=send_headers)
        r = urllib2.urlopen(req).read()
        FOUT = open('index/'+re.sub('/', '_', l.strip())+'_pg'+str(i), 'w')
        FOUT.write(r)
        FOUT.close()
        #os.system("wget "+target_url+" -O index/"+re.sub('/', '_', l.strip())+'_pg'+str(i))
        time.sleep(SLEEP_SEC)

print 'Done!'
