# coding:utf-8

if __name__ == "__main__":
    f = open("./test.txt", "r")
    f2 = open("./test2.txt", "w")
    print "源文件内容：\n"
    while True:
        line = f.readline()
        if line:
            print line
            line=line.replace("\n","")
            f2.write(line)
        else:
            break
    f.close()
    f2.close()

    f2=open("./test2.txt", "r")
    print "替换之后的文件"+f2.read()
    f2.close()