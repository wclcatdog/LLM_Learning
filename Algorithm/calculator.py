import pandas as pd
from datetime import timedelta


# 假设df是你已经读取好的DataFrame对象
df = pd.read_excel('E:/code/Algorithm/test.xlsx')

def parse_time(time_str):
    """解析时间字符串为小时、分钟和秒"""
    hours, minutes, seconds = 0, 0, 0
    if '时' in time_str:
        hours = int(time_str.split('时')[0])
        time_str = time_str.split('时')[1]
    if '分' in time_str:
        minutes = int(time_str.split('分')[0])
        time_str = time_str.split('分')[1]
    if '秒' in time_str:
        seconds = int(time_str.split('秒')[0])

    return hours, minutes, seconds


# 假设P列在DataFrame中的索引为'P'
# 从第2行开始填充是因为通常第一行是标题行
for index in range(2, len(df)):
    # 获取P列的值
    p_value = df.at[index, 'P']

    # 解析时间
    hours, minutes, seconds = parse_time(p_value)

    # 更新Q、R、S列
    df.at[index, 'Q'] = hours
    df.at[index, 'R'] = minutes
    df.at[index, 'S'] = seconds

# 打印结果或者保存到新的Excel文件
print(df[['P', 'Q', 'R', 'S']])
#df.to_excel('output.xlsx', index=False)