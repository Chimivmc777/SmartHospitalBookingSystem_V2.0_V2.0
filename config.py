import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    MYSQL_HOST = os.getenv("MYSQLHOST") or os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQLPORT") or os.getenv("MYSQL_PORT", "3306"))
    MYSQL_USER = os.getenv("MYSQLUSER") or os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQLPASSWORD") or os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQLDATABASE") or os.getenv("MYSQL_DATABASE")

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "ehealthbhutan2026"
    )