import re

FIN = open('list-index.txt')
FOUT = open('list-house.txt','w')
for l in FIN:
    file_index_pg = open(l.strip()).read()
    house_list = re.findall('<li data-index="\d+" data-id="(.*?)">', file_index_pg.split('<ul id="house-lst" class="house-lst">')[1])
    for i in house_list:
        out = 'http://bj.lianjia.com/zufang/'+i+'.html'
        FOUT.write(out)
FOUT.close()
print 'Done!'
