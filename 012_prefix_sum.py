# 012_prefix_sum.py —— 前缀和（第一个新算法 · 2026-10-18）
#
# ======================================================================
# 为什么学前缀和
# ======================================================================
#   你现在遇到「求一段区间的和」会怎么写？大概是 sum(a[l-1:r])。
#   一次询问没问题，但如果有 10 万次询问、每段长度 10 万呢？
#       暴力：每次把这段挨个加一遍  -> O(长度) x q 次 = 可能 1e10 次运算，超时
#       前缀和：预先算好一张"累计和"表，之后每次询问 O(1) -> 10 万次询问也秒过
#
#   这就是前缀和存在的唯一理由：**把"每次重新数"换成"查表相减"**。
#
# ======================================================================
# 核心定义
# ======================================================================
#   给定 a[0] a[1] ... a[n-1]
#
#   pre 数组长 n+1，比 a 多一格：
#       pre[0] = 0                    <- 一个都不取，和是 0
#       pre[1] = a[0]
#       pre[2] = a[0] + a[1]
#       pre[i] = a[0] + a[1] + ... + a[i-1]      （前 i 个数的和）
#
#   于是「a 的第 l 个到第 r 个数」（题目常用 1 开始编号）的和是：
#
#       sum(l..r) = pre[r] - pre[l-1]
#
#   为什么？pre[r] 是前 r 个的和，pre[l-1] 是前 l-1 个的和，
#   一减就只剩中间那段。这跟"用尺子量两段再相减"是一个道理。
#
#   那一格 pre[0] = 0 不是凑数：没有它，l=1 时 pre[0] 会越界。
#
# ======================================================================
# 怎么建 pre（这是唯一要背的循环）
# ======================================================================
#       pre = [0] * (n + 1)
#       for i in range(1, n + 1):
#           pre[i] = pre[i - 1] + a[i - 1]
#
#   注意 a 的下标比 pre 小 1 —— 这是前缀和最容易写错的地方。
#
# ======================================================================
# 用法
# ======================================================================
#   python 012_prefix_sum.py         跑全卷自检
#   python 012_prefix_sum.py Q2      只跑第 2 题
#
# 老规矩：期望值全部用参考解跑出来的，不是手写的。

import io
import sys

FUNCS = {}


def problem(name):
    def deco(fn):
        FUNCS[name] = fn
        return fn
    return deco


# ======================================================================
# Q1 · 区间和（单次询问）
# ======================================================================
# 【题面】给 n 个整数，再给一个区间 [l, r]（1 开始编号，闭区间），
#        求这个区间里所有数的和。
# 【输入】共 3 行
#   第 1 行：n
#   第 2 行：n 个整数
#   第 3 行：l r
# 【输出】一个整数
# 【提示】先建 pre，再用 pre[r] - pre[l-1]。
#        这一题用 sum() 也能过，但请**用前缀和写**，练手。
#        ⚠️ 注意 a 和 pre 的下标差 1。
@problem("Q1")
def Q1():
    n=int(input())
    a=list(map(int,input().split()))
    l,r=map(int,input().split())
    pre=[0]*(n+1)
    for i in range(1,n+1):
        pre[i]=pre[i-1]+a[i-1]
    result=pre[r]-pre[l-1]
    print(result)



# ======================================================================
# Q2 · 多次询问（前缀和真正的主场）
# ======================================================================
# 【题面】给 n 个整数，然后有 q 次询问，每次给一个区间 [l, r]，
#        求每个区间的和。
# 【输入】共 q+2 行
#   第 1 行：n q
#   第 2 行：n 个整数
#   第 3 行起：q 行，每行 l r
# 【输出】q 行，每行一个整数
# 【提示】pre 只建一次，q 次询问都在它上面相减。
#        这就是前缀和的意义：建表一次 O(n)，之后每次 O(1)。
#        ⚠️ 输出 q 行 —— 想想 print 该缩进在哪一层。
@problem("Q2")
def Q2():
    n,q=map(int,input().split())
    data=list(map(int,input().split()))
    a=[]
    for i in range(q):
        l,r=map(int,input().split())
        a.append((l,r))
    pre=[0]*(n+1)
    for s in range(1,n+1):
        pre[s]=pre[s-1]+data[s-1]
    for h in range(q):
        result=pre[a[h][1]]-pre[a[h][0]-1]
        print(result)



# ======================================================================
# Q3 · 长度恰好为 k 的最大和（前缀和的变形）
# ======================================================================
# 【题面】给 n 个整数和一个 k，在所有**长度恰好为 k 的连续段**里，
#        找出和最大的那个，输出这个和。
# 【输入】共 2 行
#   第 1 行：n k
#   第 2 行：n 个整数
# 【输出】一个整数
# 【提示】长度 k 的段，起点 i 从 0 到 n-k，这一段的和 = pre[i+k] - pre[i]。
#        然后就是"打擂台"（011_bitwise.py Q5 那个）：记住目前为止最大的。
#        ⚠️⚠️ 擂台初值**不能写 0**。数据里有负数，如果全是负数，
#              写 0 会输出 0，而正确答案是那个负数。想想初值该取什么。
#        ⚠️ 起点 i 的循环：range(?) 数一下最后一个起点是谁。
@problem("Q3")
def Q3():
    n,k=map(int,input().split())
    data=list(map(int,input().split()))
    pre=[0]*(n+1)
    for i in range(1,n+1):
        pre[i]=pre[i-1]+data[i-1]
    a=[]
    for s in range(0,n-k+1):
        b=pre[s+k]-pre[s]
        a.append(b)
    pos=a[0]
    for h in range(1,len(a)):
        if pos<a[h]:
            pos=a[h]
    print(pos)





# ======================================================================
# 自检（下面的代码不用改，看结果就行）
# ======================================================================

CHECKS = [
    # ---- Q1 区间和（单次） ----
    ("Q1", "5\n1 2 3 4 5\n2 4\n", "9"),
    ("Q1", "3\n10 20 30\n1 3\n", "60"),
    ("Q1", "4\n-1 2 -3 4\n2 3\n", "-1"),

    # ---- Q2 多次询问 ----
    ("Q2", "5 3\n1 2 3 4 5\n1 1\n1 5\n3 4\n", "1\n15\n7"),
    ("Q2", "1 1\n7\n1 1\n", "7"),
    ("Q2", "4 2\n-5 5 -5 5\n1 4\n2 3\n", "0\n0"),

    # ---- Q3 长度恰好为 k 的最大和 ----
    ("Q3", "5 2\n1 2 3 4 5\n", "9"),
    ("Q3", "5 5\n1 2 3 4 5\n", "15"),
    ("Q3", "6 3\n-2 -1 -3 -5 -1 -4\n", "-6"),
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
    for name in ("Q1", "Q2", "Q3"):
        if not only or name == only:
            cnt = sum(1 for c in CHECKS if c[0] == name)
            print(f"  {name}  {per.get(name, 0)} / {cnt}")
    print()
    print("顺序：Q1 练建表 -> Q2 练多次查询 + 输出缩进 -> Q3 练变形 + 擂台初值。")


if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    self_check(only)
