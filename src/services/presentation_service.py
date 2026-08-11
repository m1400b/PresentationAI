"""
PresentationAI

Presentation Service
"""

from __future__ import annotations

from src.core.service import BaseService

from src.ai.prompt_builder import (
    PromptRequest,
)

from src.ai.ai_client import AIClient

from src.ai.presentation_planner import (
    PresentationPlanner,
)

from src.ai.content_writer import (
    ContentWriter,
)

from src.services.slide_service import (
    SlideService,
)

from src.services.layout_engine import (
    LayoutEngine,
)


class PresentationService(BaseService):
    """
    Complete Presentation Pipeline

        PromptRequest
              │
              ▼
           AIClient
              │
              ▼
      PresentationPlanner
              │
              ▼
         ContentWriter
              │
              ▼
         LayoutEngine
              │
              ▼
          SlideService
    """

    # -------------------------------------------------

    def __init__(
        self,
        slide_service: SlideService,
        layout_engine: LayoutEngine,
        ai_client: AIClient,
    ):

        self.slide_service = slide_service

        self.layout_engine = layout_engine

        self.ai_client = ai_client

        self.planner = PresentationPlanner()

        self.writer = ContentWriter()

    # -------------------------------------------------

    def initialize(self):

        pass

    # -------------------------------------------------

    def shutdown(self):

        pass

    # -------------------------------------------------

    def generate(
        self,
        request: PromptRequest,
    ):

        #
        # 1) AI
        #

        response = self.ai_client.generate(
            request
        )

        #
        # 2) JSON -> PresentationPlan
        #

        plan = self.planner.build_plan(
            response,
             request,
        )

        #
        # 3) PresentationPlan -> PresentationDraft
        #

        draft = self.writer.write(
            plan
        )

        #
        # 4) Draft -> Editable Slides
        #

        slides = self.layout_engine.build(
            draft
        )

        #
        # 5) Store Slides
        #

        self.slide_service.replace_all(
            slides
        )

        return slides

    # -------------------------------------------------

    def regenerate(
        self,
        request: PromptRequest,
    ):

        return self.generate(request)