from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import os 

load_dotenv()
app = Flask(__name__)
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') 
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

mysql = MySQL(app)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower()in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    erro = None

    if request.method == 'POST':
        titulo = request.form['titulo']
        categoria = request.form['categoria']
        descricao = request.form['descricao']
        data_problema = request.form['data_problema']

        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM bugs WHERE titulo = %s", (titulo,))
        bug_existente = cur.fetchone()
        cur.close()

        if bug_existente:
            erro = "Esse bug já foi reportado e nossa equipe já está trabalhando nele"
        else:
            imagem = None
            file = request.files.get('imagem')
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                imagem = filename

            cur = mysql.connection.cursor()
            cur.execute("""
                INSERT INTO bugs (titulo, categoria, descricao, data_problema, imagem)
                VALUES (%s, %s, %s, %s, %s)
            """, (titulo, categoria, descricao, data_problema, imagem))
            mysql.connection.commit()
            cur.close()

            return redirect(url_for('index', sucesso=1))

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, titulo, categoria, status, data_problema FROM bugs")
    bugs = cur.fetchall()
    cur.close()

    return render_template('index.html', sucesso=request.args.get('sucesso'), bugs=bugs, erro=erro)
@app.route('/admin', methods=['GET'])
def admin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, titulo, categoria, status, data_problema FROM bugs")
    bugs = cur.fetchall()
    cur.close()
    return render_template('admin.html', bugs=bugs)

@app.route('/atualizar-status/<int:id>/<status>')
def atualizar_status(id, status):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE bugs SET status = %s WHERE id = %s", (status, id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
    