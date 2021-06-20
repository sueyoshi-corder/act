#!/usr/bin/env python
# coding: utf-8

# In[111]:


# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

# ウインドウの作成
root = tk.Tk()
root.title("図面検索システム　－　検索画面")
# ウインドウのサイズ指定
root.geometry("1000x600")

# メニューバーの作成
menubar = tk.Menu(root)
root.configure(menu = menubar)
# ファイルメニュー
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
# ～内容
filemenu.add_command(label = "Open File...")
# セパレーター
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = lambda: root.destroy())

# 検索画面ラベルの設定
label1 = tk.Label(root,text="【検索画面】",font=("",20),anchor = "w",fg="mediumblue",height=2)
label1.pack(fill="x")

# ダイレクト検索ボタン
eu_button = tk.Button(root, text = "E/Uダイレクト検索")
eu_button.place(x = 70, y = 80)

# テキストボックス設置 <---追加するコード
eu_input_box = tk.Entry(width = 50)
eu_input_box.place(x = 200, y = 85)

# インデックス検索
label2 = tk.Label(root,text="リスト検索",font=("",10),anchor = "w",fg="mediumblue",height=2)
label2.place(x = 70, y = 125)
index_box = tk.Entry(width = 10)
index_box.place(x = 80, y = 155)
eu_choice_box = tk.Entry(width = 50)
eu_choice_box.place(x = 170, y = 155)

label3 = tk.Label(root,text="仕様",font=("",10),anchor = "w",fg="mediumblue",height=2)
label3.place(x = 70, y = 190)
siyou_box = tk.Entry(width = 30)
siyou_box.place(x = 80, y = 220)

label4 = tk.Label(root,text="メーカー",font=("",10),anchor = "w",fg="mediumblue",height=2)
label4.place(x = 280, y = 190)
maker_box = tk.Entry(width = 30)
maker_box.place(x = 290, y = 220)

label5 = tk.Label(root,text="車型",font=("",10),anchor = "w",fg="mediumblue",height=2)
label5.place(x = 500, y = 190)
cartype_box = tk.Entry(width = 20)
cartype_box.place(x = 510, y = 220)

label6 = tk.Label(root,text="番号",font=("",10),anchor = "w",fg="mediumblue",height=2)
label6.place(x = 670, y = 190)
num_box = tk.Entry(width = 10)
num_box.place(x = 680, y = 220)

# ステータスバー設置 <---追加するコード
statusbar = tk.Label(root, text =  " No Data!!",bd=1,relief=tk.SUNKEN,anchor=tk.W)
statusbar.pack(side = tk.BOTTOM, fill=tk.X)

# ウインドウ状態の維持
root.mainloop()


# In[ ]:




