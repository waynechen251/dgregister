import os

def replace_placeholder(file_path, placeholder, replacement, output_path):
    print(f'正在處理文件：{file_path}')
    
    # 檢查輸出文件路徑是否存在，不存在則創建
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 讀取文件內容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    print(f'替換佔位符：{placeholder} -> {replacement}')
    # 替換佔位符
    new_content = content.replace(placeholder, replacement)

    print(f'輸出文件：{output_path}')
    # 將新內容寫入輸出文件
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(new_content)