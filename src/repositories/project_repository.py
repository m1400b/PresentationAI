"""
PresentationAI

Project Repository
"""

from __future__ import annotations

from src.database.database_service import DatabaseService


class ProjectRepository:
    """
    Repository for Recent Projects
    """

    def __init__(self, database: DatabaseService):

        self.database = database

    # -------------------------------------------------

    def add_recent_project(
        self,
        project_name: str,
        project_path: str
    ):

        # حذف رکورد قبلی در صورت وجود
        self.database.execute(
            """
            DELETE FROM recent_projects
            WHERE project_path = ?
            """,
            (project_path,)
        )

        # ثبت مجدد با زمان جدید
        self.database.execute(
            """
            INSERT INTO recent_projects
            (
                project_name,
                project_path,
                last_open
            )
            VALUES
            (
                ?,
                ?,
                datetime('now','localtime')
            )
            """,
            (
                project_name,
                project_path
            )
        )

        # نگهداری فقط 15 پروژه آخر
        self.database.execute(
            """
            DELETE FROM recent_projects
            WHERE id NOT IN
            (
                SELECT id
                FROM recent_projects
                ORDER BY last_open DESC
                LIMIT 15
            )
            """
        )

        self.database.commit()

    # -------------------------------------------------

    def get_recent_projects(self):

        return self.database.query(
            """
            SELECT
                id,
                project_name,
                project_path,
                last_open
            FROM recent_projects
            ORDER BY last_open DESC
            """
        )

    # -------------------------------------------------

    def clear_recent_projects(self):

        self.database.execute(
            """
            DELETE FROM recent_projects
            """
        )

        self.database.commit()

    # -------------------------------------------------

    def project_exists(
        self,
        project_path: str
    ) -> bool:

        row = self.database.query_one(
            """
            SELECT id
            FROM recent_projects
            WHERE project_path = ?
            """,
            (project_path,)
        )

        return row is not None

    # -------------------------------------------------

    def remove_recent_project(
        self,
        project_path: str
    ):

        self.database.execute(
            """
            DELETE FROM recent_projects
            WHERE project_path = ?
            """,
            (project_path,)
        )

        self.database.commit()