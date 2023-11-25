#import sesuai yang dibutuhkan
from multiprocessing import connection
import tkinter as tk
import tkinter.messagebox 
import sqlite3

top = tkinter.Tk() 

#judul 
top.title("Pemograman Kelas B")
top.geometry("400x400")
top.resizable(False,False)

#untuk wadah 
Inputframe=tk.Frame(top)
Inputframe.pack(padx= 10, pady=10, fill="x", expand=True )

#bikin label paling atas
label = tk.Label(Inputframe, text="Aplikasi Prediksi Pilihan")
label.pack()

#bikininput siswa
Input=tk.Label(Inputframe, text="Masukan Nama Siswa: ")
Input.pack(padx=10, pady=10 ,fill="x", expand=True)

#membuat entry menggunakan tkinter 
E1=tk.Entry(Inputframe)
E1.pack(padx=10, pady=10 ,fill="x", expand=True)

#bikin input nilai biologi
Input2=tk.Label(Inputframe, text="Masukan Nilai Biologi: ")
Input2.pack(padx=10, pady=10 ,fill="x", expand=True)
#membuat entry menggunakan tkinter 
E2=tk.Entry(Inputframe)
E2.pack(padx=10, pady=10 ,fill="x", expand=True)
#bikin input nilai fisika
Input3=tk.Label(Inputframe, text="Masukan Nilai Fisika: ")
Input3.pack(padx=10, pady=10 ,fill="x", expand=True)
#membuat entry menggunakan tkinter 
E3=tk.Entry(Inputframe)
E3.pack(padx=10, pady=10 ,fill="x", expand=True)
#bikin input nilai bahasa inggris
Input4=tk.Label(Inputframe, text="Masukan Nilai bahasa inggris: ")
Input4.pack(padx=10, pady=10 ,fill="x", expand=True)
#membuat entry menggunakan tkinter 
E4=tk.Entry(Inputframe)
E4.pack(padx=10, pady=10 ,fill="x", expand=True)

#bikin button
# buat fungsi

#Membuat fungsi onClickBut() untuk memproses input nilai dan memprediksi fakultas berdasarkan nilai tersebut.
def onClickBut():
    Nama_Siswa=E1.get()
    #muntuk mengambil nilai dari entry tkinter diatas
    Nilai_Biologi=int(E2.get())
    Nilai_Fisika=int(E3.get())
    Nilai_Inggris=int(E4.get())
    #membuat kondisi if else ketika nilai biologi lebih tinggi dari nilai fisika , 
    # dan nilai biologi lebih dari nilai fisika maka prediksi fakultasnya kedokteran
    if Nilai_Biologi > Nilai_Fisika and Nilai_Biologi> Nilai_Inggris:
        prediksi_fakultas = "Kedokteran"
        #jika nilai fisika lebih dari nilai biologi
        #dan nilai fisika lebih dari nilai inggris maka prediksi fakultasnya Teknik
    elif Nilai_Fisika > Nilai_Biologi and Nilai_Fisika > Nilai_Inggris:
        prediksi_fakultas = "Teknik"
        #jika nilai selain dari atas maka prediksinya fakultasnya adalah Bahasa
    else:
        prediksi_fakultas = "Bahasa"

    #save data sqlite
    #menyambungkan database dengan nama sesuai yang dibuat danangdatabase.db
    conn = sqlite3.connect('danangdatabase.db')
    #untuk mengeksekusi perintah SQL dan mengambil hasilnya.
    c = conn.cursor()
    #membuat tabel dengan isi nama siswa adalah text,biologi integer,fisika interger,prediksi_fakultas text
    #bisa langsung dibuat di sqlite atau langsung disini seperti ini
    #c.execute('''CREATE TABLE nilai_siswa (
                #nama_siswa TEXT,
               # biologi INTEGER,
                #fisika INTEGER,
               # inggris INTEGER,
               # prediksi_fakultas TEXT
           # )''')
    #membuat untuk memasukan data di variable nama siswa,nilai biologi,fisika,inggris,prediksi fakultas
    #c.execute("INSERT INTO nilai_siswa VALUES (?, ?, ?, ?, ?)", (Nama_Siswa, Nilai_Biologi, Nilai_Fisika, Nilai_Inggris, prediksi_fakultas))

    conn.commit()
    conn.close()
    #membuat tampilan 
    #print("Nama Kamu Adalah: " + Nama_Siswa + " " + str(Nilai_Biologi) + " " + str(Nilai_Fisika) + " " + str(Nilai_Inggris) + " " + prediksi_fakultas)
    #UNTUK PESAN BOX 
    tkinter.messagebox.showinfo("Keterangan", "Nama Kamu Adalah: " + Nama_Siswa + " " 
                                + "nilai biologi" + str(Nilai_Biologi) + " " "nilai fisika" + str(Nilai_Fisika) + " " + "nilai inggris" + str(Nilai_Inggris) 
                                + "dengan nilai seperti itu prediksi untuk fakultas yang cocok untuk kamu adalah" + " " + prediksi_fakultas)
#membuat button submit
#membuat button submit
tombol=tk.Button(Inputframe, text="Submit" , background="Green", fg="white", command= onClickBut)
tombol.pack(padx=10, pady=10 ,fill="x", expand=True)


top.mainloop()
# Melakukan commit dan menutup koneksi


