import pandas as pd
import matplotlib.pyplot as plt

# upload dataset
file_path = 'survivor.xlsx'  

sheet_name = 'Castaway Details'
df = pd.read_excel(file_path, sheet_name=sheet_name)

# group mapping for MBTI groups 
group_mapping = {
    'INTJ': 'Analysts', 'INTP': 'Analysts', 'ENTJ': 'Analysts', 'ENTP': 'Analysts',
    'INFJ': 'Diplomats', 'INFP': 'Diplomats', 'ENFJ': 'Diplomats', 'ENFP': 'Diplomats',
    'ISTJ': 'Sentinels', 'ISFJ': 'Sentinels', 'ESTJ': 'Sentinels', 'ESFJ': 'Sentinels',
    'ISTP': 'Explorers', 'ISFP': 'Explorers', 'ESTP': 'Explorers', 'ESFP': 'Explorers'
}

# match personality type to each category
category_series = df['Personality Type'].map(group_mapping)

# create new df with new groups
new_df = pd.DataFrame({
    'Personality Type': df['Personality Type'],
    'category': category_series
})

# count the amount of each 
category_counts = new_df['category'].value_counts()

# create plot
plt.figure(figsize=(10, 3))
category_counts.plot(kind='bar', color=['#fae879', '#55a868', '#4c72b0', '#8172b2'])
plt.title('Count of Each MBTI Personality Category')
plt.xlabel('Personality Categories')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
