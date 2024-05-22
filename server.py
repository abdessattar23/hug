from hugchat import hugchat

chatbot = hugchat.ChatBot(cookie_path="/something/")
resp = chatbot.chat("Hello")
print(resp)
