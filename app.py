import os

from flask import Flask
app = Flask(__name__)

ENV = os.environ.get("FLASK_ENV")

@app.route('/')
def hello_world():
    return '<font size=\'20pt\'> Hello world is running in : <font color=\'red\'>' + ENV + '</font> mode. </font>'
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
