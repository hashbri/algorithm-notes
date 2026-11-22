# -*- coding: utf-8 -*-
"""第 1 套真题（17 届 B 组）判卷 · 2026-11-18

肉包独立写参考解，不看用户代码，只比结果。
"""
import io
import math
import subprocess
import sys

HERE = r"D:\algorithm-notes\exam_20261118"
MOD = 998244353


# ============================================================
# 试题 A 和平干饭日：第 i 天吐出 123...i，问 1..2026 天里多少天能被 26 整除
# ============================================================
def ref_A():
    # 做法一：只维护模 26 的余数（不建大整数）
    s, cnt = 0, 0
    for i in range(1, 2027):
        s = (s * pow(10, len(str(i)), 26) + i) % 26
        if s == 0:
            cnt += 1
    return cnt


def ref_A_bigint():
    # 做法二：真·大整数直接拼（交叉验证，多一个信任来源）
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(200000)
    total = 1
    cnt = 0
    if total % 26 == 0:
        cnt += 1
    for i in range(2, 2027):
        total = total * (10 ** len(str(i))) + i
        if total % 26 == 0:
            cnt += 1
    return cnt


# ============================================================
# 试题 B 干涉条纹：a∈[0,A], b∈[0,B], a+b 是完全平方数，求方案数 mod 998244353
# ============================================================
def ref_B():
    A = 20269876543210
    B = 20260123456789
    ans = 0
    for k in range(0, math.isqrt(A + B) + 1):
        S = k * k
        lo = max(0, S - B)
        hi = min(A, S)
        if hi >= lo:
            ans += hi - lo + 1
    return ans % MOD


# ============================================================
# 3368 定制展示盘：最小 p*q >= n，p,q >= 2  <=>  最小的 >= max(n,4) 的合数
# ============================================================
def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True


def ref_3368_one(n):
    s = max(n, 4)
    while is_prime(s):
        s += 1
    return s


def ref_3368(ns):
    return [ref_3368_one(n) for n in ns]


def run_user(ns):
    """真的把用户的 p3368.py 跑一遍，看它实际打印什么。"""
    data = f"{len(ns)}\n" + "\n".join(str(x) for x in ns) + "\n"
    p = subprocess.run(
        [sys.executable, HERE + r"\p3368.py"],
        input=data, capture_output=True, text=True, encoding="utf-8", timeout=60,
    )
    return p.stdout


def main():
    print("=" * 60)
    print("试题 A  和平干饭日")
    print("=" * 60)
    a1, a2 = ref_A(), ref_A_bigint()
    print(f"  参考解（模 26）      = {a1}")
    print(f"  参考解（真大整数）    = {a2}   {'一致' if a1 == a2 else '!! 不一致 !!'}")
    with open(HERE + r"\A.txt", encoding="utf-8") as f:
        user_A = f.read().strip()
    print(f"  我交的               = {user_A!r}")
    print(f"  判定                 = {'✔ 正确' if user_A == str(a1) else '✘ 错误'}")

    print()
    print("=" * 60)
    print("试题 B  干涉条纹")
    print("=" * 60)
    b = ref_B()
    print(f"  参考解               = {b}")
    with open(HERE + r"\B.txt", encoding="utf-8") as f:
        user_B = f.read().strip()
    print(f"  我交的               = {user_B!r}")
    if user_B == "":
        print("  判定                 = ✘ 空题（0 分）")
    else:
        print(f"  判定                 = {'✔ 正确' if user_B == str(b) else '✘ 错误'}")

    print()
    print("=" * 60)
    print("3368  定制展示盘")
    print("=" * 60)
    # 1) 官方样例
    out = run_user([3, 5])
    exp = "4\n6"
    got = out.rstrip("\n")
    print(f"  样例 n=[3,5]  期望 {exp!r}  实际 {got!r}  {'✔' if got == exp else '✘'}")

    # 2) 小数据全扫 1..200，逐行比对（格式 + 数值一起查）
    ns = list(range(1, 201))
    got_lines = run_user(ns).strip().splitlines()
    exp_lines = [str(x) for x in ref_3368(ns)]
    if got_lines == exp_lines:
        print(f"  n=1..200 全扫    ✔ 200/200")
    else:
        print(f"  n=1..200 全扫    ✘ 输出 {len(got_lines)} 行，应为 {len(exp_lines)} 行")
        bad = 0
        for i, (g, e) in enumerate(zip(got_lines, exp_lines)):
            if g.strip() != e:
                if bad < 5:
                    print(f"        n={ns[i]}  期望 {e}  实际 {g}")
                bad += 1
        if bad:
            print(f"        数值错 {bad} 个")

    # 3) 大数专项：n 是两素之积且两因子都 > 998（用户的 p 上界是 998）
    hard = [1009 * 1009, 1009 * 1013, 1013 * 1019, 10 ** 9, 999999937]
    print()
    print("  大数专项（n 上界 1e9）：")
    got_lines = run_user(hard).strip().splitlines()
    exp_h = ref_3368(hard)
    for n, e, g in zip(hard, exp_h, got_lines + [""] * 9):
        print(f"    n={n:<12} 期望 {e:<12} 实际 {g:<12} {'✔' if g.strip() == str(e) else '✘'}")

    # 4) T=100 行数检查
    ns100 = [7 * i + 11 for i in range(1, 101)]
    out100 = run_user(ns100)
    n_lines = len(out100.strip().splitlines())
    print()
    print(f"  T=100 时应输出 100 行，实际 {n_lines} 行  {'✔' if n_lines == 100 else '✘'}")


if __name__ == "__main__":
    main()
