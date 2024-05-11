from sklearn.linear_model import LinearRegression  # Импорт модели линейной регрессии
from sklearn.model_selection import (
    train_test_split,
)  # Импорт функции для разделения данных на обучающий и тестовый наборы
from sklearn.metrics import (
    mean_squared_error,
)  # Импорт функции для расчета среднеквадратичной ошибки
import pandas as pd  # Импорт библиотеки pandas для работы с данными


def prepare_and_train_model(train_data_path):
    data = pd.read_csv(train_data_path)  # Загрузка данных из CSV файла

    # Подготовка признаков и целевой переменной
    X = data["Day"].values.reshape(-1, 1)
    y = data["Temperature"]

    # Разделение данных на обучающий и тестовый наборы
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Обучение модели линейной регрессии
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Прогнозирование значений на тестовом наборе и расчет среднеквадратичной ошибки
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"MSE: {mse}")
    return model


# Обучение модели на предобработанных обучающих данных
model = prepare_and_train_model("train/preprocessed_train.csv")


def test_model(model, test_data_path):
    data = pd.read_csv(test_data_path)  # Загрузка тестовых данных из CSV файла

    # Подготовка признаков и целевой переменной
    X = data["Day"].values.reshape(-1, 1)
    y = data["Temperature"]

    # Прогнозирование значений на тестовом наборе и расчет среднеквадратичной ошибки
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    print(f"Test MSE: {mse}")


# Проверка модели на предобработанных тестовых данных
test_model(model, "test/preprocessed_test.csv")
