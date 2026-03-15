from flask import Flask, jsonify
from getMusicList import get_music_list

app = Flask(__name__)

@app.route('/api/getitems', methods=['GET'])
def get_items():
    return jsonify(get_music_list())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)