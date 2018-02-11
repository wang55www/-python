# coding:utf-8
# 计算出文件的长度

import os

if __name__ == "__main__":
    print os.stat("./test.txt")[6]