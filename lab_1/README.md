![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Sublime Text](https://img.shields.io/badge/sublime_text-%23575757.svg?style=for-the-badge&logo=sublime-text&logoColor=important)


# Конвейер машинного обучения

Этот репозиторий содержит набор скриптов на Python и bash, которые используются для создания, предобработки, обучения и тестирования модели машинного обучения для предсказания температуры.

## Содержание репозитория

- `data_creation.py`: скрипт для создания наборов данных, описывающих изменение дневной температуры. Создает несколько наборов данных, некоторые из которых могут содержать аномалии или шумы. Сохраняет наборы данных в папках `train` и `test`.
- `model_preprocessing.py`: скрипт для предобработки данных. Выполняет нормализацию признаков с помощью `sklearn.preprocessing.StandardScaler`.
- `model_preparation.py`: скрипт для создания и обучения модели машинного обучения на данных из папки `train`.
- `model_testing.py`: скрипт для тестирования модели машинного обучения на данных из папки `test`. Вычисляет среднеквадратичное отклонение между предсказанными и фактическими значениями температуры.
- `pipeline.sh`: bash-скрипт, последовательно запускающий все python-скрипты.

## Требования

Для запуска скриптов необходимо установить следующие библиотеки Python:

- numpy
- pandas
- scikit-learn

## Инструкции по использованию

1. Скачайте или скопируйте репозиторий на свой компьютер.
2. Откройте терминал и перейдите в папку с репозиторием.
3. Запустите bash-скрипт `pipeline.sh` следующей командой:

`./pipeline.sh`

Скрипты последовательно выполнят создание наборов данных, предобработку, обучение и тестирование модели машинного обучения. Результаты тестирования будут выведены в консоль.

## Лицензия

Этот проект выпущен под лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.
