from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql


pymysql.install_as_MySQLdb()


#Inicializa a aplicação Flask
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'  # Endereço do seu servidor MySQL
app.config['MYSQL_USER'] = 'root'       # Seu usuário do MySQL
app.config['MYSQL_PASSWORD'] = 'templa'  # Sua senha do MySQL
app.config['MYSQL_DB'] = 'teste'         # O nome do banco de dados

#Configurações de conexão ao MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:templa@localhost/teste'  # Altere para seu usuário, senha e banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#Modelo da tabela Produto
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(255))

    def repr(self):
        return f'<Produto {self.nome}>'

#Rota principal que consulta e exibe os produtos
@app.route('/')
def index():
    # Consulta todos os produtos da tabela
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos)

@app.route('/pesquisar-produto', methods=['GET', 'POST'])
def pesquisar_produto():
    produto = None
    if request.method == 'GET':
        product_id = request.args.get('productId')  # Obtém o ID do produto do formulário
        if product_id:
            produto = Produto.query.filter_by(id=product_id).first()  # Consulta o produto pelo ID
    return render_template('index.html', produto=produto)

    if produto:
        return render_template('produto.html', produto=produto)
    else:
        return f'Produto com ID {product_id} não encontrado.', 404


if __name__ == 'main':
    app.run(debug=True)