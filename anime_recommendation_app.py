from soupsieve import select
import streamlit as st
import numpy as np
import pandas as pd
import pickle

anime_dict=pickle.load(open('/home/darik/Desktop/Dev/Anime Recomendation system/animeDict.pkl','rb'))
animes=pd.DataFrame(anime_dict)
@st.cache(allow_output_mutation=True)
def haha(anime):
    simila=pickle.load(open('/home/darik/Desktop/Dev/Anime Recomendation system/similarity.pkl','rb'))
    index=animes[animes['Name']==anime]['index'].values[0]
    distances=sorted(list(enumerate(simila[index])),reverse=True,key=lambda x:x[1] )
    recommended_anime_names=[]
    recommended_anime_summary=[]
    recommended_anime_tags=[]
    for i in distances[1:6]:
        recommended_anime_names.append(animes.iloc[i[0]].Name)
        recommended_anime_summary.append(animes.iloc[i[0]].Synopsis)
        recommended_anime_tags.append(animes.iloc[i[0]].Tags)
    return recommended_anime_names,recommended_anime_summary,recommended_anime_tags

st.title('Anime Recommender')
selected_anime=st.selectbox('Which anime do you like?',(animes['Name'].values))
if st.button('click'):
    with st.spinner(text='In Progress'):
        recom,summery,tags=haha[selected_anime]
        st.success('Done')
        st.balloons()
        for i in range(5):
            st.write(f"{i+1}"+"Title : "+str(recom[i]))
            st.write("Summary : "+str(summery[i]))
            st.write("Tags : "+str(tags[i]))