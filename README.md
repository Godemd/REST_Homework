# **Система управления обучением (LMS)**  
Полнофункциональная система управления обучением на Django, которая использует **Poetry** для управления зависимостями. Проект предоставляет интерфейсы для работы с пользователями, курсами, уроками и платежами.

---

## **Описание**
LMS позволяет:
- Управлять пользователями с кастомной аутентификацией через email.
- Работать с курсами и уроками (добавление, редактирование, удаление).
- Вести учет платежей за курсы и уроки.
- Использовать REST API для интеграции с внешними системами.

---

## **Установка**

### Требования:
- Python 3.9+  
- Poetry 1.2+  

### Шаги:

1. **Установите зависимости через Poetry**:
   ```bash
   poetry install
   ```

2. **Активируйте виртуальное окружение**:
   ```bash
   poetry shell
   ```

3. **Настройте базу данных**:
   - Откройте `settings.py` и проверьте параметры базы данных.
   - Примените миграции:
     ```bash
     python manage.py migrate
     ```

4. **Создайте суперпользователя**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Запустите сервер разработки**:
   ```bash
   python manage.py runserver
   ```

6. **Откройте приложение**:
   - [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) — для доступа к админ-панели.
   - [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) — для доступа к API.

---

## **Использование**

### **1. Запуск без активации виртуального окружения**:
Если вы не хотите вручную активировать окружение через `poetry shell`, выполните команды через Poetry:
```bash
python manage.py runserver
```

### **2. Работа с фикстурами**:
Для загрузки данных используйте фикстуры:
```bash
python manage.py loaddata <fixture_name>.json
```
По умолчанию:
```bash
python manage.py loaddata payments.json
```
---

## **Структура проекта**

```plaintext
REST_HOMEWORK/
├── courses/                # Приложение для курсов и уроков
│   ├── templates/          # HTML-шаблоны
│   ├── models.py           # Модели курсов и уроков
│   ├── serializers.py      # Сериализаторы API
│   ├── views.py            # Представления для работы с курсами и уроками
├── users/                  # Приложение для работы с пользователем и платежей
│   ├── templates/          # HTML-шаблоны
│   ├── models.py           # Модель пользователя и платежей
│   ├── serializers.py      # Сериализаторы API
│   ├── views.py            # Представления для пользователя и платежей
├── static/                 # Статические файлы (CSS, JS, изображения)
├── manage.py               # Основной файл управления проектом
├── poetry.lock             # Lock-файл Poetry для зависимостей
├── pyproject.toml          # Конфигурационный файл Poetry
├── README.md               # Текущее описание проекта
```

---

## **API Маршруты**

### Курсы:
- **Список курсов**:
  ```
  GET /api/courses/
  ```
- **Создать курс**:
  ```
  POST /api/courses/
  ```

### Уроки:
- **Список уроков**:
  ```
  GET /api/lessons/
  ```
- **Создать урок**:
  ```
  POST /api/lessons/
  ```

### Платежи:
- **История платежей**:
  ```
  GET /api/payments/
  ```
- **Фильтрация по курсу**:
  ```
  GET /api/payments/?course=1
  ```

---
2. Соберите и запустите контейнеры:
    ```sh
    docker-compose up --build
    ```
3. Примените миграции и соберите статические файлы:
    ```sh
    docker-compose run web /root/.local/bin/poetry run python manage.py migrate
    docker-compose run web /root/.local/bin/poetry run python manage.py collectstatic --noinput
    ```
4. Откройте браузер и перейдите по адресу `http://localhost:8000` для доступа к приложению.

## Использование Celery

Celery автоматически запускается вместе с Docker Compose. Для проверки статуса задач Celery используйте следующие команды:

```sh
docker-compose run web /root/.local/bin/poetry run celery -A REST_HOMEWORK status
```

Для запуска задач Celery используйте:

```sh
docker-compose run web /root/.local/bin/poetry run celery -A REST_HOMEWORK worker --loglevel=info
```

---
## **Вклад в проект**

1. Форкните репозиторий.
2. Создайте ветку:
   ```bash
   git checkout -b feature/ваша-фича
   ```
3. Закоммитьте изменения:
   ```bash
   git commit -m "Добавлена новая фича"
   ```
4. Откройте Pull Request.