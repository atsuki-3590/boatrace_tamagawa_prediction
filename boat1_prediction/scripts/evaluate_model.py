# モデルの評価

# サンプル
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

def load_model(model_path):
    return joblib.load(model_path)

def evaluate_model(model, X, y):
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    return accuracy

if __name__ == "__main__":
    model = load_model('models/best_model.pkl')
    df = pd.read_csv('data/processed/new_data.csv')
    X = df.drop(columns=['target'])
    y = df['target']
    
    accuracy = evaluate_model(model, X, y)
    print(f'Model Accuracy: {accuracy}')
