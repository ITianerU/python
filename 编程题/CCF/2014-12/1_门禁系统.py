"""
题目:涛涛最近要负责图书馆的管理工作，需要记录下每天读者的到访情况。每位读者有一个编号，
    每条记录用读者的编号来表示。给出读者的来访记录，请问每一条记录中的读者是第几次出现。
输入:输入的第一行包含一个整数n，表示涛涛的记录条数。
    第二行包含n个整数，依次表示涛涛的记录中每位读者的编号。
输出:输出一行，包含n个整数，由空格分隔，依次表示每条记录中的读者编号是第几次出现。
输入样例:
5
1 2 1 1 3
输出样例:1 1 2 3 1
"""
n = int(input())
l = input().split(" ")
d = dict()
l2 = list()
for i in range(n):
    if l[i] not in d.keys():
        d[l[i]] = 1
    else:
        d[l[i]] = d[l[i]] + 1
    l2.append(d[l[i]])

for i in l2:
    print(i, end=" ")
print()