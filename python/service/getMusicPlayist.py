from pathlib import Path
from service.getMusicList import create_file_info
import const

def get_music_playlist():
    music_list = []
    m3u8_list = []
    folder = Path(const.PLAYLISTS_FOLDER)

    for item in folder.iterdir():
        if item.is_dir():
            for sub_item in item.iterdir():
                if sub_item.is_file() and sub_item.name.endswith(".m3u8"):
                    m3u8_list.append(sub_item)

    for m3u8_item in m3u8_list:
        info = create_file_info(m3u8_item.name[0:-5])
        with open(m3u8_item, "r", encoding="utf-8") as f:
            count = 1
            for line in f:
                name = line.split("/")[-1]
                left = name.find(" ")
                right = name.rfind(".")
                name = "{0:02d}".format(count) + ". " + name[left+1:right]
                count += 1

                info["sub_list"].append(create_file_info(name))
        music_list.append(info)
                    
    return music_list