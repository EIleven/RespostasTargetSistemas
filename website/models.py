# ----------------------------------------------------------------
# O "models.py" é responsável por definir a estrutura do banco de dados utilizado na aplicação. 

# O SQLAlchemy é uma biblioteca em Python que fornece um ORM (Object-Relational Mapping) para trabalhar com bancos de dados relacionais, como o SQLite, que é usado nessa aplicação.

# A classe Note define a estrutura da tabela "Note" no banco de dados. A tabela "Note" possui uma coluna "id" que é uma chave primária, uma coluna "data" que armazena o texto da nota, uma coluna "date" que armazena a data e hora em que a nota foi criada, e uma coluna "user_id" que é uma chave estrangeira que referencia a tabela "User".

# A classe User define a estrutura da tabela "User" no banco de dados. A tabela "User" possui uma coluna "id" que é uma chave primária, uma coluna "email" que armazena o email do usuário, uma coluna "password" que armazena a senha do usuário, uma coluna "first_name" que armazena o primeiro nome do usuário, uma coluna "second_name" que armazena o sobrenome do usuário, uma coluna "cpf" que armazena o CPF do usuário e uma relação "notes" que representa uma lista de notas pertencentes a esse usuário.

# importamos de website a variável db que carrega o database.db
# flask_login é um módulo que ajuda na função de autenticação de login // Existem outros módulos que devem ser explorados
# ----------------------------------------------------------------
from flask_login import UserMixin
from sqlalchemy.sql import func
from website import db
from . import db

# Note é o objeto Note. É ele que manipulamos quando falamos das "postagens"

    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
# User também é um objeto e cada Note deve estar vinculada ao seu User de origem/ criador
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    second_name = db.Column(db.String(150))
    cpf = db.Column(db.String(150), unique = True)
    notes = db.relationship('Note')
