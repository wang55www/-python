#coding:utf-8
'''
 存在字符串"ab2b3n5n2n67mm4n2"，编程实现下面要求
    1)使用re取出字符串中所有的数字，并组合成一个新的字符串输出.
    2)统计字符串中字幕n出现的次数
    3)统计每个字符出现的次数，使用字段输出，如：{'a':1,'b':2}。
'''
import re;

if __name__ == "__main__":
    s="ab2b3n5n2n67mm4n2";
    #1)
    print "".join(re.findall(r"\d",s));
    #2)
    print re.subn("n","n", s)[1];
    #3)
    li = list(s);
    dict={};
    for i in range(0,len(li),1):
        if dict.has_key(li[i]):
            continue;
        dict[li[i]]=re.subn(li[i],"",s)[1];
    print dict;