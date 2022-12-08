import tkinter as tk
from tkinter import *

'''
############################################################
## 建立視窗並設定視窗大小
############################################################

# mainloop()是讓程式繼續執行的指令，如果要結束程式就按右上的關閉按鈕
# 用Tk()方法建立一個根視窗(root window)，之後會在這個視窗建立控件(widget)
'''
root = tk.Tk()

#print(root.winfo_screenwidth())     #輸出螢幕寬度
#print(root.winfo_screenheight())    #  輸出螢幕高度
w=720  #width
r=480  #height
x=200  #與視窗左上x的距離
y=300  #與視窗左上y的距離
root.geometry('%dx%d+%d+%d' % (w,r,x,y))

root.title('[Chicony] The GUI of the Radars')   # 設定視窗標題
root.configure(bg="#7AFEC6")                    # 可以直接打顏色名稱或是找色碼表的代號
#root.iconbitmap('heart_green.ico')              # 設定視窗圖示


'''
############################################################
## Label 外型設置
############################################################

# fonts 字型
family 字體 : Times New Roman..
size 大小 : 像素為單位
weight 粗細 : bold、normal
slant 傾斜 : italic、roman
underline 底線 : True、False
overstrike 中間橫槓 : True、False

# anchor 錨
nw      n       ne
w    center     e
sw      s       se

# wraplength: 設定文字在多少像素後自動換行

# justify: 設定標籤內容是靠左、置中還是靠右，預設是置中

# keys(): 用串列list回傳widget所有的參數
'''
'''
text=tk.Label(root, text='I am Label',                                      # Label 名稱
              height=7, width=25,                                           # 設置長與寬
              fg="#FF8000", bg="#02DF82",                                   # 更改前景與背景的顏色
              font=("Times New Roman",18,"bold","italic","underline"),      # 設定字型
              anchor='center',                                              # 設定標籤位置
              wraplength=40,                                                # 40像素後自動換行
              justify="right")                                              # 文字靠右
text.pack()

print(type(text))           # 回傳類別
print(text.keys())          # 回傳參數
'''


'''
############################################################
## Button 邊框設置
############################################################

# relief styles 邊框: 有五種標籤，分別為flat、raised、sunken、groove、ridge
'''
'''
R1 = tk.Button(root, text ="FLAT", relief="flat")           # 建立flat標籤
R2 = tk.Button(root, text ="RAISED", relief="raised")       # 建立raised標籤
R3 = tk.Button(root, text ="SUNKEN", relief="sunken")       # 建立sunken標籤
R4 = tk.Button(root, text ="GROOVE", relief="groove")       # 建立groove標籤
R5 = tk.Button(root, text ="RIDGE", relief="ridge")         # 建立ridge標籤

R1.grid()
R2.grid()
R3.grid()
R4.grid()
R5.grid()
'''


'''
############################################################
## 視窗控件配置管理員 pack
############################################################

# 分為pack方法、grid方法跟place方法
- 一個視窗中不能同時使用pack與grid排版,但place卻可以與pack或grid同時使用

# pack() 為流水式排版，是最常使用到的方法，利用相對位置的概念去做控件的配置
- 常用參數有side、fill、expand、padx/pady、ipadx/ipady跟anchor

side: 
- TOP: 預設，由上往下排
- BOTTOM: 由下往上排
- LEFT: 由左往右排
- RIGHT: 由右往左排

padx/pady: 是設定控件邊界與視窗邊界的距離或是控件之間的距離

ipadx/ipady: 是設定標籤文字跟標籤邊界的距離

fill: 是設定控件填滿控件被分配的空間，
- fill=X 就是被分配的空間X軸不留白
- fill=Y 就是被分配的空間Y軸不留白

expand: 是設定是否填滿額外的視窗空間，預設為False

anchor:
nw      n       ne
w    center     e
sw      s       se
'''
'''
L1=tk.Label(root,text='I am Label', bg='#DDA0DD', fg="#8B008B",
            font=("Viner Hand ITC", 18, "bold"))
L2=tk.Label(root,text='Welcome', bg='#6495ED', fg="#AFEEEE",
            font=("Blackadder ITC", 18, "bold"))
L3=tk.Label(root,text='Thank you', bg='#FFFACD', fg="#DAA520",
            font=("Algerian", 18, "bold"))

## side參數介紹
#L1.pack() or L1.pack(side='bottom') or L1.pack(side='left') or L1.pack(side='right')

## padx/pady與fill的介紹
#L1.pack(side='right', fill='y')     #由右排到左，填滿Y軸空間
#L2.pack(side='right', padx='50')    #由右排到左，跟左右兩邊距離10
#L3.pack(side='right', fill='y')     #由右排到左，填滿Y軸空間

## padx/pady跟ipadx/ipady & fill與expand的介紹
#L1.pack(side='right', padx='10', ipadx='20')       #由右排到左，左右間隔10，文字跟標籤邊界間隔20
#L2.pack(side='right', padx='10', ipady='20')       #由右排到左，左右間隔10，文字跟標籤邊界間隔20
#L3.pack(side='right')                              #由右排到左

## expand的應用
#L1.pack(side='left', fill='x')
#L2.pack(fill='both', expand=True)
#L3.pack()

## anchor的應用
L1.pack(anchor='s', side='right', padx=10, pady=10)     #從右開始南方位置
L2.pack(anchor='s', side='right', pady=10, padx=10)     #從右開始南方位置
L3.pack(anchor='s', side='right', pady=10, padx=10)     #從右開始南方位置
'''


'''
############################################################
## 視窗控件配置管理員 grid
############################################################

- 表格式排版，一個網格 row 跟 column 只能放一個元件

- row & column: row跟column的起始值都是0，但是沒有特別去設定的話，預設值是1

- rowspan & columnspan

- sticky: 與錨定參數 anchor 很像，但只能設定 E/W/S/N 四個常數，也就是上/下/左/右或用組合的方法
sticky=N+S:     拉長高度使控件在頂端和底端對齊
sticky=W+E:     拉長寬度度使控件在左邊和右邊對齊
sticky=N+S+E:   拉長高度使控件在頂端和底端對齊且同時切齊右邊
sticky=N+S+W:   拉長高度使控件在頂端和底端對齊且同時切齊左邊
sticky=N+S+W+E: 拉長高度使控件在頂端和底端對齊且同時切齊左右兩邊
'''
'''
L1=tk.Label(root,text='I am Label', bg='#DDA0DD', fg="#8B008B",
            font=("Viner Hand ITC", 18, "bold"))
L2=tk.Label(root,text='Welcome', bg='#6495ED', fg="#AFEEEE",
            font=("Blackadder ITC", 18, "bold"))
L3=tk.Label(root,text='Thank you', bg='#FFFACD', fg="#DAA520",
            font=("Algerian", 18, "bold"))

## row跟column的使用
#L1.grid(row=0, column=0)        #網格方法
#L2.grid(row=1, column=1)        #網格方法
#L3.grid(row=1, column=0)        #網格方法

## columnspan
#L1.grid(row=0, column=0, columnspan=2)          #網格方法
#L2.grid(row=1, column=1)                        #網格方法
#L3.grid(row=1, column=0)                        #網格方法

## rowspan
#L1.grid(row=0, column=0)                    #網格方法
#L2.grid(row=0, column=1, rowspan=2)         #網格方法
#L3.grid(row=1, column=0)                    #網格方法

## sticky
#L1.grid(row=0, column=0, columnspan=2, sticky=tk.E+tk.W)        #網格方法
#L2.grid(row=1, column=1)                                        #網格方法
#L3.grid(row=1, column=0)                                        #網格方法
'''


'''
############################################################
## Button 按下觸發 Label 變化
############################################################

# config()
首先，定義一個按鈕函數 clickHello()，處理 Hello 按鍵被按次數，
用全域變數 count，記錄 Hello 按鍵被按次數，count 會隨著 Hello 被按次數增加，
且透過呼叫元件 config() 函數更改標籤元件的文字內容
'''
'''
text=tk.Label(root, text="Please click the button of Hello",font=("Bauhaus 93", 20, "bold"))

count=0
def clickHello():
    global count
    count=count + 1
    text.config(text="Click Hello " + str(count) + " times")

B=tk.Button(root, text="Hello", command=clickHello, font=("Bauhaus 93", 20, "bold"))

text.pack()
B.pack()
'''


'''
############################################################
## Button 功能介紹
############################################################

- Button可以顯示傳達按鈕用途的文本或圖像。將一個函數或一個方法附加到一個按鈕上，點按鈕時就會執行

activebackground: 滑鼠位於按鈕時的背景顏色
activeforeground: 滑鼠位於按鈕時的前景顏色
bd: 以像素為單位的邊框寬度。 預設為 2
bg: 背景顏色
command: 按按鈕時要用的函數或方法
fg: 字型顏色
font: 字體
height: 字元高
highlightcolor: 當按鈕具有焦點時顯示的顏色
image: 要顯示在按鈕上的圖
justify: 顯示多個文本行時，LEFT 靠左對齊每一行； CENTER 使它們居中；或RIGHT 靠右對齊
padx/pady: 文字左右側的距離/文字上下的距離
relief: 按鈕邊框的類型。有 FLAT、SUNKEN、RAISED、GROOVE 和 RIDGE
state: 預設為 ACTIVE。若設為 DISABLED 可使按鈕變灰表示暫時無法使用
underline: 預設值為 -1，代表按鈕上的文字沒有底線。如果非負，代表按鈕上的文字有底線
width: 按鈕寬度
wraplength: 如果此值設置為正數，文字會換行。預設為0

compound: 可以設定文字在圖的哪邊，有top、bottom、center、left跟right
'''
'''
## Button外觀設置
B1=tk.Button(root,text='Normal Button',relief="ridge",
             activebackground='#BE77FF',        #設定滑鼠位於按鈕時的背景顏色
             activeforeground='#FFFFFF',        #設定滑鼠位於按鈕時的前景顏色
             state=tk.NORMAL,                   #設定按鈕的狀態
             cursor='heart')
B2=tk.Button(root,text='Disabled Button',relief="ridge",
             activebackground='#BE77FF',        #設定滑鼠位於按鈕時的背景顏色
             activeforeground='#FFFFFF',        #設定滑鼠位於按鈕時的前景顏色
             state=tk.DISABLED)                 #設定按鈕的狀態
B3=tk.Button(root,text='Active Button',relief="ridge",
             activebackground='#BE77FF',        #設定滑鼠位於按鈕時的背景顏色
             activeforeground='#FFFFFF',        #設定滑鼠位於按鈕時的前景顏色
             state=tk.ACTIVE)                   #設定按鈕的狀態
B1.pack()
B2.pack()
B3.pack()

## 把圖放到Button裡面
photo=tk.PhotoImage(file='./tkinter_UI/Hello.gif')
B4=tk.Button(root, image=photo, text='Love', compound='top')    #設定文字在圖的top
B4.pack(side='bottom')
'''


'''
############################################################
## 如何將影像放到介面上
############################################################
'''

## 在Python中使用Label組件加入Gif動態圖片
gif = tk.PhotoImage(file="./tkinter_UI/Hello.gif")
text_gif = tk.Label(root, image=gif)
text_gif.pack() 

## 在Python中使用Label組件加入Jpg圖片
from PIL import Image,ImageTk

jpg = Image.open("./tkinter_UI/OEM.jpg")
# 獲取圖像的原始大小  
w_jpg, h_jpg = jpg.size 
# 縮放圖像
jpg_resized = jpg.resize((480, 320))  
OEM = ImageTk.PhotoImage(jpg_resized)
text_jpg = tk.Label(root, image=OEM, height=320, width=480)
text_jpg.pack() 

## Separator分隔線
from tkinter.ttk import Separator
sep = Separator(root, orient=tk.HORIZONTAL)      # 分隔線
sep.pack(fill='x', padx=7)

## 在Python中使用Label組件加入圖片與文字
lyrics_compound = """This is my fight song
Take back my life song
Prove I'm alright song
My power's turned on
Starting right now I'll be strong
I'll play my fight song
And I don't really care if nobody else believes
'Cause I've still got a lot of fight left in me"""  #文字內容
gif_compound = tk.PhotoImage(file="./tkinter_UI/Hello.gif")#圖片
text_compound = tk.Label(root, image=gif_compound, text=lyrics_compound, bg="#F5F5DC",
              compound="left", fg="#556B2F",
              font=("Viner Hand ITC", 12, "bold", "italic"))
text_compound.pack()



'''
############################################################
## messagebox 基本用法
############################################################

messagebox.showinfo(): 一般訊息
messagebox.showwarning(): 警告訊息
messagebox.showerror(): 錯誤訊息
messagebox.askokcancel(): 問問題對話框，確定或取消
messagebox.askquestion(): 問問題對話框，是或否
messagebox.askyesnocancel(): 問問題對話框，是或否或取消
messagebox.askretrycancel(): 重試或取消對話框
'''
'''
from tkinter import messagebox
messagebox.showinfo('My messagebox', 'Hola')
messagebox.showwarning('My messagebox', 'Oops!')
messagebox.showerror('My messagebox', 'Error!!!')
messagebox.askokcancel('My messagebox', 'Cancel or not ?')
messagebox.askquestion('My messagebox', 'Are you sure you want to leave ?')
messagebox.askyesnocancel('My messagebox', '是或否或取消?')
messagebox.askretrycancel('My messagebox', '重試或取消?')
'''


'''
############################################################
## 文字方塊Entry
############################################################

- Entry常見的參數

bg: 邊框背景顏色
fg: 字型顏色
bd: 邊框大小，預設為 2px
cursor: 滑鼠形狀設定
font: 字體
command: 按按鈕時要用的函數或方法
highlightcolor: 當按鈕具有焦點時顯示的顏色
relief: 邊框有五種標籤，分別為flat、raised、sunken、groove、ridge
justify: 顯示多個文本行時，LEFT 靠左對齊每一行； CENTER 使它們居中；或RIGHT 靠右對齊
selectbackground: 被選取字串的背景顏色
selectborederwidth: 被選取字串的背景框寬度
selectforeground: 被選取字串的文字顏色
width: 按鈕寬度
show: 指定文字框內容顯示哪種字符，預設為 '*'
state: 文字框狀態，有兩種為只能讀取跟可修改，NORMAL、DISABLE，預設值為NORMAL
textvariable: 文字框的值
xscrollcommand/yscrollcommand: 滾動條，X為水平的，Y為垂直的
command: 使用者更改內容時，此行會自動執行

- Entry的呼叫方式

delete(first, last=None): 刪除文本框裡的值，直接指定位置
get(): 獲得文本框的值
'''
'''
## show參數的使用
L1=tk.Label(root, text='Account', bg='#DDA0DD', fg="#8B008B",
            font=("Algerian", 15, "bold"), padx=9)
L2=tk.Label(root, text='Password', bg='#DDA0DD', fg="#8B008B",
            font=("Algerian", 15, "bold"))
L1.grid(row=0, column=0)
L2.grid(row=1, column=0)

E1=tk.Entry(root)
E2=tk.Entry(root, show="*")     #設定用*遮住密碼
E1.grid(row=0, column=1)
E2.grid(row=1, column=1)

## get參數的使用
from tkinter import messagebox
def Info():
    if E1.get() == 'chicony' and E2.get() == 'svn123':
        messagebox.showinfo('Messagebox', 'Login successful！')
    else:
        messagebox.showinfo('Messagebox', 'Login Error！')

b1=tk.Button(root, text='Login', anchor='c', width=6, height=1, command=Info)
b1.grid(row=2,column=0)
b2=tk.Button(root, text='Exit', anchor='c', width=6, height=1, command=root.quit)    #quit可以讓pyhon shell結束
b2.grid(row=2,column=1)

## eval參數的使用
label =tk.Label(root, text="Enter your math question:", bg="#7AFEC6", fg='#FFAAD5', font=("Ravie",10,"bold"))
label.grid(row=3, column=0, columnspan=2, pady='20')

equ = tk.Entry(root)    #輸入要算的東西
equ.grid(row=4, column=0, columnspan=2)

result = tk.Label(root, bg="#7AFEC6", fg='#FF5151', font=("Ravie", 15, "bold"))   #儲存計算結果
result.grid(row=5, column=0, columnspan=2)

def math():
    result.configure(text = 'Answer: '+ str(eval(equ.get())))
    print("equ.get()=", equ.get())

b3 = tk.Button(root, text="compute", command=math)      #執行鈕
b3.grid(row=6, column=0, columnspan=2)
'''


'''
############################################################
## 按鈕觸發子視窗 以及 Message介紹
############################################################
'''
'''
def createNewWindow():
    newWindow = tk.Toplevel(root)
    subw=480   # width
    subr=320   # height
    subx=200   # 與視窗左上x的距離
    suby=200   # 與視窗左上y的距離
    newWindow.geometry('%dx%d+%d+%d' % (subw, subr, subx, suby))
    newWindow.title('[Chicony] Mode Parameters')
    #newWindow.configure(bg=sub_bg)

    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    Message(newWindow, text='这是一则消息', width=100).pack()
    Message(newWindow, text='这是一则长长长长长长长长长长长消息', width=100).pack()
    Message(newWindow, text='这是\n一则长长长长长长长长长长长消息', width=100).pack()# 可以强制换行 

    labelExample.pack()
    buttonExample.pack()


buttonExample = tk.Button(root,
              text="Create new window",
              command=createNewWindow)
buttonExample1 = tk.Button(root,
              text="Create new window",
              command=createNewWindow)

buttonExample.pack()
buttonExample1.pack()
'''



root.mainloop()

