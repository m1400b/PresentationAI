"""
PresentationAI

Slide Service
"""

from __future__ import annotations

from datetime import datetime

from src.core.service import BaseService

from src.models.slide import Slide
from src.models.presentation_document import PresentationDocument

from src.repositories.slide_repository import SlideRepository
from src.repositories.element_repository import ElementRepository


class SlideService(BaseService):
    """
    Business logic for editable PresentationDocument.
    """

    # -------------------------------------------------

    def __init__(
        self,
        repository: SlideRepository,
        element_repository: ElementRepository,
        project_service=None,
    ):

        self.repository = repository

        self.element_repository = element_repository

        self.project_service = project_service

        self.document = PresentationDocument()

    # -------------------------------------------------

    def initialize(self):

        print("SlideService.initialize()")

    # -------------------------------------------------

    def shutdown(self):

        print("SlideService.shutdown()")

    # -------------------------------------------------

    @property
    def slides(self) -> list[Slide]:

        return self.document.slides

    # -------------------------------------------------

    def load(self):

        """
        Loads slides and all elements from database.
        """

        print("Loading slides...")

        self.document.slides.clear()

        slides = self.repository.get_all()

        for slide in slides:

            slide.elements = (
                self.element_repository.load_by_slide(
                    slide.id
                )
            )

            self.document.slides.append(slide)

        print(
            f"{self.count()} slide(s) loaded."
        )

    # -------------------------------------------------

    def clear(self):

        """
        Removes all slides and elements.
        """

        for slide in self.document.slides:

            self.element_repository.delete_by_slide(
                slide.id
            )

        self.repository.clear()

        self.document.slides.clear()

        self._mark_dirty()

    # -------------------------------------------------

    def replace_all(
        self,
        slides: list[Slide],
    ):

        """
        Replaces the current presentation.
        """

        self.clear()

        for slide in slides:

            self.repository.save(slide)

            self._save_elements(slide)

            self.document.slides.append(slide)

        self._mark_dirty()

    # -------------------------------------------------

    def add_existing_slide(
        self,
        slide: Slide,
    ):

        """
        Adds an already-created slide.
        """

        self.repository.save(slide)

        self._save_elements(slide)

        self.document.slides.append(slide)

        self._mark_dirty()

    # -------------------------------------------------

    def add_slide(self):

        """
        Creates a new empty slide.
        """

        slide = Slide()

        slide.order = self.count() + 1

        slide.title = f"Slide {slide.order}"

        slide.layout = "Title + Content"

        slide.status = "Draft"

        slide.ai_model = "GPT-5.5"

        now = datetime.now().isoformat(
            timespec="seconds"
        )

        slide.created_at = now

        slide.modified_at = now

        self.repository.save(slide)

        self.document.slides.append(slide)

        self._mark_dirty()

        print(
            f"Slide {slide.order} added."
        )

        return slide
        # -------------------------------------------------

    def delete_slide(
        self,
        index: int,
    ):

        """
        Deletes one slide.
        """

        slide = self.get(index)

        if slide is None:

            return

        self.element_repository.delete_by_slide(
            slide.id
        )

        self.repository.delete(
            slide.id
        )

        self.document.slides.pop(index)

        self.renumber()

        self._mark_dirty()

        print(
            f"Slide {slide.order} deleted."
        )

    # -------------------------------------------------

    def save_slide(
        self,
        slide: Slide,
    ):

        """
        Saves one slide and all its elements.
        """

        slide.modified_at = datetime.now().isoformat(
            timespec="seconds"
        )

        self.repository.save(
            slide
        )

        self.element_repository.delete_by_slide(
            slide.id
        )

        self._save_elements(
            slide
        )

        self._mark_dirty()

    # -------------------------------------------------

    def renumber(self):

        """
        Recalculates slide order.
        """

        now = datetime.now().isoformat(
            timespec="seconds"
        )

        for index, slide in enumerate(
            self.document.slides,
            start=1,
        ):

            slide.order = index

            slide.modified_at = now

            self.repository.save(
                slide
            )

    # -------------------------------------------------

    def get(
        self,
        index: int,
    ) -> Slide | None:

        if 0 <= index < self.count():

            return self.document.slides[index]

        return None

    # -------------------------------------------------

    def index_of(
        self,
        slide_id: str,
    ) -> int:

        for index, slide in enumerate(
            self.document.slides
        ):

            if slide.id == slide_id:

                return index

        return -1

    # -------------------------------------------------

    def count(self) -> int:

        return len(
            self.document.slides
        )
        
        # -------------------------------------------------

    def _save_elements(
        self,
        slide: Slide,
    ):

        """
        Saves all elements of a slide.
        """

        if not slide.elements:

            return

        for element in slide.elements:

            self.element_repository.save(
                slide.id,
                element,
            )

    # -------------------------------------------------

    def _mark_dirty(self):

        """
        Marks the project as modified.
        """

        if self.project_service is None:

            return

        self.project_service.mark_dirty()

    # -------------------------------------------------

    def find_by_id(
        self,
        slide_id: str,
    ) -> Slide | None:

        """
        Returns a slide by its ID.
        """

        for slide in self.document.slides:

            if slide.id == slide_id:

                return slide

        return None

    # -------------------------------------------------

    def exists(
        self,
        slide_id: str,
    ) -> bool:

        """
        Checks whether a slide exists.
        """

        return self.find_by_id(
            slide_id
        ) is not None

    # -------------------------------------------------

    def all(self) -> list[Slide]:

        """
        Returns editable slide collection.
        """

        return self.document.slides

    # -------------------------------------------------

    def last(self) -> Slide | None:

        """
        Returns last slide.
        """

        if not self.document.slides:

            return None

        return self.document.slides[-1]