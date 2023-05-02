from flask import Flask, request
from prueba import find_closest_answer
from flask_cors import CORS
import re
import json

app = Flask(__name__)
                                                                                                                                                                                                                                          
CORS(app)

# Código de importación y definición de funciones

@app.route('/answer', methods=['GET'])
def get_answer(question):
    question = request.args.get('question')
    line = question
    match = re.match(r'EPR:\((.*?)\) \((.*?)\)', line)
    if match:
        with open('datos.json', 'r') as f:
            data = json.load(f)
        question = match.group(1)
        answerdata = match.group(2)
        data['questions'].append(question)
        data['answers'].append(answerdata)
        with open('datos.json', 'w') as f:
            json.dump(data, f)
        answer = "Se agrego correctamente."
    else:
        answer = find_closest_answer(question)
    return answer



@app.route('/api', methods=['GET'])
def api():
    question = request.args.get('question')
    answer = get_answer(question)
    return {'answer': answer}


