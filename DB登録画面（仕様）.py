#!/usr/bin/env python
# coding: utf-8

# In[2]:


# -*- coding: utf-8 -*-

import tkinter as tk

# rootフレームの設定
root = tk.Tk()
root.title("図面検索システム　－　仕様登録")
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
label_enddb1 = tk.Label(root,text="【仕様登録】",font=("",20),anchor = "w",fg="mediumblue",height=2)
label_enddb1.pack(fill="x")

label_siyou_num = tk.Label(root,text="仕様のナンバーを入力してください",font=("",10),anchor = "w",fg="mediumblue",height=2)
label_siyou_num.place(x = 30, y = 65)
index_box_siyou_num = tk.Entry(width = 10)
index_box_siyou_num.place(x = 50, y = 95)

label_siyoudb_data = tk.Label(root,text="仕様を入力してください",font=("",10),anchor = "w",fg="mediumblue",height=2)
label_siyoudb_data.place(x = 30, y = 130)
index_box_siyoudb_data = tk.Entry(width = 50)
index_box_siyoudb_data.place(x = 50, y = 160)

# 登録ボタンの設定
touroku_siyou_button = tk.Button(root,text="登録",font=("",14),width=10,bg="gray",fg="white")
touroku_siyou_button.place(x = 50, y = 230)


# メインループ
root.mainloop()


# In[ ]:




