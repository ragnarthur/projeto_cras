from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from datetime import datetime
from models import db, User, Filho, Conjuge
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cras_users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sua_chave_secreta_aqui'

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(
            nome=request.form['nome'].upper(),
            data_nascimento=datetime.strptime(request.form['data_nascimento'], '%Y-%m-%d'),
            estado_civil=request.form['estado_civil'],
            rua=request.form['rua'].upper(),
            numero=int(request.form['numero']),
            bairro=request.form['bairro'].upper(),
            rg=request.form['rg'],
            cpf=request.form['cpf'],
            telefone=request.form['telefone'],
            tem_filho='tem_filho' in request.form,
            gestante='gestante' in request.form,
            retirada_cesta=datetime.strptime(request.form['retirada_cesta'], '%Y-%m-%d') if 'retirada_cesta' in request.form else None
        )
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id

        if request.form.get('tem_filho', 'off') == 'on':
            return redirect(url_for('register_filhos'))
        if request.form['estado_civil'] == 'casado':
            return redirect(url_for('register_conjuge'))

        return redirect(url_for('success'))
    return render_template('register.html')

@app.route('/register/conjuge', methods=['GET', 'POST'])
def register_conjuge():
    user_id = session.get('user_id')
    if not user_id:
        return "Nenhum usuário selecionado para adicionar cônjuge.", 400

    if request.method == 'POST':
        conjuge = Conjuge(
            nome=request.form['nome_conjuge'].upper(),
            cpf=request.form['cpf_conjuge'],
            rg=request.form['rg_conjuge'],
            data_nascimento=datetime.strptime(request.form['data_nascimento_conjuge'], '%Y-%m-%d'),
            user_id=user_id
        )
        db.session.add(conjuge)
        db.session.commit()
        return redirect(url_for('users'))

    return render_template('register_conjuge.html', user_id=user_id)

@app.route('/register/filhos', methods=['GET', 'POST'])
def register_filhos():
    user_id = session.get('user_id')
    if not user_id:
        return "Nenhum usuário selecionado para adicionar filhos.", 400

    if request.method == 'POST':
        for i in range(len(request.form.getlist('nome[]'))):
            filho = Filho(
                nome=request.form.getlist('nome[]')[i].upper(),
                cpf=request.form.getlist('cpf[]')[i],
                rg=request.form.getlist('rg[]')[i],
                user_id=user_id
            )
            db.session.add(filho)
        db.session.commit()
        return redirect(url_for('users'))

    return render_template('register_filhos.html', user_id=user_id)

@app.route('/users')
def users():
    all_users = User.query.options(db.joinedload(User.filhos), db.joinedload(User.conjuge)).order_by(User.nome).all()
    return render_template('users.html', users=all_users)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.nome = request.form['nome']
        user.data_nascimento = datetime.strptime(request.form['data_nascimento'], '%Y-%m-%d')
        user.estado_civil = request.form['estado_civil']
        user.telefone = request.form['telefone']
        user.rua = request.form['rua']
        user.numero = int(request.form['numero'])
        user.bairro = request.form['bairro']
        user.rg = request.form['rg']
        user.cpf = request.form['cpf']
        user.tem_filho = 'tem_filho' in request.form
        user.numero_filhos = int(request.form['numero_filhos']) if user.tem_filho and request.form['numero_filhos'] else 0
        user.gestante = 'gestante' in request.form
        user.retirada_cesta = datetime.strptime(request.form['retirada_cesta'], '%Y-%m-%d') if 'retirada_cesta' in request.form else None
        db.session.commit()
        return redirect('/users')
    return render_template('edit_user.html', user=user)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "Usuário não encontrado"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuário excluído com sucesso"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
