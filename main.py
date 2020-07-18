from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user
from app import app, db
from app.models import User, Cliente, Grupo, Categoria, Endereco, Assinante
from werkzeug.security import generate_password_hash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
        user = User(name, email, pwd)
        db.session.add(user)
        db.session.commit()
        flash('Usuario adicionado com sucesso!')
        return redirect(url_for('usuario'))
    
    return render_template('register.html')

    
@app.route('/edit_register/<int:user_id>', methods=['GET', 'POST'])
def edit_register(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.password = generate_password_hash(request.form['password'])
        db.session.commit()
        flash('Usuario alterado com sucesso!')
        return redirect(url_for('usuario'))
    else:
        users = User.query.all()
        return render_template('edit_register.html', user=user, users=users)
 
@app.route('/delete_register/<int:user_id>', methods=['GET', 'POST'])
def delete_register(user_id):
    users = User.query.all()
    if request.method == 'GET':
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        flash('Usuario apagado com sucesso!')
        return redirect(url_for('usuario'))
    return render_template('usuario.html', users=users)
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        user = User.query.filter_by(email=email).first()
        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
             
    return render_template('login.html')

@app.route('/add_cliente', methods=['GET', 'POST'])
def add_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        cidade = request.form['cidade']
        telefone = request.form['telefone']
        celular = request.form['celular']
        email = request.form['email']
        cliente = Cliente(nome, cidade, telefone, celular, email)
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente adicionado com sucesso!')
        return redirect(url_for('cliente'))
    
    return render_template('add_cliente.html')
 

@app.route('/edit_cliente/<int:cliente_id>', methods=['GET', 'POST'])
def edit_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.cidade = request.form['cidade']
        cliente.telefone = request.form['telefone']
        cliente.celular = request.form['celular']
        cliente.email = request.form['email']
        db.session.commit()
        flash('Cliente alterado com sucesso!')
        return redirect(url_for('cliente'))
    else:
        clientes = Cliente.query.all()
        return render_template('edit_cliente.html', cliente=cliente, clientes=clientes)
 

@app.route('/delete_cliente/<int:cliente_id>', methods=['GET', 'POST'])
def delete_cliente(cliente_id):
    clientes = Cliente.query.all()
    if request.method == 'GET':
        cliente = Cliente.query.get_or_404(cliente_id)
        db.session.delete(cliente)
        db.session.commit()
        flash('Cliente apagado com sucesso!')
        return redirect(url_for('cliente'))
    return render_template('cliente.html', clientes=clientes)
  

@app.route('/usuario')
def usuario():
    users = User.query.all()
    return render_template('usuario.html', users=users)
    
@app.route('/cliente')
def cliente():
    clientes = Cliente.query.all()
    return render_template('cliente.html', clientes=clientes)
   

@app.route('/grupo')
def grupo():
    grupos = Grupo.query.all()
    return render_template('grupo.html', grupos=grupos)
    
@app.route('/assinante')
def assinante():
    assinantes = Assinante.query.all()
    return render_template('assinante.html', assinantes=assinantes)

   
@app.route('/add_grupo', methods=['GET', 'POST'])
def add_grupo():
    if request.method == 'POST':
        nome = request.form['nome']
        grupo = Grupo(nome)
        db.session.add(grupo)
        db.session.commit()
        flash('Grupo adicionado com sucesso!')
        return redirect(url_for('grupo'))
    
    return render_template('add_grupo.html')
   
  
@app.route('/edit_grupo/<int:grupo_id>', methods=['GET', 'POST'])
def edit_grupo(grupo_id):
    grupo = Grupo.query.get_or_404(grupo_id)
    if request.method == 'POST':
        grupo.nome = request.form['nome']
        db.session.commit()
        flash("Grupo alterado com sucesso!")
        return redirect(url_for('grupo'))
    else:
        grupos = Grupo.query.all()
        return render_template('edit_grupo.html', grupo=grupo, grupos=grupos)

  
@app.route('/delete_grupo/<int:grupo_id>', methods=['GET', 'POST'])
def delete_grupo(grupo_id):
    grupos = Grupo.query.all()
    if request.method == 'GET':
        grupo = Grupo.query.get_or_404(grupo_id)
        db.session.delete(grupo)
        db.session.commit()
        flash("Grupo apagado com sucesso!")
        return redirect(url_for('grupo'))
    return render_template('add_grupo.html', grupos=grupos)
   
 
@app.route('/categoria')
def categoria():
    categorias = Categoria.query.all()
    return render_template('categoria.html', categorias=categorias)
 
 
@app.route('/add_categoria', methods=['GET', 'POST'])
def add_categoria():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = Categoria(nome)
        db.session.add(categoria)
        db.session.commit()
        flash('Categoria adicionada com sucesso!')
        return redirect(url_for('categoria'))
    
    return render_template('add_categoria.html')
 
 
@app.route('/edit_categoria/<int:categoria_id>', methods=['GET', 'POST'])
def edit_categoria(categoria_id):
    categoria = Categoria.query.get_or_404(categoria_id)
    if request.method == 'POST':
        categoria.nome = request.form['nome']
        db.session.commit()
        flash("Categoria alterada com sucesso!")
        return redirect(url_for('categoria'))
    else:
        categorias = Categoria.query.all()
        return render_template('edit_categoria.html', categoria=categoria, categorias=categorias)
 
 
@app.route('/delete_categoria/<int:categoria_id>', methods=['GET', 'POST'])
def delete_categoria(categoria_id):
    categorias = Categoria.query.all()
    if request.method == 'GET':
        categoria = Categoria.query.get_or_404(categoria_id)
        db.session.delete(categoria)
        db.session.commit()
        flash("Categoria apagada com sucesso!")
        return redirect(url_for('categoria'))
    return render_template('add_categoria.html', categorias=categorias)
 
 
@app.route('/endereco')
def endereco():
    enderecos = Endereco.query.all()
    return render_template('endereco.html', enderecos=enderecos)
 
 
 
@app.route('/add_endereco', methods=['GET', 'POST'])
def add_endereco():
    if request.method == 'POST':
        endereco = request.form['endereco']
        numero = request.form['numero']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cep = request.form['cep']
        endereco = Endereco(endereco, numero, bairro, cidade, estado, cep)
        db.session.add(endereco)
        db.session.commit()
        flash('Endereco adicionado com sucesso!')
        return redirect(url_for('endereco'))
    
    return render_template('add_endereco.html')
 
 
@app.route('/edit_endereco/<int:endereco_id>', methods=['GET', 'POST'])
def edit_endereco(endereco_id):
    endereco = Endereco.query.get_or_404(endereco_id)
    if request.method == 'POST':
        endereco.endereco = request.form['endereco']
        endereco.numero = request.form['numero']
        endereco.bairro = request.form['bairro']
        endereco.cidade = request.form['cidade']
        endereco.estado = request.form['estado']
        endereco.cep = request.form['cep']
        db.session.commit()
        flash('Endereco alterado com sucesso!')
        return redirect(url_for('endereco'))
    else:
        enderecos = Endereco.query.all()
        return render_template('edit_endereco.html', endereco=endereco, enderecos=enderecos)
 
 
 
@app.route('/delete_endereco/<int:endereco_id>', methods=['GET', 'POST'])
def delete_endereco(endereco_id):
    enderecos = Endereco.query.all()
    if request.method == 'GET':
        endereco = Endereco.query.get_or_404(endereco_id)
        db.session.delete(endereco)
        db.session.commit()
        flash("Endereco apagado com sucesso!")
        return redirect(url_for('endereco'))
    return render_template('add_endereco.html', enderecos=enderecos)
 


@app.route('/add_assinante', methods=['GET', 'POST'])
def add_assinante():
    grupos = Grupo.query.all()
    categorias = Categoria.query.all()
    enderecos = Endereco.query.all()
    if request.method == 'POST':
        grupo = request.form['grupo']
        categoria = request.form['categoria']
        endereco = request.form['endereco']
        codigo_assinante = request.form['codigo_assinante']
        nome = request.form['nome']
        telefone = request.form['telefone']
        celular = request.form['celular']
        email = request.form['email']
        assinante = Assinante(grupo, categoria, endereco, codigo_assinante, nome, telefone, celular, email)
        db.session.add(assinante)
        db.session.commit()
        flash('Assinante adicionado com sucesso!')
        return redirect(url_for('assinante'))
    
    return render_template('add_assinante.html', grupos=grupos,
                                                 categorias=categorias,
                                                 enderecos=enderecos)



                                                 
@app.route('/edit_assinante/<int:assinante_id>', methods=['GET', 'POST'])
def edit_assinante(assinante_id):
    grupos = Grupo.query.all()
    categorias = Categoria.query.all()
    enderecos = Endereco.query.all()
    assinante = Assinante.query.get_or_404(assinante_id)
    if request.method == 'POST':
        assinante.grupo_id = request.form['grupo']
        assinante.categoria_id = request.form['categoria']
        assinante.endereco_id = request.form['endereco']
        assinante.codigo_assinante = request.form['codigo_assinante']
        assinante.nome = request.form['nome']
        assinante.telefone = request.form['telefone']
        assinante.celular = request.form['celular']
        assinante.email = request.form['email']
        db.session.commit()
        flash('Assinante alterado com sucesso!')
        return redirect(url_for('assinante'))
    else:
        assinantes = Assinante.query.all()
        return render_template('edit_assinante.html', grupos=grupos,
                                                      categorias=categorias,
                                                      enderecos=enderecos,
                                                      assinante=assinante,
                                                      assinantes=assinantes)                                                 
                                                 
                                                 
@app.route('/delete_assinante/<int:assinante_id>', methods=['GET', 'POST'])
def delete_assinante(assinante_id):
    assinantes = Assinante.query.all()
    if request.method == 'GET':
        assinante = Assinante.query.get_or_404(assinante_id)
        db.session.delete(assinante)
        db.session.commit()
        flash('Assinante apagado com sucesso!')
        return redirect(url_for('assinante'))
    return render_template('assinante.html', assinantes=assinantes)

                                                 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
    
app.run(debug=True)