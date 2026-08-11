"""
PresentationAI

Presentation Document
"""

from dataclasses import dataclass, field
from datetime import datetime
import uuid

from src.models.slide import Slide


@dataclass(slots=True)
class PresentationDocument:
    """
    Complete editable presentation.
    """

    # -------------------------------------------------
    # Identity
    # -------------------------------------------------

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    title: str = "Untitled Presentation"

    subject: str = ""

    description: str = ""

    author: str = ""

    company: str = ""

    language: str = "fa"

    # -------------------------------------------------
    # Theme
    # -------------------------------------------------

    theme: str = "Default"

    slide_width: int = 960

    slide_height: int = 540

    # -------------------------------------------------
    # Content
    # -------------------------------------------------

    slides: list[Slide] = field(
        default_factory=list
    )

    # -------------------------------------------------
    # State
    # -------------------------------------------------

    dirty: bool = False

    selected_slide: int = -1

    # -------------------------------------------------
    # History
    # -------------------------------------------------

    undo_stack: list = field(
        default_factory=list
    )

    redo_stack: list = field(
        default_factory=list
    )

    # -------------------------------------------------
    # Metadata
    # -------------------------------------------------

    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(
            timespec="seconds"
        )
    )

    modified_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(
            timespec="seconds"
        )
    )

    # =================================================
    # Helpers
    # =================================================

    @property
    def slide_count(self) -> int:

        return len(self.slides)

    # -------------------------------------------------

    def clear(self):

        self.slides.clear()

        self.selected_slide = -1

        self.dirty = False

        self.undo_stack.clear()

        self.redo_stack.clear()

    # -------------------------------------------------

    def mark_dirty(self):

        self.dirty = True

        self.modified_at = datetime.now().isoformat(
            timespec="seconds"
        )

    # -------------------------------------------------

    def mark_saved(self):

        self.dirty = False