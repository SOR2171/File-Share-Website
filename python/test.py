from service.getMusicList import get_music_list
from service.getMusicPlayist import get_music_playlist

def get_output(folder_item, layer):
    res = "    " * layer + folder_item["name"] + "\n"
    for item in folder_item["sub_list"]:
        res += get_output(item, layer + 1)
    return res

def depart_dict_list(l):
    output = ""
    for item in l:
        output += get_output(item, 0)
    return output

if __name__ == "__main__":
    # folder_list = depart_dict_list(get_music_list())
    # print(folder_list)
    
    playlists_list = depart_dict_list(get_music_playlist())
    print(playlists_list)