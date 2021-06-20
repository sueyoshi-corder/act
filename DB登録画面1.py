#!/usr/bin/env python
# coding: utf-8

# In[36]:


# -*- coding: utf-8 -*-

import tkinter as tk

# rootフレームの設定
root = tk.Tk()
root.title("図面検索システム　－　入力画面")
root.geometry("400x400")

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
label1 = tk.Label(root,text="【データベース登録画面】",font=("",20),anchor = "w",fg="forestgreen",height=2)
label1.pack(fill="x")

label2 = tk.Label(root,text="登録したいデータベースを選択してください",font=("",15),anchor = "w",fg="forestgreen",height=2)
label2.pack(fill="x")

button1 = tk.Button(root,text="インデックス",font=("",20),bg="antique white",bd=3,width=20)
button1.pack(anchor="center")
button2 = tk.Button(root,text="エンドユーザー",font=("",20),bg="antique white",bd=3,width=20)
button2.pack(anchor="center")
button3 = tk.Button(root,text="仕様",font=("",20),bg="antique white",bd=3,width=20)
button3.pack(anchor="center")
button4 = tk.Button(root,text="メーカー",font=("",20),bg="antique white",bd=3,width=20)
button4.pack(anchor="center")
button4 = tk.Button(root,text="車型",font=("",20),bg="antique white",bd=3,width=20)
button4.pack(anchor="center")

# メインループ
root.mainloop()


# In[ ]:




