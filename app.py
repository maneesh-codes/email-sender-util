from flask import Flask, request
from utils import mail

app = Flask(__name__)

@app.route(rule='/email', methods=['POST'])
def send_mail():
    print(request.get_json())
    content = request.get_json()['content']
    to = request.get_json()['to']
    print(">>>",content, to)
    mail(to=to, content=content)

    
    return 'ok'


if __name__ == "__main__":
    app.run(debug=True, port=3000, host='0.0.0.0')
