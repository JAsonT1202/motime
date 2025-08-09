import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('wikipeople_unimodal.csv')

# 获取前5行数据
top_5 = df.head()

# 设置图形大小
plt.figure(figsize=(12, 6))

# 为每个人物创建一个子图
for i, (index, row) in enumerate(top_5.iterrows(), 1):
    plt.subplot(2, 3, i)
    
    # 提取每个人的属性
    name = row['name']
    birth_year = row['birth_year']
    death_year = row['death_year'] if pd.notna(row['death_year']) else 'Present'
    occupation = row['occupation']
    
    # 创建文本显示
    info_text = f"Name: {name}\nBirth: {birth_year}\nDeath: {death_year}\nOccupation: {occupation}"
    
    # 移除坐标轴
    plt.axis('off')
    
    # 添加文本
    plt.text(0.1, 0.5, info_text, fontsize=10, va='center')

# 调整子图之间的间距
plt.tight_layout()

# 添加总标题
plt.suptitle('Information of First 5 People', fontsize=16, y=1.05)

# 显示图表
plt.show()