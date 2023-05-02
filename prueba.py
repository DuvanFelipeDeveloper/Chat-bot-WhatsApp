import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import json

# Leer datos desde el archivo JSON
with open('datos.json', 'r') as f:
    data = json.load(f)

# Almacenar los datos en las variables correspondientes
questions = data['questions']
answers = data['answers']


question_tokens = [nltk.word_tokenize(question.lower()) for question in questions]
answer_tokens = [nltk.word_tokenize(answer.lower()) for answer in answers]


documents = [' '.join(token_list) for token_list in question_tokens + answer_tokens]


vectorizer = TfidfVectorizer()


features = vectorizer.fit_transform(documents)



def find_closest_answer(question):

    question_tokens = nltk.word_tokenize(question.lower())


    question_features = vectorizer.transform([' '.join(question_tokens)])
    

    similarities = cosine_similarity(question_features, features)
    


    closest = np.argmax(similarities)



    if closest < len(answers):

        return answers[closest]
    else:

        return "Lo siento, no pude encontrar una respuesta para esa pregunta."

question = 'dieta para una persona ectomorfo'
answer = find_closest_answer(question)
print(answer)
