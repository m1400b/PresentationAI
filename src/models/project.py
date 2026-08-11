"""
PresentationAI

Project Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import uuid


@dataclass(slots=True)
class Project:

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    name: str = "Untitled Project"

    description: str = ""

    author: str = ""

    company: str = ""

    version: str = "1.0"

    language: str = "fa"

    theme: str = "Default"

    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(timespec="seconds")
    )

    modified_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(timespec="seconds")
    )

    path: str = ""

    database: str = "database.db"

    slide_count: int = 0
    
    @property
    def project_file(self) -> Path:

        return Path(self.path) / "project.json"

    @property
    def database_file(self) -> Path:

        return Path(self.path) / self.database