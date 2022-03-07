import glob
import pandas as pd
import pandas as pd
import matplotlib as plt
import japanize_matplotlib
# 検証する通貨のデータを選択

currency = 'AUDJPY'
file = [i for i in glob.glob('C:/Users/klay1/OneDrive/デスクトップ/python/.venv/10minute_data/*.csv') if currency in i]
# データの結合
df_concat = pd.DataFrame()
for i in file:
    df = pd.read_csv(i,encoding='cp932')
    df_concat = pd.concat([df_concat,df])

df_concat.drop_duplicates(inplace=True)
df_concat.sort_values('日付',inplace=True)
df_concat.reset_index(inplace=True,drop=True)
df_2 = df_concat
df_2['devi_close_high'] = df_2['高値'] - df_2['終値']
df_2['devi_close_low'] = df_2['終値'] - df_2['安値']
df_2['devi_devi_'] = df_2['devi_close_high'] - df_2['devi_close_low']
df_2['0'] = 0
df_2['trend'] = df_2['終値'] - df_2['終値'].mean()
close_price = df_2['終値'].to_list()
check_flg = [0]
for i in range(1,len(close_price)):
    if close_price[i]-0.05 > close_price[i-1]:
        check_flg.append(1)
    elif close_price[i]+0.05 < close_price[i-1]:
        check_flg.append(-1)
    else:
        check_flg.append(0)
df_2['flg'] = check_flg
high_price = df_2['高値'].to_list()
low_price = df_2['安値'].to_list()
counter,score,check,score2 = 0,0,0,0
counter_list = [0] * len(df_2)
check_list = [0] * len(df_2)
score_list = [0] * len(df_2)
check_flg2 = [0] * len(check_flg)
for index,value in enumerate(check_flg):
    if value == 1:
        check += 1
        check_list[index] = check
        for i in range(index+1,len(df_2)):
            if high_price[i] >= close_price[index]+0.1:
                counter += 1
                score += 1
                check_flg2[index] = 2
                counter_list[i] = counter
                score_list[i] = score
                break
            elif low_price[i] >= close_price[index]-0.1:
                counter += 1
                score += -1
                check_flg2[index] = -2
                counter_list[i] = counter
                score_list[i] = score
                break
            else:
                counter_list[i] = counter
                score_list[i] = score
    elif value == -1:
        check += 1
        check_list[index] = check
        for i in range(index+1,len(df_2)):
            if high_price[i] >= close_price[index]+0.1:
                counter += 1
                score2 += -1
                check_flg2[index] = -2
                counter_list[i] = counter
                score_list[i] = score
                break
            elif low_price[i] >= close_price[index]-0.1:
                counter += 1
                score2 += +1
                check_flg2[index] = 2
                counter_list[i] = counter
                score_list[i] = score
                break
            else:
                counter_list[i] = counter
                score_list[i] = score
    else:
        check_list[index] = check
        continue
print(score_list)