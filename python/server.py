from flask import Flask, jsonify
from getMusicList import get_music_list
from entity.vo.restBean import RestBean

app = Flask(__name__)

@app.route('/api/getitems', methods=['GET'])
def get_items():
    try:
        data = get_music_list()
        return jsonify(RestBean.success(data))
    except Exception as e:
        return jsonify(RestBean.error(str(e)))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)