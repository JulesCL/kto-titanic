import mlflow
mlflow.autolog()
with mlflow.start_run():
    print('toto')
