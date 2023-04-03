# ----------------------------------------------------------------
# O arquivo __init__.py é o arquivo principal da aplicação, que inicializa e configura a aplicação Flask, além de registrar as blueprints e modelos da aplicação.

# O arquivo começa importando o Flask e outros módulos necessários, incluindo SQLAlchemy para trabalhar com banco de dados. 

# Ele também define uma constante DB_NAME com o nome do arquivo de banco de dados.

# A função create_app() é usada para criar e configurar a aplicação Flask. Nesta função, a aplicação é instanciada, as configurações são definidas e o objeto db é inicializado com a aplicação.

# As blueprints são registradas na aplicação dentro da função create_app(). As blueprints são módulos que contêm rotas e views para partes específicas da aplicação, neste caso, as rotas para a autenticação e para as notas (posts).

# O modelo de usuário e de nota (post) também são importados no arquivo e criados no banco de dados. A função create_database() é usada para criar o banco de dados se ele ainda não existir.

# Por fim, o LoginManager é inicializado e configurado para gerenciar o login do usuário. A função load_user() é usada para carregar o usuário atual a partir do banco de dados, com base no seu ID armazenado em um cookie seguro.
# ----------------------------------------------------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "db_dados.db"

def create_app():
    
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'Bcbr11@#'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    db.init_app(app)
    
    
    from .views import views
    from .auth import auth
    
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

        
    from .models import User, Note
    
    with app.app_context():
        create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    with app.app_context():
        if not path.exists('website' + DB_NAME):
            db.create_all(),
            print('O Database foi criado com sucesso!')
            




# end def

