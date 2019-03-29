"""
题目:涛涛最近要负责图书馆的管理工作，需要记录下每天读者的到访情况。
    每位读者有一个编号，每条记录用读者的编号来表示。给出读者的来访记录，请问每一条记录中的读者是第几次出现。
输入:输入的第一行包含一个整数n，表示涛涛的记录条数。
    第二行包含n个整数，依次表示涛涛的记录中每位读者的编号。
输出:输出一行，包含n个整数，由空格分隔，依次表示每条记录中的读者编号是第几次出现。
输入样例:
5
1 2 1 1 3
输出样例:1 1 2 3 1
提示:1≤n≤1,000，读者的编号为不超过n的正整数。
"""


n = int(input())
mod = 1000000007
a = [[0, 0, 0, 0, 0, 0] for i in range(n)]
a[0][0] = 1
for i in range(1, n):
    j = i-1
    # 2
    a[i][0] = (a[j][0]) % mod
    # 20
    a[i][1] = (a[j][0] + a[j][1] * 2) % mod
    # 23
    a[i][2] = (a[j][0] + a[j][2]) % mod
    # 201
    a[i][3] = (a[j][1] + a[j][3] * 2) % mod
    # 203/230
    a[i][4] = (a[j][1] + a[j][2] + a[j][4] * 2) % mod
    # 2013/2031/2301
    a[i][5] = (a[j][3] + a[j][4] + a[j][5] * 2) % mod

print(a[n-1][5])
