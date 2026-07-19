from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# 1. LOAD ENVIRONMENT VARIABLES
# This lets us use a .env file for our DB URL instead of hardcoding it in alembic.ini
from dotenv import load_dotenv
import os
load_dotenv() # looks for a .env file in your project root

# 2. ALEMBIC CONFIG SETUP
# this is the Alembic Config object, which provides access to the values within the .ini file
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# 3. TELL ALEMBIC ABOUT YOUR MODELS - THIS MUST BE BEFORE THE FUNCTIONS
# Import your Base here so Alembic can see all your tables
# Make sure models.py exists and has: from database import Base
from models import Base

# This is what alembic uses to detect changes for --autogenerate
target_metadata = Base.metadata


# 4. HELPER FUNCTION TO GET DB URL
def get_url():
    """
    Get the database URL from alembic.ini, 
    but allow it to be overridden by an environment variable DB_URL
    """
    return os.getenv("DB_URL", config.get_main_option("sqlalchemy.url"))


def run_migrations_offline() -> None:
    """
    Run migrations in 'offline' mode.
    This just generates SQL without connecting to the DB.
    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata, # <-- now this is Base.metadata, not None
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True, # lets alembic detect column type changes
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Run migrations in 'online' mode.
    This connects to the DB and runs migrations directly.
    """
    configuration = config.get_section(config.config_ini_section, {})
    configuration["sqlalchemy.url"] = get_url() # override with .env value
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata, # <-- now this is Base.metadata
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()