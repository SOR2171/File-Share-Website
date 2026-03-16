from pathlib import Path
import const

def create_file_info(name):
    return {
        "name": name,
        "sub_list": []
    }

def folder_detect(folder_list, folder):
    for folder_item in sorted(folder.iterdir()): 
        if folder_item.is_dir():
            next_folder = create_file_info("folder:" + folder_item.name)
            folder_list.append(next_folder)
            folder_detect(next_folder["sub_list"], folder_item)
        else:
            if folder_item.name.find(".lrc") == -1:
                folder_list.append(create_file_info("file:" + folder_item.name[0:-4]))

def get_music_list():
    root_folder_list = []
    folder = Path(const.MUSIC_FOLDER)
    
    for folder_item in sorted(folder.iterdir()): 
        if folder_item.is_dir() and folder_item.name.find(".") == -1:
            next_folder = create_file_info("folder:" + folder_item.name)
            root_folder_list.append(next_folder)
            folder_detect(next_folder["sub_list"], folder_item)

    return root_folder_list

def get_output(folder_item, layer):
    res = "    " * layer + folder_item["name"] + "\n"
    for item in folder_item["sub_list"]:
        res += get_output(item, layer + 1)
    return res

if __name__ == "__main__":
    folder_list = get_music_list()
    output = ""
    for item in folder_list:
        output += get_output(item, 0)

    print(output)