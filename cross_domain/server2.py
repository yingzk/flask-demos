from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, source=r'/*', supports_credentials=True)


@app.route('/api', methods=['POST'])
def api():
    return jsonify({'name': 'ying'})


if __name__ == '__main__':
    app.run(port=5001)
