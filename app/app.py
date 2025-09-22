# app/app.py
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

sns.set(style="whitegrid")

# --- Title and description ---
st.title("COVID-19 Data Explorer")
st.write("""
Explore a subset of the COVID-19 research papers dataset.
Visualize publications by year, top journals, paper sources, and most frequent words in titles.
""")

# --- Load data ---
@st.cache_data
def load_data():
    app_dir = os.path.dirname(__file__)
    csv_path = os.path.join(app_dir, 'metadata_subset.csv')
    df = pd.read_csv(csv_path)
    return df

df = load_data()

# --- Sidebar filters ---
st.sidebar.header("Filters")

# Year filter
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.sidebar.slider("Select year range", min_year, max_year, (min_year, max_year))

# Journal filter (interactive fix: default empty)
top_journals = df['journal'].value_counts().head(20).index.tolist()
selected_journal = st.sidebar.multiselect("Select journal(s)", top_journals, default=[])

# Filter dataset
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
if selected_journal:
    filtered_df = filtered_df[filtered_df['journal'].isin(selected_journal)]

st.write(f"Showing {filtered_df.shape[0]} papers from {year_range[0]} to {year_range[1]}")

# --- Display sample of data ---
st.subheader("Sample Data")
st.dataframe(filtered_df[['title', 'authors', 'journal', 'year', 'source_x']].head(10))

# --- Publications by Year ---
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x=year_counts.index, y=year_counts.values, palette="viridis", ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# --- Top Journals ---
st.subheader("Top 10 Journals")
top_journals_counts = filtered_df['journal'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=top_journals_counts.values, y=top_journals_counts.index, palette="magma", ax=ax)
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
st.pyplot(fig)

# --- Distribution by Source ---
st.subheader("Distribution by Source")
source_counts = filtered_df['source_x'].value_counts()

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x=source_counts.index, y=source_counts.values, palette="coolwarm", ax=ax)
ax.set_xlabel("Source")
ax.set_ylabel("Number of Papers")
plt.xticks(rotation=45)
st.pyplot(fig)

# --- Word Cloud of Titles ---
st.subheader("Word Cloud of Paper Titles")
all_titles = ' '.join(filtered_df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)

fig, ax = plt.subplots(figsize=(15,7))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)
