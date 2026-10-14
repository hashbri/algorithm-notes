# -*- coding: utf-8 -*-
"""
Day 1 · 输入输出四件套 —— 2026-10-07
比赛：学院校内程序设计上机竞赛 2026-10-14

玩法：
    1) 先直接跑：  python day1_io.py
       看每个模板长什么样、输出什么。
    2) 然后逐个把 main() 里的 TODO 填上，再跑一次。
    3) 全部填完，去 OJ 上找 3 道最简单的题，只做"读入 + 打印"。

判断标准：读入不再卡壳。看到题目能立刻说出"这是模板几"。
"""

import sys


# ============================================================
# 模板 ①：一行一个整数
# 适用：题目说"输入一个整数 n"
# ============================================================

def template_1():
    """比赛写法就是： n = int(input())"""
    n = int(input())
    print(n)


# ============================================================
# 模板 ②：一行多个整数
# 适用：题目说"输入两个整数 a b" 或 "输入 n 个整数"
# ============================================================

def template_2_fixed():
    """固定个数。比赛写法： a, b = map(int, input().split())"""
    a, b = map(int, input().split())
    print(a, b)


def template_2_list():
    """一行一串，变列表。比赛写法： arr = list(map(int, input().split()))"""
    arr = list(map(int, input().split()))
    print(arr)
    return arr


# ============================================================
# 模板 ③：多行 / 多组数据 —— 一次性全读（最稳）
# 适用：题目说"第一行是 n，接下来 n 行每行一个数"
# ============================================================

def template_3():
    """
    比赛写法：
        data = sys.stdin.read().split()
    好处：不怕换行位置怪，也不怕末尾没空行。是最不容易错的读法。
    """
    data = sys.stdin.read().split()
    # data 是字符串列表，要算数就得自己转
    nums = list(map(int, data))
    print(nums)
    return nums


# ============================================================
# 模板 ④：读到文件结束（EOF）—— 多组输入
# 适用：题目说"输入包含多组数据，每组一行"，且没说有几组
# 这是入门选手最容易踩的坑：只读一组，直接错一半测试点！
# ============================================================

def template_4():
    """
    比赛写法：
        while True:
            try:
                n = int(input())
            except EOFError:
                break
            # 处理这一组
    """
    results = []
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        results.append(n * 2)      # 这里假装处理一下
    for r in results:
        print(r)


# ============================================================
# 练习区：把 TODO 填掉，再跑一次
# 注意：每填一个就单独跑一次测试（见文件末尾的说明）
# ============================================================

def practice_a():
    """
    题目：输入两个整数 a 和 b，输出它们的和。
    样例输入： 3 5
    样例输出： 8

    提示：一行两个整数 → 去上面看模板②。
    """
    a,b=map(int,input().split())
    print(a+b)

import sys
def practice_b():
    """
    题目：第一行输入 n，第二行输入 n 个整数，输出这 n 个数的和。
    样例输入：
        5
        1 2 3 4 5
    样例输出： 15

    提示：第一行单独读（一个整数），第二行整行读成列表。
          求和可以用 sum()。
    """
    n=int(input())
    num=list(map(int,input().split()))
    print(sum(num))# ← 把这一行换成你的代码


def practice_c():
    """
    题目：输入若干个整数，每行一个，不知道总共有几个（读到没有为止），
         输出其中最大的那个。
    样例输入：
        3
        7
        2
    样例输出： 7

    提示：这是模板④的场景（多组输入读到 EOF）。
          先把所有数收集到一个列表里，最后再取最大值。
          求最大值可用 max()。
    """
    result=[]
    while True:
        try:
            n=int(input())
        except EOFError:
            break
        result.append(n)
    a=max(result)
    print(a)
# ← 把这一行换成你的代码


# ============================================================
# 演示：直接运行本文件时，把四个模板走一遍
# 用输入流喂固定的数据，方便你看到效果
# ============================================================

def _demo():
    samples = {
        "template_1":      ("42\n", template_1),
        "template_2_fixed": ("3 5\n", template_2_fixed),
        "template_2_list":  ("1 2 3 4 5\n", template_2_list),
        "template_3":      ("5\n1 2 3 4 5\n", template_3),
        "template_4":      ("3\n7\n2\n", template_4),
    }

    for name, (fake_input, func) in samples.items():
        print("=" * 52)
        print(f"{name}    （喂入的输入：{fake_input!r}）")
        print("=" * 52)

        # 用 io 把 input()/sys.stdin 换成固定输入，方便演示
        import io
        old_stdin, old_input = sys.stdin, __builtins__.input if isinstance(__builtins__, dict) else __builtins__.input
        sys.stdin = io.StringIO(fake_input)
        try:
            func()
        finally:
            sys.stdin = old_stdin
        print()

    print("=" * 52)
    print("上面是 4 个模板。现在去填 practice_a / practice_b / practice_c")
    print("=" * 52)


if __name__ == "__main__":
    _demo()
