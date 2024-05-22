from hugchat import hugchat
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def receive():
  chatbot = hugchat.ChatBot(cookie_path="/something/")
  d = request.json
  query = d.get('prompt')
  resp = chatbot.query(query)
  return resp
@app.route('/chat', methods=['GET'])
def normal():
  chatbot = hugchat.ChatBot(cookie_path="/something/")
  query = request.args.get('prompt')
  resp = chatbot.query(query)
  return resp
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
