"""
PresentationAI

Export Service
"""

from __future__ import annotations

from pathlib import Path

from src.core.service import BaseService

from src.exporters.pptx_exporter import PPTXExporter

from src.services.slide_service import SlideService


class ExportService(BaseService):
    """
    Handles presentation export operations.
    """

    # -------------------------------------------------

    def __init__(
        self,
        slide_service: SlideService,
    ):

        self.slide_service = slide_service

        self.pptx_exporter = PPTXExporter()

    # -------------------------------------------------

    def initialize(self):

        pass

    # -------------------------------------------------

    def shutdown(self):

        pass

    # -------------------------------------------------

    @property
    def slide_count(self) -> int:

        return self.slide_service.count()

    # -------------------------------------------------

    def export_pptx(
        self,
        filename: str,
    ) -> bool:

        if self.slide_count == 0:

            print("Nothing to export.")

            return False

        try:

            output = Path(filename)

            output.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            self.pptx_exporter.export(

                slides=self.slide_service.slides,

                filename=str(output),

            )

            print()

            print("=" * 50)
            print("Presentation exported successfully.")
            print(output)
            print("=" * 50)

            return True

        except Exception as ex:

            print()

            print("=" * 50)
            print("Export failed.")
            print(ex)
            print("=" * 50)

            return False

    # -------------------------------------------------

    def export_current_project(

        self,

        filename: str = "output/presentation.pptx",

    ) -> bool:

        return self.export_pptx(filename)