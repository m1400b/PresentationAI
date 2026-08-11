"""
PresentationAI

Base Repository
"""

from src.database.database_service import DatabaseService


class BaseRepository:
    """
    Base class for all repositories.
    Provides common database helper methods.
    """

    def __init__(self, database: DatabaseService):

        self.db = database

        self.create_table()

    # -------------------------------------------------

    def create_table(self):
        """
        Override in child repositories.
        """
        pass

    # -------------------------------------------------

    def execute(self, sql: str, params=()):

        return self.db.execute(sql, params)

    # -------------------------------------------------

    def query(self, sql: str, params=()):

        return self.db.query(sql, params)

    # -------------------------------------------------

    def query_one(self, sql: str, params=()):

        return self.db.query_one(sql, params)

    # -------------------------------------------------

    def execute_many(self, sql: str, values):

        cursor = self.db.connection.cursor()

        cursor.executemany(sql, values)

        return cursor

    # -------------------------------------------------

    def commit(self):

        self.db.commit()

    # -------------------------------------------------

    def rollback(self):

        self.db.rollback()

    # -------------------------------------------------

    def table_exists(self, table_name: str) -> bool:

        row = self.query_one(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
              AND name=?
            """,
            (table_name,)
        )

        return row is not None