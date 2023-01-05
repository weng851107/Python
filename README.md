```Text
Author: Antony_Weng <weng851107@gmail.com>

This file is only used for the record of the learning process, only used by myself and the file has never been leaked out.
If there is related infringement or violation of related regulations, please contact me and the related files will be deleted immediately. Thank you!
```

# 目錄

- [Note](#0)
  - [學習資源](#0.1)
  - [技術網站](#0.2)
- [實際操作](#2)
  - [Telnet](#2.1)
  - [matplotlib極座標應用](#2.2)
  - [tkinter UI](#2.3)
  - [Uart](#2.4)
  - [Excel](#2.5)
  - [OpenCV](#2.6)
- [相關知識](#3)
  - [如何在linux下執行python程式](#3.1)
  - [Ubuntu修改默認Python版本](#3.2)
  - [套件管理工具 pip 指令用法](#3.3)
    - [requirements.txt](#3.3.1)
- [Python Tutorial](#4)
  - [Syntax](#4.1)
  - [Variables](#4.2)
  - [Data Types](#4.3)
  - [Numbers](#4.4)
  - [Casting](#4.5)
  - [Strings](#4.6)
- [交叉編譯ARM架構Python](#5)



<h1 id="0">Note</h1>

<h2 id="0.1">學習資源</h2>

[Python Tutorial - W3Schools](https://www.w3schools.com/python/default.asp)

[Python Tutorial - GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/?ref=ghm)

[菜鳥教程 - Python3](https://www.runoob.com/python3/python3-tutorial.html)

[STEAM教學網 - Python 教學](https://steam.oxxostudio.tw/category/python/index.html)

[OpenCV-Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

[STEAM教學網 - OpenCV 教學](https://steam.oxxostudio.tw/category/python/ai/opencv-index.html)

[OpenCV 函式庫](https://steam.oxxostudio.tw/category/python/ai/opencv.html)

<h2 id="0.2">技術網站</h2>

[如何在python中执行另一个py文件](https://cloud.tencent.com/developer/article/1738484)

[Linux和Windows下用python找到并杀死进程](https://beltxman.com/3406.html)

[Python string 轉 bytes 的 3 種方法](https://shengyu7697.github.io/python-string-to-bytes/)

[基於python goto的正確用法說明](https://walkonnet.com/archives/22204)

[變量類型 & 進位制](https://ithelp.ithome.com.tw/articles/10284114)

[Python 字串格式化教學與範例](https://officeguide.cc/python-string-formatters-tutorial/)

[Python的 Convert Hex to Float value](https://andy851220.medium.com/python%E7%9A%84hex-to-float-value-ce228d90bc6b)

[Python如何控制小數點後面的小數位數](https://www.796t.com/content/1549397542.html)

class設計

- [[Python物件導向]淺談Python類別(Class)](https://www.learncodewithmike.com/2020/01/python-class.html)
- [Python多執行緒程式設計(Class形式)](https://tw511.com/3/39/1391.html)

Parser for command line options

- [optparse — Parser for command line options](https://docs.python.org/3/library/optparse.html)
- [Python之optparse模塊OptionParser的使用方法](https://www.twblogs.net/a/5ef5b6a4efdbac7f8b1072d7)
- [Python處理命令列引數模組optpars用法例項分析](https://www.itread01.com/article/1527736700.html)


<h1 id="2">實際操作</h1>

<h2 id="2.1">Telnet</h2>

- [telnet_test.py](./code/telnet_test.py)

<h2 id="2.2">matplotlib極座標應用</h2>

[Official Website: Matplotlib](https://matplotlib.org/)

Use python telnetlib to get the data, and display in the figure with the same thread

- [DQARadarDisplayData_v1.py](./code/DQARadarDisplayData_v1.py)

collect_data_telnet(): Use python telnetlib to get the data. --> sub-thread
thread_plot_polar(): display in the figure. --> main-thread

- [DQARadarDisplayData_v2.py](./code/DQARadarDisplayData_v2.py)

Show the data with animation

- [DynPlotRadar.py](./code/DynPlotRadar.py)

<h2 id="2.3">tkinter UI</h2>

python內建的tkinter，不是使用其他第三方的套件，所以在其他平台相依性上會比較好，但比較不方便的是它沒有支援拖曳編輯的介面

- [[Python]-GUI(圖形使用者介面)](https://vocus.cc/article/627bc705fd8978000146162a)
- [How to Pass Arguments to Tkinter Button Command?](https://www.geeksforgeeks.org/how-to-pass-arguments-to-tkinter-button-command/)
- [Python tkinter GUI 基本用法](https://vocus.cc/article/6277e7a1fd897800012b1e8a)
- [IT邦幫忙 - 30 Day 用python寫UI](https://ithelp.ithome.com.tw/articles/10262967)
- [解决Python Tkinter中Toplevel插入图片无法显示问题](https://blog.csdn.net/qq_23944945/article/details/102815742)

簡單 tkinter UI 功能介紹：[tkinter_UI.py](./code/tkinter_UI.py)

實際範例：[RadarUI.py](./code/RadarUI.py)

<h2 id="2.4">Uart</h2>

[pySerial官方文檔](https://pyserial.readthedocs.io/en/latest/pyserial.html)

[用Python 玩轉串口（基於pySerial）](https://blog.csdn.net/bryanwang_3099/article/details/120493736)

- [stm32_uart.py](./code/Uart/stm32_uart.py)：Tx完接收之後的RX
- [stm32_uart_rx.py](./code/Uart/stm32_uart_rx.py)：一個程序在Rx, [stm32_uart_tx.py](./code/Uart/stm32_uart_tx.py)：另一個程序在Tx，透過mutex且判斷某file數值作為是否在Tx，Tx時disable Rx

<h2 id="2.5">Excel</h2>

[5個實用的Pandas讀取Excel檔案資料技巧](https://www.learncodewithmike.com/2020/12/read-excel-file-using-pandas.html)

### 利用Python的Pandas套件

**安裝套件**

Python的Pandas套件

```bash
pip install pandas
```

操作Excel的相依性套件openpyxl

```bash
pip install openpyxl
```

### 讀取Excel檔案的資料

利用read_excel()方法(Method)

```python
import pandas as pd
 
df = pd.read_excel("歷年國內主要觀光遊憩據點遊客人數月別統計.xlsx")
print(df)
```

讀取特定的工作表(sheet)

```python
import pandas as pd
 
df = pd.read_excel("歷年國內主要觀光遊憩據點遊客人數月別統計.xlsx", sheet_name="2019")
# df = pd.read_excel("歷年國內主要觀光遊憩據點遊客人數月別統計.xlsx", sheet_name=["2018", "2019"])
print(df)
```

讀取某些欄位(column)的資料內容

- 可以使用usecols關鍵字參數來指定所要選取的「欄位標題」、「索引值」或「欄位名稱」

    ```python
    import pandas as pd
    
    # 指定欄位標題
    df = pd.read_excel("歷年國內主要觀光遊憩據點遊客人數月別統計.xlsx",
                        sheet_name="2019",
                        usecols=["年別", "細分", "合計"])
    
    # 指定欄位索引值
    # df = pd.read_excel("歷年國內主要觀光遊憩據點遊客人數月別統計.xlsx",
    #                      sheet_name="2019",
    #                      usecols=[0, 3, 17])
    
    # 指定欄位名稱
    # df = pd.read_excel("歷年國內主要觀光遊憩據點遊客人數月別統計.xlsx",
    #                      sheet_name="2019",
    #                      usecols="A, D, R")

    # 選取範圍欄位名稱
    # df = pd.read_excel("歷年國內主要觀光遊憩據點遊客人數月別統計.xlsx",
    #                     sheet_name="2019",
    #                     usecols="A, D, F:R")
    print(df)
    ```

利用nrows關鍵字參數，來指定所要讀取的列(row)數量

```python
import pandas as pd
 
# 讀取前20列資料
df = pd.read_excel("歷年國內主要觀光遊憩據點遊客人數月別統計.xlsx",
                     sheet_name="2019",
                     nrows=21)
print(df)
```

- 選取Excel檔中，特定列(row)的資料時，使用Pandas DataFrame的「[]」符號來範圍選取所需的列(row)資料

    ```python
    import pandas as pd
    
    # 讀取2012年的列資料
    df = pd.read_excel("歷年國內主要觀光遊憩據點遊客人數月別統計.xlsx")
    new_df = df[0:287]  # 索引值0~286的列資料
    print(new_df)
    ```

讀取Excel某儲存格資料：使用at或iat屬性(Property)來進行儲存格的定位

```python
import pandas as pd
 
df = pd.read_excel("歷年國內主要觀光遊憩據點遊客人數月別統計.xlsx")
d2 = df.at[0, "細分"]  # 讀取D2儲存格的值(以列索引值及欄位標題來定位)
# d2 = df.iat[0, 3]  # 讀取D2儲存格的值(以列索引值及欄索引值來定位)
print(d2)  #陽明山遊客中心
```

---

取出Excel中所要的值，重新組合成C struct的形式，避免一個一個複製

- [get_data_from_excel.py](./code/excel/get_data_from_excel.py)

<h2 id="2.6">OpenCV</h2>

全白或全黑的底

```Python
#shape = (32, 32, 3)        # 3-channel 8bit
shape = (32, 32)            # 1-channel 8bit
pt_img = np.zeros(shape, np.uint8)
pt_img.fill(255)            # Set White or Black
```

cv.applyColorMap(src, colormap)

- `cv.applyColorMap(pt_img, cv.COLORMAP_RAINBOW) `
- [偽彩色圖像處理](https://blog.csdn.net/youcans/article/details/125298385)

<h1 id="3">相關知識</h1>

<h2 id="3.1">如何在linux下執行python程式</h2>

1. 直接使用 `python ***x.py` 執行。其中python可以寫成python的絕對路徑。使用 `which python` 進行查詢。

2. 在檔案的頭部（第一行）寫上 `#!/usr/bin/python2.7`，這個地方使用python的絕對路徑，就是上面用 `which python` 查詢來的結果。

然後在外面就可以使用./***.py執行了。

<h2 id="3.2">Ubuntu修改默認Python版本</h2>

查看系統有的Python版本

```bash
ls /usr/bin/python*
```

查看系統默認的Python版本

```bash
python --version
```

用戶級修改

- 開啟用戶`~/.bashrc`

    ```bash
    vim ~/.bashrc
    ```

- 新增別名來修改默認Python版本

    ```bash
    alias python='/usr/bin/python3.7'
    ```

- 重新登錄或加載.bashrc文件

    ```bash
    source ~/.bashrc
    ```

在具體的某個Python文件中修改

- 在第一行處修改如下：將 `#!/usr/bin/python` 修改為 `#!/usr/bin/python2 `表示採用Python2來對該文件進行編譯，改為python3亦然

軟連結

```bash
ls /usr/bin/python*

rm /usr/bin/python

ln -s /usr/bin/python3.7 /usr/bin/python
```

採用指令update-alternatives切換

- https://blog.csdn.net/Hiking_Yu/article/details/104373221

<h2 id="3.3">套件管理工具 pip 指令用法</h2>

pip 是 Python 標準庫管理器，也就是一個工具讓你安裝不同的套件來使用

`pip --version` 得到你電腦的 pip版本 也會知道你對應的 python版本 是多少

```bash
> pip --version
pip 22.3.1 from c:\users\10008577\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)
> pip -V
pip 22.3.1 from c:\users\10008577\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)
```

`pip list` 就能取得到你安裝的套件(包含自帶)有哪些以及對應的版本號

```bash
> pip list
Package           Version
----------------- --------
cycler            0.11.0
et-xmlfile        1.1.0
fonttools         4.38.0
kiwisolver        1.4.4
matplotlib        3.5.3
numpy             1.21.6
opencv-python     4.6.0.66
............
```

`pip install XXX` 安裝對應的套件

`pip install XXX==XX` 指定安裝版本 XXX代表套件名稱 XX代表版本號

`pip uninstall XXX` 卸載對應的套件

`pip freeze` 列出安裝(不包含自帶，即不可卸載者)的套件

```bash
> pip freeze
cycler==0.11.0
et-xmlfile==1.1.0
fonttools==4.38.0
kiwisolver==1.4.4
matplotlib==3.5.3
numpy==1.21.6
opencv-python==4.6.0.66
openpyxl==3.0.10
packaging==21.3
pandas==1.3.5
Pillow==9.3.0
pyparsing==3.0.9
pyserial==3.5
python-dateutil==2.8.2
python-math==0.0.1
pytz==2022.6
six==1.16.0
typing_extensions==4.4.0
```

`python -m pip install --upgrade pip` 升級 pip 套件

`pip show XXX` 顯示指定套件資訊

```bash
> pip show pyserial
Name: pyserial
Version: 3.5
Summary: Python Serial Port Extension
Home-page: https://github.com/pyserial/pyserial
Author: Chris Liechti
Author-email: cliechti@gmx.net
License: BSD
Location: c:\users\10008577\appdata\local\programs\python\python37\lib\site-packages
Requires:
Required-by:
```

<h3 id="3.3.1">requirements.txt</h3>

在 Python Package中，通常會加入一個名為 requirements.txt 的檔案，裡面放的是執行這包 Package 所需要用到的library套件。

在Github隨便找幾篇別人寫的程式來當範例：[[1]](https://github.com/allenai/deep_qa/blob/master/requirements.txt) [[2]](https://github.com/python/docsbuild-scripts/blob/main/requirements.txt) [[3]](https://github.com/binder-examples/requirements/blob/main/requirements.txt)

requirements.txt 就是一串文字、字串，來讓 pip 這項工具安裝

- \# 是註解
- 剩下的資訊就只有 套件名稱、以及套件版本


`pip freeze > requirements.txt` 把本地所安裝的套件名稱以及版本號寫入到 requirements.txt

```bash
> pip freeze > requirements.txt
> cat .\requirements.txt
cycler==0.11.0
et-xmlfile==1.1.0
fonttools==4.38.0
kiwisolver==1.4.4
matplotlib==3.5.3
numpy==1.21.6
opencv-python==4.6.0.66
openpyxl==3.0.10
packaging==21.3
pandas==1.3.5
Pillow==9.3.0
pyparsing==3.0.9
pyserial==3.5
python-dateutil==2.8.2
python-math==0.0.1
pytz==2022.6
six==1.16.0
typing_extensions==4.4.0
```

`pip install -r requirements.txt` 安裝txt內的套件與版本

`pip uninstall -r requirements.txt -y` 卸載requirements.txt內的所有套件

<h1 id="4">Python Tutorial</h1>

<h2 id="4.1">Syntax</h2>

### Indentation

Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to **indicate a block of code**.

### Variables

Python has no command for declaring a variable.

```python
x = 5
y = "Hello, World!"
```

### Comments

Usage：

- Comments can be used to explain Python code.
- Comments can be used to make the code more readable
- Comments can be used to prevent execution when testing code.

Single Line Comment：

```Python
# This is comment
```

Multi Line Comments：

```Python
'''
This is comment
'''

"""
This is comment
"""
```

<h2 id="4.2">Variables</h2>

Variables are containers for storing data values.

### Creating Variables

Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

```Python
x = 5
y = "John"
print(x)
print(y)
```

Variables do not need to be declared with any particular type, and can even change type after they have been set.

```Python
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
```

### Casting 型別轉換

```Python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

### Get the Type

```Python
x = 5
y = "John"
print(type(x))
print(type(y))

'''
<class 'int'>
<class 'str'>
'''
```

### Single or Double Quotes

String variables can be declared either by using single or double quotes

```Python
x = "John"
# is the same as
x = 'John'
```

### Case-sensitive 大小寫敏感性

```Python
a = 4
A = "Sally"
#A will not overwrite a
```

### Assign Multiple Values

Many Values to Multiple Variables

```Python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

'''
Orange
Banana
Cherry
'''
```

One Value to Multiple Variables

```Python
x = y = z = "Orange"
print(x)
print(y)
print(z)

'''
Orange
Orange
Orange
'''
```

### Unpack a Collection

If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables.

將打包好的資料取出來

```Python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

'''
apple
banana
cherry
'''
```

### Output Variables - print()

```Python
x = "Python is awesome"
print(x)
'''
Python is awesome
'''

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
'''
Python is awesome
'''

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
'''
Python is awesome
'''
```

%s 是以字串輸出，%f 是以浮點數輸出、%d 是以十進位整數輸出

舊式字串格式化（%）

```Python
text = 'world'
print('hello %s' % text)
'''
hello world
'''

print('%x' % 23)
'''
17
'''

print('hello %s %s' % ('world', 'go'))
'''
hello world go
'''
```

新式字串格式化（format()）

- 一般基本用法

    ```Python
    text = 'world'
    print('hello {}'.format(text))
    '''
    hello world
    '''
    ```

- 使用名稱來指定變數變換順序

    ```Python
    name = 'Jack'
    text = 'world'

    print('hello {name}, hello {text}'.format(name=name, text=text))
    '''
    hello Jack, hello world
    '''
    ```

- 如果希望把內容轉成十六進位的話可以使用 format spec 在 `{}` 新增 `:x`

    ```Python
    print('{:x}'.format(23))
    '''
    17
    '''
    ```

字串插值（Formatted String Literal）

- 把 Python 運算式嵌入在字串常數中

    ```Python
    x = 10
    y = 27
    print(f'x + y = {x + y}')
    '''
    37
    '''
    ```

    ```Python
    def hello(text, name):
        return f'hello {text}, hello {name}'

    # 實際上 Python 會把它變成字串常數和變數（過程中有優化）

    def hello(text, name):
        return 'hello ' + text + ', hello' + name
    ```

預設會自動在最後加上換行 `\n` 的字串，若要修改 end格式，即在print中修改

```Python
print("Hello World!", end = '')
print("Hello World!")
'''
Hello World!Hello World!
'''
```

### Global Variables

Variables that are created outside of a function are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.

```Python
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

'''
Python is fantastic
Python is awesome
'''
```

To create a global variable inside a function, you can use the global keyword.

Also, use the global keyword if you want to change a global variable inside a function.

```Python
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

'''
Python is fantastic
'''
```

<h2 id="4.3">Data Types</h2>

Python has the following data types built-in by default, in these categories:

- Text Type:	`str`
- Numeric Types:	`int`, `float`, `complex`
- Sequence Types:	`list`, `tuple`, `range`
- Mapping Type:	`dict`
- Set Types:	`set`, `frozenset`
- Boolean Type:	`bool`
- Binary Types:	`byte`s, `bytearray`, `memoryview`
- None Type:	`NoneType`

Getting the Data Type： `type(variable)`

![tutorial_img00](./Tutorial/image/tutorial_img00.PNG)

Setting the Specific Data Type：

![tutorial_img01](./Tutorial/image/tutorial_img01.PNG)

<h2 id="4.4">Numbers</h2>

### Type Conversion

```Python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

'''
1.0
2
(1+0j)
<class 'float'>
<class 'int'>
<class 'complex'>
'''
```

### Random Number

A built-in module called random that can be used to make random numbers

```Python
import random

print(random.randrange(1, 10))
```

<h2 id="4.5">Casting</h2>

```Python
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
```

<h2 id="4.6">Strings</h2>

- `'hello'` is the same as `"hello"`

Multiline Strings：

```Python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

'''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
```

### Strings are Arrays

strings in Python are arrays of bytes representing unicode characters

```Python
a = "Hello, World!"
print(a[1])

'''
e
'''
```

### Looping Through a String

```Python
for x in "banana":
    print(x)

'''
b
a
n
a
n
a
'''
```

### String Length - `len()`

```Python
a = "Hello, World!"
print(len(a))

'''
13
'''
```

### Check String - `in` or `not in`

```Python
txt = "The best things in life are free!"
print("free" in txt)
'''
True
'''

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
'''
Yes, 'free' is present.
'''

txt = "The best things in life are free!"
print("expensive" not in txt)
'''
True
'''

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
'''
No, 'expensive' is NOT present.
'''
```

### Slicing Strings

You can return a range of characters by using the slice syntax

```Python
b = "Hello, World!"
print(b[2:5])
'''
llo
'''

# Slice From the Start
b = "Hello, World!"
print(b[:5])
'''
Hello
'''

# Slice To the End
b = "Hello, World!"
print(b[2:])
'''
llo, World!
'''

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])
'''
orl
'''
```

### Upper or Lower Case - `upper()` & `lower()`

```Python
a = "Hello, World!"
print(a.upper())
'''
HELLO, WORLD!
'''

a = "Hello, World!"
print(a.lower())
'''
hello, world!
'''
```

### Remove Whitespace - `strip()`

Whitespace is the space before and/or after the actual text

```Python
a = " Hello, World! "
print(a.strip())
'''
Hello, World!
'''
```

### Replace String - `replace()`

```Python
a = "Hello, World!"
print(a.replace("H", "J"))
'''
Jello, World!
'''
```

### Split String - `split()`

The `split()` method returns a **list** where the text between the specified separator becomes the list items.

```Python
a = "Hello, World!"
print(a.split(","))
'''
['Hello', ' World!']
'''
```

### String Concatenation - `+`

```Python
a = "Hello"
b = "World"
c = a + " " + b
print(c)
'''
Hello World
'''
```

### Format Strings

We cannot combine strings and numbers, ut we can combine strings and numbers by using the `format()` method

```Python
age = 36
print("My name is John, and I am {}".format(age))
'''
My name is John, and I am 36
'''

quantity = 3
itemno = 567
price = 49.95
print("I want {} pieces of item {} for {} dollars.".format(quantity, itemno, price))
'''
I want 3 pieces of item 567 for 49.95 dollars.
'''
```

Use index numbers {0} to be sure the arguments are placed in the correct placeholders

```Python
quantity = 3
itemno = 567
price = 49.95
print("I want to pay {2} dollars for {0} pieces of item {1}.".format(quantity, itemno, price))
'''
I want to pay 49.95 dollars for 3 pieces of item 567.
'''
```

### Escape Characters - `\`

![tutorial_img02](./Tutorial/image/tutorial_img02.PNG)

### String Methods API

https://www.w3schools.com/python/python_strings_methods.asp




<h1 id="5">交叉編譯ARM架構Python</h1>






