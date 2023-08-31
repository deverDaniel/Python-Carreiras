from flask import Flask, render_template, jsonify

app = Flask(__name__)

vagas = [
  {
    "id": 1,
    "titulo": "analista de sistemas",\
    "localidade": "Curitiba",
    "salario": "5.000$"
  },
  {
    "id": 2,
    "titulo": "analista de dados",\
    "localidade": "Curitiba",
    "salario": "3.000$"
  },
  {
    "id": 3,
    "titulo": "cientista de dados",\
    "localidade": "Curitiba",
    "salario": "7.000$"
  },
  {
    "id": 4,
    "titulo": "Desenvolvedor backend",\
    "localidade": "Curitiba",
    "salario": "10.000$"
  },
{
    "id": 5,
    "titulo": "Desenvolvedor frontend",\
    "localidade": "são paulo",
    "salario": "6.000$"
  }
]

@app.route("/")
def hello():
  return render_template("home.html", vagas= vagas)
@app.route("/vagas")
def Lista_Vagas():
  return jsonify(vagas)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
