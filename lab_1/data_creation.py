import numpy as np  # Импорт библиотеки NumPy для работы с массивами данных
import os  # Импорт модуля os для работы с операционной системой
import pandas as pd  # Импорт библиотеки pandas для работы с данными в виде таблиц


def create_data(anomaly=False, noise=False):
    np.random.seed(42)  # Задание случайного зерна для воспроизводимости результатов
    days = np.arange(1, 366)  # Генерация дней в году
    base_temperature = 15  # Базовая температура
    temperature_variation = 5  # Вариация температуры
    if anomaly:
        anomaly_day = np.random.randint(1, 365)  # Генерация случайного дня-аномалии
        anomaly_temperature = base_temperature + np.random.uniform(
            -temperature_variation, temperature_variation
        )
        temperatures = np.where(
            days == anomaly_day,
            anomaly_temperature,
            base_temperature + np.random.normal(0, temperature_variation, len(days)),
        )
    else:
        temperatures = base_temperature + np.random.normal(
            0, temperature_variation, len(days)
        )  # Генерация температур без аномалии

    if noise:
        noise_factor = np.random.uniform(0.1, 0.5)  # Генерация коэффициента шума
        temperatures += np.random.normal(
            0, noise_factor, len(days)
        )  # Добавление шума к температуре

    return pd.DataFrame(
        {"Day": days, "Temperature": temperatures}
    )  # Создание DataFrame с днями и температурами


def save_data(data, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)  # Создание директории, если её нет
    data.to_csv(
        os.path.join(folder, filename), index=False
    )  # Сохранение данных в CSV файл


# Создание и сохранение данных
for i in range(5):
    data = create_data(
        anomaly=i % 2 == 0, noise=i % 3 == 0
    )  # Генерация данных с аномалиями и шумом
    if i < 3:
        save_data(data, "train", f"data_{i}.csv")  # Сохранение тренировочных данных
    else:
        save_data(data, "test", f"data_{i}.csv")  # Сохранение тестовых данных
