import os
import json
import re

def replace_placeholder(file_path, config_path, output_path):
    
    # load json config
    with open(config_path, 'r', encoding='utf-8') as file:
        config = json.load(file)
    
    # flatten config dictionary
    def flatten_dict(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
    
    flat_config = flatten_dict(config)
    
    # read file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # replace placeholders
    def replace_placeholders(text, config):
        for key, value in config.items():
            text = re.sub(rf'\$\({re.escape(key)}\)', str(value), text)
        return text
    
    new_content = replace_placeholders(content, flat_config)
    
    # 檢查輸出文件路徑是否存在，不存在則創建
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # write to output file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(new_content)