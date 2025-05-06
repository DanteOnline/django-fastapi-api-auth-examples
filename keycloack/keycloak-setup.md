# Настройка Keycloak вручную после запуска:

- Зайти в Keycloak: http://localhost:8080
- Авторизоваться: admin / admin
- Создать Client, например fastapi, с типом public, и разреши Direct Access Grants
- Создать User, например user, и задай ему пароль user123
- Отметить, что user подтвержден по email
- keycloak -> Realm Settings -> Keys -> RS256 -> Public Key скопировать в файл auth.py
- (опционально) Добавить Role и привязать её к пользователю