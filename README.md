# algorithm-notes

**算法与 Python 语法练习记录** · 佛山大学 智能科学与技术

从零开始的 Python 学习过程。每个文件对应一天的主题，**文件顶部写明知识点、思路和踩过的坑**。

> 这不是题解搬运 —— 每道题的注释记录了**我当时为什么写错、后来怎么想通的**。

---

## 学习路线

| 文件 | 主题 | 核心收获 |
|---|---|---|
| `day1_io.py` | 输入输出 | `input()` 一次一行；输出格式是第一考点 |
| `day1_extra.py` | IO 综合练习 | 字符串切片、格式化输出 |
| `day2_sort.py` | 列表与排序 | `sort()` 原地修改 vs `sorted()` 返回新对象 |
| `day2_extra.py` | 排序综合 | 多关键字排序、`key=` 参数 |
| `day3_sim.py` | 循环与模拟 | 模拟题的步骤拆解 |
| `day4_search.py` | 二分查找 | **两套模板**：命中查找 / 下界查找 |
| `day4_extra.py` | 二分强化 | 上界查找（复用下界骨架）、贪心入门 |
| `day5_mock.py` | 模拟卷 | 三档分层策略：必拿 / 可争 / 放弃 |
| `day6_memorize.py` | 闭卷默写 | 7 道换皮题，检验是否真掌握 |
| `day7_contest.py` | 竞赛原题重做 | 校内赛可做的三道题 |
| `contest_io_template.py` | 竞赛 IO 模板 | 快速读取、多组数据 |
| `practice_return.py` | 返回值专题 | 混淆"原地修改型"与"返回结果型"的代价 |
| `practice_return_quiz.py` | 返回值自测 | — |
| `知识点.py` | 笔记碎片 | — |

---

## ★ 核心知识点

### 二分查找的两套模板

```python
# 模板 A：查找目标值是否存在
left, right = 0, n - 1
while left <= right:
    mid = (left + right) // 2
    if data[mid] == x:
        return mid
    elif data[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

# 模板 B：查找第一个 >= x 的位置（下界）
left, right = 0, n
while left < right:
    mid = (left + right) // 2
    if data[mid] < x:
        left = mid + 1
    else:
        right = mid          # 注意：不带 -1
```

**口诀：左大胆跳（mid+1），右保守留（mid）。**

### 返回值：最容易犯的错

| 原地修改型（返回 `None`，**不用接**） | 返回结果型（**必须接住**） |
|---|---|
| `list.sort()` | `sorted()` |
| `list.reverse()` | `reversed()` |
| `list.append()` | `list.index()` |
| `set.add()` | `list.count()` |

**口诀：带 -ed 的返回新对象，不带的正地改。**

> 这是我犯错最多的一类 —— 丢过 `index()` 的返回值，也丢过 `sorted(set(n))` 的结果。

---

## 竞赛相关

- **蓝桥杯**：软件赛 · Python 程序设计 · 大学 B 组（2027 年 4 月省赛）
- **赛制关键**：OI 赛制 —— **提交后无实时反馈**，按测试点给分（暴力解也拿部分分）
- → 所以两条硬规矩：① 写不出来就交暴力解；② **自己造用例自检**

`day5_mock.py` / `day6_memorize.py` / `day7_contest.py` 都内置了自检器，
用法：`python day5_mock.py` 跑全卷，或 `python day5_mock.py E` 只跑某一题。

---

## 运行

```bash
python day5_mock.py        # 跑模拟卷自检
python day7_contest.py P1  # 只跑第 1 题
```
