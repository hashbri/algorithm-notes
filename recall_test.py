"""
recall_test · 空白默写卷  ——  10/14 竞赛前热身

★ 这份卷子和 mock_exam.py 最大的区别：

    mock_exam.py 的函数里塞满了"提示"，你是在提示旁边抄代码。
    这份卷子【只有题面】，一个字的解法提示都没有。

    这才是真实考场的状态 —— 屏幕上只有题，没有别人写好的公式。


================================================================
怎么用（重要，别破坏它）
================================================================
1. 别往下翻看自检里的期望输出。（题面里的样例可以看，那是题目本来就给的。）
2. 一次只做一道：读题 → 手算样例 → 写 → 心里跑一遍 → 再往下做。
3. 七道全写完，再运行自检：

       python recall_test.py          # 跑全部
       python recall_test.py Q3       # 只跑 Q3

4. 写不出来就空着，别偷看。空着的才是有价值的 ——
   那才是你周三真正拿不到的分。


================================================================
这七道题考什么（题号和 mock_exam.py 的 A~H 没有对应关系）
================================================================
    Q1  倒着数      循环 + 倒序输出             ← mock_exam.py  A 的变式
    Q2  从大到小    排序（反向）                ← mock_exam.py  B 的变式
    Q3  换个位置    交换两个变量 + f-string     ← mock_exam.py  C 的变式
    Q4  单词去重    去重 + 排序                 ← mock_exam.py  D 的变式
    Q5  中间那个    排序后取中间                ← mock_exam.py  E 的变式
    Q6  平均分      浮点数 + 保留 2 位小数      ← mock_exam.py  G 的变式
    Q7  倒三角      空格 + 星号，格式输出       ← mock_exam.py  H 的变式

七道全是 mock_exam.py 第一、二档那 7 道题的【换皮版】：
知识点完全一样，题目长得不一样。

所以默写不出来，不是"没见过"，是"没记住"。
"""

import sys


# ============================================================
# Q1 · 倒着数
# ============================================================

def Q1():
    """
    输入格式：一行，一个整数 n。
    输出格式：一行，从 n 开始倒数到 1，每个数字后面跟一个空格。
    数据范围：1 <= n <= 100

    样例输入：
        3
    样例输出：
        3 2 1
    """
    # ↓ 把下面这行删掉，写你的代码
    n=int(input())
    data=[]
    for i in range(1,n+1):
        data.append(i)
    data.sort(reverse=True)
    print(*data)


# ============================================================
# Q2 · 从大到小
# ============================================================

def Q2():
    """
    输入格式：第一行一个整数 n，第二行 n 个整数。
    输出格式：一行，把这 n 个数按【从大到小】输出，空格分隔。

    样例输入：
        5
        3 1 4 1 5
    样例输出：
        5 4 3 1 1
    """
    n=int(input())
    data=list(map(int,input().split()))
    data.sort(reverse=True)
    print(*data)


# ============================================================
# Q3 · 换个位置
# ============================================================

def Q3():
    """
    输入格式：一行，两个整数 a 和 b。
    输出格式：一行，输出【交换之后】的 a 和 b，
              写成  a=<a的值> b=<b的值>  的形式，中间一个空格。

    样例输入：
        3 5
    样例输出：
        a=5 b=3
    """
    a,b=map(int,input().split())
    a,b=b,a
    print(f"a={a} b={b}")


# ============================================================
# Q4 · 单词去重
# ============================================================

def Q4():
    """
    输入格式：一行，若干个用空格分开的英文单词（其中可能有重复的）。
    输出格式：一行，把出现过的所有单词【去掉重复】之后，
              按字典序【从小到大】输出，空格分隔。

    样例输入：
        apple banana apple cherry
    样例输出：
        apple banana cherry
    """
    n=list(input().split())
    a=sorted(set(n))
    print(*a)

# ============================================================
# Q5 · 中间那个
# ============================================================

def Q5():
    """
    输入格式：一行，三个整数。
    输出格式：一行，输出这三个数中【大小排在中间】的那个数。

    样例输入：
        2 3 1
    样例输出：
        2
    """
    data=list(map(int,input().split()))
    data.sort()
    print(data[1])



# ============================================================
# Q6 · 平均分
# ============================================================

def Q6():
    """
    输入格式：一行，三个实数。
    输出格式：一行，输出这三个数的平均值，保留 2 位小数。

    样例输入：
        1 2 3
    样例输出：
        2.00
    """
    a,b,c=map(float,input().split())
    result=(a+b+c)/3
    print(f"{result:.2f}")


# ============================================================
# Q7 · 倒三角
# ============================================================

def Q7():
    """
    输入格式：一行，一个整数 n（1 <= n <= 9）。
    输出格式：n 行，一个【倒着的】星星金字塔：
              第一行星星最多，往下每行少 2 个星，最后一行只有 1 个星；
              并且每一行都要【左右对称】地居中。

    样例输入：
        3
    样例输出：（下面这三行，每行前面都有空格，注意数清楚）
        *****
         ***
          *
    """
    n=int(input())
    for i in range(n,0,-1):
        print(" "*(n-i)+"*"*(2*i-1))


# ============================================================
# 测试数据  ——  写完全部七道题之后再往下看
# ============================================================

CHECKS = [
    # ---- Q1 倒着数 ----
    ("Q1", "3\n",          "3 2 1"),
    ("Q1", "1\n",          "1"),
    ("Q1", "5\n",          "5 4 3 2 1"),

    # ---- Q2 从大到小 ----
    ("Q2", "5\n3 1 4 1 5\n",   "5 4 3 1 1"),
    ("Q2", "1\n7\n",           "7"),
    ("Q2", "4\n10 20 15 18\n", "20 18 15 10"),

    # ---- Q3 换个位置 ----
    ("Q3", "3 5\n",    "a=5 b=3"),
    ("Q3", "0 0\n",    "a=0 b=0"),
    ("Q3", "-1 7\n",   "a=7 b=-1"),

    # ---- Q4 单词去重 ----
    ("Q4", "apple banana apple cherry\n", "apple banana cherry"),
    ("Q4", "hello\n",                     "hello"),
    ("Q4", "Tom amy Bob Bob\n",           "Bob Tom amy"),

    # ---- Q5 中间那个 ----
    ("Q5", "2 3 1\n",   "2"),
    ("Q5", "5 5 5\n",   "5"),
    ("Q5", "-3 0 7\n",  "0"),

    # ---- Q6 平均分 ----
    ("Q6", "1 2 3\n",         "2.00"),
    ("Q6", "2.5 2.25 2.75\n", "2.50"),
    ("Q6", "0 0 0\n",         "0.00"),

    # ---- Q7 倒三角 ----
    ("Q7", "3\n", "*****\n ***\n  *"),
    ("Q7", "1\n", "*"),
    ("Q7", "4\n", "*******\n *****\n  ***\n   *"),
]

NAMES = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"]


# ============================================================
# 自检
# ============================================================

def self_check(only=None):
    import io

    print("=" * 64)
    print("默写卷自检：期望值 vs 实际输出")
    print("=" * 64)

    ok, total = 0, 0
    per_problem = {}
    for name, fake_input, expected in CHECKS:
        if only and name != only:
            continue
        total += 1
        per_problem.setdefault(name, [0, 0])
        per_problem[name][1] += 1

        func = globals().get(name)
        if func is None:
            print(f"  {name}  ✗ 函数不存在")
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
            # 只去掉末尾换行，保留行首/行内空格 —— Q7 靠空格拿分
            actual = buf.getvalue().replace("\r\n", "\n").rstrip("\n")
        except NotImplementedError:
            actual = "<还没写>"
        except Exception as e:
            actual = f"<报错: {type(e).__name__}: {e}>"
        finally:
            sys.stdin = old_stdin

        expected_norm = expected.rstrip("\n")
        passed = (actual == expected_norm)
        if passed:
            ok += 1
            per_problem[name][0] += 1
        print(f"  {name}  {'✓ 通过' if passed else '✗ 未过'}")
        if not passed:
            print(f"       输入: {fake_input!r}")
            print(f"       期望: {expected_norm!r}")
            print(f"       实际: {actual!r}")

    print("-" * 64)
    if per_problem:
        line = "  ".join(f"{k}:{v[0]}/{v[1]}" for k, v in per_problem.items())
        print("按题统计  " + line)
    print(f"通过 {ok} / {total}")

    # 单题模式不评分
    if not only:
        print("-" * 64)
        perfect = [n for n in NAMES if per_problem.get(n, [0, 0])[0] == per_problem.get(n, [0, 1])[1]]
        notyet = [n for n in NAMES if not (per_problem.get(n, [0, 0])[0] == per_problem.get(n, [0, 1])[1])]
        print(f"  一次写对: {' '.join(perfect) if perfect else '（无）'}")
        print(f"  还要练:   {' '.join(notyet) if notyet else '（无）'}")
        if not notyet:
            print()
            print("  ★ 七道全绿，而且是默写出来的 —— 第一档你真正拿下了。")
    print("=" * 64)


if __name__ == "__main__":
    only = sys.argv[1].upper() if len(sys.argv) > 1 else None
    if only and only not in NAMES:
        print(f"没有这道题：{only}（可选：{' '.join(NAMES)}）")
        sys.exit(1)
    self_check(only)
