#!/bin/bash

# Функция для создания виртуального окружения
create_venv() {
    local env_name=${1:-".venv"}
    python3 -m venv "$env_name"
    echo "Виртуальное окружение '$env_name' создано."
}

# Функция для активации виртуального окружения
activate_venv() {
    local env_name=${1:-".venv"}
    if [ ! -d "$env_name" ]; then
        echo "Виртуальное окружение '$env_name' не найдено. Используйте '$0 create [env_name]' для создания."
        return 1
    fi
    if [ -z "$VIRTUAL_ENV" ]; then
        source "./$env_name/bin/activate"
        echo "Виртуальное окружение '$env_name' активировано."
    else
        echo "Виртуальное окружение уже активировано."
    fi
}

# Функция для установки зависимостей из requirements.txt
install_deps() {
    if [ ! -f "requirements.txt" ]; then
        echo "Файл requirements.txt не найден."
        return 1
    fi

    # Проверка, установлены ли все зависимости из requirements.txt
    for package in $(cat requirements.txt | cut -d '=' -f 1); do
        if ! pip freeze | grep -q "^$package=="; then
            echo "Установка зависимостей..."
            pip install -r requirements.txt
            echo "Зависимости установлены."
            return 0
        fi
    done

    echo "Все зависимости уже установлены."
}

# Создание виртуального окружения, если оно еще не создано
if [ ! -d ".venv" ]; then
    create_venv
fi

# Активация виртуального окружения
activate_venv

# Установка зависимостей
install_deps

# Получение количества наборов данных
n_datasets=$1

# Запуск скрипта создания данных
python python_scripts/data_creation.py $n_datasets

# Запуск скрипта предобработки данных
python python_scripts/model_preprocessing.py $n_datasets

# Запуск скрипта подготовки и обучения модели
python python_scripts/model_preparation.py $n_datasets

# Запуск скрипта тестирования модели
python python_scripts/model_testing.py $n_datasets
