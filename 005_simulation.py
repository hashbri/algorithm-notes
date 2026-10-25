# -*- coding: utf-8 -*-
"""
基础模拟 —— 2026-10-08 提前学（原定 10/9）

═══ 什么叫"模拟题" ═══
    题目把一件事的【规则】讲清楚，让你照着规则一步步算。
    没有算法技巧，考察的是：
        ① 读懂题目（这题到底要我做什么）
        ② 把过程翻译成循环 + 判断
        ③ 边界情况想全（i 从 0 还是 1？数组够不够长？）

    这类题在比赛里通常是【第一道、第二道】，必须全清。
    特点：暴力循环通常能过，不用优化复杂度。

═══ 做模拟题的三步固定动作 ═══
    ① 手算样例：拿笔按题目规则走一遍，写下每一步的中间值
    ② 找重复：哪一部分在"重复做"？→ 那就是循环体
    ③ 数清楚：循环从哪到哪？一共几次？下标从 0 还是 1？

═══ 用法 ═══
    python 005_simulation.py           # 跑全部
    python 005_simulation.py ex3       # 只跑 ex3
"""

import sys


# ============================================================
# 演示区：先看两个模拟题的完整解题思路
# ============================================================

def demo_clock():
    """
    演示题：现在时间是 h 点 m 分，问 x 分钟后是几点几分？

    手算样例： 23:50 + 25 分钟 = ?
        50 + 25 = 75 分 → 75 >= 60，进位：75 - 60 = 15 分，小时 +1
        23 + 1 = 24 点 → 24 >= 24，归零：24 - 24 = 0 点
        答案：0 点 15 分

    翻译成代码：
        m += x
        if m >= 60:
            h += m // 60      # 进了几个小时
            m = m % 60        # 剩下的分钟
        h = h % 24            # 小时超过 24 就归零
    """
    h, m, x = 23, 50, 25
    m += x
    h += m // 60
    m = m % 60
    h = h % 24
    return h, m


def demo_stairs():
    """
    演示题：爬 n 级台阶，每次可以走 1 级或 2 级，问有几种走法。

    这道题【手算】就能发现规律：
        n=1 → 1 种  (1)
        n=2 → 2 种  (1+1, 2)
        n=3 → 3 种  (1+1+1, 1+2, 2+1)
        n=4 → 5 种
    规律：每一项 = 前两项之和（就是斐波那契）

    这就是"模拟/递推"的典型：先手算前几项，找到规律，再写循环。
    """
    dp = [1, 1]                  # dp[i] = 走到第 i 级的方法数
    for i in range(2, 6):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[1:6]               # n=1..5 的答案


# ============================================================
# 练习区
# ============================================================

def ex1():
    """
    题（秒转时分秒）：输入一个整数 s，表示秒数，输出「时 分 秒」，空格分隔。

    样例输入： 3661
    样例输出： 1 1 1

    解释：3661 秒 = 1 小时（3600 秒）+ 1 分钟（60 秒）+ 1 秒

    提示：
        1 小时 = 3600 秒，1 分钟 = 60 秒
        先算小时：h = s // 3600      （// 是整除，取商）
        再用余数算分钟：s %= 3600
        再算分钟：m = s // 60
        最后剩下的就是秒：sec = s % 60
        print(h, m, sec)    ← print 多个值自动空格分隔

    手算先行：拿 3661 自己走一遍 3600 / 60 这两个数。
    """
    n=int(input())
    a=n//3600
    b=n%3600//60
    c=n%60
    print(a,b,c)



def ex2():
    """
    题（日期天数）：输入年份和月份（格式「2026 2」），输出这个月有多少天。
        闰年规则：能被 4 整除且不能被 100 整除，或者能被 400 整除。
        闰年 2 月有 29 天，平年 28 天。其余月份固定：1/3/5/7/8/10/12 → 31 天，
        4/6/9/11 → 30 天。

    样例输入： 2026 2
    样例输出： 28

    样例输入： 2024 2
    样例输出： 29

    提示：
        先用一个列表把每个月的天数装好：
            days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            #         ↑ 下标 0 占个位，这样 days[1] 正好是 1 月
        这样比写 12 个 if 干净得多 —— 【用下标取答案】是模拟题常见技巧。

        然后判断闰年，如果是闰年就把 days[2] 改成 29。
        最后 print(days[m])。

    闰年判断写成一行：
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    """
    days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    a,b=map(int,input().split())
    if a%4==0 and a%100!=0:
        days[2]=29
        print(days[b])
    print(days[b])


def ex3():
    """
    题（数字反转）：输入一个正整数 n，输出它反转后的数。
        反转后前导 0 要省掉，例如 1200 → 21。

    样例输入： 12345
    样例输出： 54321

    样例输入： 1200
    样例输出： 21

    提示（两种做法，任选）：
        做法 1（字符串法，简单）：
            s = input().strip()
            r = s[::-1]              # 反转字符串
            print(int(r))            # 转成 int，前导零自动消失

        做法 2（数学法，理解取位）：
            ans = 0
            while n > 0:
                ans = ans * 10 + n % 10    # 每次把最后一位"接"到答案右边
                n //= 10                   # 去掉最后一位
            print(ans)

        建议两种都写一遍，做法 2 是理解"取位"的核心，后面很多题用得上。
        这里自检需要做法 2（因为自检传的是数字），但你可以两个都试试。
    """
    n=input()
    a=n[::-1]
    print(int(a))


def ex4():


    """
    题（成绩等级）：输入一个 0~100 的整数分数，按下面规则输出等级：
        90~100 → A
        80~89  → B
        70~79  → C
        60~69  → D
        0~59   → F

    样例输入： 85
    样例输出： B

    提示：
        if/elif 链，从上往下判断，第一个满足就停。
        【顺序很重要】：必须从高分往低分写，或者用区间判断。
        如果先写 if s >= 60 → D，那 85 也会被吞掉。

        写法： if s >= 90: ... elif s >= 80: ... 这样写最安全。
    """
    n=int(input())
    if n<=100 and n>=90:

        print("A")
    elif n<=89 and n>=80:
        print("B")
    elif n<=79 and n>=70:
        print("C")
    elif n<=69 and n>=60:
        print("D")
    else:
        print("F")


def ex5():
    """
    题（简单累加）：输入 n，再输入 n 个整数，输出它们的和。
        但有个特殊规则：如果某个数是【负数】，就把它按【它的相反数】加进去
        （也就是全部当正数加，等于求绝对值之和）。

    样例输入：
        5
        1 -2 3 -4 5

    样例输出： 15

    解释：|1| + |-2| + |3| + |-4| + |5| = 1+2+3+4+5 = 15

    提示：
        total = 0
        for x in arr:
            if x < 0:
                x = -x        # 变正
            total += x
        print(total)

        或者直接用内置函数 abs(x) —— 求绝对值。
    """
    n=int(input())
    total=0
    a=list(map(int,input().split()))
    for i in a:
        if i<0:
            i=-i
        total+=i
    print(total)


def ex6():
    """
    题（模拟排队）：输入 n 个人的处理时间，每个人处理完才轮到下一个。
        输出每个人的【完成时刻】（第 1 个人从 0 开始处理）。

    样例输入：
        4
        3 5 2 4

    样例输出：
        3 8 10 14

    解释：
        第 1 人：0 开始，处理 3 → 3 结束
        第 2 人：3 开始，处理 5 → 8 结束
        第 3 人：8 开始，处理 2 → 10 结束
        第 4 人：10 开始，处理 4 → 14 结束

    提示：
        cur = 0                  # 当前时间
        ans = []
        for t in arr:
            cur += t             # 这个人处理完的时刻
            ans.append(cur)
        print(*ans)

        这就是"模拟"的精髓：用一个变量记录【当前状态】，边循环边更新。
        （学名叫"前缀和"，但你现在只需要理解"累着加"这个动作。）
    """
    n=int(input())
    a=list(map(int,input().split()))
    total=0
    b=[]
    for i in a:
        total+=i
        b.append(total)
    print(*b)


def ex7():
    """
    题（模拟走迷宫式移动）：一开始在位置 0。
        输入一串移动指令，L 表示向左 1 格，R 表示向右 1 格。
        输出最终位置。

    样例输入： LLRRRL
    样例输出： -1

    解释：0 →L -1 →L -2 →R -1 →R 0 →R 1 →L 0

    等等，上面手算错了，重算一遍：
        起点 0
        L: -1
        L: -2
        R: -1
        R: 0
        R: 1
        L: 0
        最终 0

    （题面我留了个手算错误的痕迹，是故意的 —— 想告诉你【手算也要认真】，
     比赛时因为手算马虎丢掉的分，比不会做还冤。）

    样例输出： 0

    提示：
        pos = 0
        s = input().strip()       # .strip() 去掉行末换行
        for ch in s:              # 直接遍历字符串的每个字符
            if ch == 'L':
                pos -= 1
            else:
                pos += 1
        print(pos)

        注意：字符串可以直接 for 遍历，每个字符就是一轮 —— 这是很重要的手感。
    """
    start=0
    n=input().strip()
    for i in n:
        if i=="L":
            a=-1
        else:
            a=1
        start=start+a
    print(start)



def ex8():
    """
    题（综合）：一栋楼有 n 层（1 楼到 n 楼），电梯一开始在 1 楼。
        给出一串要去的楼层，按顺序输出电梯【每层移动的距离】的总和。

    样例输入：
        3
        5
        3
        8

    样例输出： 11

    解释：从 1 到 5 → 走 4 层
          从 5 到 3 → 走 2 层
          从 3 到 8 → 走 5 层
          合计 4 + 2 + 5 = 11

    输入格式：第一行 n 表示有几次乘梯，接下来 n 行每行一个目标楼层。

    提示：
        n = int(input())
        cur = 1                  # 当前楼层
        total = 0
        for i in range(n):
            target = int(input())
            total += abs(target - cur)     # 距离永远取正，用 abs
            cur = target                   # 到了之后更新当前位置
        print(total)

        关键：abs() 用来算"距离"，因为下楼是负数。
    """
    n=int(input())
    start=1
    total=0
    for i in range(n):
        target=int(input())
        a=abs(target-start)
        total=total+a
        start=target
    print(total)






# ============================================================
# 自检
# ============================================================

CHECKS = [
    ("ex1", "3661\n",                    "1 1 1"),
    ("ex2", "2026 2\n",                  "28"),
    ("ex3", "12345\n",                   "54321"),
    ("ex4", "85\n",                      "B"),
    ("ex5", "5\n1 -2 3 -4 5\n",          "15"),
    ("ex6", "4\n3 5 2 4\n",              "3 8 10 14"),
    ("ex7", "LLRRRL\n",                  "0"),
    ("ex8", "3\n5\n3\n8\n",              "11"),
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
    print("演示 1：时钟模拟（23:50 + 25 分钟 = ?）")
    print("=" * 64)
    h, m = demo_clock()
    print(f"  {h} 点 {m} 分")

    print()
    print("=" * 64)
    print("演示 2：爬楼梯（先手算找规律）")
    print("=" * 64)
    print(f"  n=1..5 的走法数: {demo_stairs()}")


if __name__ == "__main__":
    import sys as _sys
    only = next((a for a in _sys.argv[1:] if a.startswith("ex")), None)
    if only:
        self_check(only)
    else:
        run_demos()
        print()
        self_check()
