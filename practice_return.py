# ============================================================
#  练习项目：智能储物柜系统
#  目标：把 return True / return False 用透
#
#  核心规则（先记住这一条）：
#    return 是「干完这活儿，带着结果走人」——它当场结束整个函数，
#    不管嵌了多少层循环。返回值给调用者用。
#
#  break  是「我不转这一层了」，人还在函数里，只跳一层循环。
# ============================================================

import random
import time

# ---------------- 全局状态（本练习刻意用全局，先专注 return） ----------------
locker_count = 6          # 储物柜总数
lockers = {}              # {柜号: 密码}，空的表示可用
MAX_TRIES = 3             # 取物密码最多试 3 次


# ============================================================
#  第 1 关：最基础的 return True / False
#  一个函数只判断一件事，用返回值汇报结论
# ============================================================

def is_valid_locker(no):
    if no>=1 and no<=locker_count:
        return True
    return False


    """
    判断柜号是否合法（1 ~ locker_count 之间的整数）。
    合法 → return True；不合法 → return False。
    """
    # TODO 1：写你的判断。提示：两个条件用 and 连接
    # if no >= 1 and no <= locker_count:
    #     return True
    # return False
    pass


def is_empty(no):
    """判断这个柜子是否空着（没被存过东西）。空 → True，已占用 → False。"""
    # TODO 2：用 in 或 not in 判断 no 是否在 lockers 的键里
    if no not in lockers :
        return True
    return False


# ============================================================
#  第 2 关：把 return 当"提前退出"用 —— 这是它最大的价值
#  return 能一次性穿透所有循环，比 break 干净得多
# ============================================================

def find_first_empty():
    """
    从头找一个空柜子，返回它的柜号。
    全都占满了 → return None（None 是"没有结果"的约定）。
    """
    # TODO 3：用 for 遍历 1 到 locker_count
    #   发现空的就立刻 return no，别用 break、别设标志位
    # 循环跑完说明一个都没找到 → return None
    for no in range(1,locker_count+1):
        if no not in lockers:
            return no
    return None


def find_password(no):
    """
    取物：让用户输密码，最多试 MAX_TRIES 次。
    密码正确 → return True；试满次数还不对 → return False。

    这是本练习最关键的一题 —— 注意 return 直接结束函数，
    不需要 win 标志位，也不需要 break。
    """
    for i in range(MAX_TRIES):
        passward=input("请输入密码：")
        if passward==lockers[no]:
            print ("yes")
            return True
        print("no","还剩",MAX_TRIES-1-i,"次")
    return False


    # TODO 4：
    #   for i in range(MAX_TRIES):
    #       让用户输入密码 pw
    #       if pw == lockers[no]:
    #           打印提示，return True      ← 当场结束，循环都不管了
    #       打印"密码错误，还剩 X 次"
    #   循环跑完（说明次次都错）→ return False
    pass


# ============================================================
#  第 3 关：一个函数里多个"成功出口"，都要能正确返回
# ============================================================

def can_store(no):

    #检查某柜子现在是否可以存东西。必须同时满足：
      #① 柜号合法
      #② 柜子是空的
   ##考点：这里要「调用」上面写好的函数，靠它们的返回值来判断。
    if not is_valid_locker(no):
        return False
    if not is_empty(no):
        return False
    return True


# ============================================================
#  第 4 关：返回值不是布尔，但同样靠 return 送出去
# ============================================================

def count_used():
    """返回已被占用的柜子数量（用 len）。"""
    # TODO 6：一行搞定
    pass


def make_random_password():
    """生成一个 4 位数字密码，作为字符串返回。"""
    # TODO 7：用 random.randint(1000, 9999) 再用 str() 转字符串 return 出去
    pass


# ============================================================
#  主流程（这部分不用改，写完上面 7 个函数它就能跑）
# ============================================================

def show_lockers():
    print("\n--- 储物柜状态 ---")
    for no in range(1, locker_count + 1):
        state = "空" if is_empty(no) else "已占用"
        print(f"  {no} 号柜：{state}")
    print(f"  已用 {count_used()} / {locker_count}")
    print("------------------")


def do_store():
    no = int(input("要使用哪个柜子？请输入柜号："))
    if not can_store(no):
        print("这个柜子不能用（柜号不存在，或者已经占用）")
        return                      # 这里的 return 不带值，就是"到此为止"
    pw = make_random_password()
    lockers[no] = pw
    print(f"存好了！请记住密码：{pw}")
    print("（别忘了）")


def do_take():
    no = int(input("要取哪个柜子？请输入柜号："))
    if not is_valid_locker(no) or is_empty(no):
        print("这个柜子不存在或者本来就是空的")
        return
    if find_password(no):
        print("取物成功，欢迎下次使用")
        del lockers[no]
    else:
        print("密码错误次数过多，柜子已锁定")


def main():
    print("智能储物柜系统")
    time.sleep(1)

    while True:
        show_lockers()
        print("1-存东西  2-取东西  3-退出")
        choice = input("请选择：")

        if choice == "1":
            do_store()
        elif choice == "2":
            do_take()
        elif choice == "3":
            print("再见")
            return                  # 最外层也是靠 return 退出
        else:
            print("输入无效，请重新选择")

        # 如果没有可用柜子，提示一下
        if find_first_empty() is None:
            print("注意：所有柜子都占满了")


if __name__ == "__main__":
    main()
