"""
PresentationAI

Project Service
"""

from __future__ import annotations

import json

from pathlib import Path
from dataclasses import asdict
from datetime import datetime

from src.core.service import BaseService
from src.models.project import Project


class ProjectService(BaseService):
    """
    Responsible for Project lifecycle.

        • Create
        • Open
        • Save
        • Close
        • Dirty State
    """

    # -------------------------------------------------

    def __init__(
        self,
        repository,
        slide_service,
    ):

        self.repository = repository

        self.slide_service = slide_service

        self.current_project: Project | None = None

        self.is_dirty = False

    # -------------------------------------------------

    def initialize(self):

        print("ProjectService.initialize()")

        self.current_project = None

        self.is_dirty = False

    # -------------------------------------------------

    def shutdown(self):

        print("ProjectService.shutdown()")

        if self.project_is_open():

            self.save_project()

    # =================================================
    # Properties
    # =================================================

    @property
    def project_name(self):

        if self.current_project:

            return self.current_project.name

        return ""

    # -------------------------------------------------

    @property
    def project_path(self):

        if self.current_project:

            return Path(self.current_project.path)

        return None

    # =================================================
    # Dirty Flag
    # =================================================

    def mark_dirty(self):

        self.is_dirty = True

        if self.current_project:

            self.current_project.modified_at = (
                datetime.now().isoformat(
                    timespec="seconds"
                )
            )

    # -------------------------------------------------

    def mark_saved(self):

        self.is_dirty = False

    # =================================================
    # Create
    # =================================================

    def create_project(

        self,

        project_name: str,

        location: str,

    ) -> Project:

        print("Create Project")

        project_path = Path(location) / project_name

        project_path.mkdir(

            parents=True,

            exist_ok=True,

        )

        self._create_project_structure(
            project_path
        )

        project = Project(

            name=project_name,

            path=str(project_path),

        )

        self.current_project = project

        self.repository.add_recent_project(

            project.name,

            project.path,

        )

        self.slide_service.clear()

        self.save_project()

        print("Project created successfully.")

        return project

    # =================================================
    # Open
    # =================================================

    def load_project(

        self,

        folder: str,

    ) -> Project:

        print("Loading project:")

        print(folder)

        project = self._read_project_file(folder)

        self.current_project = project

        self.repository.add_recent_project(

            project.name,

            project.path,

        )

        self.slide_service.load()

        self.mark_saved()

        print("Project loaded.")

        return project

    # =================================================
    # Save
    # =================================================

    def save_project(self):

        if not self.project_is_open():

            return

        self.current_project.slide_count = (

            self.slide_service.count()

        )

        self.current_project.modified_at = (

            datetime.now().isoformat(

                timespec="seconds"

            )

        )

        self._write_project_file()

        self.mark_saved()

    # =================================================
    # Close
    # =================================================

    def close_project(self):

        if self.project_is_open():

            self.save_project()

        self.current_project = None

        self.is_dirty = False

    # =================================================
    # Status
    # =================================================

    def project_is_open(self) -> bool:

        return self.current_project is not None

    # =================================================
    # Private
    # =================================================

    def _create_project_structure(

        self,

        project_path: Path,

    ):

        folders = (

            "assets",

            "images",

            "exports",

            "cache",

            "prompts",

        )

        for folder in folders:

            (

                project_path / folder

            ).mkdir(

                exist_ok=True

            )

    # -------------------------------------------------

    def _write_project_file(self):

        project_file = (

            self.project_path

            / "project.json"

        )

        print("Saving project:")

        print(project_file)

        with open(

            project_file,

            "w",

            encoding="utf-8",

        ) as file:

            json.dump(

                asdict(

                    self.current_project

                ),

                file,

                indent=4,

                ensure_ascii=False,

            )

    # -------------------------------------------------

    def _read_project_file(

        self,

        folder: str,

    ) -> Project:

        project_file = (

            Path(folder)

            / "project.json"

        )

        if not project_file.exists():

            raise FileNotFoundError(

                f"Project file not found:\n{project_file}"

            )

        with open(

            project_file,

            "r",

            encoding="utf-8",

        ) as file:

            data = json.load(file)

        return Project(**data)