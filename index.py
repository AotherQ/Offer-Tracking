from flask import *
from flask_cors import *
from flask_session import *
from sqlite3 import *

app=Flask(__name__, static_folder='static/')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')

def index():

    return render_template('UI.html')

#Burada tekrardan render edilme sebebi signup sayfasındaki a linkinde kullanmış olmamızdır.
@app.route('/signin')

def render():
    return render_template('signin.html')

#Giriş sayfası için gerekli kodlar.
@app.route('/signin', methods=['GET', 'POST'])

def signin():
    #Eğer method post ise yapılıcaklar.
    if request.method == 'POST':

        kadi = request.form['kadi']

        pas = request.form['pas']


        con = connect("stok.db")
        cursor = con.cursor()

        cursor.execute(("select * from users where İsim=? and Sifre=?"),(kadi, pas))

        liste = cursor.fetchall()

        if len(liste) > 0:
            #Session ile burada aldığımız kullanıcı adı ve şifreyi daha sonra kullanmak için kayıt altına alıyoruz.
            session["kadi"]=request.form.get("kadi")
            # Burada giriş başarılı olduğunda yapılacak session verisi alınıyor.
            # Aslında burada session içerisinde kadi ve pass isminde iki değişken ve dize oluşturuluyor.
            
            #Daha sonra index olarak değişicek.
            return render_template('homepage.html', kadi=kadi)
    #Daha sonra index olarak değişicek.
    return redirect(url_for('index'))



#Kayıt sayfası için gerekli kodlar.
@app.route('/signup')
def index2():
    return render_template('signup.html')

@app.route('/signup',methods=['GET','POST'])

def signup():
    #Kayıt sayfasındaki method post ise yapılıcak.
    if request.method=='POST':
        nick=request.form['uName']
        sifre=request.form['uPas']

        
        con = connect("stok.db")
        cursor=con.cursor()
        cursor.execute(("select * from users where İsim=? or Sifre=?"),(nick,sifre))
        liste = cursor.fetchall()
        l=list(liste)

        #Burada l listesinin içerisinde b elementi döndürülüyor ve kontrol yapılıyor daha önce başka hesap var mı diye.
        for b in l:
            if b[0]==nick or b[1]==sifre:

                return render_template('UI.html')
            
        
        #Eğer daha önce başka hesap yok ise burada kayıt yaptırılıyor.
        else:
            if not liste:
                cursor.execute(("insert into users values(?,?)"),(nick,sifre))
            
        con.commit()
        return render_template('UI.html')


@app.route('/verilen_teklif')
def verilen_teklif():
    if session.get("kadi"):
        kadi = session.get("kadi")
        # Burada aldığımız session verisi kullanılyor.
        return render_template('takip.html', kadi=kadi)
    else:
        return render_template('takip.html',kadi=kadi)

@app.route('/homepage')
def homepage():
    if session.get("kadi"):
        kadi = session.get("kadi")
        # Burada aldığımız session verisi kullanılyor.
        return render_template('homepage.html',kadi=kadi)
    else:
        return render_template('homepage.html',kadi=kadi)
    

@app.route('/get_data')
def get_data():
    con = connect("stok.db")
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Teklif')
    rows = cursor.fetchall()
    con.close()
    return jsonify(rows)

@app.route('/getir', methods=['POST'])
def getir():
    if request.method == 'POST':
        girdi = request.json['giris']
        con = connect("stok.db")
        cursor = con.cursor()
        cursor.execute(('SELECT * FROM Teklif WHERE Id=? or Firma=? or Urun=?'), (girdi,girdi,girdi))
        rows = cursor.fetchall()
        con.close()

        return jsonify(rows)

@app.route('/durum_page')
def durum_page():
    if session.get("kadi"):
        kadi = session.get("kadi")
        # Burada aldığımız session verisi kullanılyor.
        return render_template('durum.html',kadi=kadi)
    else:
        return render_template('durum.html',kadi=kadi)
    

@app.route('/api/durum', methods=['GET'])
def get_durum():
    con = connect("stok.db")
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Teklif')
    rows = cursor.fetchall()
    con.close()
    return jsonify(rows)

@app.route('/durum', methods=['POST'])
def durum():
    if request.method == 'POST':
        girdi = request.form['giris']
        durum = request.form['durum']
        
        con = connect("stok.db")
        cursor = con.cursor()

        # SQLite veritabanında güncelleme işlemi
        cursor.execute('UPDATE Teklif SET durum = ? WHERE Firma = ?', (durum, girdi))
        con.commit()  # Güncellemeleri veritabanına kaydet

        con.close()

        return redirect(url_for('durum_page'))


@app.route('/fatura_page')
def fatura_page():
    if session.get("kadi"):
        kadi = session.get("kadi")
        # Burada aldığımız session verisi kullanılyor.
        return render_template('fatura.html',kadi=kadi)
    else:
        return render_template('fatura.html',kadi=kadi)

@app.route('/api/ara', methods=['GET'])
def ara():
    con = connect("stok.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Teklif WHERE Durum='Faturalandı'")
    rows = cursor.fetchall()
    con.close()
    return jsonify(rows)

@app.route('/bul', methods=['POST'])
def bul():
    if request.method == 'POST':
        girdi = request.json['giris']
        con = connect("stok.db")
        cursor = con.cursor()
        cursor.execute(("SELECT * FROM Teklif WHERE Durum='Faturalandı'"), (girdi,girdi,girdi))
        rows = cursor.fetchall()
        con.close()

        return jsonify(rows)

    
if __name__== "__main__":

    app.run(debug=True)