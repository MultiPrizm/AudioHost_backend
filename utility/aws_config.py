import colorama
from envManager import *

if input("using awscli [Y/n]") == "Y":

    edit_conf_json("awscli", True)
else:
    save_to_env("AWS_ACCESS_KEY", input("AWS_ACCESS_KEY="), "../.env")
    save_to_env("AWS_SECRET_KEY", input("AWS_SECRET_KEY="), "../.env")
    save_to_env("AWS_REGION", input("AWS_REGION="), "../.env")

print("ENV[", colorama.Fore.BLUE + "INFO",colorama.Style.RESET_ALL + "]: aws configured.")