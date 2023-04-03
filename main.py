# ----------------------------------------------------------------
# O arquivo main.py tem a função de iniciar o servidor Flask. Ele importa a função create_app() do arquivo website/init.py e a executa, atribuindo o resultado à variável app. Em seguida, verifica se o módulo está sendo executado diretamente e, caso positivo, inicia o servidor Flask com a opção debug habilitada.


#senha: Teste@123465, usuário: teste0@gmail.com
# ----------------------------------------------------------------


from website import create_app

def new_func():
    return create_app()

app = new_func()

if __name__ == '__main__':
    app.run(debug=True)