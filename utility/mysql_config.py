from envManager import save_to_env

save_to_env("DB_HOST", input("DB_HOST="), "../.env")
save_to_env("DB", input("DB="), "../.env")
save_to_env("DB_USER", input("DB_USER="), "../.env")
save_to_env("DB_PASSWORD", input("DB_PASSWORD="), "../.env")

print("База даних сконфігурована")