"""
PresentationAI

Presentation Service
"""

from __future__ import annotations


from src.models.presentation import Presentation
from src.models.presentation_plan import PresentationPlan


class PresentationService:
    """
    High level presentation workflow.

    Responsibilities
    ----------------
    • Generate presentation
    • Build presentation model
    • Render output
    • Manage pipeline
    """


    def __init__(
        self,
        ai_client,
        planner,
        writer,
        layout_engine,
        renderer,
        theme,
    ):

        self.ai_client = ai_client

        self.planner = planner

        self.writer = writer

        self.layout_engine = layout_engine

        self.renderer = renderer

        self.theme = theme


        self.current_presentation = None


    # =================================================
    # Generate
    # =================================================

    def generate(
        self,
        request,
    ) -> Presentation:
        """
        Full AI pipeline.
        """


        result = self.ai_client.generate(
            request
        )


        plan = self.planner.build_plan(
            result,
            request,
        )


        draft = self.writer.write(
            plan
        )


        presentation = self.layout_engine.build(
            draft,
            self.theme,
        )


        self.current_presentation = presentation


        return presentation



    # =================================================
    # Render
    # =================================================

    def render(
        self,
        output_path: str,
    ) -> str:
        """
        Export current presentation.
        """

        if self.current_presentation is None:

            raise RuntimeError(
                "No presentation available."
            )


        return self.renderer.render(
            self.current_presentation,
            output_path,
        )



    # =================================================
    # Build from plan
    # =================================================

    def build_from_plan(
        self,
        plan: PresentationPlan,
    ):

        draft = self.writer.write(
            plan
        )


        presentation = self.layout_engine.build(
            draft,
            self.theme,
        )


        self.current_presentation = presentation


        return presentation



    # =================================================
    # Properties
    # =================================================

    @property
    def presentation(
        self,
    ):

        return self.current_presentation



    def clear(
        self,
    ):

        self.current_presentation = None