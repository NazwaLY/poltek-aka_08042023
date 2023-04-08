# library
import streamlit as st

# write
st.title('software perkalian')
st.write('Ini adalah aplikasi untuk mengalikan bilangan bil.bul')

#input bilangan pertama
number1 = st.number_input('Masukkan bilangan pertama')
st.write(f'bilangan pertama adalah {number1}')

#input bilangan kedua
number2 = st.number_input('Masukkan bilangan kedua')
st.write(f'bilangan kedua adalah {number2}')

if st.button('hitung'):
    st.write(f'hasil kali antara {number1} dan {number2} adalah {number1*number2}')
else:
    st.write('silahkan klik tombol hitung')