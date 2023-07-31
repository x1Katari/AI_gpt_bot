DATABASE_CONFIG = {
    "connections": {"default": 'postgres://postgres:postgres@ai_db:5432/test'},
    "apps": {
        "models": {
            "models": ["src.db.models", "aerich.models"],
            "default_connection": "default",
        },
    }
}
