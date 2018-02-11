# coding:utf-8

if __name__ == "__main__":
    f = open("./test.txt", "r")
    while True:
        line = f.readline()
        if line:
            print (line)
        else:
            break;
    f.close()
