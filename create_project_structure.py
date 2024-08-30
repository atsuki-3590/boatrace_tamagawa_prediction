# テンプレート構造
import os


def create_directory_structure(base_path):
    directories = [
        'data/raw',
        'data/processed',
        'scripts',
        'notebooks',
        'models',
        'config',
        'utils',
        'docs'
    ]

    files = {
        'README.md': '',
        'requirements.txt': '',
        'scripts/data_preprocessing.py': '',
        'scripts/feature_engineering.py': '',
        'scripts/train_model.py': '',
        'scripts/evaluate_model.py': '',
        'notebooks/exploratory_data_analysis.ipynb': '',
        'notebooks/model_training.ipynb': '',
        'models/best_model.pkl': '',
        'config/config.yaml': '',
        'utils/data_loader.py': '',
        'utils/metrics.py': '',
        'docs/API_specification.md': '',
        '.gitignore': ''
    }

    for directory in directories:
        path = os.path.join(base_path, directory)
        os.makedirs(path, exist_ok=True)
        print(f'Created directory: {path}')

    for file, content in files.items():
        path = os.path.join(base_path, file)
        with open(path, 'w') as f:
            f.write(content)
        print(f'Created file: {path}')

if __name__ == "__main__":
    base_path = 'boat_race_prediction'
    create_directory_structure(base_path)