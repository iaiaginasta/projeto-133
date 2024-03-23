# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Iasmin" 
    idade = "15" 

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def pai():
    name = "pai"
    return render_template("pai.html", index_variable = name)

# defina a rota para a página da mãe
@app.route("/mae")
def mae():
    name = "mae"
    return render_template("mae.html", index_variable = name)

# defina a rota para a página do amigo

@app.route("/amigo")
def amigo():
    name = "amigo"
    return render_template("amigo.html", index_variable = name)
# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
