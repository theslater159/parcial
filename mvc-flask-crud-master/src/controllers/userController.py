from flask import render_template, request, redirect, url_for, jsonify
from src import app
from src.models.user import UsuarioModel

@app.route('/usuarios', methods=['GET'])
def usuarios():
    usuarioModel = UsuarioModel()
    usuarios = usuarioModel.listarUser()
    return jsonify({"usuarios":usuarios})

@app.route("/create", methods=["POST"])
def createUser():
    usuarioModel = UsuarioModel()
    request_data = request.get_json()

    nombre = request.json['nombre']
    apellido = request.json['apellido']
    celular = request.json['celular']
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    usuarioModel.crearUser(nombre,apellido,celular,correo,contrasena)

    print("inof------------ ", request_data)
    print(request_data['nombre'])
    return 'OK'

@app.route("/update/<id>",methods=["PUT"])
def apdate(id):
    usuarioModel = UsuarioModel()
    request_data = request.get_json()
    nombre = request_data['nombre']
    apellido = request_data['apellido']
    celular = request_data['celular']
    correo = request_data['correo']
    contrasena = request_data['contrasena']
    usuarioModel.update(id,nombre,apellido,celular,correo,contrasena)
    return "ok"
@app.route("/delete/<id>",methods=["DELETE"])
def deleteUser(id):
    usuarioModel = UsuarioModel()
    usuarioModel.delete(id)
    return "ok"