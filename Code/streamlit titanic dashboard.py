import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Daten laden
file_path = 'Titanic Dataset.csv'
data = pd.read_csv(file_path)

data['age_group'] = pd.cut(data['age'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90], labels=["0-10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80-90"])

# Streamlit Konfiguration
st.set_page_config(layout="wide")
st.title("Titanic Dashboard")

# Seitenleiste - Filter
st.sidebar.header("Filter")
age_group_filter = st.sidebar.multiselect("Altersgruppe", options=data['age_group'].dropna().unique(), default=data['age_group'].dropna().unique())
class_filter = st.sidebar.multiselect("Passagierklasse", options=sorted(data['pclass'].unique()), default=sorted(data['pclass'].unique()))
gender_filter = st.sidebar.multiselect("Geschlecht", options=data['sex'].unique(), default=data['sex'].unique())

# Filter anwenden
df_filtered = data[(data['age_group'].isin(age_group_filter)) & (data['pclass'].isin(class_filter)) & (data['sex'].isin(gender_filter))]

# Anzahl Passagiere und Überlebensrate
total_passengers = len(df_filtered)
survival_rate = df_filtered['survived'].mean() if total_passengers > 0 else 0

# Visualisierungen
col1, col2 = st.columns(2)

with col1:
    st.subheader("Anzahl Passagiere")
    st.metric("Gesamtanzahl", total_passengers)

with col2:
    st.subheader("Überlebensrate")
    st.metric("Überlebensrate", f"{survival_rate:.2%}")

# Barplot - Überlebensrate nach Altersgruppe
st.subheader("Überlebensrate nach Altersgruppe")
survival_by_age = df_filtered.groupby('age_group')['survived'].mean()
fig, ax = plt.subplots()
survival_by_age.plot(kind='bar', color='skyblue', ax=ax)
ax.set_ylabel("Überlebensrate")
ax.set_title("Überlebensrate nach Altersgruppe")
st.pyplot(fig)

# Barplot - Überlebensrate nach Passagierklasse
st.subheader("Überlebensrate nach Passagierklasse")
survival_by_class = df_filtered.groupby('pclass')['survived'].mean()
fig, ax = plt.subplots()
survival_by_class.plot(kind='bar', color='salmon', ax=ax)
ax.set_ylabel("Überlebensrate")
ax.set_title("Überlebensrate nach Passagierklasse")
st.pyplot(fig)

# Barplot - Überlebensrate nach Geschlecht
st.subheader("Überlebensrate nach Geschlecht")
survival_by_gender = df_filtered.groupby('sex')['survived'].mean()
fig, ax = plt.subplots()
survival_by_gender.plot(kind='bar', color='green', ax=ax)
ax.set_ylabel("Überlebensrate")
ax.set_title("Überlebensrate nach Geschlecht")
st.pyplot(fig)
