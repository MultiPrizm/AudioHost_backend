import os, json

if not os.path.isfile("../.env"):

        with open("../.env", 'w') as file:
            file.write('')

if not os.path.isfile("../conf.json"):

        with open("../conf.json", 'w') as file:
            data = {
                 "awscli": False,
                 "cookies_encrypt": False
            }
            json.dump(data, file, indent=4, sort_keys=True)


def save_to_env(key, value, env_file='.env'):

    try:
        with open(env_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    updated = False
    for i, line in enumerate(lines):
        if line.startswith(f'{key}='):
            lines[i] = f'{key}={value}\n'
            updated = True
            break

    if not updated:
        lines.append(f'{key}={value}\n')

    with open(env_file, 'w') as file:
        file.writelines(lines)


def edit_conf_json(key: str, value: str):
    data = None
    with open("../conf.json", 'r') as f:
        data = f.read()
        data = json.loads(data)
        data[key] = value
          
    with open("../conf.json", 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)