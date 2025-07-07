from flask import Flask, render_template, request, send_file
from app.contrato_generator import generar_contrato
from num2words import num2words

from app import app 

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        datos = request.form.to_dict()
        pdf_file = generar_contrato(datos)
        return send_file(pdf_file, as_attachment=True)
    return render_template('formulario.html')

@app.route('/num2words/<numero>')
def convertir_numero(numero):
    try:
        numero_int = int(numero)
        en_letras = num2words(numero_int, lang='es').upper()
        return en_letras
    except:
        return "CANTIDAD INVALIDA"
