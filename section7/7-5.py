# coding:utf-8
# 计算出文件的长度

import os

if __name__ == "__main__":
    f = open("./test.txt", "r")
    f2 = open("./test2.txt", "w")
    print "源文件内容：\n"
    while True:
        line = f.readline()
        if line:
            print line
            f2.write(line)
        else:
            break
    f.close()
    f2.close()

    f2=open("./test2.txt", "r")
    print "替换之后的文件:\n"+f2.read()
    f2.close()