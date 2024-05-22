from hugchat import hugchat
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def receive():
  chatbot = hugchat.ChatBot(cookie_path="/something/", default_llm=2)
  d = request.json
  query = d.get('prompt')
  resp = chatbot.chat(query).wait_until_done().strip()
  return resp
@app.route('/chat', methods=['GET'])
def normal():
  chatbot = hugchat.ChatBot(cookie_path="/something/", default_llm=2)
  query = request.args.get('prompt')
  resp = chatbot.chat(query).wait_until_done().strip()
  return resp
@app.route('/ok', methods=['GET'])
def s():
  ok = "ok"
  return ok
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
