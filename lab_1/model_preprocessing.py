import pandas as pd
from sklearn.preprocessing import StandardScaler
import os


def preprocess_data(folder):
    data = pd.concat(
        [
            pd.read_csv(os.path.join(folder, f))
            for f in os.listdir(folder)
            if f.endswith(".csv")
        ]
    )
    scaler = StandardScaler()
    data["Temperature"] = scaler.fit_transform(data[["Temperature"]])
    return data


# Предобработка и сохранение данных
train_data = preprocess_data("train")
test_data = preprocess_data("test")
train_data.to_csv("train/preprocessed_train.csv", index=False)
test_data.to_csv("test/preprocessed_test.csv", index=False)
