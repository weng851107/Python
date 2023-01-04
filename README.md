```Text
Author: Antony_Weng <weng851107@gmail.com>

This file is only used for the record of the learning process, only used by myself and the file has never been leaked out.
If there is related infringement or violation of related regulations, please contact me and the related files will be deleted immediately. Thank you!
```

# 目錄

- [Note](#0)
  - [學習資源](#0.1)
  - [技術網站](#0.2)
  - [如何在linux下執行python程式](#0.3)
  - [Ubuntu修改默認Python版本](#0.4)
- [實際操作](#2)
  - [Telnet](#2.1)
  - [matplotlib極座標應用](#2.2)
  - [tkinter UI](#2.3)
  - [Uart](#2.4)
  - [Excel](#2.5)
  - [OpenCV](#2.6)


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

<h2 id="0.3">如何在linux下執行python程式</h2>

1. 直接使用 `python ***x.py` 執行。其中python可以寫成python的絕對路徑。使用 `which python` 進行查詢。

2. 在檔案的頭部（第一行）寫上 `#!/usr/bin/python2.7`，這個地方使用python的絕對路徑，就是上面用 `which python` 查詢來的結果。

然後在外面就可以使用./***.py執行了。

<h2 id="0.4">Ubuntu修改默認Python版本</h2>

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

<h2 id="2.">OpenCV</h2>

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

