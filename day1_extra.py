# -*- coding: utf-8 -*-
"""
Day 1 加练 · 输入输出四模板全覆盖 —— 2026-10-07

用法：
    1) 逐个填函数，填一个测一个：
         printf '输入内容' | python -c "import day1_extra; day1_extra.ex1()"
    2) 每道题的文档字符串里写了 "用模板X"，卡住了去看 day1_io.py 顶部。
    3) 全部填完，跑 python day1_extra.py 看自检结果。

注意：OJ 判题时 input() 里绝对不能写提示语！这里是本地练习，
      我把提示语也省略了，养成习惯。
"""

import sys


# ============================================================
# 【模板 ①】一行一个整数
# ============================================================

def ex1():
    """
    题：输入一个整数 n，输出 n 的两倍。
    样例输入： 7
    样例输出： 14
    用模板 ①
    """
    n=int(input())
    print(n*2)


def ex2():
    """
    题：输入一个整数 n（代表秒数），输出它等于多少分钟零多少秒，
         格式为 "X Y"（X 是分钟，Y 是秒）。
    样例输入： 130
    样例输出： 2 10
    用模板 ①
    提示：整除用 //（取整），求余用 %。
    """
    n=int(input())
    print(n//60,n%60)


# ============================================================
# 【模板 ②】一行多个整数 —— 两种用法
# ============================================================

def ex3():
    """
    题：输入三个整数 a b c，输出它们的乘积。
    样例输入： 2 3 4
    样例输出： 24
    用模板 ② 的"固定个数"写法
    """
    a,b,c=map(int,input().split())
    print(a*b*c)


def ex4():
    """
    题：输入一行若干个整数，输出其中最大的那个。
    样例输入： 3 9 2 7 5
    样例输出： 9
    用模板 ② 的"整行变列表"写法
    提示：列表求最大值用 max()。
    """
    a=list(map(int,input().split()))
    print(max(a))


def ex5():
    """
    题：输入一行若干个整数，输出它们的平均值（保留一位小数）。
    样例输入： 1 2 3 4
    样例输出： 2.5
    用模板 ② 的"整行变列表"写法
    提示：平均值 = 总和 / 个数。想要小数就用 / 而不是 //。
          保留一位小数用 round(值, 1)。
    """
    a=list(map(int,input().split()))
    b=len(a)
    print(round(sum(a)/b,1))


# ============================================================
# 【模板 ③】多行 / 一次全读
# ============================================================

def ex6():
    """
    题：第一行输入 n，第二行输入 n 个整数，输出其中大于等于 60 的数的个数。
    样例输入：
        6
        59 60 85 30 100 61
    样例输出： 4
    用模板 ③（一次全读，或逐行读都行）
    提示：统计个数可以写循环计数，也可以用 len([x for x in arr if x >= 60])。
    """
    n=int(input())
    a=list(map(int,input().split()))
    num=0
    for i in a:
        if i >=60:
            num=num+1
    print(num)





def ex7():
    """
    题：输入两行，每行若干整数，输出两行数字的总和。
    样例输入：
        1 2 3
        4 5 6
    样例输出： 21
    用模板 ③（sys.stdin.read() 最方便 —— 两行混在一起一次性求和）
    """

    data=sys.stdin.read().split()
    num = list(map(int, data))
    print(sum(num))

# ============================================================
# 【模板 ④】多组输入读到 EOF  ← 今天的重点，多练两道
# ============================================================

def ex8():
    """
    题：输入若干行，每行一个整数，读到没有为止，输出所有数的和。
    样例输入：
        1
        2
        3
    样例输出： 6
    用模板 ④
    """
    result=[]
    while True:
        try:
            n=int(input())
        except EOFError:
            break
        result.append(n)
    print(sum(result))


def ex9():
    """
    题：多组数据。每组一行，包含两个整数 a 和 b，
         对每组输出 a+b，每组结果占一行。
    样例输入：
        1 2
        3 4
        5 6
    样例输出：
        3
        7
        11
    用模板 ④（重点：每组都要立刻输出，而不是攒到最后）
    提示：把 try / except EOFError 写在 while True 里面，
         读到的这一行在 try 之后紧接着处理。
    """
    while True:
        try:
            a,b=map(int,input().split())
        except EOFError:
            break
        print(a+b)


def ex10():
    """
    题（综合）：多组数据。每组第一行是 n，第二行是 n 个整数，
               对每组输出这 n 个数的和，每组结果占一行。
    样例输入：
        3
        1 2 3
        2
        10 20
    样例输出：
        6
        30
    用模板 ④ + 模板 ②（考你能不能把两种读法接在一起）
    提示：while True 里先读 n（要处理 EOFError），
         再读一行数字。注意第二行的读取也要在 try 的保护范围内。
    """
    while True:
        try:
            n=int(input())
            a=list(map(int,input().split()))
        except EOFError:
            break
        print(sum(a))


# ============================================================
# 自检：全部填完后运行本文件，看每道题的实际输出
# ============================================================

CHECKS = [
    ("ex1",  "7\n",                              "14"),
    ("ex2",  "130\n",                            "2 10"),
    ("ex3",  "2 3 4\n",                          "24"),
    ("ex4",  "3 9 2 7 5\n",                      "9"),
    ("ex5",  "1 2 3 4\n",                        "2.5"),
    ("ex6",  "6\n59 60 85 30 100 61\n",          "4"),
    ("ex7",  "1 2 3\n4 5 6\n",                   "21"),
    ("ex8",  "1\n2\n3\n",                        "6"),
    ("ex9",  "1 2\n3 4\n5 6\n",                  "3\n7\n11"),
    ("ex10", "3\n1 2 3\n2\n10 20\n",             "6\n30"),
]


def self_check():
    import io

    print("=" * 60)
    print("自检：期望值 vs 实际输出")
    print("=" * 60)

    ok_count = 0
    for name, fake_input, expected in CHECKS:
        func = globals().get(name)
        if func is None:
            print(f"  {name:6s} ✗ 函数不存在")
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
            actual = buf.getvalue().strip()
        except Exception as e:
            actual = f"<报错: {type(e).__name__}: {e}>"
        finally:
            sys.stdin = old_stdin

        passed = (actual == expected.strip())
        if passed:
            ok_count += 1
        mark = "✓ 通过" if passed else "✗ 未过"
        print(f"  {name:6s} {mark}   期望: {expected.strip()!r}   实际: {actual!r}")

    print("-" * 60)
    print(f"通过 {ok_count} / {len(CHECKS)}")
    print("=" * 60)


if __name__ == "__main__":
    self_check()
