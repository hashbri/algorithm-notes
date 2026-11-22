# -*- coding: utf-8 -*-
"""031 · 白纸重写：试题 B「干涉条纹」（2026-11-20）

规则：不许打开 exam_20261118\\scratch.py，不许打开 _judge.py。
限时 15 分钟。

题面：
    a 是 1 号激光器功率，0 <= a <= A
    b 是 2 号激光器功率，0 <= b <= B
    A = 20269876543210
    B = 20260123456789
    问有多少对 (a, b) 使 a + b 恰好是完全平方数。
    答案对 998244353 取模。

只写 count_pairs 一个函数，返回方案数（取模后）。
"""

import math


def count_pairs(A, B):
    # ===== 你写这里 =====
    ans=0
    C=math.isqrt(A+B)
    for k in range(0,C+1):
        S=k*k
        lo=max(0,S-B)
        hi=min(A,S)
        if hi>=lo:
            ans+=hi-lo+1
    return ans%998244353


# ================= 自检（不要改动这一段） =================
if __name__ == "__main__":
    SMALL = [
        ((3, 4), 7),
        ((0, 0), 1),
        ((1, 1), 3),
        ((2, 3), 5),
        ((10, 10), 23),
    ]
    ok = 0
    print("小用例（可以手算核对的）：")
    for (A, B), exp in SMALL:
        got = count_pairs(A, B)
        good = got == exp
        ok += good
        print(f"  A={A:<3} B={B:<3} 期望 {exp:<4} 实际 {got!r:<6} {'✓' if good else '✗'}")

    print()
    print("真数据（结果发给我，我来判）：")
    big = count_pairs(20269876543210, 20260123456789)
    print(f"  count_pairs(A, B) = {big}")

    print()
    print(f"小用例 {ok} / {len(SMALL)}")
    if ok < len(SMALL):
        print("小用例没过就别看真数据了 —— 先用 A=3, B=4 手算一遍，看差在哪。")
