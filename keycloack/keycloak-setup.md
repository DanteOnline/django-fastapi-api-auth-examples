# Настройка Keycloak вручную после запуска:

- Зайти в Keycloak: http://localhost:8080
- Авторизоваться: admin / admin
- Создать Realm, например calculations
- Создать Client, например fastapi, с типом public, и разреши Direct Access Grants
- Создать User, например user, и задай ему пароль user123
- (опционально) Добавить Role и привязать её к пользователю