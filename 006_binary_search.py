# -*- coding: utf-8 -*-
"""
查找（线性 / 二分 / bisect）+ 贪心入门 —— 2026-10-09

═══ 先回答你那个问题 ═══
    你问："继续算法训练吧，还是要学 Python 语言？"
    答：算法是主线，但"语言工具"确实得补 —— 只是不用单独开课，跟着题目学。

    你已经会了的（001_io_input.py~005_simulation.py）：
        input / map / split / list / sort / sorted / lambda
        Counter / // / % / [::-1] / strip / abs

    你现在【缺】的是工具库 —— 不知道有这些东西，就只能用笨办法写：
        list.index()     找下标
        list.count()     数个数
        enumerate()      遍历时同时拿下标
        set              去重 + 判断"在不在"（比列表快得多）
        bisect           现成的二分查找
        列表推导式        一行代替"建空表 + for + append"

    006_binary_search.py 的每道题都绑一个新工具。做完这 8 道，武器库就齐了。

═══ 今天的算法主题：查找 ═══
    查找 = 在一堆数据里找某个东西。
        ① 线性查找：从头一个个比      —— 简单，但慢
        ② 二分查找：每次砍掉一半      —— 快得多

    100 万个数据，找一个数：
        线性查找最坏要试 1000000 次
        二分查找最多只要 20 次        ← 差 5 万倍

    前提：二分要求数据【已经排好序】。乱序数据用不了二分。

    最后两题（ex7 / ex8）是【贪心】入门 —— 冲刺手册 10/10 的内容。

═══ 用法 ═══
    python 006_binary_search.py          # 跑全部
    python 006_binary_search.py ex3      # 只跑 ex3
"""
import bisect
import sys


# ============================================================
# 演示区：先看两个完整解题过程
# ============================================================

def demo_binary_search():
    """
    演示题：在有序数组里找 13，二分要几步？

    数组 arr = [1, 3, 5, 7, 9, 11, 13]，下标 0~6

    手算：
        第1步：left=0, right=6 → mid=(0+6)//2=3 → arr[3]=7
               7 < 13，目标在右半边 → left = 3+1 = 4
        第2步：left=4, right=6 → mid=(4+6)//2=5 → arr[5]=11
               11 < 13 → left = 5+1 = 6
        第3步：left=6, right=6 → mid=(6+6)//2=6 → arr[6]=13  ✓ 找到

    3 步搞定。如果从头一个个比，要 7 步。
    数组越长，差距越夸张。
    """
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 13

    left, right = 0, len(arr) - 1
    steps = 0
    pos = -1
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            pos = mid
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return pos, steps


def demo_greedy_coin():
    """
    演示题：面值 50/20/10/5/1 元，凑 87 元最少几枚？

    贪心策略：每一步都拿"不超过剩余金额的最大面值"。

    手算：
        87 → 拿 50，剩 37
        37 → 拿 20，剩 17
        17 → 拿 10，剩 7
         7 → 拿 5， 剩 2
         2 → 拿 1， 剩 1
         1 → 拿 1， 剩 0
        共 6 枚

    每一轮做的事完全一样 → 循环体：
        cnt += n // c     # 这种面值能拿几张
        n %= c            # 拿完还剩多少
    """
    coins = [50, 20, 10, 5, 1]
    n = 87
    detail = []
    for c in coins:
        k = n // c
        if k:
            detail.append(f"{c}元×{k}")
        n %= c
    return " + ".join(detail)


# ============================================================
# 练习区：8 道题
# ============================================================

def ex1():
    """
    题：第一行 n，第二行 n 个整数，第三行目标值 x。
        输出 x 第一次出现的【下标】（从 0 开始）；找不到输出 -1。

    样例输入：      样例输出：
        5               2
        3 1 4 1 5
        4

    ── 新工具 ──
        x in arr        判断 x 在不在 arr 里 → True / False
        arr.index(x)    返回 x 第一次出现的下标
                        ⚠️ x 不存在时会直接报错，所以必须先判断！

    读入提醒：
        第一行一个数 → int(input())
        第二行多个数 → list(map(int, input().split()))
    """
    n=int(input())
    data=list(map(int,input().split()))
    x=int(input())
    pos=-1
    if x in data:
        pos=data.index(x)
    print(pos)



def ex2():
    """
    题：第一行 n，第二行 n 个整数，第三行目标值 x。
        输出【所有】等于 x 的下标，空格分隔；一个都没有则输出 -1。

    样例输入：      样例输出：
        5               1 3
        3 1 4 1 5
        1

    ── 新工具：enumerate ──
        普通的 for 只能拿到【值】：
            for v in arr:              # v 是元素
        加上 enumerate 就能同时拿下标：
            for i, v in enumerate(arr):  # i 是下标，v 是元素

    骨架：
        pos = []                          # 先建表（你栽过 4 次的坑）
        for i, v in enumerate(arr):
            if v == x:
                pos.append(i)
        然后：有内容就 print(*pos)，空的话 print(-1)
    """
    n=int(input())
    data=list(map(int,input().split()))
    x=int(input())
    pos=[]
    for i,v in enumerate(data):
        if v==x:
            pos.append(i)
    if pos:
        print(*pos)
    else:
        print(-1)






def ex3():
    """
    题：第一行 n，第二行【已排好序】的 n 个整数，第三行目标值 x。
        用【二分查找】找到 x 的下标；找不到输出 -1。

    样例输入：              样例输出：
        7                       3
        1 3 5 7 9 11 13
        7

    ── 二分查找模板（背下来，比赛手速靠它）──
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                # 找到了，记下 mid 后 break
            elif arr[mid] < x:
                left = mid + 1        # 目标在右半边
            else:
                right = mid - 1       # 目标在左半边

    ⚠️ 三个坑，错一个就死循环或漏答案：
        ① right 从 n-1 开始（不是 n）
        ② 循环条件必须是 left <= right（有等号）
        ③ left / right 收缩必须 ±1（不 ±1 就永远跳不出来）

    找不到的情况：用一个变量记答案，初始 -1，找到才改。
    """
    n=int(input())
    data=sorted(list(map(int,input().split())))
    x=int(input())
    left,right=0,n-1
    pos=-1
    while left<=right:
        mid=(left+right)//2
        if data[mid]==x:
            pos=mid
            break
        elif data[mid]<x:
            left=mid+1
        else:
            right=mid-1
    print(pos)




def ex4():
    """
    题：第一行 n，第二行【已排好序】的 n 个整数，第三行 x。
        输出【第一个 >= x】的元素下标；如果全都 < x，输出 n。

    样例：
        输入 5 / 1 3 5 7 9 / 4    → 输出 2    （arr[2]=5 是第一个 >= 4 的）
        输入 5 / 1 3 5 7 9 / 10   → 输出 5    （全都比 10 小，所以返回 n）
        输入 5 / 1 3 5 7 9 / 0    → 输出 0

    ── 这叫「求下界」，二分模板要改两处 ──
        ① right 从 n 开始（不是 n-1）—— 因为答案可能是 n
        ② 循环条件变成 while left < right（没有等号）
        ③ 收缩方式不同：
               arr[mid] < x  →  mid 不可能是答案，left = mid + 1
               否则 arr[mid] >= x → mid 可能是答案，right = mid（不要 -1）

    骨架：
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                ???
            else:
                ???
        循环结束时 left 就是答案，不用再判断。

    这题比 ex3 难，但它是"二分求边界"的通用套路，比赛里出现频率很高。
    """
    n=int(input())
    data=(list(map(int,input().split())))
    x=int(input())
    left,right=0,n
    while left<right:
        mid=(left+right)//2
        if data[mid]<x:
            left=mid+1
        else:
            right=mid
    print(left)




def ex5():
    """
    题：输入输出和 ex4【完全一样】。
        区别：这次不许手写 while，用现成的库解决。

    ── 新工具：bisect 模块 ──
        import bisect

        bisect.bisect_left(arr, x)    → 第一个 >= x 的位置   ← ex4 要的就是它
        bisect.bisect_right(arr, x)   → 第一个 >  x 的位置

    一行搞定 ex4。

    ── 为什么要先手写再用库 ──
        ① 有些平台版本老，模块可能没有
        ② 面试官问"二分怎么实现"，你得能徒手写出来
        ③ 知道原理，才知道什么时候【不能】用二分（数据无序时）

    ⚠️ 注意：bisect 要求 arr 是【升序排好的】，乱序数据结果没意义。
    """
    n=int(input())
    data=sorted((list(map(int,input().split()))))
    x=int(input())
    b=bisect.bisect_left(data,x)
    print(b)


def ex6():
    """
    题：第一行 n，第二行 n 个整数；
        第三行 m，第四行 m 个整数。
        输出两个数组的【公共元素】：去重 + 升序 + 空格分隔。
        没有公共元素则输出 -1。

    样例输入：          样例输出：
        3                   2 3
        1 2 3
        4
        2 3 4 5

    ── 新工具：集合 set ──
        set(arr)     把列表变成集合（自动去重）
        a & b        交集：两个集合都有的
        a | b        并集：两个集合合起来（去重）
        a - b        差集：a 有但 b 没有的
        x in s       判断在不在 —— 比在列表里找快得多

    ── 提示 ──
        答案就是 sorted(set(a) & set(b))
        但要注意【可能是空的】，空的时候得输出 -1，不能直接 print

    ⚠️ 集合是无序的，所以必须再用 sorted() 排一次。
    """
    n=int(input())
    data=list(map(int,input().split()))
    m=int(input())
    arr=list(map(int,input().split()))
    b=sorted(set(data)&set(arr))
    if b:
        print(*b)
    else:
        print(-1)

def ex7():
    """
    题：输入一个金额 n（整数，单位元）。
        硬币面值固定 50 / 20 / 10 / 5 / 1 元，每种无限多。
        输出【最少】需要几枚硬币。

    样例：87  →  6
        50 + 20 + 10 + 5 + 1 + 1 = 87，共 6 枚

    ── 贪心是什么 ──
        每一步都选"当前能选的最大的"，不管以后。
        本币种下贪心是对的（现实货币面值都设计成能贪心的样子）。

    ── 循环骨架 ──
        coins = [50, 20, 10, 5, 1]
        cnt = 0
        for c in coins:
            cnt += n // c     # 这种面值能用几张
            n %= c            # 用掉之后还剩多少
        print(cnt)

    记两个语法糖：
        cnt += n // c    等价于   cnt = cnt + n // c
        n %= c           等价于   n = n % c
    """
    n=int(input())
    coins = [50, 20, 10, 5, 1]
    cnt=0
    for i in coins:
        cnt=cnt+n//i
        n=n%i
    print(cnt)




def ex8():
    """
    题：第一行 n，接下来 n 行每行两个整数 start end，表示一个活动的时间段。
        同一时间只能参加一个活动。
        后一个活动的【开始时间 >= 前一个的结束时间】时，才能接着参加。
        问最多能参加几个活动。

    样例输入：          样例输出：
        3                   2
        1 3
        2 4
        3 5

    解释：(2,4) 和 (1,3) 冲突，(3,5) 和 (1,3) 刚好接得上 → 最多 2 个。

    ── 贪心策略（关键！先想清楚再写）──
        ✗ 不是按开始时间排
        ✓ 而是按【结束时间升序】排

        理由：结束得越早，后面剩下的时间越多，能塞的活动就越多。

        排完序后从头扫一遍：
            如果当前活动的开始 >= 上一个选中的活动的结束 → 就选它

    ── 新工具 ──
        acts.sort(key=lambda x: x[1])    # 按每行的第 2 个数（结束时间）排
        for s, e in acts:                # 一行拆成两个变量（元组解包）

    ── 提示 ──
        需要一个变量记住"上一个选中的活动什么时候结束"。
        初值设成 -1（比任何开始时间都小），这样第一个一定会被选中。

    ⚠️ 这题和 ex7 都是贪心，但贪心策略完全不同 ——
       贪心的难点从来不是代码，是【想出按什么排序】。
    """
    n=int(input())
    data=[]
    for i in range(n):
        start,end=map(int,input().split())
        data.append((start,end))
    data.sort(key=lambda x:(x[1]))
    result=0
    last_end=-1
    for s,e in data:
        if s>=last_end:
            last_end=e
            result=result+1
    print(result)





# ============================================================
# 自检
# ============================================================

CHECKS = [
    ("ex1", "5\n3 1 4 1 5\n4\n",         "2"),
    ("ex1", "5\n3 1 4 1 5\n9\n",         "-1"),
    ("ex2", "5\n3 1 4 1 5\n1\n",         "1 3"),
    ("ex2", "3\n1 2 3\n9\n",             "-1"),
    ("ex3", "7\n1 3 5 7 9 11 13\n7\n",   "3"),
    ("ex3", "7\n1 3 5 7 9 11 13\n8\n",   "-1"),
    ("ex4", "5\n1 3 5 7 9\n4\n",         "2"),
    ("ex4", "5\n1 3 5 7 9\n10\n",        "5"),
    ("ex4", "5\n1 3 5 7 9\n0\n",         "0"),
    ("ex5", "5\n1 3 5 7 9\n4\n",         "2"),
    ("ex5", "5\n1 3 5 7 9\n10\n",        "5"),
    ("ex5", "5\n1 3 5 7 9\n0\n",         "0"),
    ("ex6", "3\n1 2 3\n4\n2 3 4 5\n",    "2 3"),
    ("ex6", "3\n1 2 3\n2\n4 5\n",        "-1"),
    ("ex7", "87\n",                      "6"),
    ("ex7", "100\n",                     "2"),
    ("ex8", "3\n1 3\n2 4\n3 5\n",        "2"),
    ("ex8", "4\n1 5\n2 3\n4 6\n5 7\n",   "2"),
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


def run_demos():
    print("=" * 64)
    print("演示 1：二分查找（在 [1,3,5,7,9,11,13] 里找 13）")
    print("=" * 64)
    pos, steps = demo_binary_search()
    print(f"  找到位置 {pos}，一共 {steps} 步（线性查找要 7 步）")

    print()
    print("=" * 64)
    print("演示 2：贪心凑 87 元（面值 50/20/10/5/1）")
    print("=" * 64)
    print(f"  {demo_greedy_coin()}")


if __name__ == "__main__":
    import sys as _sys
    only = next((a for a in _sys.argv[1:] if a.startswith("ex")), None)
    if only:
        self_check(only)
    else:
        run_demos()
        print()
        self_check()
