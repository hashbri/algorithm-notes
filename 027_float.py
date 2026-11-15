# -*- coding: utf-8 -*-
# 027_float.py —— 浮点精度（2026-11-12 晚加练）
#
# 阶段 0 的 L1 缺口最后一项。这个缺口不是"不会用浮点"，
# 是两件很具体的事：
#   ① **不能用 == 比浮点**（0.1 + 0.2 不等于 0.3）
#   ② **输出的格式要精确控制**（保留几位、四舍五入、百分号）
#
# 两件事各一题，都不是"数学题"，是"输出题"——
# 蓝桥杯里因为格式错丢的分，和因为算法错丢的分一样多。
#
# 用法：
#   python 027_float.py          跑全部
#   python 027_float.py F1       只跑 F1

import io
import sys

FUNCS = {}


def problem(name):
    def deco(fn):
        FUNCS[name] = fn
        return fn
    return deco


# ======================================================================
# F1 · 对账（浮点能不能用 == 比）
# ======================================================================
# 【题面】
#   读入三个小数 a、b、target，判断 a + b 是否等于 target。
#   相等输出 YES，不相等输出 NO。
#
#   "相等"的判定：允许极小的误差，差值小于 1e-9 就算相等。
#
# 【输入】一行三个小数
# 【输出】YES 或 NO
#
# 【例】
#   0.1 0.2 0.3    →  YES
#   0.1 0.2 0.4    →  NO
#   1 2 3          →  YES
#
# 【提示】
#   ① 先试试 `a + b == target` 这行，跑第一个用例看看输出什么。
#      如果输出 NO，想想为什么 —— 这不是 bug，是浮点数本身的表示方式。
#   ② 既然不能用"是否相等"，那用什么判断"够不够接近"？
#      数学上，两个数"差不多"是怎么描述的？
#   ③ 差值可能是负的（a+b 比 target 小），怎么办？
#
#   ⚠️ 不许用 round() 来绕（round 也有它自己的坑）。就用差值判断。
@problem("F1")
def F1():
    a,b,target=map(float,input().split())
    if abs(target-a-b)<1e-9:
        print("YES")
    else:
        print("NO")





# ======================================================================
# F2 · 成绩统计（输出格式）
# ======================================================================
# 【题面】
#   读入 n 个学生的整数成绩（0~100），输出两行：
#     第 1 行：平均分，保留 **2 位小数**
#     第 2 行：及格率，保留 **1 位小数**，后面带一个百分号 %
#   （及格线是 60 分，含 60）
#
# 【输入】
#   第 1 行：n
#   第 2 行：n 个整数（空格分隔）
#
# 【输出】两行，见样例
#
# 【例】
#   输入            输出
#   4               65.00
#   50 60 70 80     75.0%
#
#   （平均 260/4 = 65 → 65.00；及格 3 个 → 3/4 = 75.0%）
#
# 【提示】
#   ① 保留 2 位小数，Python 里怎么写？（f-string 里有个冒号后面能带格式）
#   ② 百分号怎么输出？如果直接写 `print(x, "%")`，中间会多一个空格 ——
#      你的老毛病就在这儿。怎么让它贴紧？
#   ③ 平均分是 sum/n，n 是整数、sum 是整数，除出来是什么类型？
#
#   ⚠️ 两个数的格式不一样（2 位 vs 1 位），别写成一个。
@problem("F2")
def F2():
    n=int(input())
    data=list(map(int,input().split()))
    a=sum(data)/len(data)
    x=0
    s=0
    for i in range(len(data)):
        if data[i]>=60:
            x+=1
    if x==0:
        b=0
    else:
        b=x/n*100
    print(f"{a:.2f}")
    print(f"{b:.1f}%")




# ======================================================================
# 自检（别改）
# ======================================================================

CHECKS = [
    # ---- F1 对账 ----
    ("F1", "0.1 0.2 0.3\n", "YES"),
    ("F1", "0.1 0.2 0.4\n", "NO"),
    ("F1", "1 2 3\n", "YES"),
    ("F1", "1.5 2.5 4.0\n", "YES"),
    ("F1", "0.7 0.1 0.8\n", "YES"),
    ("F1", "0.1 0.7 0.9\n", "NO"),
    # —— 2026-11-12 补：原 6 个用例全是「相等」或「a+b 比 target 小」，
    #    漏掉了「a+b 明显比 target 大」，导致不带 abs 的写法一路绿灯（我的用例失手）。
    ("F1", "1 2 1\n", "NO"),
    ("F1", "10 20 1\n", "NO"),
    ("F1", "5 5 6\n", "NO"),

    # ---- F2 成绩统计 ----
    ("F2", "4\n50 60 70 80\n", "65.00\n75.0%"),
    ("F2", "3\n60 70 80\n", "70.00\n100.0%"),
    ("F2", "1\n100\n", "100.00\n100.0%"),
    ("F2", "3\n59 59 59\n", "59.00\n0.0%"),
    ("F2", "2\n60 59\n", "59.50\n50.0%"),
]


def self_check(only=None):
    total = ok = 0
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
            print(f"  {name}  ✓ 通过")
        else:
            print(f"  {name}  ✗ 未过")
            print(f"       输入: {fake_input!r}")
            print(f"       期望: {exp!r}")
            print(f"       实际: {actual!r}")

    print()
    print(f"总计 {ok} / {total}")


if __name__ == "__main__":
    self_check(sys.argv[1] if len(sys.argv) > 1 else None)
