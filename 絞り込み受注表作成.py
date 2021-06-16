import pandas as pd
from datetime import datetime

#表示行数セット
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 7)

#受注台帳の読み込みと受注日をdaytimeとして読み込み
df = pd.read_csv('受注台帳.csv',parse_dates=["受注日"],encoding="shift-jis_")

#インデックスを１から順にする
df.index = df.index + 1


#検索する請負会社名を入力
print("")
print("")
ukeoi_kaisya = input("請負会社名を入力してください（部分一致検索）")
print(f"検索する請負会社は　{ukeoi_kaisya}　です")

# 入力された請負会社名でDfを抽出


df_ukeoi = df[df['請負会社'].str.contains(ukeoi_kaisya)]
print("")
print("検索対象のデータは以下のとおり（一部表示）")
print("")
print(df_ukeoi.head(3))
print(df_ukeoi.tail(3))


# 都道府県名の入力

print("")
print("")
adress = input("都道府県名を入力してください（部分一致検索）")
print("")
print("")
print(f"検索する地域は　{adress}　です")


# 入力された都道府県名でDfを抽出

df_adress = df_ukeoi[df_ukeoi['住所'].str.contains(adress)]
df_adress


# In[208]:

print("")
print("")
print("集計開始年月日を指定します")


# 検索開始年月日の年の入力　１９８０年～２０５０年以外は受け付けない


def How_start_year():
    start_year = input("西暦で年を入力してください ... ")
    try:
        start_year = int(start_year)
    except:
        print("数字で入力してください")
        return How_start_year()
    if start_year <= 1980 or start_year >= 2050:
        print("年は1980年から2050年の間で指定してください")
        return How_start_year()
    else:
        return start_year

start_year = How_start_year()


# 検索開始年月日の月の入力　１月～１２月以外は受け付けない


def How_start_month():
    start_month = input("月を入力してください ... ")
    try:
        start_month = int(start_month)
    except:
        print("数字で入力してください")
        return How_start_month()
    if start_month > 12:
        print("月は1から12の間で指定してください")
        return How_start_month()
    else:
        return start_month

start_month = How_start_month()


# 検索開始年月日の日の入力　１日～３１日以外は受け付けない


def How_start_day():
    start_day = input("日を入力してください ... ")
    try:
        start_day = int(start_day)
    except:
        print("数字で入力してください")
        return How_start_day()
    if start_day > 31:
        print("日は1から31の間で指定してください")
        return How_start_day()
    else:
        return start_day

start_day = How_start_day()
print("")
print("")
print(f"　{start_year}　年　{start_month}　月　{start_day}　日　からのデータを抽出します")


# 入力された年月日でDfを抽出


df_date = df_adress[(df_adress["受注日"] >= datetime(start_year,start_month,start_day))]


# 最終結果をエクスポート

df_date.to_excel("絞り込み受注表.xlsx",index=False,encoding="shift-jis")


# In[224]:


import openpyxl as px


# 台数の合計値を入力


file = '絞り込み受注表.xlsx'
wb = px.load_workbook(filename=file)
ws1 = wb['Sheet1']

cmax1 = ws1.max_row

goukei = 0


for i in range(2,cmax1+1):
    daisuu = ws1['F' + str(i)].value
    goukei += daisuu

ws1['G1'].value = "合計台数"
ws1['G2'].value = goukei


wb.save('絞り込み受注表.xlsx')
