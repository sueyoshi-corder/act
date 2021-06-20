#!/usr/bin/env python
# coding: utf-8

# In[11]:


# -*- coding: utf-8 -*-

import tkinter as tk

# rootフレームの設定
root = tk.Tk()
root.title("図面検索システム　－　エンドユーザ登録")
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
label_enddb1 = tk.Label(root,text="【エンドユーザ登録】",font=("",20),anchor = "w",fg="forestgreen",height=2)
label_enddb1.pack(fill="x")

label_enddb_idx = tk.Label(root,text="インデックスを選択してください",font=("",10),anchor = "w",fg="mediumblue",height=2)
label_enddb_idx.place(x = 30, y = 65)
index_box_enddb_idx = tk.Entry(width = 10)
index_box_enddb_idx.place(x = 50, y = 95)

label_enddb_eu = tk.Label(root,text="登録する顧客名を入力してください",font=("",10),anchor = "w",fg="mediumblue",height=2)
label_enddb_eu.place(x = 30, y = 130)
index_box_enddb_eu = tk.Entry(width = 50)
index_box_enddb_eu.place(x = 50, y = 160)


# メインループ
root.mainloop()


# In[ ]:




