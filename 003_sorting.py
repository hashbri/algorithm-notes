# -*- coding: utf-8 -*-
"""
列表与排序 —— 2026-10-07 提前学（原定 10/8）

今天的四件事：
    1. sort() 与 sorted() 的区别  ← 会改原列表吗？
    2. 多关键字排序 key=lambda      ← 比赛高频，重点中的重点
    3. Counter 统计词频
    4. 列表常用操作（切片、反转、求和、去重）

用法：
    1) 先跑 python 003_sorting.py 看「演示区」的实际输出。
    2) 再填「练习区」的 6 道题。
    3) 全部填完再跑一次 python 003_sorting.py，看自检结果。

═══ 核心口诀 ═══
    升序：直接排
    降序：加负号  key=lambda x: -x
    多关键字：写成元组  key=lambda x: (-第一关键字, 第二关键字)
"""

import sys
from collections import Counter


# ============================================================
# 演示区：直接跑本文件就能看到效果，不用改这里
# ============================================================

def demo_sort_vs_sorted():
    """sort() 原地改；sorted() 返回新的，原列表不动。"""
    a = [3, 1, 4, 1, 5]
    b = [3, 1, 4, 1, 5]

    a.sort()                    # 原地排序，返回 None
    result_a = a                # a 已经被改了

    result_b = sorted(b)        # 返回新列表，b 不动

    return {
        "原列表 b（没动）": b,
        "sorted 返回的新列表": result_b,
        "sort 之后 a 被改成了": result_a,
        "sort 的返回值": None,   # 注意！a.sort() 返回的是 None
    }


def demo_multi_key():
    """多关键字排序：分数降序，分数相同按年龄升序。"""
    students = [
        ("Tom", 90, 18),
        ("Amy", 90, 17),
        ("Bob", 85, 19),
        ("Zoe", 90, 16),
    ]
    return sorted(students, key=lambda x: (-x[1], x[2]))


def demo_counter():
    """Counter：一步统计每个元素出现几次。"""
    words = ["a", "b", "a", "c", "a", "b"]
    cnt = Counter(words)
    return {
        "Counter 对象": dict(cnt),
        "a 出现几次": cnt["a"],
        "出现最多的一个": cnt.most_common(1),
        "出现最多的前两个": cnt.most_common(2),
    }


def demo_list_ops():
    """列表常用操作速览。"""
    arr = [3, 1, 4, 1, 5]
    return {
        "原列表": arr,
        "求和 sum": sum(arr),
        "最大 max": max(arr),
        "最小 min": min(arr),
        "长度 len": len(arr),
        "反转 arr[::-1]": arr[::-1],
        "切片 arr[1:3]": arr[1:3],
        "去重后（转 set 再转回）": sorted(set(arr)),
        "统计 1 出现几次": arr.count(1),
        "5 在不在里面": 5 in arr,
    }


# ============================================================
# 练习区：填这 6 道
# ============================================================

def ex1():
    """
    题：输入一行若干整数，按【从小到大】输出，数字之间用空格分隔。
    样例输入： 3 1 4 1 5
    样例输出： 1 1 3 4 5
    提示：排完序的列表要输出成一行——用 print(*arr) 可以自动拆成空格分隔。
          或者 print(" ".join(map(str, arr)))。
    """
    a=list(map(int,input().split()))
    b=sorted(a)
    print(*b)

def ex2():
    """
    题：输入一行若干整数，按【从大到小】输出。
    样例输入： 3 1 4 1 5
    样例输出： 5 4 3 1 1
    提示：升序是 sort()，降序是 sort(reverse=True)。
          注意 reverse=True 是一个参数，别写成 sort(reverse) 或者 sort(-1)。
    """
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    print(*a)



def ex3():
    """
    题：输入 n 个同学的信息，每个同学一行，格式为「姓名 分数」，
         按分数从高到低输出姓名；分数相同的，按名字字典序（升序）输出。
    样例输入：
        4
        Tom 90
        Amy 90
        Bob 85
        Zoe 90
    样例输出：
        Amy
        Tom
        Zoe
        Bob

    这是【多关键字排序】的经典题，也是今天最重要的一道。去上面看 demo_multi_key。
    提示：
        - 每个同学读进来是 "Tom 90" 这样的字符串，要拆成 name 和 score
        - score 要转成 int 才能比大小
        - 最终按 (-score, name) 排序
        - 排序后只输出姓名部分
    """
    n=int(input())
    student=[]
    for i in range(n):
        line=input()
        a=line.split()
        name=a[0]
        score=int(a[1])
        student.append((name,score))
    student.sort(key=lambda x:(-x[1],x[0]))
    for s in student:
        print(s[0])





def ex4():
    """
    题：输入一行若干整数，输出其中出现次数最多的那个数。
        如果并列，取其中较大的那个。
    样例输入： 1 3 3 2 1 3 1
    样例输出： 3
    解释：1 出现 3 次，3 出现 3 次，并列；取较大的 → 3。
    提示：用 Counter 统计，most_common(n) 拿到的是 [(元素, 次数), ...] 列表。
          并列时的取舍规则：把 (次数, 元素) 当成排序关键字，取最大的那组。
    """
    word=list(map(int,input().split()))
    cnt=Counter(word)
    b=sorted(cnt.items(),key=lambda x:(x[1],x[0]))
    print(b[-1][0])


def ex5():
    """
    题：输入一行若干整数，输出去重后的结果，按从小到大排。
    样例输入： 3 1 4 1 5 3
    样例输出： 1 3 4 5
    提示：set() 能自动去重，但它是无序的，所以要再排一次序。
          sorted(set(arr)) 一行搞定。
    """
    num=list(map(int,input().split()))
    a=sorted(set(num))
    print(*a)

def ex6():
    """
    题（综合）：输入 n，再输入 n 个整数，输出第 2 大的数（不重复计数）。
    样例输入：
        5
        10 5 8 8 3
    样例输出： 8
    解释：数字是 10 5 8 8 3，去重后是 3 5 8 10，第 2 大是 8。
    提示：先 sorted(set(arr)) 去重排序，再取倒数第 2 个（下标 -2）。
    """
    n=int(input())
    num=list(map(int,input().split()))
    a=sorted(set(num))
    print(a[-2])

# ============================================================
# 自检
# ============================================================

CHECKS = [
    ("ex1", "3 1 4 1 5\n",              "1 1 3 4 5"),
    ("ex2", "3 1 4 1 5\n",              "5 4 3 1 1"),
    ("ex3", "4\nTom 90\nAmy 90\nBob 85\nZoe 90\n", "Amy\nTom\nZoe\nBob"),
    ("ex4", "1 3 3 2 1 3 1\n",          "3"),
    ("ex5", "3 1 4 1 5 3\n",            "1 3 4 5"),
    ("ex6", "5\n10 5 8 8 3\n",          "8"),
]


def self_check():
    import io

    print("=" * 60)
    print("自检：期望值 vs 实际输出")
    print("=" * 60)

    ok = 0
    for name, fake_input, expected in CHECKS:
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
        except Exception as e:
            actual = f"<报错: {type(e).__name__}: {e}>"
        finally:
            sys.stdin = old_stdin

        passed = (actual == expected.strip())
        ok += passed
        print(f"  {name:5s} {'✓ 通过' if passed else '✗ 未过'}   期望: {expected.strip()!r}   实际: {actual!r}")

    print("-" * 60)
    print(f"通过 {ok} / {len(CHECKS)}")
    print("=" * 60)


def run_demos():
    print("=" * 60)
    print("演示 1：sort() vs sorted()")
    print("=" * 60)
    for k, v in demo_sort_vs_sorted().items():
        print(f"  {k:24s} = {v}")

    print()
    print("=" * 60)
    print("演示 2：多关键字排序（分数降序，同分按年龄升序）")
    print("=" * 60)
    print("  原始:", [("Tom", 90, 18), ("Amy", 90, 17), ("Bob", 85, 19), ("Zoe", 90, 16)])
    print("  排序后:", demo_multi_key())

    print()
    print("=" * 60)
    print("演示 3：Counter 统计词频")
    print("=" * 60)
    for k, v in demo_counter().items():
        print(f"  {k:24s} = {v}")

    print()
    print("=" * 60)
    print("演示 4：列表常用操作")
    print("=" * 60)
    for k, v in demo_list_ops().items():
        print(f"  {k:24s} = {v}")


if __name__ == "__main__":
    import sys as _sys
    if "--demo" in _sys.argv:
        run_demos()
    else:
        run_demos()
        print()
        self_check()
