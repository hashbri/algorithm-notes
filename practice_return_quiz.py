# ============================================================
#  自测题：验证你对 return True / False 的理解
#  先做 practice_return.py，再跑这个文件看答案
# ============================================================

# ---------- 题 1：预测输出 ----------
print("=== 题 1 ===")


def f1():
    for i in range(5):
        if i == 3:
            return True
        print("循环中 i =", i)
    print("循环结束了")
    return False


print("返回值是：", f1())
# 想清楚：
#   ① "循环结束了" 这行会打印吗？为什么？
#   ② i = 3 之后还打印 i = 4 吗？
#   ③ 最终返回值是 True 还是 False？


# ---------- 题 2：return 也是提前退出 ----------
print("\n=== 题 2 ===")


def f2(n):
    for i in range(n):
        if i > 2:
            return "提前走了"
    return "正常走完"


print(f2(10))
print(f2(2))


# ---------- 题 3：最容易踩的坑 —— 忘写 return 得到 None ----------
print("\n=== 题 3 ===")


def f3_bad(x):
    if x > 0:
        return True
    # 忘了写 return False！


def f3_good(x):
    if x > 0:
        return True
    return False


print("bad(5)  =", f3_bad(5))
print("bad(-5) =", f3_bad(-5), "  ← 是 None，不是 False！")
print("bad(-5) 在 if 里当条件：", "真" if f3_bad(-5) else "假", " ← None 是假值，碰巧没出错")
print("good(5)  =", f3_good(5))
print("good(-5) =", f3_good(-5))


# ---------- 题 4：return 可以一次穿透多层循环 ----------
print("\n=== 题 4 ===")


def f4():
    for i in range(3):
        for j in range(3):
            if i * j == 4:
                return i, j          # 直接退出两层循环
    return None


print("找到的是：", f4())


def f4_break():
    result = None
    for i in range(3):
        for j in range(3):
            if i * j == 4:
                result = (i, j)
                break                # 只跳出内层
        if result:
            break                    # 还得再跳一次才出得来
    return result


print("用 break 要写两遍：", f4_break())


# ---------- 题 5：return 后代码不执行 ----------
print("\n=== 题 5 ===")


def f5():
    print("第一行")
    return "结束了"
    print("这行永远不执行")


print(f5())


# ---------- 题 6：改错题 —— 找出下面函数的 bug ----------
print("\n=== 题 6 ===")


def check_password(pw):
    """密码是 '1234' 时返回 True"""
    if pw == "1234":
        return True
    else:
        return "错"        # 这里应该返回什么？调用方拿它当条件用会怎样？


print("check_password('1234') →", check_password("1234"))
print("check_password('0000') →", check_password("0000"))
print("  问题：'错' 是真值！if check_password('0000') 判成 True，逻辑反了")
