"""
PresentationAI

Planned Slide Model
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class PlannedSlide:
    """
    One slide inside a PresentationPlan.
    """

    order: int = 0

    title: str = ""

    subtitle: str = ""

    objective: str = ""

    layout: str = "Title + Content"

    content: list[str] = field(
        default_factory=list
    )

    image_prompt: str = ""

    speaker_notes: str = ""

    image_required: bool = False

    chart_required: bool = False

    table_required: bool = False

    estimated_bullets: int = 0