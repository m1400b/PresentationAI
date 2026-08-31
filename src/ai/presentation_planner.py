"""
PresentationAI

Presentation Planner
"""

from __future__ import annotations

import json

from src.ai.layout_registry import (
    normalize_layout,
)

from src.ai.prompt_request import (
    PromptRequest,
)

from src.models.presentation_plan import (
    PresentationPlan,
)

from src.models.planned_slide import (
    PlannedSlide,
)


class PresentationPlanner:
    """
    Converts raw AI JSON into a normalized
    PresentationPlan.

    Responsibilities
    ----------------
    • Parse AI response
    • Validate structure
    • Normalize layouts
    • Normalize text
    • Detect image/chart/table needs
    • Build PresentationPlan
    """

    # -------------------------------------------------
    # Main
    # -------------------------------------------------

    def build_plan(
        self,
        response: str,
        request: PromptRequest | None = None,
    ) -> PresentationPlan:
        """
        Converts an AI response into a PresentationPlan.

        The original PromptRequest is optional so the
        planner can preserve presentation and AI metadata.
        """

        data = self._parse_json(
            response
        )

        title = self._normalize_text(
            data.get(
                "title",
                (
                    request.topic
                    if request is not None
                    else "Untitled Presentation"
                ),
            )
        )

        # -------------------------------------------------
        # Create Plan
        # -------------------------------------------------

        plan = PresentationPlan(
            title=title,
            prompt=(
    request.notes
    if request is not None
    else ""
),
            language=(
                request.language
                if request is not None
                else "Persian"
            ),
            audience=(
                request.audience
                if request is not None
                else ""
            ),
            tone="Professional",
            theme=(
                request.theme
                if request is not None
                else "Corporate"
            ),
            provider=(
                request.provider
                if request is not None
                else "Auto"
            ),
            model="",
        )

        # -------------------------------------------------
        # Slides
        # -------------------------------------------------

        slides = self._safe_list(
            data.get(
                "slides",
            )
        )

        for index, item in enumerate(
            slides,
            start=1,
        ):

            if not isinstance(
                item,
                dict,
            ):
                continue

            plan.add_slide(
                self._build_slide(
                    index,
                    item,
                )
            )

        return plan

    # -------------------------------------------------
    # JSON
    # -------------------------------------------------

    def _parse_json(
        self,
        response: str,
    ) -> dict:
        """
        Parses AI response into a dictionary.
        """

        if not response or not response.strip():

            raise ValueError(
                "AI returned an empty response."
            )

        try:

            data = json.loads(
                response
            )

        except json.JSONDecodeError as exc:

            raise ValueError(
                "Invalid JSON returned by AI."
            ) from exc

        # -------------------------------------------------
        # Optional presentation wrapper
        # -------------------------------------------------

        if (
            isinstance(data, dict)
            and "presentation" in data
        ):

            data = data[
                "presentation"
            ]

        if not isinstance(
            data,
            dict,
        ):

            raise ValueError(
                "Presentation root must be an object."
            )

        return data

    # -------------------------------------------------
    # Safe List
    # -------------------------------------------------

    def _safe_list(
        self,
        value,
    ) -> list:

        if value is None:

            return []

        if isinstance(
            value,
            list,
        ):

            return value

        return [value]

    # -------------------------------------------------
    # Text
    # -------------------------------------------------

    def _normalize_text(
        self,
        text,
    ) -> str:

        if text is None:

            return ""

        text = str(
            text
        )

        text = text.replace(
            "\r",
            "",
        )

        text = text.strip()

        while "  " in text:

            text = text.replace(
                "  ",
                " ",
            )

        return text

    # -------------------------------------------------
    # Slide
    # -------------------------------------------------

    def _build_slide(
        self,
        order: int,
        item: dict,
    ) -> PlannedSlide:
        """
        Builds one normalized PlannedSlide.
        """

        title = self._normalize_text(
            item.get(
                "title",
                f"Slide {order}",
            )
        )

        bullets = self._normalize_bullets(
            item.get(
                "content",
                [],
            )
        )

        image_prompt = self._normalize_text(
            item.get(
                "image_prompt",
                "",
            )
        )

        notes = self._normalize_text(
            item.get(
                "speaker_notes",
                "",
            )
        )

        layout = self._choose_layout(
            item.get(
                "layout",
                "",
            ),
            bullets,
            image_prompt,
        )

        slide = PlannedSlide(
            order=order,
            title=title,
            objective=title,
            layout=layout,
        )
        

        # -------------------------------------------------
        # Optional Data
        # -------------------------------------------------

        slide.subtitle = self._normalize_text(
            item.get(
                "subtitle",
                "",
            )
        )

        slide.content = bullets

        slide.image_prompt = image_prompt

        slide.speaker_notes = notes

        # -------------------------------------------------
        # Requirements
        # -------------------------------------------------

        slide.image_required = (
            self._detect_image(
                image_prompt
            )
        )

        slide.estimated_bullets = (
            self._estimate_bullets(
                bullets
            )
        )
        
        slide.chart_required = (
    self._detect_chart(
        bullets
    )
)

        slide.table_required = (
            self._detect_table(
                bullets
            )
        )
        
        return slide
        

    # -------------------------------------------------
    # Bullets
    # -------------------------------------------------

    def _normalize_bullets(
        self,
        value,
    ) -> list[str]:

        bullets = []

        if value is None:

            return bullets

        if isinstance(
            value,
            str,
        ):

            value = [
                value
            ]

        if not isinstance(
            value,
            list,
        ):

            return bullets

        for item in value:

            text = self._normalize_text(
                item
            )

            if text:

                bullets.append(
                    text
                )

        return bullets

    # -------------------------------------------------
    # Detection
    # -------------------------------------------------

    def _detect_image(
        self,
        image_prompt: str,
    ) -> bool:

        return bool(
            image_prompt.strip()
        )

    # -------------------------------------------------

    def _detect_chart(
        self,
        bullets: list[str],
    ) -> bool:

        keywords = (
            "chart",
            "graph",
            "trend",
            "growth",
            "statistics",
            "percent",
            "comparison",
            "نمودار",
            "آمار",
            "روند",
            "درصد",
            "مقایسه",
        )

        text = " ".join(
            bullets
        ).lower()

        return any(
            keyword in text
            for keyword in keywords
        )

    # -------------------------------------------------

    def _detect_table(
        self,
        bullets: list[str],
    ) -> bool:

        keywords = (
            "table",
            "rows",
            "columns",
            "جدول",
            "ردیف",
            "ستون",
        )

        text = " ".join(
            bullets
        ).lower()

        return any(
            keyword in text
            for keyword in keywords
        )

    # -------------------------------------------------

    def _estimate_bullets(
        self,
        bullets: list[str],
    ) -> int:

        return len(
            bullets
        )

    # -------------------------------------------------
    # Layout
    # -------------------------------------------------

    def _choose_layout(
        self,
        ai_layout: str,
        bullets: list[str],
        image_prompt: str,
    ) -> str:
        """
        Selects the most appropriate layout.
        """

        if ai_layout:

            return normalize_layout(
                ai_layout
            )

        if image_prompt:

            return normalize_layout(
                "title_image"
            )

        count = len(
            bullets
        )

        if count <= 6:

            return normalize_layout(
                "title_content"
            )

        if count <= 10:

            return normalize_layout(
                "two_columns"
            )

        return normalize_layout(
            "agenda"
        )