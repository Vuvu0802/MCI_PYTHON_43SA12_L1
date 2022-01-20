import pandas as pd
import seaborn as sns
import streamlit as st


tips_df = sns.load_dataset('tips')
st.title('This is tips dashboard')

st.header('Tips dataset')
tips_df

st.header('Total bill following gender')
total_bill_gender = tips_df.groupby('sex').total_bill.sum()
st.bar_chart(total_bill_gender, 100, 700)

st.radio('Please choose the name', ['Truong', 'Huy', 'Vinh'])

