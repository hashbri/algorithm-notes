# algorithm-notes

**算法与 Python 语法练习记录** · 佛山大学 智能科学与技术

从零开始的 Python 学习过程。**文件按主题命名，一个文件 = 一个主题**，同主题的强化练习加 `_drill` 后缀。
每个文件顶部写明知识点、思路和踩过的坑。

> 这不是题解搬运 —— 每道题的注释记录了**我当时为什么写错、后来怎么想通的**。

---

## 文件索引（按学习顺序）

> **三位编号 ＝ 进仓库时的排列顺序**。001~013 是主学习线；014 以后是工具模板和杂项，不影响阅读顺序。
> 同主题的强化练习用 `_drill` 后缀，紧跟在本体后面。

| 编号 | 文件 | 主题 | 起始 | 核心收获 |
|---|---|---|---|---|
| 001 | `001_io_input.py` | 输入输出四件套 | 10-07 | `input()` 一次一行；输出格式是第一考点 |
| 002 | `002_io_input_drill.py` | IO 加练 | 10-07 | 字符串切片、格式化输出 |
| 003 | `003_sorting.py` | 列表与排序 | 10-07 | `sort()` 原地修改 vs `sorted()` 返回新对象 |
| 004 | `004_sorting_drill.py` | 排序加练 | 10-07 | 多关键字排序、`key=` 参数 |
| 005 | `005_simulation.py` | 基础模拟 | 10-08 | 模拟题的步骤拆解 |
| 006 | `006_binary_search.py` | 二分查找 + 贪心入门 | 10-09 | **两套模板**：命中查找 / 下界查找 |
| 007 | `007_binary_search_drill.py` | 二分 / 贪心加练 | 10-10 | 上界查找（复用下界骨架）、贪心入门 |
| 008 | `008_mock_exam.py` | 全真模拟卷 | 10-11 | 三档分层策略：必拿 / 可争 / 放弃 |
| 009 | `009_recall_test.py` | 闭卷默写卷 | 10-11 | 7 道换皮题，检验是否真掌握 |
| 010 | `010_contest_replay.py` | 校内赛原题重做 | 10-14 | 校内赛能做的三道题（12/12） |
| 011 | `011_bitwise.py` | 位运算 + 碎片小题 | 10-17 | 拆位、进制转换、二分下界复用 |
| 012 | `012_prefix_sum.py` | 前缀和 | 10-18 | `pre[0]=0`，区间和 = `pre[r] - pre[l-1]` |
| 013 | `013_fill_blank.py` | 结果填空题本 | 10-22 | 蓝桥填空题专用本，**代码 + 手算双验** |
| 014 | `014_contest_io_template.py` | 竞赛 IO 模板 | 10-06 | 快速读取、多组数据（工具，随时可查） |

另外两个**不编号**的文件（不是「课」，不参与顺序）：

| 文件 | 说明 |
|---|---|
| `知识点.py` | 笔记碎片，异常处理伪代码，**故意不是合法 Python**，跑不了 |
| — | 返回值专题已移到 `python-learning` 仓库，那里才是它的归档处 |

> `013_fill_blank.py` 是**一本会一直长的册子**：以后每道填空题往里面加一块，不新建文件。

---

## ★ 核心知识点

### 二分查找的两套模板

```python
# 模板 A：查找目标值是否存在（左闭右闭）
left, right = 0, n - 1
while left <= right:
    mid = (left + right) // 2
    if data[mid] == x:
        return mid
    elif data[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

# 模板 B：查找第一个 >= x 的位置（下界，左闭右开）
left, right = 0, n
while left < right:
    mid = (left + right) // 2
    if data[mid] < x:
        left = mid + 1
    else:
        right = mid          # 注意：不带 -1
```

**口诀：左大胆跳（mid+1），右保守留（mid）。**
**两套模板的三件套必须配套用，混着写必错。**

### 返回值：最容易犯的错

| 原地修改型（返回 `None`，**不用接**） | 返回结果型（**必须接住**） |
|---|---|
| `list.sort()` | `sorted()` |
| `list.reverse()` | `reversed()` |
| `list.append()` | `list.index()` |
| `set.add()` | `list.count()` |

**口诀：带 -ed 的返回新对象，不带的正地改。**

> 这是我犯错最多的一类 —— 丢过 `index()` 的返回值，也丢过 `sorted(set(n))` 的结果。

### 前缀和

```python
pre = [0] * (n + 1)          # pre[0] = 0 是哨兵，不是浪费
for i in range(1, n + 1):
    pre[i] = pre[i - 1] + data[i - 1]
# 区间 [l, r] 的和（1-based）
s = pre[r] - pre[l - 1]
```

---

## 竞赛相关

- **蓝桥杯**：软件赛 · Python 程序设计 · 大学 B 组（2027 年 4 月省赛）
- **赛制关键**：OI 赛制 —— **提交后无实时反馈**，按测试点给分（暴力解也拿部分分）
- → 所以两条硬规矩：① 写不出来就交暴力解；② **自己造用例自检**

`008_mock_exam.py` / `009_recall_test.py` / `010_contest_replay.py` / `012_prefix_sum.py` / `011_bitwise.py` / `013_fill_blank.py`
都内置了自检器。

---

## 运行

```bash
python 008_mock_exam.py         # 跑模拟卷全部用例
python 008_mock_exam.py E       # 只跑 E 题
python 010_contest_replay.py P1 # 只跑第 1 题
python 013_fill_blank.py        # 跑填空题本所有块
```
