from sqlite3 import*

con=connect("stok.db")
cursor=con.cursor()


def stokGiris():
    firma=input("Firma adı:")
    urun=input("Ürün adı:")
    fiyat=input("Fiyat:")
    urun_sayısı=input("Ürün sayısı:")

    cursor.execute(("insert into Stok values(?,?,?,?)"),(firma,urun,fiyat,urun_sayısı))
    cursor.execute("select * from Stok ")
    liste=cursor.fetchall()

    #return render_template(giris.html,db=con)
    print(liste)
#stokGiris()

def stokCıkıs():
    firma=input("Firma adı:")
    urun=input("Ürün adı:")
    fiyat=input("Fiyat:")
    urun_sayısı=input("Ürün sayısı:")

            
    cursor.execute("select * from Teklif ")
    liste=cursor.fetchall()
    a=list(liste)
    for s in a:
        Id=s[0]+1
        #session["firma_adi"]=request.form.get("nick")
        cursor.execute(("insert into Teklif values(?,?,?,?,?)"),(Id,firma,urun,urun_sayısı,fiyat))
        cursor.execute("select * from Teklif ")
        liste=cursor.fetchall()
        print(liste)
        con.commit()

stokCıkıs()

def stokTakip():
    cursor.execute("Select * From Stok")
    stok=cursor.fetchall()
    print(stok)


def stokTeklif():
    cursor.execute("Select * From Teklif")
    teklifler=cursor.fetchall()
    print(teklifler)

    f_id=input("İd'yi giriniz:")
    #burası html sayfasına göre ayarlanıcak.




def teklifGiris():
    firma=input("Firma adı:")
    urun=input("Ürün adı:")
    fiyat=input("Fiyat:")
    urun_sayısı=input("Ürün sayısı:")

    cursor.execute(("insert into Stok values(?,?,?,?)"),(firma,urun,fiyat,urun_sayısı))
    cursor.execute("select * from Stok ")
    liste=cursor.fetchall()

    #return render_template(giris.html,db=con)
    print(liste)


con.commit()
