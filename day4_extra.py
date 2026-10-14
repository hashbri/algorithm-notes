"""
Day4 加练 · 查找 / 二分 / 贪心  ——  23 个测试用例，先跑再交

用法：
    python day4_extra.py            # 跑全部（先看演示，再自检）
    python day4_extra.py ex3        # 只跑 ex3

分组：
    A 组  ex1~ex4   二分（你的重点：命中 / 下界 / 上界 / 用库）
    B 组  ex5~ex7   贪心（换面额 / 换数据 / 换题型）
    C 组  ex8~ex10  工具（set 三运算 / Counter / 列表推导式）

⚠️ A 组是重头戏。二分不熟练，就靠这四道刷出肌肉记忆。
"""

from collections import Counter
from bisect import bisect_left
import sys


# ============================================================
# A 组 · 二分
# ============================================================

def ex1():
    """
    题：第一行 n，第二行 n 个【升序】整数，第三行 x。
        输出 x 在数组中的下标；不存在输出 -1。

    样例：
        输入 7 / 1 3 5 7 9 11 13 / 7   → 输出 3
        输入 5 / 2 4 6 8 10 / 5        → 输出 -1

    ── 这就是 ex3 的原版，练手用 ──
        left, right = 0, n - 1
        while left <= right:        ← 有等号
            mid = (left + right) // 2
            if arr[mid] == x:   记下来，break
            elif arr[mid] < x:  left = mid + 1
            else:               right = mid - 1
        循环外输出记录的下标（没找到就是 -1）

    提示：pos = -1 要写在【循环外面】。
    """
    n=int(input())
    data=list(map(int,input().split()))
    x=int(input())
    left,right=0,n-1
    pos=-1
    while left<=right:
        mid=(left+right)//2
        if data[mid]==x:
            pos=mid
            break
        elif data[mid]>x:
            right=mid-1
        else:
            left=mid+1
    print(pos)



def ex2():
    """
    题：第一行 n，第二行 n 个【升序】整数，第三行 x。
        输出【第一个 >= x】的元素下标；如果全都 < x，输出 n。

    样例：
        输入 5 / 1 3 5 7 9 / 4    → 输出 2   （arr[2]=5 是第一个 >= 4 的）
        输入 5 / 1 3 5 7 9 / 6    → 输出 3   （6 不在数组里，第一个 >= 6 的是 7）
        输入 5 / 1 3 5 7 9 / 10   → 输出 5   （全都 < 10，所以输出 n）

    ── 求下界模板（和 ex4 里那道一样，换组数据再练一遍）──
        left, right = 0, n          ← right 从 n 开始（答案可能是 n）
        while left < right:         ← 没有等号
            mid = (left + right) // 2
            if arr[mid] < x:  left = mid + 1     ← mid 不满足，排除
            else:             right = mid        ← mid 可能满足，留着
        循环结束 left == right，就是答案，直接输出 left
    """
    n=int(input())
    data=list(map(int,input().split()))
    x=int(input())
    left,right=0,n
    while left<right:
        mid=(left+right)//2
        if data[mid]<x:
            left=mid+1
        else:
            right=mid
    print(left)

    


def ex3():
    """
    题：第一行 n，第二行 n 个【升序】整数，第三行 x。
        输出【最后一个 <= x】的元素下标；如果全都 > x，输出 -1。

    样例：
        输入 5 / 1 3 5 7 9 / 6    → 输出 2   （5 是最后一个 <= 6 的）
        输入 5 / 1 3 5 7 9 / 0    → 输出 -1  （1 都 > 0）
        输入 5 / 1 3 5 7 9 / 9    → 输出 4

    ── 新题型：求上界。但不用新模板，只需改一个字 ──
        ex2 找的是【第一个 >= x】，位置记为 p
        这题找的是【最后一个 <= x】

        巧办法：先求「第一个 > x」的位置 p，那么答案就是 p - 1。

        所以把 ex2 的条件从 arr[mid] < x 改成 arr[mid] <= x：
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= x:  left = mid + 1     ← 只剩 <= 的
                else:              right = mid
        循环结束 left 就是「第一个 > x」的位置 → 输出 left - 1

    ⚠️ 两种边界要想清楚：
        - x 比所有元素都大  → left 会变成 n，输出 n-1（最后一个元素）✓
        - x 比所有元素都小  → left 停在 0，输出 -1 ✓
    """
    n=int(input())
    data=list(map(int,input().split()))
    x=int(input())
    left,right=0,n
    while left<right:
        mid=(left+right)//2
        if data[mid]>x:
            right=mid
        else:
            left=mid+1
    print(left-1)



def ex4():
    """
    题：同 ex2（输出第一个 >= x 的下标，没有则输出 n），但【必须用库】。

    样例：同 ex2 —— 5 / 1 3 5 7 9 / 4 → 2 ；/ 6 → 3 ；/ 10 → 5

    ── 工具：bisect ──
        from bisect import bisect_left
        print(bisect_left(arr, x))

        bisect_left(arr, x) 的返回值就是「第一个 >= x 的下标」，
        范围 0 ~ n，正好和 ex2 的要求一模一样 —— 一行顶你写八行。

    ── 记清楚这两个别再搞混 ──
        bisect_left (arr, x)   →  第一个 >= x 的下标
        bisect_right(arr, x)   →  第一个 >  x 的下标

        注意：两个都要求 arr 是【升序】的，否则结果没有意义。
    """
    from bisect import bisect_left
    n=int(input())
    data=list(map(int,input().split()))
    x=int(input())
    print(bisect_left(data,x))


# ============================================================
# B 组 · 贪心
# ============================================================

def ex5():
    """
    题：输入一个金额 n，用面额 100 50 20 10 5 1 的纸币凑出来，
        问【最少要几张】。

    样例：
        输入 87   → 输出 6    （50+20+10+5+1+1，共 6 张）
        输入 100  → 输出 1    （1 张 100）
        输入 9    → 输出 5    （5+1+1+1+1，共 5 张）

    ── 贪心策略：从大面额开始尽量多拿 ──
        coins = [100, 50, 20, 10, 5, 1]
        for c in coins:
            cnt += n // c        ← 这个面额最多能拿几张
            n %= c               ← 拿完后剩下的钱

    ⚠️ 两个连着的运算符分工不同：
        // 是「能拿几张」
        %  是「剩下多少」
        这两行是贪心凑钱的标准写法，背下来。
    """
    x=0
    n=int(input())
    coins = [100, 50, 20, 10, 5, 1]
    for i in coins:
        x=x+n//i
        n=n%i
    print(x)



def ex6():
    """
    题：第一行 n，接下来 n 行每行两个整数 start end，表示一个活动的时间段。
        同一时间只能参加一个活动，后一个的开始时间 >= 前一个的结束时间才能接着参加。
        问最多能参加几个活动。

    样例：
        输入 4 / 1 2 / 2 3 / 3 4 / 4 5   → 输出 4   （首尾相接，全都能参加）
        输入 3 / 1 10 / 2 3 / 4 5        → 输出 2   （(1,10) 太长，选它会亏）

    ── 贪心策略：按【结束时间】升序排 ──
        acts.sort(key=lambda x: x[1])
        last_end = -1
        for s, e in acts:
            if s >= last_end:
                cnt += 1
                last_end = e      ← 只在【选中】时更新
        print(cnt)

    ⚠️ 三个易错点（你昨天都碰过）：
        ① sort 的 key 别拼错（是 key，不是 ket）
        ② last_end 更新成【当前活动的结束时间 e】
        ③ last_end 只在【选中】的时候改，跳过时不能动
    """
    n=int(input())
    list=[]
    for i in range(n):
        start,end=map(int,input().split())
        list.append((start,end))
    list.sort(key=lambda x:(x[1]))
    last_end=-1
    a=0
    for s,e in list:
        if s>=last_end:
            a=a+1
            last_end=e
    print(a)





def ex7():
    """
    题：第一行 n（孩子数），第二行 n 个整数表示每个孩子的胃口；
        第三行 m（饼干数），第四行 m 个整数表示每块饼干的大小。
        一块饼干能满足一个孩子，当且仅当 饼干大小 >= 孩子胃口。
        每个孩子最多一块，每块饼干最多给一个孩子。问最多能满足几个孩子。

    样例：
        输入 2 / 1 2 / 3 / 1 1 1      → 输出 1   （只有 1 大小的饼干，只能满足胃口 1 的孩子）
        输入 3 / 1 2 3 / 2 / 1 2      → 输出 2   （1→孩子1，2→孩子2，孩子3 没得吃）

    ── 新贪心策略：两个列表都排序，然后用两个指针走 ──
        kids.sort()
        cookies.sort()
        i = j = 0        ← i 走孩子，j 走饼干
        while i < n and j < m:
            if cookies[j] >= kids[i]:   饼干够 → 满足这个孩子，两个都前进
                cnt += 1
                i += 1
                j += 1
            else:                       饼干不够 → 这块饼干废了，只前进饼干
                j += 1
        print(cnt)

    ── 为什么这么贪心是对的 ──
        「用小饼干满足小胃口、把大饼干留给大胃口」——
        饼干大小和胃口都排好序，从小到大一对一配，就是最省的用法。
        这个模式叫【双指针】，比赛里非常常见。
    """
    n=int(input())
    kids=list(map(int,input().split()))
    m=int(input())
    cookies=list(map(int,input().split()))
    kids.sort()
    cookies.sort()
    i=j=0
    cnt=0
    while i<n and j<m:
        if cookies[j]>=kids[i]:
            i+=1
            j+=1
            cnt+=1
        else:
            j+=1
    print(cnt)






# ============================================================
# C 组 · 工具
# ============================================================

def ex8():
    """
    题：第一行 n，第二行 n 个整数（集合 A）；第三行 m，第四行 m 个整数（集合 B）。
        输出三行：
            第一行：A 和 B 的【交集】，升序，空则输出 -1
            第二行：A 和 B 的【并集】，升序，空则输出 -1
            第三行：A 和 B 的【差集 A-B】，升序，空则输出 -1

    样例：
        输入 3 / 1 2 3 / 4 / 2 3 4 5
        输出：
            2 3
            1 2 3 4 5
            1

    ── 工具：set 的三种运算 ──
        A = set(...)   B = set(...)
        A & B    交集（两边的都有）
        A | B    并集（合并去重）
        A - B    差集（A 有、B 没有）

        set 会自动去重，所以不用自己处理重复元素。
        排序用 sorted(...)，因为 set 本身是【无序】的，直接输出顺序不固定。

    ⚠️ 输出格式：
        print(*ans) 拆包输出（一行一个空格分隔）
        空的时候要输出 -1 —— 用 if ans: 判断（不是 len）
    """
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))




def ex9():
    """
    题：第一行 n，第二行 n 个整数。输出所有【只出现一次】的数，升序，一行空格分隔；
        如果一个都没有，输出 -1。

    样例：
        输入 5 / 1 2 2 3 3   → 输出 1
        输入 7 / 4 4 5 6 6 7 7   → 输出 5

    ── 工具：Counter（Day2 用过，这里复习）──
        cnt = Counter(arr)
        ans = sorted(k for k, v in cnt.items() if v == 1)
        print(*ans) if ans else print(-1)

        sorted(...) 里直接写生成器也行 —— 这是列表推导式的变体。
    """
    raise NotImplementedError


def ex10():
    """
    题：一行若干个整数，输出所有【值为偶数】的元素下标（从 0 开始），空格分隔；
        一个都没有则输出 -1。

    样例：
        输入 1 2 3 4 5 6   → 输出 1 3 5   （下标 1、3、5 的值是 2、4、6）
        输入 1 3 5         → 输出 -1

    ── 工具：列表推导式（这是 Day4 工具清单的最后一项）──
        老写法（for + append 三步）：
            idx = []
            for i, v in enumerate(arr):
                if v % 2 == 0:
                    idx.append(i)

        列表推导式（一行）：
            idx = [i for i, v in enumerate(arr) if v % 2 == 0]

        读法：「把每个符合条件的 i 收集成列表」
              [ 要收集什么  for 变量 in 数据源  if 条件 ]

    ⚠️ 注意是 i（下标）不是 v（值）—— 跟 ex2 那次别搞反。
    """
    raise NotImplementedError


# ============================================================
# 自检
# ============================================================

CHECKS = [
    ("ex1", "7\n1 3 5 7 9 11 13\n7\n",    "3"),
    ("ex1", "5\n2 4 6 8 10\n5\n",         "-1"),

    ("ex2", "5\n1 3 5 7 9\n4\n",          "2"),
    ("ex2", "5\n1 3 5 7 9\n6\n",          "3"),
    ("ex2", "5\n1 3 5 7 9\n10\n",         "5"),

    ("ex3", "5\n1 3 5 7 9\n6\n",          "2"),
    ("ex3", "5\n1 3 5 7 9\n0\n",          "-1"),
    ("ex3", "5\n1 3 5 7 9\n9\n",          "4"),

    ("ex4", "5\n1 3 5 7 9\n4\n",          "2"),
    ("ex4", "5\n1 3 5 7 9\n6\n",          "3"),
    ("ex4", "5\n1 3 5 7 9\n10\n",         "5"),

    ("ex5", "87\n",                       "6"),
    ("ex5", "100\n",                      "1"),
    ("ex5", "9\n",                        "5"),

    ("ex6", "4\n1 2\n2 3\n3 4\n4 5\n",    "4"),
    ("ex6", "3\n1 10\n2 3\n4 5\n",        "2"),

    ("ex7", "2\n1 2\n3\n1 1 1\n",         "1"),
    ("ex7", "3\n1 2 3\n2\n1 2\n",         "2"),

    ("ex8", "3\n1 2 3\n4\n2 3 4 5\n",     "2 3\n1 2 3 4 5\n1"),

    ("ex9", "5\n1 2 2 3 3\n",             "1"),
    ("ex9", "7\n4 4 5 6 6 7 7\n",         "5"),

    ("ex10", "1 2 3 4 5 6\n",             "1 3 5"),
    ("ex10", "1 3 5\n",                   "-1"),
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
    only = next((a for a in sys.argv[1:] if a.startswith("ex")), None)
    self_check(only)
