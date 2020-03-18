from data.make_dataset  import download_raw_data
from models.train_model import mlflow_model
import sys


if __name__ == "__main__":
    alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
    data = download_raw_data()
    
    mlflow_model(data,alpha,l1_ratio)
    
