from logging.config import fileConfig
import sys
import os

from sqlalchemy import engine_from_config, pool
from alembic import context

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

# Importa o Base e a URL da tua aplicação
from app.db.base import Base
from app.db.session import DATABASE_URL as SQLALCHEMY_DATABASE_URL

# Importa todos os modelos para que o Alembic possa detectá-los
from app.models import user, product

# Alembic Config
config = context.config

# Substitui a URL do alembic.ini pela tua string de conexão
if SQLALCHEMY_DATABASE_URL:
    config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)
else:
    raise ValueError("DATABASE_URL não está configurada!")

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define o metadata para autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
