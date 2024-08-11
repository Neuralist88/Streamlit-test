# импортируем библиотеки
import streamlit as st
import pandas as pd
import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt
from model import open_data
import numpy as np

# Добвим заголовок приложения
st.title('Пробное приложение на Streamlit. Часть 1')

df = open_data()
st.write('Исходный датасет')
st.write(df)

# Добавим кнопку, при нажатии на которую отображаются какие-то данные
def click_button():
    st.session_state.button = not st.session_state.button

if 'button' not in st.session_state:
    st.session_state.button = False

# Опишем, что должно происходить при нажатии на кнопку
st.button('Показать инсайт №1', on_click=click_button)
if st.session_state.button:
    st.write('Индекс процветания взаимосвязан с типом политического режима в стране')
    df_1 = df.groupby(by='political_regime')['average_score'].mean()
    fig, ax = plt.subplots(figsize=(3, 4))
    # Добавим возможность выбора цвета диаграммы при помощи контрола color_picker
    picked_color = st.color_picker('Выберите цвет диаграммы', '#0024FF')
    ax.bar(df_1.index, df_1, color=picked_color) 
    ax.set_title('Группировка индекса процветания по политическим режимам') 
    ax.set_xlabel('политический режим')  
    ax.set_ylabel('индекс процветания') 
    ax.set_xticklabels(df_1.index, rotation=90) 
    # Добавим возможность выбора сетки при помощи контрола toggle
    on = st.toggle('Добавить сетку') 
    if on:
        ax.grid(True)  
    st.pyplot(fig)

# Добавим еще один контрол (checkbox)
if st.checkbox('Показать матрицу корреляции всех признаков между собой'):
    fig_corr, ax_corr = plt.subplots()
    df_corr = df.iloc[:, 4:]
    sns.heatmap(df_corr.corr(), ax=ax_corr)
    st.write(fig_corr)
          



          