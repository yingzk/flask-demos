from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='./')
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
# CORS(app, source=r'/*', supports_credentials=True)


@app.route('/api', methods=['POST'])
def api():
    return jsonify({'name': 'ying'})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
