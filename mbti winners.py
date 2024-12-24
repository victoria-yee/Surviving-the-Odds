import pandas as pd
import matplotlib.pyplot as plt

# import dataset
file_path = 'survivor.xlsx'

sheet_name = 'Castaways'
df = pd.read_excel(file_path, sheet_name=sheet_name)

# map categories
category_series = df['Personality Type'].map(group_mapping)

# filter out top 3
filtered_result = ['Sole Survivor', 'Runner-up', '2nd runner-up']
df = df[df['Result'].isin(filtered_result)]

counts = df['Result'].value_counts()

# group mapping for 16 personalities
group_mapping = {
    'INTJ': 'Analysts', 'INTP': 'Analysts', 'ENTJ': 'Analysts', 'ENTP': 'Analysts',
    'INFJ': 'Diplomats', 'INFP': 'Diplomats', 'ENFJ': 'Diplomats', 'ENFP': 'Diplomats',
    'ISTJ': 'Sentinels', 'ISFJ': 'Sentinels', 'ESTJ': 'Sentinels', 'ESFJ': 'Sentinels',
    'ISTP': 'Explorers', 'ISFP': 'Explorers', 'ESTP': 'Explorers', 'ESFP': 'Explorers'
}

# create df with 3 categories
new_df = pd.DataFrame({
    'Personality Type': df['Personality Type'],
    'category': category_series,
    'Result': df['Result']
})

# count each respective category
grouped_data = new_df.groupby(['category', 'Result']).size().unstack(fill_value=0)

# plot stacked bar chart
grouped_data.plot(kind='bar', stacked=True, figsize=(10, 6), color=['#4c72b0', '#55a868', '#c44e52'])
plt.title('Stacked Bar Chart of Personality Categories by Results')
plt.xlabel('Personality Categories')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(title='Results')
plt.show()
