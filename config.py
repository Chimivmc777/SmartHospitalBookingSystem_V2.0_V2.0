import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MYSQL_HOST = os.getenv("MYSQLHOST")
    MYSQL_PORT = int(os.getenv("MYSQLPORT", "3306"))
    MYSQL_USER = os.getenv("MYSQLUSER")
    MYSQL_PASSWORD = os.getenv("MYSQLPASSWORD")
    MYSQL_DB = os.getenv("MYSQLDATABASE")

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "ehealthbhutan2026"
    )