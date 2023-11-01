# !pip install langchain
# !pip install openai
# !pip install chromadb
# !pip install tiktoken
# !pip install flask
# !pip install flask-cors


from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import OpenAIEmbeddings
import os


app = Flask(__name__)
CORS(app)

# Set the OpenAI API key as an environment variable
os.environ['OPENAI_API_KEY'] = 'PLACE YOUR OPENAI API KEY HERE'

# Initialize OpenAIEmbeddings with the API key
embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])

# Folder containing your text files
folder_path = 'C:/MEAN-STACK/backend/Store'

# Create a list to hold TextLoader instances
text_loaders = []

# Loop through files in the folder and create TextLoader instances
for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        text_loader = TextLoader(file_path, encoding='utf-8')
        text_loaders.append(text_loader)

# Create an index using VectorstoreIndexCreator and the list of TextLoader instances
index = VectorstoreIndexCreator().from_loaders(text_loaders)

@app.route('/')
def serveIndex():
    return send_from_directory(os.path.dirname(__file__), 'index.html');

@app.route('/api/answer', methods=['GET'])
def get_answer():
    question = request.args.get('question')
    # question="who piloted the census act";
    if question:
        results = index.query(question)
        # Assuming you have some logic here to choose the best answer from results
        # This example just uses the first result
        best_answer = results;
        return jsonify({'answer': best_answer})
    else:
        return jsonify({'error': 'Question not provided'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

    
