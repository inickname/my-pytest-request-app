# Начало работы с MyPytestRequestApp

### Этот документ представляет собой краткую инструкцию по установке и использованию MyPytestRequestApp для MacOS.

## Предусловия

### Для работы приложения должно быть установлено:

#### 1. Интерпретатор Python версии 3.11.8. Проверить его версию можно командой:

```
python3 --version
```

#### 2. Java версии 8 и выше. Проверка версии:

```
java -version
javac -version
```

#### 3. Homebrew — это менеджер пакетов для macOS. Для проверки корректной установки выполните:

```
brew --version
```

#### 4. Allure. Проверка корректной установки:

```
allure --version
```

## Установка

#### 1. Клонирование репозитория:

```
git clone https://github.com/inickname/my-pytest-request-app
```

#### 2. Установка пакетного менеджера UV:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 3. Выполните команду:

```
uv sync
```

#### 4. Смените python интерпретатор на UV.

#### 5. Создание директории для хранения результатов тестов:

```
mkdir allure-results
```

## Использование

### Запуск тестов с pytest и сохранение результатов для Allure:

```
python -m pytest tests/test_create_booking.py -v -s --alluredir=allure-results
```

### После выполнения тестов создайте и откройте отчет:

```
allure serve allure-results
```
