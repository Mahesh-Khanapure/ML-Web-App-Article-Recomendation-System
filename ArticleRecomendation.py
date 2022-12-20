import streamlit as st
html_temp="""
<div style="background-color:lightblue;padding:16px">
<h2 style="color:back;text-algin:center;">Article Recommendation</h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)
import pandas as pd
import pickle
arti_dict=pickle.load(open('Aricles.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
article=pd.DataFrame(arti_dict)

def Recommende(Article):
    Article_idx = article[article['Title'] == Article].index[0]
    distances = similarity[Article_idx]
    Article_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    Articles=[]
    for i in Article_list:
        Articles.append(article.iloc[i[0]].Title)

    return Articles

Title=st.selectbox('Name Of The Article Title',article['Title'].values)

if st.button('Recomendation'):

    prediction=Recommende(Title)
    for i in prediction:
        st.write(i)