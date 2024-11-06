import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# menyiapkan file csv
heute_df = pd.read_csv('day.csv')
uhr_df = pd.read_csv('hour.csv')

# Judul dashboard
st.title('Proyek Akhir')
st.title('Dashboard Sistem Berbagi Sepeda🚲')

#Grafik penyewaan sepeda berdasarkan musim
if st.button('Pertanyaan 1'):
    st.write('Berapa Jumlah Penyewa Sepeda Berdasarkan Kondisi Musim ?')

sm_season = heute_df.groupby(by='season').agg({
    'cnt' : 'sum'}).reset_index()
print(sm_season)

st.markdown(
        """
        <style>
        .title{
            text-align: center;
            font-size: 15px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
)
st.markdown('<div class="title">Pengaruh Musim terhadap Jumlah Sewa Sepeda</div>', unsafe_allow_html=True)

plt.figure(figsize=(10, 5))
sns.barplot(x='season', y='cnt', data=sm_season, color='coral')
plt.xlabel('Musim')
plt.ylabel('Jumlah Sewa')

st.pyplot(plt)

st.text('1 = Musim Semi, 2 = Musim Panas, 3 = Musim Gugur, 4 = Musim Dingin')

#Korelasi antara kondisi cuaca dengan jumlah sewa sepeda
if st.button('Pertanyaan 2'):
    st.write('Bagaimana Hubungan Antara Kondisi Cuaca Dengan Jumlah Penyewaan Sepeda ?')
    
mn_weather = uhr_df.groupby(by='weathersit').agg({
    'cnt' : 'count'}).reset_index()
print(mn_weather)

st.markdown(
        """
        <style>
        .title{
            text-align: center;
            font-size: 15px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
)
st.markdown('<div class="title">Jumlah Penyewa Sepeda VS Cuaca</div>', unsafe_allow_html=True)

st.scatter_chart(mn_weather, x='weathersit', y='cnt', color='#ffaa0088')

#Pola penyewaan sepeda
if st.button('Pertanyaan 3'):
    st.write('Bagaimana Pola Penyewaan Sepeda Berdasrkan Jam ?')
    
jam_df = uhr_df.groupby(by='hr').agg({
    'cnt' : 'count'}).reset_index()
print(jam_df)

st.markdown(
        """
        <style>
        .title{
            text-align: center;
            font-size: 15px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
)
st.markdown('<div class="title">Pola Penyewaan Sepeda Berdasarkan Jam</div>', unsafe_allow_html=True)

plt.figure(figsize=(11, 5))
sns.lineplot(x='hr', y='cnt', data=jam_df, orient='x', color='#0C666E',
marker='o')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewa')
plt.grid(True)

st.pyplot(plt)
        
# Expander
with st.expander("Lihat Analisis"):
    st.write(
        """
        - Grafik tertinggi berada pada musim Gugur dan terendah dimusim Semi, karena musim Gugur merupakan waktu peralihan menuju musim dingin dan menghasilkan suhu yang lebih dingin dibanginkan musim Semi.
        - Hubungan yang dihasilkan antara kondisi cuaca dan jumlah penyewaan sepeda ialah korelasi negatif, karena variabel cuaca dan jumlah penyewa sepeda bergerak berlawanaan arah.
        - Penyewaan sepeda mengalami penurunan pada jam 0:00-04:00 dan terjadi kenaikan pada jam 05:00 hingga 23:00, dengan kondisi kenaikan dan penurunan jumlah penyewa pada rentang yang dekat.
        """
    )

st.caption("By: Saskia Belgis S")
