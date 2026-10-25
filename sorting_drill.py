# -*- coding: utf-8 -*-
"""
加练 · 12 道 —— 2026-10-07

你自己的定位：
    ex3（多关键字排序）、ex4（Counter 并列规则）最不熟练
    → 这两块是本文件的【重头戏】，各给了 3 道递进练习（ex1~ex3 / ex4~ex6）
    其他列表操作也想要练习
    → ex7~ex12 覆盖切片、去重、求和、反转、字符串排序

用法：
    1) 填下面每个 def exN() 的函数体（把 raise NotImplementedError 那一行删掉）
    2) 全填完跑：  python sorting_drill.py
    3) 只跑某一道： python sorting_drill.py ex4

═══ 本次要刻进肌肉记忆的三条 ═══
    ① 一行若干整数   → list(map(int, input().split()))
       一行一个整数   → int(input())
    ② 多关键字排序   → sorted(data, key=lambda x: (-第一关键字, 第二关键字))
       降序加负号；关键字按 【优先级从左到右】 排
    ③ Counter 并列   → most_common() 并列时不可控！
       要定规则就自己写：sorted(cnt.items(), key=lambda x: (x[1], x[0]))
                     格式： (元素, 次数)  →  x[0]=元素  x[1]=次数
"""

import sys
from collections import Counter


# ════════════════════════════════════════════════════════════
# 组 A · 多关键字排序（对应你卡住的 ex3）
# ════════════════════════════════════════════════════════════

def ex1():
    """
    题：输入 n 个商品，每行「商品名 价格 销量」。
        按【销量从高到低】排，销量相同的按【价格从低到高】排。
        输出排序后的商品名，一行一个。

    样例输入：
        4
        苹果 5 100
        香蕉 3 100
        橙子 8 50
        葡萄 3 80

    样例输出：
        香蕉
        苹果
        葡萄
        橙子

    解释：销量 100/100/50/80 → 香蕉和苹果并列 100，按价格 3 < 5 → 香蕉在前。

    提示（照抄结构，只换关键字）：
        data.append((name, int(price), int(sales)))
        data.sort(key=lambda x: (-x[2], x[1]))     # 注意下标：价格在第1位，销量在第2位
        遍历输出 x[0]
    """
    n=int(input())
    data=[]
    for i in range(n):
        a=input().split()
        fruit=a[0]
        price=int(a[1])
        sales=int(a[2])
        data.append((fruit,price,sales))
    data.sort(key=lambda x:(-x[2],x[1]))
    for s in data:
        print(s[0])



def ex2():
    """
    题：输入 n 个学生，每行「姓名 语文 数学 英语」。
        按【总分从高到低】排，总分相同按【姓名升序】排。
        输出排序后的姓名，一行一个。

    样例输入：
        3
        Tom 80 90 70
        Amy 90 90 60
        Bob 70 70 70

    样例输出：
        Amy
        Tom
        Bob

    解释：总分 240 / 240 / 210 → Tom 和 Amy 并列 240，按姓名升序
          "Amy" < "Tom" → Amy 在前。

    ⚠️ 关于"姓名升序"：Python 比字符串是按【Unicode 码点】逐个字符比，
       不是按拼音。比如 "张"(U+5F20) < "李"(U+674E)，所以汉字排序结果
       和你的拼音语感可能不一致 —— 比赛里遇到汉字排序，以码点为准。

    提示：这里你【不能】直接用 -x[...]，因为总分是【三个数加起来】算出来的，
          不是现成的某一项。
          解决：先把总分算出来存进去，变成一个现成的数字。

          data.append((name, total))          # total = int(yw) + int(sx) + int(yy)
          data.sort(key=lambda x: (-x[1], x[0]))
    """
    n = int(input())
    data = []
    for i in range(n):
        a = input().split()
        name = a[0]
        total = int(a[1]) + int(a[2]) + int(a[3])
        data.append((name, total))
    data.sort(key=lambda x: (-x[1], x[0]))
    for s in data:
        print(s[0])


def ex3():
    """
    题（三个关键字）：输入 n 个人，每行「姓名 年龄 身高」。
        按【年龄从小到大】排；年龄相同的按【身高从高到低】排；
        都相同的按【姓名升序】排。
        输出排序后的人名，一行一个。

    样例输入：
        4
        Tom 18 175
        Amy 18 180
        Bob 20 170
        Zoe 18 180

    样例输出：
        Amy
        Zoe
        Tom
        Bob

    解释：年龄 18/18/20/18 → 18 岁组是 Tom(175) Amy(180) Zoe(180)
          身高降序：Amy 和 Zoe 并列 180 → 姓名升序 Amy < Zoe → Amy, Zoe, Tom。

    提示：三个关键字的元组就是 (-x[?], -x[?], x[?])，注意每个的方向。
          年龄升序 → 不加符号；身高降序 → 加负号；姓名升序 → 不加符号。
    """
    n=int(input())
    data=[]
    for i in range(n):
        a=input().split()
        name=a[0]
        age=int(a[1])
        tall=int(a[2])
        data.append((name,age,tall))
    data.sort(key=lambda x:(x[1],-x[2],x[0]))
    for s in data:
        print(s[0])


# ════════════════════════════════════════════════════════════
# 组 B · Counter 统计 + 并列规则（对应你卡住的 ex4）
# ════════════════════════════════════════════════════════════

def ex4():
    """
    题：输入一行若干整数，输出出现次数【最少】的那个数。
        如果并列，取其中【较小】的那个。

    样例输入： 5 5 2 2 2 9
    样例输出： 5

    解释：统计 {5:2, 2:3, 9:1} → 最少的是 9（1次），只有它一个 → 输出 9？

    等等——上面解释写错了，重看：
        5 出现 2 次，2 出现 3 次，9 出现 1 次
        最少的是 9，只有 1 次，没有并列 → 输出 9

    样例如有并列的情况，例如输入： 1 1 2 2 3 4
        1:2  2:2  3:1  4:1  → 最少次数是 1，并列的是 3 和 4 → 取较小 → 3

    提示：
        cnt = Counter(arr)
        pairs = sorted(cnt.items(), key=lambda x: (x[1], x[0]))   # 次数升序，并列时元素升序
        print(pairs[0][0])        # 取【第一个】——因为这里要的是最少的
        注意和 ex4（原题）的区别：原题取 [-1]，这里取 [0]。
    """
    data=list(map(int,input().split()))
    cnt=Counter(data)
    pairs=sorted(cnt.items(),key=lambda x:(x[1],x[0]))
    print(pairs[0][0])


def ex5():
    """
    题（字符串版）：输入一行若干英文单词（空格分隔），
        输出出现次数最多的那个单词。如果并列，取字典序【较小】的那个。

    样例输入： apple banana apple cherry banana
    样例输出： apple

    解释：apple 2 次，banana 2 次，cherry 1 次 → 并列取字典序较小的 apple。

    提示：读入用 input().split()  —— 注意这里【不能】用 map(int, ...)，
          因为读的是单词不是数字。这是和纯数字题最大的区别。
          sorted(cnt.items(), key=lambda x: (x[1], x[0]))
          要取"次数最多且字典序最小" —— 次数是主要的，元素要小的，
          所以负号加在【次数】上：key=lambda x: (-x[1], x[0])，然后取 [0][0]。
    """
    data=list(input().split())
    cnt=Counter(data)
    b=sorted(cnt.items(),key=lambda x:(-x[1],x[0]))
    print(b[0][0])


def ex6():
    """
    题（综合）：输入 n，再输入 n 个整数。
        输出出现次数第二多的那个数（如果有多个并列，取较大的那个）。
        保证至少有两种不同数字。

    样例输入：
        6
        1 1 1 2 2 3

    样例输出： 2

    解释：1:3  2:2  3:1 → 次数排序 3 > 2 > 1 → 第二多是 2。

    提示：先去重拿到"出现次数"的不同取值，或者直接对 pairs 排序后从后往前找
          第一个【次数不等于最大值】的。

          简单做法：
              pairs = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
              # pairs[-1] 是次数最多的，从后往前找到第一个次数不同的
              top = pairs[-1][1]
              for p in reversed(pairs):
                  if p[1] != top:
                      print(p[0]); break
    """
    n=int(input())
    data=list(map(int,input().split()))
    cnt=Counter(set(data))
    pairs=sorted(cnt.items(),key=lambda x:(-x[1],-x[0]))
    print(pairs[1][0])


# ════════════════════════════════════════════════════════════
# 组 C · 其他列表操作（手感练习）
# ════════════════════════════════════════════════════════════

def ex7():
    """
    题：输入一行若干整数，输出它们的【和】、【最大值】、【最小值】，
        三个值用空格分隔，输出一行。

    样例输入： 3 1 4 1 5
    样例输出： 14 5 1

    提示：sum(arr) / max(arr) / min(arr)
          print(a, b, c)  会自动用空格分隔 —— 不用自己拼字符串。
    """
    data=list(map(int,input().split()))
    print(sum(data),max(data),min(data))


def ex8():
    """
    题：输入一行若干整数，输出【反转】后的结果，空格分隔。

    样例输入： 1 2 3 4 5
    样例输出： 5 4 3 2 1

    提示：arr[::-1] 得到反转的新列表（原列表不动）。
          对比：arr.reverse() 是原地反转，返回 None —— 和 sort/sorted 一个套路。
          这里用 arr[::-1] 或 arr.reverse() 都行。
    """
    data=list(map(int,input().split()))
    a=data[::-1]
    print(*a)

def ex9():
    """
    题：输入一行若干整数，输出【第 3 个到第 6 个】元素（从 1 开始数），空格分隔。
        如果不足 6 个，输出能取到的部分。

    样例输入： 1 2 3 4 5 6 7 8
    样例输出： 3 4 5 6

    提示：切片是【左闭右开】的。
          "第 3 个到第 6 个"（从 1 数）→ 下标 2 到 5 → 切片 arr[2:6]
          切片写超出范围【不会报错】，会自动截断 —— 所以不用判断"够不够"。
    """
    data=list(map(int,input().split()))
    print(*data[2:6])


def ex10():
    """
    题（字符串排序）：输入 n 个名字，每行一个，按【长度从小到大】输出；
        长度相同的按【字典序升序】输出。

    样例输入：
        4
        Tom
        Alexander
        Amy
        Bob

    样例输出：
        Amy
        Bob
        Tom
        Alexander

    解释：长度 3/9/3/3 → 三个长度 3 的按字典序：Amy < Bob < Tom
          → Amy, Bob, Tom，然后才是 Alexander。
          按字符码点比：'A'=65 < 'B'=66 < 'T'=84。

    提示：len(x) 是长度，x 是名字本身（这里 data 是一堆字符串，不是元组！）
          sorted(names, key=lambda x: (len(x), x))
          注意：字符串题目里 x 就是字符串本身，所以取长度要写 len(x)，
                而不是 x[1] —— 别把元组的取法套过来。
    """
    n=int(input())
    names=[]
    for i in range(n):
        name=input()
        names.append(name)
    b=sorted(names,key=lambda x:(len(x),x))
    for s in b:
        print(s)


def ex11():
    """
    题（组合拳）：输入一行若干整数，去重后按【从大到小】输出，空格分隔。

    样例输入： 3 1 4 1 5 3 9 2 6
    样例输出： 9 6 5 4 3 2 1

    提示：sorted(set(arr), reverse=True)
          链式调用：set 去重 → sorted 排序 → reverse=True 倒序。
    """
    data=list(map(int,input().split()))
    b=sorted(set(data),reverse=True)
    print(*b)


def ex12():
    """
    题（对原题加深）：输入一行若干整数，输出出现次数最多的那个数（并列取较大的）。
        然后【再输出一行】，把这个数字出现了几次。

    样例输入： 1 3 3 2 1 3 1
    样例输出：
        3
        3

    解释：1 和 3 都出现 3 次 → 取较大的 3；然后第二行输出它的次数 3。

    提示：这就是 original ex4 的加强版 —— 多让你输出次数。
          pairs = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
          best = pairs[-1]        # (3, 3)
          print(best[0])          # 元素
          print(best[1])          # 次数
          把 best 存成一个变量，就不用写两遍长长的 sorted 了。
    """
    data=list(map(int,input().split()))
    cnt=Counter(data)
    c=sorted(cnt.items(),key=lambda x:(-x[1],-x[
    print(c[0][0])
    print(c[0][1])


# ════════════════════════════════════════════════════════════
# 自检
# ════════════════════════════════════════════════════════════

CHECKS = [
    ("ex1",  "4\n苹果 5 100\n香蕉 3 100\n橙子 8 50\n葡萄 3 80\n",
             "香蕉\n苹果\n葡萄\n橙子"),

    ("ex2",  "3\nTom 80 90 70\nAmy 90 90 60\nBob 70 70 70\n",
             "Amy\nTom\nBob"),

    ("ex3",  "4\nTom 18 175\nAmy 18 180\nBob 20 170\nZoe 18 180\n",
             "Amy\nZoe\nTom\nBob"),

    ("ex4",  "1 1 2 2 3 4\n",      "3"),

    ("ex5",  "apple banana apple cherry banana\n",  "apple"),

    ("ex6",  "6\n1 1 1 2 2 3\n",   "2"),

    ("ex7",  "3 1 4 1 5\n",        "14 5 1"),

    ("ex8",  "1 2 3 4 5\n",        "5 4 3 2 1"),

    ("ex9",  "1 2 3 4 5 6 7 8\n",  "3 4 5 6"),

    ("ex10", "4\nTom\nAlexander\nAmy\nBob\n",
             "Amy\nBob\nTom\nAlexander"),

    ("ex11", "3 1 4 1 5 3 9 2 6\n", "9 6 5 4 3 2 1"),

    ("ex12", "1 3 3 2 1 3 1\n",    "3\n3"),
]


def self_check(only=None):
    import io

    print("=" * 64)
    print("自检：期望值 vs 实际输出")
    print("=" * 64)

    ok, total = 0, 0
    for name, fake_input, expected in CHECKS:
        if only and name != only:
            continue
        total += 1

        func = globals().get(name)
        if func is None:
            print(f"  {name:5s} ✗ 函数不存在")
            continue

        old_stdin = sys.stdin
        sys.stdin = io.StringIO(fake_input)
        try:
            buf = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = buf
            try:
                func()
            finally:
                sys.stdout = old_stdout
            actual = buf.getvalue().strip().replace("\r\n", "\n")
        except NotImplementedError:
            actual = "<还没写>"
        except Exception as e:
            actual = f"<报错: {type(e).__name__}: {e}>"
        finally:
            sys.stdin = old_stdin

        passed = (actual == expected.strip())
        ok += passed
        print(f"  {name:5s} {'✓ 通过' if passed else '✗ 未过'}")
        if not passed:
            print(f"        期望: {expected.strip()!r}")
            print(f"        实际: {actual!r}")

    print("-" * 64)
    print(f"通过 {ok} / {total}")
    print("=" * 64)


if __name__ == "__main__":
    import sys as _sys
    only = next((a for a in _sys.argv[1:] if a.startswith("ex")), None)
    self_check(only)
