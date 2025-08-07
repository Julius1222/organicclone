from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
[PASTE YOUR ENTIRE HTML CODE HERE - the one you showed me in the screenshot]
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
