"""
PresentationAI

Content Generator Service
"""

from src.ai.providers.base_ai_provider import BaseAIProvider
from src.models.presentation_plan import PresentationPlan
from src.models.presentation_draft import PresentationDraft


class ContentGeneratorService:
    """
    Generates presentation content using the configured AI provider.
    """

    # -------------------------------------------------

    def __init__(self, provider: BaseAIProvider):

        self.provider = provider

    # -------------------------------------------------

    def generate(
        self,
        plan: PresentationPlan
    ) -> PresentationDraft:

        return self.provider.generate(plan)