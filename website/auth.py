
# ----------------------------------------------------------------
# README: 

# A primeira rota /login permite que o usuário faça login com seu email e senha.Se o email e a senha inseridos estiverem corretos, o usuário é redirecionado para a página inicial, caso contrário, uma mensagem de erro é exibida na página de login. 

# A segunda rota /logout permite que o usuário faça logout do sistema. 

# A terceira rota /sign-up permite que o usuário crie uma nova conta fornecendo seu email, primeiro nome, sobrenome, CPF e senha. Se todos os campos estiverem corretos e o email ainda não estiver registrado, uma nova conta é criada e o usuário é redirecionado para a página inicial. Caso contrário, uma mensagem de erro é exibida na página de inscrição.
# ----------------------------------------------------------------


from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# Callback de autenticação de Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password, password):
                flash('Você está logado!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Senha incorreta, tente novamente.', category='error')
        else:
            flash('E-mail não encontrado.', category='error')
            
    return render_template("login.html", user=current_user)
# Callback de Logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

# Callback de Inscrição na plataforma
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstname')
        secondName = request.form.get('secondname')
        cpf = request.form.get('cpf')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email já cadastrado.', category='error')
        elif len(email) < 4:
            flash('O email deve estar completo', category='error')
        elif len(first_name) < 2:
            flash('O Primeiro nome deve estar completo', category='error')
        elif len(secondName) < 2:
            flash('O sobrenome deve estar completo', category='error')
        elif password1 != password2:
            flash('Erro: A segunda senha deve ser igual a primeira.', category='error')
        elif len(password1) < 7:
            flash('Inválido: A senha deve possuir mais que 6 caracteres.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Seja bem vindo(a)! Sua conta foi criada com sucesso!', category='success')
            # Adiciona o usuário à Base de dados
            return redirect(url_for('views.home'))
        
    return render_template("sign_up.html", user=current_user)