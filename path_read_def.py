import configparser

def read_config(FILE_PATH):
    # ConfigParserのインスタンスを作成
    config = configparser.ConfigParser()
    # config.ini を読み込む
    config.read('config.ini', encoding='utf-8')
    # 指定されたキーの値を取得
    try:
        csv_file_path = config['DEFAULT'][FILE_PATH]
    except KeyError:
        raise KeyError(f"設定ファイルに '{FILE_PATH}' が存在しません。")
    return csv_file_path