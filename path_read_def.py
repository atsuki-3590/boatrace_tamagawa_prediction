import configparser
from pathlib import Path

def read_config(file_key, base_key='base_path', config_file='config.ini'):
    """
    設定ファイルからベースパスとファイル名を読み込み、完全なパスを返します。

    Args:
        base_key (str): base_path のキー名。
        file_key (str): ファイルパスのキー名。
        config_file (str): 設定ファイルのパス（デフォルトは 'config.ini'）。

    Returns:
        Path: 完全なファイルパス。

    Raises:
        KeyError: 指定されたキーが設定ファイルに存在しない場合。
        FileNotFoundError: 設定ファイルが存在しない場合。
    """
    config = configparser.ConfigParser()
    # config.ini を読み込む
    read_files = config.read(config_file, encoding='utf-8-sig')
    if not read_files:
        raise FileNotFoundError(f"設定ファイル '{config_file}' が見つかりません。")

    try:
        base_path = config['paths'][base_key]
    except KeyError:
        raise KeyError(f"設定ファイルの '[paths]' セクションに '{base_key}' が存在しません。")

    try:
        file_name = config['paths'][file_key]
    except KeyError:
        raise KeyError(f"設定ファイルの '[paths]' セクションに '{file_key}' が存在しません。")

    # Pathオブジェクトを使用してパスを結合
    full_path = Path(base_path) / file_name
    return full_path
