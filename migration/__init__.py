import psycopg
import yaml
import logging

logging.basicConfig(level=logging.DEBUG)

_logger = logging.getLogger(__name__)


def load_config():
    with open("config.yml") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def get_new_cursor():
    conn = psycopg.connect(f"dbname={config['target_db']}")
    return conn.cursor()


def get_old_cursor():
    conn = psycopg.connect(f"dbname={config['source_db']}")
    return conn.cursor()


config = load_config()
new_cursor = get_new_cursor()
old_cursor = get_old_cursor()
models_tree = set()
env = set()


def init_database_migration():
    new_cursor.execute("SET session_replication_role = 'replica';")


def finish_database_migration():
    new_cursor.execute("SET session_replication_role = 'origin';")


from migration import models

# Initializing models
for model in list(models_tree):
    env.add(model(old_cursor, new_cursor))


def run():
    init_database_migration()
    for model in list(env):
        model.migrate()
    new_cursor.connection.commit()
    finish_database_migration()


def analyze():
    for model in list(env):
        model.analyze()
