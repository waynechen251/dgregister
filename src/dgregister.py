import argparse
from replace_placeholder import replace_placeholder

def main():
    parser = argparse.ArgumentParser(description='選擇要執行的功能')
    parser.add_argument('function', help='要執行的功能', choices=['replace_placeholder'])
    parser.add_argument('file', help='要處理的文件路徑')
    parser.add_argument('placeholder', help='要替換的佔位符')
    parser.add_argument('replacement', help='替換佔位符的內容')
    parser.add_argument('output', help='輸出文件的路徑')
    
    args = parser.parse_args()
    
    if args.function == 'replace_placeholder':
        replace_placeholder(args.file, args.placeholder, args.replacement, args.output)
    
    return 0

if __name__ == '__main__':
    main()