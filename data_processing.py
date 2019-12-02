import pandas as pd

d1=pd.read_excel(r"C:\Users\Song\Desktop\降雨数据\1951-2000天降雨量永靖.xlsx")
d11=d1[0]
d2=pd.read_excel(r"C:\Users\Song\Desktop\降雨数据\滑坡发生时间年.xlsx")
d22=d2["时间"]

for m in range(100):

    for i in range(18263):

        if d22[m] == d11[i] :



            j = 1
            a = d1[1][i]
            n = 1

            d2["当天"][m] = a

            while j < 5:
                a = a + d1[1][i - 1]

                if d1[1][i-1] != 0:
                    n = n + 1

                i = i - 1
                j = j + 1
            d2["五天"][m] = a
            d2["五天内有几天降雨"][m] = n

            while j < 10:
                a = a + d1[1][i - 1]

                if d1[1][i - 1] != 0:
                    n = n + 1

                i = i - 1
                j = j + 1
            d2["十天"][m] = a
            d2["十天内有几天降雨"][m] = n

            while j < 30:
                a = a + d1[1][i - 1]

                if d1[1][i - 1] != 0:
                    n = n + 1

                i = i - 1
                j = j + 1
            d2["三十天"][m] = a
            d2["三十天内有几天降雨"][m] = n

            while j < 60:
                a = a + d1[1][i - 1]

                if d1[1][i - 1] != 0:
                    n = n + 1

                i = i - 1
                j = j + 1
            d2["六十天"][m] = a
            d2["六十天内有几天降雨"][m] = n

            while j < 90:
                a = a + d1[1][i - 1]

                if d1[1][i - 1] != 0:
                    n = n + 1

                i = i - 1
                j = j + 1
            d2["九十天"][m] = a
            d2["九十天内有几天降雨"][m] = n
print(d2)
d2.to_excel("C:/Users/Song/Desktop/降雨数据/d2.xlsx")