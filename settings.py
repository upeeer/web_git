TT_orm={
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",  # MySQL or MariaDB
            "credentials": {
                "host": "127.0.0.1",
                "port": "3306",
                "user": "root",
                "password": "Gyb@2005412",
                "database": "project1",
                "minsize": 1,
                "maxsize": 5,
                "charset": "utf8mb4",
                "echo": True
            }
        }
    },
    "apps": {
        "models": {
            "models": ["basic_data","aerich.models"],#！！注意加上project1.！！
            "default_connection": "default"
        }
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai"
}