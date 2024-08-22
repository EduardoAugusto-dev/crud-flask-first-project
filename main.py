from flask import Flask
from config import general_config

#inicializa o flask
app = Flask(__name__)

general_config(app)

#executa
app.run(debug=True, port=5001)


