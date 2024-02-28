import json
def func_write_to_json(jsonfile_name: str, json_dict: dict):
    with open(jsonfile_name, 'w') as outfile:
        json.dump(json_dict, outfile, indent=4, ensure_ascii=False)

def func_write_to_file(file_name: str, msg: str):
    with open(file=file_name, mode='a', encoding='utf-8') as f:
        f.write(msg)