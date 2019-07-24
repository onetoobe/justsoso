import re,chardet
import os
import MySQLdb

# def get_txt(file,w1,w2):
#     f = open(file, 'rb')
#     a = []
#     text = f.readlines()
#     for lines in text:
#         result = re.findall(w1+"(.+?)"+w2, str(lines.decode()))
#         for x in result:
#             a.append(x.strip())
#     f.close()
#     return a
#
# file = 'F:/测试.txt'
# w1 = '*<'
# w2 = '存在差异'
#
# print(get_txt(file,w1,w2))
#
# def get_mysql(sql):
#     # 打开数据库连接
#     db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8')
#     # 使用cursor()方法获取操作游标
#     cursor = db.cursor()
#
#     cursor.execute(sql)
#
#     # 关闭数据库连接
#     db.close()

# final = []
# tip = 0
# for i1 in t1:
#     final.append(nx[i1 - 1])
#     for i2 in range(lines[tip] - 1):
#         final.append(nx[i1 - 1 + i2])
#     tip = tip + 1



def get_txt(file):
    test = open(file, 'rb')
    text = test.readlines()
    n = []
    for txt in text:
        n.append(txt.decode())
    test.close()
    return n


def get_table_num(file,w1,w2):
    n = 0
    table = []
    txt = get_txt(file)
    for text in txt:
        result = re.findall(w1 + "(.+?)" + w2, text)
        n = n + 1
        if result != []:
            table.append(n)
    return table

def get_diffrict_num(file):

    t1 = get_table_num(file,'<','>存在差异')
    t2 = get_table_num(file,'<','>完全一致')

    nx = get_txt(file)

    n = 0
    lines = []
    for i1 in t1:
        for i2 in t2:
            if i2 > i1 and n == len(t1)-1:
                lines.append(i2 - i1)
                break
            if i2 > i1 and n != len(t1)-1:
                if t1[n+1] < i2:
                    lines.append(t1[n+1]-i1)
                    break
                else:
                    lines.append(i2-i1)
                    break
        n=n+1

    final = []
    tip = 0
    for i1 in t1:
        final.append(lines[tip]-1)
        tip = tip+1
    return final

def get_diffrite_table(file):
    t1 = get_table_num(file, '<', '>存在差异')
    nx = get_txt(file)
    final = []
    tip = 0
    for i1 in t1:
        final.append(nx[i1-1])
        tip = tip+1
    return final

a = get_diffrict_num('F:/测试.txt')
b = get_diffrite_table('F:/测试.txt')
c = get_diffrict_num('F:/测试2.txt')
d = get_diffrite_table('F:/测试2.txt')
print(a)
print(len(a))
print(b)
print(len(b))
print(c)
print(len(c))
print(d)
print(len(d))