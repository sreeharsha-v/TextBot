# TextBot
# Text Indexing and Question-Answering Web Service

This project is a Flask-based web service that combines text indexing and natural language processing to provide answers to user questions. It uses the Langchain library for text indexing and the OpenAI API for language processing.

## Features

- Text indexing and retrieval system for efficient information retrieval from text datasets.
- API endpoint for answering questions using the indexed data.
- Integration with the OpenAI library for natural language processing.
- A simple web interface for serving static HTML content.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/sreeharsha-v/TextBot.git
   cd TextBot


2. Install all the python library requirements for the project using pip install globally which i have provided in the main.py file. For chromadb library you have to install microsoft visual studio c++ tools and you have do pip install chromadb by using command prompt in administrator mode.

3. Use the OpenAi api key of your own in the python main.py file.

Usage

     Access the web interface by navigating to http://localhost:5000/ in your web browser. You can use this interface to ask questions and receive answers.
     Use the API endpoint to programmatically retrieve answers by sending a GET request to http://localhost:5000/api/answer?question=your_question.

Project Structure

     app.py: The main Flask application.
     static/: Contains the static HTML file (index.html) served by the application.
     C:/MEAN-STACK/backend/Store/: This is where you can place your text data files for indexing. Make sure the files are in the .txt format.

Dependencies

     Flask: Web framework for creating the application.
     Langchain: Library for text indexing and retrieval.
     OpenAI: Library for natural language processing.
     Flask-CORS: Extension for enabling Cross-Origin Resource Sharing.


Contributing

     Feel free to open issues and pull requests for any improvements or suggestions you may have.

Acknowledgments

     This project was created with the aim of demonstrating text indexing, question-answering capabilities, and web development skills.
