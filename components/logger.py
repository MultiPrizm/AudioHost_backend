import logging, os, AppCore, fastapi

LOGPATH = "./log"

if not os.path.exists(LOGPATH):
    try:
        os.makedirs(LOGPATH)
    except OSError as e:
        print(f"Помилка створення папки для логів: {LOGPATH} - {e}")

debug_logger = logging.getLogger('debug_logger')
debug_logger.setLevel(logging.DEBUG)
debug_handler = logging.FileHandler(f'{LOGPATH}/debug.log')
debug_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
debug_handler.setFormatter(debug_formatter)
debug_logger.addHandler(debug_handler)

error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler(f'{LOGPATH}/error.log')
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)

def debug(mes: str):
    debug_logger.debug(mes)

def error(mes: str):
    error_logger.error(mes)

@AppCore.app.exception_handler(Exception)
def unicorn_exception_handler(request: fastapi.Request, exc: Exception):

    error(exc)

    return fastapi.responses.JSONResponse(content={}, status_code=500)

    