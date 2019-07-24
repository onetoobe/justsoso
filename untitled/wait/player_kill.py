import xlrd
import re

wb = xlrd.open_workbook('F:/新建 XLSX 工作表.xlsx')
sh1 = wb.sheet_by_index(0)
sh2 = wb.sheet_by_index(1)
num = 0
t = []

for rownum in range(sh1.nrows):
    t1 = sh1.row_values(rownum)
    modle = str(int(t1[2]))
    teamid = str(int(t1[4]))
    year1 = str(t1[5])[2:-2]
    lv = int(t1[3])
    ll = len(str(t1[5]))
    caseid = int(t1[0])
    year2 = '0'
    if ll > 13 :
        w1 = '\[\"'
        w2 = '\",\"'
        w3 = '\"\]'
        year1 = str(re.findall(w1 + "(.+?)" + w2, str(t1[5])))[2:-2]
        year2 = str(re.findall(w2 + "(.+?)" + w3, str(t1[5])))[2:-2]
    sa = 0
    # print(caseid,modle,teamid,year1,year2,lv)
    for rownum in range(sh2.nrows):
        t2=sh2.row_values(rownum)
        ctype = sh2.cell(rownum , 55).ctype
        if ctype == 2:
            ny=str(int(t2[55]))
        else:
            ny=str(t2[55])
        if caseid == int(t2[3]) and int(t2[47]) in (0,5):
            t.append(caseid)
        if modle == str(int(t2[2])) and teamid == str(int(t2[0])) and year1 == '0' and lv <= int(t2[4]) and int(t2[47]) not in (0,5):
            sa =+1
        if modle == str(int(t2[2])) and teamid == str(int(t2[0])) and year1 == ny and lv <= int(t2[4]) and int(t2[47]) not in (0,5):
            sa =+1
        if modle == str(int(t2[2])) and teamid == str(int(t2[0])) and year2 == ny and lv <= int(t2[4]) and int(t2[47]) not in (0,5):
            sa =+1
    if sa == 0 and caseid not in t:
        num = num + 1
        print(caseid)
print('合计：'+str(num))








