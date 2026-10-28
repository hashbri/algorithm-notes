# -*- coding: utf-8 -*-
# 015_review.py —— 复习本（复习池的落地页）
#
# 为什么单独建这一本：
#   复习池有 11 条，要一直轮转。以前每次都在别的文件里改来改去，
#   自检用例对不上、旧代码也容易看见，等于抄。
#   这本只放**复习变式**：题目都是从踩过的坑里变形出来的，
#   不是原题重复 —— 原题写第二遍靠的是记忆，变式靠的才是理解。
#
# 用法：
#   python 015_review.py          跑全部
#   python 015_review.py R1       只跑 R1
#
# 老规矩：
#   1. 期望值全部用参考解跑出来的，不是手写的。
#   2. 写完先跑自检，别用眼睛看。
#   3. 结果写进 `每日练习_打卡表.md`：一次过 / 死在第几个用例。

import io
import sys

FUNCS = {}


def problem(name):
    def deco(fn):
        FUNCS[name] = fn
        return fn
    return deco


# ======================================================================
# R1 · 打擂台（复习点 #5）
# 对应错误：初值给错、并列时该不该换
# ======================================================================

# 【题面】读入一行单词（空格分隔），输出最长的那个单词。
#        **如果有多个一样长，输出最后出现的那个。**
#        （注意：和 011_bitwise.py 的 Q5 要求相反，别照抄。）
# 【输入】一行单词
# 【输出】一个单词
# 【提示】还是打擂台。先想清楚两件事：
#        ① 擂台上第一个站的是谁？
#        ② 遇到"一样长"的，换还是不换？这一题和 Q5 的答案不一样。
@problem("R1")
def R1():
    data=input().split()
    pos=data[0]
    for i in data:
        if len(pos)<=len(i):
            pos=i
    print(pos)



# ======================================================================
# R2 · 切片方向（复习点 #6）
# 对应错误：[:k] 和 [k:] 写反
# ======================================================================

# 【题面】读入一行字符串 s，再读入一个整数 k（0 ≤ k ≤ len(s)），
#        把 s 从第 k 个字符处劈开，中间插一个竖线 "|" 后输出。
#        劈开后左边保留前 k 个字符，右边从第 k 个字符开始。
# 【输入】第一行一个字符串，第二行一个整数 k
# 【输出】一行，形如 "左边|右边"
# 【提示】两个切片，冒号的哪一边放 k —— 这一题就是为了治这个。
#        想一下 k=0 和 k=len(s) 的时候应该输出什么。
@problem("R2")
def R2():
    data=input()
    k=int(input())
    a=data[:k]
    b=data[k:]
    print(f"{a}|{b}")


# ======================================================================
# R3 · 相邻两数差的最大值（2026-10-28 周三 · 第 1 道）
# 对应错误：#2  range 边界（写成 range(n) 会 IndexError）、#5 打擂台初值
# ======================================================================

# 【题面】读入一行整数，输出**相邻两项之差（后减前）的绝对值**里最大的那个。
#        如果只有 1 个数（没有"相邻"），输出 0。
# 【输入】一行整数
# 【输出】一个整数
# 【提示】"相邻"的意思是 a[i] 和 a[i-1] 配对。
#        想清楚两件事：
#        ① 循环变量的范围该是多少？（能不能从 0 开始？到几为止？）
#        ② 擂台的初值给什么？n=1 的时候你的代码会输出什么？
@problem("R3")
def R3():
    data=list(map(int,input().split()))
    if len(data)==1:
        print(0)
    else:
        a=[]
        for i in range(1,len(data)):
            b=abs(data[i]-data[i-1])
            a.append(b)
        print(max(a))


# ======================================================================
# R4 · 连续相同数字的最长一段（2026-10-28 周三 · 第 2 道）
# 对应错误：#7 变量名与循环变量一致、状态的初值和重置
# ======================================================================

# 【题面】读入一行整数，输出「连续相同」最长那一段的长度。
#        例：1 1 2 2 2 3 → 最长是三个 2 → 输出 3
# 【输入】一行整数
# 【输出】一个整数（至少是 1）
# 【提示】需要用**两个**变量：一个记"当前这段有多长"，一个记"到目前为止最好的是多少"。
#        想清楚三件事：
#        ① 这两个变量的初值分别给几？
#        ② 什么时候"当前长度"要加 1？
#        ③ 什么时候"当前长度"要**推倒重来**，重来之后等于几？
@problem("R4")
def R4():
    data=list(map(int,input().split()))
    pos=1
    a=[]
    for i in range(0,len(data)-1):
        if data[i]==data[i+1]:
            pos+=1
        else:
            a.append(pos)
            pos=1
    a.append(pos)
    if a:
        print(max(a))
    else:
        print(1)





# ======================================================================
# 自检
# ======================================================================

CHECKS = [
    # ---- R1 最长的单词（并列取最后）----
    ("R1", "i love python\n", "python"),
    ("R1", "aa bb cc\n", "cc"),
    ("R1", "ab cd ef gh\n", "gh"),

    # ---- R2 劈开字符串 ----
    ("R2", "abcdef\n2\n", "ab|cdef"),
    ("R2", "abcdef\n0\n", "|abcdef"),
    ("R2", "x\n1\n", "x|"),

    # ---- R3 相邻差的最大值 ----
    ("R3", "1 5 2 9\n", "7"),
    ("R3", "7 8\n", "1"),
    ("R3", "5\n", "0"),
    ("R3", "3 3 3\n", "0"),

    # ---- R4 连续相同的最长一段 ----
    ("R4", "1 1 2 2 2 3\n", "3"),
    ("R4", "5\n", "1"),
    ("R4", "1 2 3\n", "1"),
    ("R4", "2 2 2 2\n", "4"),
    # ---- 以下 5 个是 10-28 补的：专门治「把"次数"当成"连续长度"」----
    ("R4", "1 1 2 1\n", "2"),
    ("R4", "1 2 1 2 1\n", "1"),
    ("R4", "1 1 2 2 1 1 1\n", "3"),
    ("R4", "3 1 1 3\n", "2"),
    ("R4", "5 5 1 5 5 5 5 1\n", "4"),
]


def self_check(only=None):
    total = 0
    ok = 0
    per = {}
    for name, fake_input, expected in CHECKS:
        if only and name != only:
            continue
        total += 1
        old_stdin, old_stdout = sys.stdin, sys.stdout
        sys.stdin = io.StringIO(fake_input)
        buf = io.StringIO()
        sys.stdout = buf
        err = None
        try:
            FUNCS[name]()
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
        finally:
            sys.stdin, sys.stdout = old_stdin, old_stdout

        if err:
            print(f"  {name}  x 报错 -> {err}")
            continue

        # 只去末尾换行，行首空格必须保留（格式题全靠它）
        actual = buf.getvalue().replace("\r\n", "\n").rstrip("\n")
        exp = expected.rstrip("\n")

        if actual == exp:
            ok += 1
            per[name] = per.get(name, 0) + 1
            print(f"  {name}  ✓ 通过")
        else:
            print(f"  {name}  ✗ 未过")
            print(f"       输入: {fake_input!r}")
            print(f"       期望: {exp!r}")
            print(f"       实际: {actual!r}")

    print()
    print(f"总计 {ok} / {total}")
    for name in ("R1", "R2", "R3", "R4"):
        if not only or name == only:
            cnt = sum(1 for c in CHECKS if c[0] == name)
            print(f"  {name}  {per.get(name, 0)} / {cnt}")
    print()
    print("卡住了先别翻旧代码，也别翻同文件里别的题 —— 每道题的要求都不一样，抄错了更麻烦。")


if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    self_check(only)
