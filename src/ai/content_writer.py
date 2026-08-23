"""
PresentationAI

Content Writer
"""

from __future__ import annotations

from src.models.presentation_plan import (
    PresentationPlan,
)

from src.models.presentation_draft import (
    PresentationDraft,
)

from src.models.draft_slide import (
    DraftSlide,
)


class ContentWriter:
    """
    Converts a PresentationPlan into a fully
    written PresentationDraft.

    Responsibilities
    ----------------
    • Normalize content
    • Clean text
    • Build DraftSlide objects
    • Generate summaries
    • Generate keywords
    """

    # -------------------------------------------------

    def write(
        self,
        plan: PresentationPlan,
    ) -> PresentationDraft:

        draft = PresentationDraft(

            title=plan.title,

            language=plan.language,

            theme=plan.theme,

            provider=plan.provider,

            model=plan.model,

        )

        for slide in plan.slides:

            draft.add_slide(

                self._build_slide(

                    slide

                )

            )

        draft.keywords = self._build_keywords(
            draft
        )

        draft.references = []

        return draft
        # -------------------------------------------------

    def _build_slide(
        self,
        plan_slide,
    ) -> DraftSlide:
        """
        Converts one PlannedSlide into DraftSlide.
        """

        draft = DraftSlide(

            order=plan_slide.order,

            title=self._build_title(
                plan_slide
            ),

            subtitle=self._build_subtitle(
                plan_slide
            ),

            layout=plan_slide.layout,

        )

        #
        # Content
        #

        draft.bullets = self._build_bullets(
            plan_slide
        )

        draft.notes = self._build_notes(
            plan_slide
        )

        draft.summary = self._build_summary(
            draft.bullets
        )

        #
        # Image
        #

        draft.image_required = (
            plan_slide.image_required
        )

        draft.image_prompt = (
            plan_slide.image_prompt
        )

        #
        # Charts / Tables
        #

        draft.chart_required = (
            plan_slide.chart_required
        )

        draft.table_required = (
            plan_slide.table_required
        )

        #
        # Metadata
        #

        draft.keywords = self._extract_keywords(
            draft
        )

        draft.references = []

        #
        # Animation
        #

        draft.transition = "Fade"

        draft.animation = "Appear"

        return draft

    # -------------------------------------------------

    def _build_title(
        self,
        slide,
    ) -> str:
        """
        Returns cleaned title.
        """

        return self._cleanup(
            slide.title
        )

    # -------------------------------------------------

    def _build_subtitle(
        self,
        slide,
    ) -> str:
        """
        Returns subtitle.
        """

        return self._cleanup(

            getattr(
                slide,
                "subtitle",
                "",
            )

        )

    # -------------------------------------------------

    def _build_bullets(
        self,
        slide,
    ) -> list[str]:
        """
        Cleans bullet list.
        """

        bullets = []

        for bullet in getattr(
            slide,
            "content",
            [],
        ):

            bullet = self._cleanup(
                bullet
            )

            if bullet:

                bullets.append(
                    bullet
                )

        return bullets
        # -------------------------------------------------

    def _build_notes(
        self,
        slide,
    ) -> str:
        """
        Builds speaker notes.
        """

        notes = getattr(
            slide,
            "speaker_notes",
            "",
        )

        return self._cleanup(
            notes
        )

    # -------------------------------------------------

    def _build_summary(
        self,
        bullets: list[str],
    ) -> str:
        """
        Creates a short summary from bullets.
        """

        if not bullets:

            return ""

        return " | ".join(

            bullets[:3]

        )

    # -------------------------------------------------

    def _extract_keywords(
        self,
        slide: DraftSlide,
    ) -> list[str]:
        """
        Extract simple keywords from a slide.
        """

        words = set()

        #
        # Title
        #

        words.update(

            slide.title.split()

        )

        #
        # Bullets
        #

        for bullet in slide.bullets:

            words.update(

                bullet.split()

            )

        #
        # Cleanup
        #

        keywords = []

        for word in words:

            word = word.strip()

            if len(word) >= 3:

                keywords.append(
                    word
                )

        return sorted(
            keywords
        )

    # -------------------------------------------------

    def _build_keywords(
        self,
        draft: PresentationDraft,
    ) -> list[str]:
        """
        Collects keywords from all slides.
        """

        keywords = set()

        for slide in draft:

            keywords.update(
                slide.keywords
            )

        return sorted(
            keywords
        )

    # -------------------------------------------------

    def _cleanup(
        self,
        text: str,
    ) -> str:
        """
        Normalizes text.
        """

        if not text:

            return ""

        text = str(text)

        text = text.replace(
            "\r",
            ""
        )

        text = text.replace(
            "\t",
            " "
        )

        text = text.strip()

        while "  " in text:

            text = text.replace(
                "  ",
                " ",
            )

        return text

    # -------------------------------------------------

    def _truncate(
        self,
        text: str,
        limit: int,
    ) -> str:
        """
        Limits text length.
        """

        text = self._cleanup(
            text
        )

        if len(text) <= limit:

            return text

        return text[:limit].rstrip() + "..."