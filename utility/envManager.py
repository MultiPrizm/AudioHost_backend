import os

if not os.path.isfile("../.env"):
        # Якщо файл не існує, створюємо його
        with open("../.env", 'w') as file:
            file.write('')  # Створюємо порожній файл
        print(f'Файл {".env"} було створено.')

def save_to_env(key, value, env_file='.env'):
    # Прочитати існуючі дані з файлу .env
    try:
        with open(env_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    # Оновити або додати нову змінну
    updated = False
    for i, line in enumerate(lines):
        if line.startswith(f'{key}='):
            lines[i] = f'{key}={value}\n'
            updated = True
            break

    if not updated:
        lines.append(f'{key}={value}\n')

    # Записати оновлені дані назад у файл .env
    with open(env_file, 'w') as file:
        file.writelines(lines)