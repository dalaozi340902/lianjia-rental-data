import re
import os
import time

SLEEP_SEC = 2
FIN = open('list-house.txt')
for l in FIN:
    target_url = l.strip()
    house_name = l.split('zufang/')[1].split('.html')[0]
    os.system('mkdir prod/'+house_name)
    os.system("wget "+target_url+" -O prod/"+house_name+'/detailPage.html')
    file_detail = open('prod/'+house_name+'/detailPage.html').read()
    resblockId = re.findall("resblockId:'(.*?)',", file_detail)[0]
    houseId = re.findall("houseId:'(.*?)',", file_detail)[0]
    xhr_url = 'http://bj.lianjia.com/zufang/housestat?hid='+houseId+'&rid='+resblockId
    os.system("wget "+xhr_url+" -O prod"+house_name+'/xhr.txt')
    time.sleep(SLEEP_SEC)
    image_part = file_detail.split('<div class="img" id="topImg">')[1].split('</ul>')[0]
    lis = re.findall('<li data-src=(.*?)><img src=', image_part)
    for i in lis:
        img_url = i.split('"')[1]
        img_name = i.split('"')[3]
        img_num = img_url.split('/')[-1].split('.')[0]
        location = 'prod/'+house_name+'/'+img_name+'_'+img_num+'.jpg'
        os.system('wget '+img_url+' -O '+location)
        time.sleep(SLEEP_SEC-1)
print 'Done!'
