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
    
import numpy as np
array1 = np.random.randint(10,40, size=(10,))
array2 = np.random.randint(10,40, size=(10,))

import pandas as pd
st.dataframe(pd.DataFrame({'kelas A': array1,
                           'kelas B': array2
                          })
            )