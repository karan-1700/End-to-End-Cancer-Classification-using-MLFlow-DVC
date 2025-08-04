

import os
import sys
import logging
import warnings

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(y_true=actual, y_pred=pred)
    r2 = r2_score(y_true=actual, y_pred=pred)
    return rmse, mae, r2


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    # set random seed
    np.random.seed(40)

    # read the wine-quality csv file from the URL
    csv_url = ("https://raw.githubusercontent.com/plotly/datasets/master/winequality-red.csv")

    try:
        data_df = pd.read_csv(csv_url)
    except Exception as e:
        logger.exception(
            "Unable to download the dataset csv file, check your internet connection. Error: %s", e
        )

    # print("data_df.shape = ", data_df.shape)
    # print(data_df.columns)
    # print(data_df.head(3))

    # split the data into training and testing sets. (0.75, 0.25) split.
    train, test = train_test_split(data_df, test_size=0.25)

    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    # print("train_x.shape = ", train_x.shape)
    # print("test_x.shape = ", test_x.shape)
    # print("train_y.shape = ", train_y.shape)
    # print("test_y.shape = ", test_y.shape)

    alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

    with mlflow.start_run():
        
        regressor = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        regressor.fit(train_x, train_y)

        pred_y = regressor.predict(test_x)

        rmse, mae, r2 = eval_metrics(actual=test_y, pred=pred_y)

        print("ElasticNet model (alpha=%f, li_ratio=%f)" % (alpha, l1_ratio))
        print("  RMSE = %s" % rmse)
        print("  MAE = %s" % mae)
        print("  r2 = %s" % r2)

        mlflow.log_param(key="alpha", value=alpha)
        mlflow.log_param(key="l1_ratio", value=l1_ratio)

        mlflow.log_metric(key="rmse", value=rmse)
        mlflow.log_metric(key="mae", value=mae)
        mlflow.log_metric(key="r2", value=r2)

        mlflow.sklearn.log_model(regressor, "model")








