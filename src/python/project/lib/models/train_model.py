from metrics.metrics import eval_metrics
from models.prepare_for_modeling import traintest_split
import mlflow
from sklearn.linear_model import ElasticNet
import mlflow.sklearn
import os

PROJECT_PATH=os.environ["PROJECT_PATH"] 
MODELS_PATH="{0}/models".format(PROJECT_PATH)


def train_model(train_x,train_y,alpha,l1_ratio,random_state=42):
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    lr.fit(train_x, train_y)
    return lr
    


def mlflow_model(data,alpha,l1_ratio): 
    mlflow.set_tracking_uri("file:{0}/mlruns".format(MODELS_PATH))   
    with mlflow.start_run():
        train_x,test_x,train_y,test_y = traintest_split(data)
        lr = train_model(train_x,train_y,alpha,l1_ratio)
        predicted_qualities = lr.predict(test_x)
        (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)
        test_x["predicted_qualities"]=predicted_qualities

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)
        test_x.to_csv("predictions.csv")
        mlflow.log_artifact("predictions.csv")
        mlflow.sklearn.log_model(lr, "model")
