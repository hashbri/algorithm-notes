# -*- coding: utf-8 -*-
# 017_difference_drill.py —— 差分练习（2026-11-01）
#
# 模板已经验证过了，下面直接给你，不用重写：
#
#   build_diff(a, n)     由 a 造差分数组，长度 n+2
#   range_add(d, l, r, x) 把 a[l..r] 每个数加 x，只改 d
#   restore(d, n)        由 d 还原 a
#
# 这两道题考的不是模板，是**怎么把模板用进一道完整的题**：
# 读入、调用、输出格式。你前两周栽的错，一大半都在这三件事上。
#
# 用法：
#   python 017_difference_drill.py        跑全部
#   python 017_difference_drill.py T1     只跑 T1


import io
import sys

# ======================================================================
# 模板（已验证，直接用）
# ======================================================================

def build_diff(a, n):
    d = [0] * (n + 2)
    for i in range(1, n + 1):
        d[i] = a[i] - a[i - 1]
    return d


def range_add(d, l, r, x):
    d[l] += x
    d[r + 1] -= x


def restore(d, n):
    a = [0] * (n + 1)
    cur = 0
    for i in range(1, n + 1):
        cur += d[i]
        a[i] = cur
    return a


FUNCS = {}


def problem(name):
    def deco(fn):
        FUNCS[name] = fn
        return fn
    return deco


# ======================================================================
# T1 · 区间加法（模板直用）
# ======================================================================
# 【题面】
#   第一行 n m
#   第二行 n 个整数 a[1] a[2] ... a[n]
#   接下来 m 行，每行 l r x，表示把 a[l..r] 每个数加上 x
#   **输出所有操作做完之后的整个数组**，一行，空格分隔。
#
# 【样例】
#   输入            输出
#   5 2             13 13 16 13 15
#   3 1 4 1 5
#   2 4 2
#   1 5 10
#   （先 a[2..4] 各 +2 → 3 3 6 3 5；再整体 +10 → 13 13 16 13 15）
#
# 【提示】流程是固定的四步：读入 → build_diff → 循环 range_add → restore。
#        唯一容易错的是第一行：数组要自己补一个 0 挡在前面，
#        让 a[1] 真的是 1 号，而不是 0 号。
@problem("T1")
def T1():
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    a=[0]+arr
    def build_diff(a,n):
        d=[0]*(n+2)
        for i in range(1,n+1):
            d[i]=a[i]-a[i-1]
        return d
    d=build_diff(a,n)
    def range_add(d,l,r,x):
        d[l]+=x
        d[r+1]-=x
    for s in range(m):
        l, r, x = map(int, input().split())
        range_add(d, l, r, x)
    def restore(d,n):
        a=[0]*(n+1)
        cur=0
        for i in range(1,n+1):
            cur+=d[i]
            a[i]=cur
        return a
    ans=restore(d,n)
    print(*ans[1:])



# ======================================================================
# T2 · 加分之后的最低分
# ======================================================================
# 【题面】
#   输入格式和 T1 完全一样。
#   输出**所有操作做完之后，数组里的最小值**。
#
# 【样例】
#   输入            输出
#   5 3             13
#   3 1 4 1 5
#   2 4 2
#   1 5 10
#   3 3 1
#
# 【提示】
#   ① 只盯着"被加过的位置"是不够的 —— 没被动过的位置也可能是最小的。
#   ② 找最小是打擂台。**擂台上的第一个人是谁？** 这道题里初值给错直接全灭，
#      因为分数可以是负数。
@problem("T2")
def T2():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    a = [0] + arr
    d = build_diff(a, n)
    for s in range(m):
        l, r, x = map(int, input().split())
        range_add(d, l, r, x)
    ans = restore(d, n)
    k=ans[1]
    for w in range(2,len(ans)):
        if ans[w]<k:
            k=ans[w]
    print(k)


# ======================================================================
# T3 · 区间覆盖计数（变式：标记就是 +1 / -1）
# ======================================================================
# 【题面】
#   一条线段有 L 个位置，编号 1 ~ L，一开始全是空的。
#   接下来 n 次操作，每次把 [l, r] 涂上颜色（涂过的地方还能再涂，颜色不区分）。
#   问：最后有多少个位置**被涂过至少一次**？
#
# 【输入】
#   第 1 行：L n
#   接下来 n 行：每行两个整数 l r
# 【输出】一个整数
#
# 【样例】
#   输入            输出
#   10 2            8
#   1 5
#   3 8
#   （1~8 全被涂过，共 8 个位置；9、10 没被涂到）
#
# 【提示】
#   ① 这题根本没有"加 x"—— 标记就是 **+1** 和 **-1**。
#      差分本来就是这个样子，前两题只是把标记值换成了 x 而已。
#   ② **不许用 restore！** 从头累加的时候顺手就能判断，
#      不要先把整个数组还原出来、再扫第二遍。一个循环搞定。
@problem("T3")
def T3():
    L,n=map(int,input().split())
    a=[0]*(L+2)
    for i in range(n):
        l,r=map(int,input().split())
        range_add(a,l,r,1)
    res=0
    cur=0
    for i in range(1,L+1):
        cur+=a[i]
        if cur>0:
            res+=1
    print(res)





# ======================================================================
# 自检
# ======================================================================

CHECKS = [
    # ---- T1 区间加法 ----
    ("T1", "5 2\n3 1 4 1 5\n2 4 2\n1 5 10\n", "13 13 16 13 15"),
    ("T1", "4 1\n5 5 5 5\n2 3 10\n", "5 15 15 5"),
    ("T1", "1 1\n7\n1 1 3\n", "10"),

    # ---- T2 最低分 ----
    ("T2", "5 3\n3 1 4 1 5\n2 4 2\n1 5 10\n3 3 1\n", "13"),
    ("T2", "3 1\n100 50 80\n1 2 -100\n", "-50"),
    ("T2", "4 1\n5 5 5 5\n2 3 10\n", "5"),

    # ---- T3 区间覆盖计数 ----
    ("T3", "10 2\n1 5\n3 8\n", "8"),
    ("T3", "5 1\n1 5\n", "5"),
    ("T3", "5 2\n1 2\n4 5\n", "4"),
    ("T3", "1 1\n1 1\n", "1"),
    ("T3", "6 2\n2 2\n2 2\n", "1"),
]


def self_check(only=None):
    total = ok = 0
    per = {}
    for name, fake_input, expected in CHECKS:
        if only and name != only:
            continue
        total += 1
        old_in, old_out = sys.stdin, sys.stdout
        sys.stdin = io.StringIO(fake_input)
        buf = io.StringIO()
        sys.stdout = buf
        err = None
        try:
            FUNCS[name]()
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
        finally:
            sys.stdin, sys.stdout = old_in, old_out

        if err:
            print(f"  {name}  x 报错 -> {err}")
            continue

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
    for name in ("T1", "T2", "T3"):
        if not only or name == only:
            cnt = sum(1 for c in CHECKS if c[0] == name)
            print(f"  {name}  {per.get(name, 0)} / {cnt}")


if __name__ == "__main__":
    self_check(sys.argv[1] if len(sys.argv) > 1 else None)
