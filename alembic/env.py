from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from core.config import settings
from db.base import Base
import models  # noqa: F401


print("Registered tables:", list(Base.metadata.tables.keys()))


# Alembic Configh
config = context.config

# Override DB URL from settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_SYNC_URL)

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata for autogenerate
target_metadata = Base.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


from sqlalchemy import create_engine

def run_migrations_online() -> None:
    # 🔹 AUTOGENERATE PATH (SYNC ENGINE)
    if context.is_autogenerate():
        sync_engine = create_engine(
            settings.DATABASE_SYNC_URL,
            poolclass=pool.NullPool,
        )

        with sync_engine.connect() as connection:
            do_run_migrations(connection)

        return

    # 🔹 NORMAL MIGRATION PATH (ASYNC ENGINE)
    async_engine = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async def run_async_migrations():
        async with async_engine.connect() as connection:
            await connection.run_sync(do_run_migrations)
        await async_engine.dispose()

    import asyncio
    asyncio.run(run_async_migrations())

