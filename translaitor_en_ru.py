import io
import streamlit as st
from transformers import pipeline

st.title('TranslatorEnRu в облаке Streamlit')

res = st.text_input('Please enter text')

en_ru_translator = pipeline("translation_en_to_ru", 'Helsinki-NLP/opus-mt-en-ru')
trans = en_ru_translator(res)
st.write('Translation')
for i in trans:
    st.write(i['translation_text'])
