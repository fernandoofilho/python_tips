from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/OlaMundo", methods= ["GET"])
def tirar_tinta():
    return ("""
            <h1>modelo de input</h1>
            <input type="text" value= "input seu nome"/> 
            <h2> Tente voce agora! </h2>    
            """   
)