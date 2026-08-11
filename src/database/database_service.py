"""
PresentationAI

Database Service
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from src.core.service import BaseService


class DatabaseService(BaseService):

    def __init__(self, database_path: str = "database/app.db"):

        self.database_path = Path(database_path)

        self.connection = None

    # -------------------------------------------------

    def initialize(self):

        self.database_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.connection = sqlite3.connect(
            self.database_path
        )

        self.connection.row_factory = sqlite3.Row

        #
        # SQLite options
        #

        self.execute("PRAGMA foreign_keys = ON")
        self.execute("PRAGMA journal_mode = WAL")
        self.execute("PRAGMA synchronous = NORMAL")

        self.create_tables()

        self.migrate()

    # -------------------------------------------------

    def shutdown(self):

        if self.connection:

            self.connection.commit()

            self.connection.close()

            self.connection = None

    # -------------------------------------------------

    def execute(self, sql, params=()):

        cursor = self.connection.cursor()

        cursor.execute(sql, params)

        return cursor

    # -------------------------------------------------

    def query(self, sql, params=()):

        cursor = self.connection.cursor()

        cursor.execute(sql, params)

        return cursor.fetchall()

    # -------------------------------------------------

    def query_one(self, sql, params=()):

        cursor = self.connection.cursor()

        cursor.execute(sql, params)

        return cursor.fetchone()

    # -------------------------------------------------

    def commit(self):

        self.connection.commit()

    # -------------------------------------------------

    def rollback(self):

        self.connection.rollback()

    # -------------------------------------------------

    def create_tables(self):

        # -------------------------------------------------
        # app_info
        # -------------------------------------------------

        self.execute("""

        CREATE TABLE IF NOT EXISTS app_info
        (
            key TEXT PRIMARY KEY,
            value TEXT
        )

        """)

        # -------------------------------------------------
        # settings
        # -------------------------------------------------

        self.execute("""

        CREATE TABLE IF NOT EXISTS settings
        (
            key TEXT PRIMARY KEY,
            value TEXT
        )

        """)

        # -------------------------------------------------
        # recent_projects
        # -------------------------------------------------

        self.execute("""

        CREATE TABLE IF NOT EXISTS recent_projects
        (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            project_name TEXT NOT NULL,

            project_path TEXT UNIQUE NOT NULL,

            last_open TEXT NOT NULL

        )

        """)

        # -------------------------------------------------
        # slides
        # -------------------------------------------------

        self.execute("""

        CREATE TABLE IF NOT EXISTS slides
        (

            id TEXT PRIMARY KEY,

            title TEXT,

            subtitle TEXT,

            content TEXT,

            prompt TEXT,

            notes TEXT,

            layout TEXT,

            tags TEXT,

            status TEXT,

            ai_model TEXT,

            slide_order INTEGER,

            created_at TEXT,

            modified_at TEXT

        )

        """)

        # -------------------------------------------------
        # elements
        # -------------------------------------------------

        self.execute("""

        CREATE TABLE IF NOT EXISTS elements
        (

            id TEXT PRIMARY KEY,

            slide_id TEXT NOT NULL,

            type TEXT NOT NULL,

            name TEXT,

            x REAL,

            y REAL,

            width REAL,

            height REAL,

            rotation REAL,

            z_index INTEGER DEFAULT 0,

            visible INTEGER DEFAULT 1,

            locked INTEGER DEFAULT 0,

            opacity REAL DEFAULT 1.0,

            data TEXT,

            created_at TEXT,

            modified_at TEXT,

            FOREIGN KEY(slide_id)
                REFERENCES slides(id)
                ON DELETE CASCADE

        )

        """)

        # -------------------------------------------------
        # Indexes
        # -------------------------------------------------

        self.execute("""

        CREATE INDEX IF NOT EXISTS
        idx_slide_order

        ON slides(slide_order)

        """)

        self.execute("""

        CREATE INDEX IF NOT EXISTS
        idx_elements_slide

        ON elements(slide_id)

        """)

        self.execute("""

        CREATE INDEX IF NOT EXISTS
        idx_elements_z

        ON elements(slide_id, z_index)

        """)

        self.commit()
    # -------------------------------------------------

    def migrate(self):

        """
        Automatically upgrades older databases
        without losing data.
        """
    
        # =================================================
        # slides
        # =================================================
    
        slide_columns = {
        
            row["name"]
    
            for row in self.query(
            
                "PRAGMA table_info(slides)"
    
            )
    
        }
    
        slide_required = {
        
            "content": "TEXT",
    
        }
    
        for column, column_type in slide_required.items():
        
            if column not in slide_columns:
            
                self.execute(
                
                    f"""
    
                    ALTER TABLE slides
    
                    ADD COLUMN {column} {column_type}
    
                    """
    
                )
    
        # =================================================
        # elements
        # =================================================
    
        element_columns = {
        
            row["name"]
    
            for row in self.query(
            
                "PRAGMA table_info(elements)"
    
            )
    
        }
    
        element_required = {
        
            "name": "TEXT",
    
            "z_index": "INTEGER DEFAULT 0",
    
            "opacity": "REAL DEFAULT 1.0",
    
        }
    
        for column, column_type in element_required.items():
        
            if column not in element_columns:
            
                self.execute(
                
                    f"""
    
                    ALTER TABLE elements
    
                    ADD COLUMN {column} {column_type}
    
                    """
    
                )
    
        self.commit()