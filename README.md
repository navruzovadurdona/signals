# signals

🔁 Signals (Сигналы)

Позволяют выполнять действия при определённых событиях, таких как post_save, post_delete и т.д.
✅ Пример: автоматическое создание UserProfile после создания User

    Используется @receiver(post_save, sender=User)

    Создание профиля происходит только при created == True

    Также добавлен сигнал для сохранения профиля после сохранения пользователя

⚠️ Важно: убедитесь, что у User есть связанный profile, например через OneToOneField и related_name='profile'.
👤 Кастомная модель пользователя

Когда стандартной модели User недостаточно — создаём свою через AbstractBaseUser.
Компоненты:

    CustomUserManager: с методами create_user() и create_superuser()

    CustomUser: модель с полями email, username, флагами is_active, is_staff

🧠 Памятка:

    Модель пользователя нужно задавать до миграций, иначе придётся пересоздавать базу.

    USERNAME_FIELD = 'email' означает, что аутентификация будет идти по email.

🔐 Аутентификация

Пример логина с кастомной моделью через email.
Основные шаги:

    Форма LoginForm с полями email, password

    View-функция с authenticate() и login()

    Шаблон login.html с выводом формы

⚠️ Не забудьте, что если используете CustomUser, то authenticate() должен поддерживать email вместо username.
