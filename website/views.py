
#----------------------------------------------------------------
# views.py é responsável por definir as rotas para a página principal ('/') e a função home() é executada quando o usuário acessa essa rota.

#A função home() é decorada com o login_required, o que significa que apenas usuários autenticados podem acessar essa rota. Isso é importante para garantir a segurança e a privacidade dos dados do usuário.

#Se a requisição HTTP for do tipo POST, a função home() verifica se a postagem feita pelo usuário não está vazia e se não excede 250 caracteres. Se a postagem estiver dentro desses limites, uma nova nota é adicionada ao banco de dados.

#Por outro lado, se a requisição HTTP for do tipo DELETE, a função home() recebe o ID da nota que o usuário deseja excluir e a nota correspondente é removida do banco de dados.

#No final, a função home() retorna a página HTML "home.html", que será renderizada com a ajuda do Flask. É nessa página que o usuário poderá ver as notas postadas, adicionar novas notas ou excluir as existentes.

# ----------------------------------------------------------------

from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, current_user
from .models import Note
from . import db



views = Blueprint('views', __name__)


# Callback para postage redigida / respostas
@views.route('/', methods=['GET', 'POST', 'DELETE'])
@login_required
def home():
    indice = 13
    soma = sum(range(1, indice + 1))
    
    new_note= ""
    if request.method == 'POST' and request.form.get('note') is not None:
        note = request.form.get('note')
        if note is not None and len(note) < 1:
            flash('Você não pode fazer uma postagem vazia!', category = 'error')
        elif len(note) > 250:
            flash('A postagem é muito longa.', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('A nota foi postada com sucesso', category='success')
    elif request.method == 'DELETE':
        note_id = request.args.get('id')
        if note_to_delete == Note.query.filter_by(
            id=note_id, user_id=current_user.id
        ).first():
            db.session.delete(note_to_delete)
            db.session.commit()
            flash('Nota excluída com sucesso.', category='success')
        else:
            flash('Não foi possível excluir a nota.', category='error')
            
            
    numpi= ""
    new_numpi = ""
    if request.method == "POST":
        numpi = request.form["numpi"]
        if not numpi:
            flash('Digite um número válido.', category='error')
        elif numpi = None:
            flash('Digite algum número inteiro!', category='error')
        elif not numpi.isnumeric():
            flash('Digite apenas números.', category='error')
        elif numpi < 0:
            flash('Digite um número inteiro.', category='error')            
        else:
            fibs = [0, 1]
            while fibs[-1] < int(numpi):
                fibs.append(fibs[-1] + fibs[-2])
            if int(numpi) in fibs:
                flash(
                    f'O número {numpi} está presente na sequência de Fibonacci',
                    category='success',
                )
                new_numpi = f"O número {numpi} foi encontrado na sequência de Fibonacci"
            else:
                flash(
                    f'O número {numpi} não está presente na sequência de Fibonacci!',
                    category='error',
                )
                new_numpi = f"O número {numpi} não foi encontrado na sequência de Fibonacci!"


    impares = []
    n = request.args.get('numero')
    if n is not None:
        n=int(n)
        impares.extend(i for i in range(1, n+1) if i % 2 != 0)
    sequencia = []
    numero = request.args.get('numeroseq')
    if numero is not None:
        numero = int(numero)
        sequencia = [2 ** i for i in range(numero) if 2 ** i > 1 and 2 ** i <= numero]
        sequencia = [x for x in sequencia if x <= numero]



    seqsomaimpar = []
    numseq = request.args.get('numseq')
    if numseq is not None:
        numseq = int(numseq)
        seqsomaimpar = [i**2 for i in range(numseq+1)]
        seqsomaimpar = [x for x in seqsomaimpar if x <= numseq]



    seqmultdois = []
    multip = request.args.get('multdois')
    if multip is not None:
        multip = int(multip)
        seqmultdois = [i**2 for i in range(2, multip+1, 2)]
        seqmultdois = [x for x in seqmultdois if x <= multip] 


    somaresanterior = [0,1]
    valor = request.args.get('somanterior')
    if valor is not None:
        valor = int(valor)
        i = 0
        while i < len(somaresanterior)-1 and somaresanterior[i+1] <= valor:
            if i < len(somaresanterior):
                somaresanterior.append(somaresanterior[i] + somaresanterior[i+1])
            else:
                break
            somaresanterior = [x for x in somaresanterior if x <= valor]
            i += 1
    seq = [2]
    increment = 8
    num_range_primo = request.args.get('numrangeprimo')
    if num_range_primo is not None:
        num_range_primo = int(num_range_primo)
        last_num = 2
        while last_num < num_range_primo:
            last_num += increment
            seq.append(last_num)
            if increment == 8:
                increment = 2
            elif increment == 2:
                increment = 4
            else:
                increment = 1


    velocidade_carro = request.args.get('velcarro') # km/h
    velocidade_caminhao = request.args.get('velcaminhao') # km/h
    resultado = str()
    if velocidade_caminhao is not None and velocidade_carro is not None:
        velocidade_caminhao = int(velocidade_caminhao)
        velocidade_carro = int(velocidade_carro)
        distancia_total = 100 # km
        tempo_sem_pedagios = distancia_total / (velocidade_carro + velocidade_caminhao) # horas
        distancia_carro = velocidade_carro * tempo_sem_pedagios # km
        distancia_caminhao = velocidade_caminhao * tempo_sem_pedagios # km
        # leva 5 minutos a mais para o caminhão passar em cada pedágio
        tempo_pedagios = 0.0833 # horas
        distancia_caminhao -= velocidade_caminhao * tempo_pedagios * 2 # km (2 pedágios)
        # distância em que o carro e o caminhão se cruzam
        distancia_cruzamento = (velocidade_carro * distancia_total) / (velocidade_carro + velocidade_caminhao)
        if distancia_carro < distancia_cruzamento:
            resultado = 'O carro está mais próximo de Ribeirão Preto'
            flash('O carro está mais próximo de Ribeirão Preto', category='success')
        else:
            resultado = 'O caminhão e o carro estão à mesma distância de Ribeirão Preto ao se cruzarem.'
            flash('O caminhão e o carro estão à mesma distância de Ribeirão Preto ao se cruzarem.', category='success')
        resultado += f' - Distância de cruzamento: {distancia_cruzamento:.2f} km'
    else:
        resultado = 'Por favor, informe as velocidades do carro e do caminhão.'


    texto_invertido = request.args.get('invertestring')
    if texto_invertido is not None:
        texto_invertido = str(texto_invertido)
        caracteres = list(texto_invertido)
        indice_final = len(caracteres) - 1
        for x in range(len(caracteres)//2):
            aux = caracteres[x]
            caracteres[x] = caracteres [indice_final - x]
            caracteres[indice_final - x] = aux
        texto_invertido = ''.join(caracteres)
    return render_template("/home.html", user=current_user, soma=str(soma), new_numpi=new_numpi, new_note=new_note, impares=impares, sequencia=sequencia, seqsomaimpar=seqsomaimpar, seqmultdois=seqmultdois, somaresanterior=somaresanterior, seq=seq, resultado=resultado, texto_invertido=texto_invertido)
