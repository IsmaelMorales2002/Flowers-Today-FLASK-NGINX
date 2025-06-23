from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/home/ec2-user/uploads' 

@app.route('/usuario/',methods=['POST'])
def usuario():
    if 'file' not in request.files:
        return 'No se encontro el archivo en la solicitud',400
    file = request.files['file']
    if file.filename == '':
        return 'No se selecciono ningún archivo',400
    file.save(os.path.join(UPLOAD_FOLDER,file.filename))
    return 'Fotografia de Usuario Subida Exitosamente',200

@app.route('/producto/',methods=['POST'])
def producto():
    if 'file' not in request.files:
        return 'No se encontro el archivo en la solicitud',400
    file = request.files['file']
    if file.filename == '':
        return 'No se selecciono ningún archivo',400
    file.save(os.path.join(UPLOAD_FOLDER,file.filename))
    return 'Fotografia de Producto Subida Exitosamente',200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)