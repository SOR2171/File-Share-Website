from flask import Flask, jsonify
from entity.vo.restBean import RestBean

from service import getMusicList, getMusicPlayist

app = Flask(__name__)

@app.route('/api/get-items', methods=['GET'])
def get_items():
    try:
        data = getMusicList.get_music_list()
        return jsonify(RestBean.success(data))
    except Exception as e:
        return jsonify(RestBean.error(str(e)))

@app.route('/api/get-playlists', methods=['GET'])
def get_playlist():
    try:
        data = getMusicPlayist.get_music_playlist()
        return jsonify(RestBean.success(data))
    except Exception as e:
        return jsonify(RestBean.error(str(e)))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)