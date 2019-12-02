
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy as np
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']



def adjacent_values(vals, q1, q3):
    upper_adjacent_value = q3 + (q3 - q1) * 1.5
    upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])

    lower_adjacent_value = q1 - (q3 - q1) * 1.5
    lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)
    return lower_adjacent_value, upper_adjacent_value


def set_axis_style(ax, labels):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('滑坡前n天')


# create test data
'''
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 10)) for std in range(1, 5)]   #sorted 排序,    data是个列表 可看成4x10'''

d= pd.read_excel(r"C:\Users\Song\Desktop\test.xlsx",index_col = 0  ,header=None)
da = d.reset_index(drop=True)
da1 = da.iloc[0,:]
data_array = np.array(da1)
data_list1 = data_array.tolist()

da2 = da.iloc[1,:]
data_array = np.array(da2)
data_list2 = data_array.tolist()

da3 = da.iloc[2,:]
data_array = np.array(da3)
data_list3 = data_array.tolist()

da4 = da.iloc[3,:]
data_array = np.array(da4)
data_list4 = data_array.tolist()

da5 = da.iloc[4,:]
data_array = np.array(da5)
data_list5 = data_array.tolist()

data = [data_list1,data_list2, data_list3, data_list4, data_list5]



fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(9, 4), sharey=True)   #指生成一行两列个图

ax1.set_title('滑坡前降雨天数分布图')
ax1.set_ylabel('滑坡前n天降雨天数（/天）')
ax1.violinplot(data)

ax2.set_title('Customized violin plot')
parts = ax2.violinplot(
        data, showmeans=False, showmedians=False,
        showextrema=False)

for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)  #求取数列第25 50 75%分位的数值,axis为1，在横行上求     得到的三个结果都是4x1，因为是列表所以也是1x4
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
whiskersMin, whiskersMax = whiskers[:, 0], whiskers[:, 1]  # 得到两个1x4 的

inds = np.arange(1, len(medians) + 1)
ax2.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax2.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax2.vlines(inds, whiskersMin, whiskersMax, color='k', linestyle='-', lw=1)

# set style for the axes
labels = ['五天', '十天', '三十天', '六十天', '九十天']
for ax in [ax1, ax2]:
    set_axis_style(ax, labels)

plt.subplots_adjust(bottom=0.15, wspace=0.05)
plt.show()

np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 4)) for std in range(1, 2)]   #sorted 排序,    data是个列表 可看成4x10
print(data)
#要注意的问题是，输入的数据是[[4,5,6,1,3,4,4,5,][4,5,5,9,4,2,5,8,]] 这种列表类型的，官方示例是生成两个图，本次只用一个图，所以更改了只生成一个图。






