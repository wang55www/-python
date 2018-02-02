# -*-coding: UTF-8-*-
#存在字符串"I,love,python", 取出love并输出


import re;

if __name__ == "__main__":
    s="I,love,python";
    print(re.findall(r"love",s));
    print(s[2:6]);