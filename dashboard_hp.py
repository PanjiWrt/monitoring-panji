import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tampilan di HP
st.set_page_config(page_title="Panji Produksi", layout="centered")
st.title("📊 Monitoring Produksi Panji")

st.info("Input data di bawah untuk update grafik & Excel")

# Input Data
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
col1, col2 = st.columns(2)

output = []
suhu = []

with col1:
    st.subheader("Output (kg)")
    for h in hari:
        val = st.number_input(f"Output {h}", value=450, key=f"out_{h}")
        output.append(val)

with col2:
    st.subheader("Suhu (°C)")
    for h in hari:
        val = st.number_input(f"Suhu {h}", value=180, key=f"suh_{h}")
        suhu.append(val)

# Grafik Korelasi
fig, ax1 = plt.subplots()
ax1.plot(hari, output, color='blue', marker='o', label="Output")
ax1.set_ylabel("Produksi (kg)", color="blue")

ax2 = ax1.twinx()
ax2.plot(hari, suhu, color='red', marker='s', linestyle="--", label="Suhu")
ax2.set_ylabel("Suhu (°C)", color="red")
ax2.axhline(y=190, color='red', alpha=0.3)

st.pyplot(fig)

# Tombol Simpan ke Excel
if st.button("💾 SIMPAN KE EXCEL", use_container_width=True):
    df = pd.DataFrame({"Hari": hari, "Output": output, "Suhu": suhu})
    df.to_excel("Laporan_Produksi_Panji.xlsx", index=False)
    st.success("Berhasil disimpan ke Excel!")
    import time

# ... (kode atasnya tetap sama)

if st.button("💾 SIMPAN KE EXCEL", use_container_width=True):
    # Tambahkan jam menit agar nama file unik
    waktu_skrg = time.strftime("%Y%m%d-%H%M%S")
    nama_file = f"Laporan_Produksi_{waktu_skrg}.xlsx"
    
    df = pd.DataFrame({"Hari": hari, "Output": output, "Suhu": suhu})
    df.to_excel(nama_file, index=False)
    st.success(f"Berhasil! Tersimpan sebagai: {nama_file}")
    import io

# ... (kode input data tetap sama)

if st.button("📊 PROSES DATA", use_container_width=True):
    df = pd.DataFrame({"Hari": hari, "Output": output, "Suhu": suhu})
    
    # Membuat file Excel di memori (biar bisa di-download di HP)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    
    st.download_button(
        label="📥 DOWNLOAD EXCEL KE HP",
        data=buffer.getvalue(),
        file_name=f"Laporan_Panji_{time.strftime('%H%M%S')}.xlsx",
        mime="application/vnd.ms-excel",
        use_container_width=True
    )
    st.success("Data siap di-download!")
