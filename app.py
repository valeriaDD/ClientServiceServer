import logging

from flask import Flask


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')



@app.route("/")
def miaw():
    return "Hello from clientService server"


if __name__ == '__main__':
    app.run(debug=True, port=5002, host="0.0.0.0")