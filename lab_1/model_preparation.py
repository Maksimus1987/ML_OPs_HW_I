from sklearn.linear_model import LinearRegression  # Импорт модели линейной регрессии
from sklearn.model_selection import (
    train_test_split,
)  # Импорт функции для разделения данных на обучающий и тестовый наборы
from sklearn.metrics import (
    mean_squared_error,
)  # Импорт функции для расчета среднеквадратичной ошибки
import pandas as pd  # Импорт библиотеки pandas для работы с данными


def prepare_and_train_model(train_data_path):
    data = pd.read_csv(train_data_path)  # Загрузка обучающих данных из CSV файла
    X = data["Day"].values.reshape(-1, 1)  # Выделение признаков
    y = data["Temperature"]  # Выделение целевой переменной
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )  # Разделение данных на обучающий и тестовый наборы

    model = LinearRegression()  # Создание модели линейной регрессии
    model.fit(X_train, y_train)  # Обучение модели на обучающем наборе

    y_pred = model.predict(X_test)  # Прогнозирование значений на тестовом наборе
    mse = mean_squared_error(y_test, y_pred)  # Вычисление среднеквадратичной ошибки
    print(f"MSE: {mse}")  # Вывод значения среднеквадратичной ошибки
    return model  # Возвращение обученной модели


model = prepare_and_train_model(
    "train/preprocessed_train.csv"
)  # Обучение модели на предобработанных обучающих данных
