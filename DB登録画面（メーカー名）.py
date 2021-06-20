#!/usr/bin/env python
# coding: utf-8

# In[2]:


# -*- coding: utf-8 -*-

import tkinter as tk

# rootフレームの設定
root = tk.Tk()
root.title("図面検索システム　－　メーカー登録")
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
label_maker1 = tk.Label(root,text="【メーカー登録】",font=("",20),anchor = "w",fg="mediumblue",height=2)
label_maker1.pack(fill="x")

label_maker_num = tk.Label(root,text="メーカーのナンバーを入力してください",font=("",10),anchor = "w",fg="mediumblue",height=2)
label_maker_num.place(x = 30, y = 65)
index_box_maker_num = tk.Entry(width = 10)
index_box_maker_num.place(x = 50, y = 95)

label_makerdb_data = tk.Label(root,text="メーカーを入力してください",font=("",10),anchor = "w",fg="mediumblue",height=2)
label_makerdb_data.place(x = 30, y = 130)
index_box_makerdb_data = tk.Entry(width = 50)
index_box_makerdb_data.place(x = 50, y = 160)

# 登録ボタンの設定
touroku_maker_button = tk.Button(root,text="登録",font=("",14),width=10,bg="gray",fg="white")
touroku_maker_button.place(x = 50, y = 230)


# メインループ
root.mainloop()


# In[ ]:




