-Открыть терминал 

-Перейти в дерикторию %%%/Shop (дериктория в которой содержится файл manage.py)

Прописать следующие команды:

(для Linux используйте pip3 и python3)

    -pip install -r requirements.txt

    -python manage.py makemigrations

    -python manage.py migrate

    -python manage.py runserver (запуск сервера)

        -перейдите по ссылке http://127.0.0.1:8000/admin/

        -войдите в учетную запись (username=admin, password=admin)

-теперь, когда вы вошли в уч запись перейдите на главную http://127.0.0.1:8000/ что бы проверить весь функционал

