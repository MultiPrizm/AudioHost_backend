from envManager import save_to_env
import colorama

save_to_env("DB_HOST", input("DB_HOST="), "../.env")
save_to_env("DB", input("DB="), "../.env")
save_to_env("DB_USER", input("DB_USER="), "../.env")
save_to_env("DB_PASSWORD", input("DB_PASSWORD="), "../.env")

print("MSDB[", colorama.Fore.BLUE + "INFO",colorama.Style.RESET_ALL + "]: database configured.")