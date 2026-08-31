"""
PresentationAI

Prompt Builder
"""

from __future__ import annotations

from dataclasses import dataclass

from src.ai.prompt_request import (
    PromptRequest,
)


@dataclass(slots=True)
class PromptBundle:
    """
    Complete prompt package sent to an AI provider.
    """

    system_prompt: str
    user_prompt: str
    response_schema: str


class PromptBuilder:
    """
    Builds AI prompts from PromptRequest objects.

    PromptBuilder is intentionally kept independent
    from specific AI providers.
    """

    # -------------------------------------------------
    # Main
    # -------------------------------------------------

    def build(
        self,
        request: PromptRequest,
    ) -> PromptBundle:
        """
        Builds a complete prompt bundle.
        """

        return PromptBundle(
            system_prompt=self.build_system_prompt(
                request,
            ),
            user_prompt=self.build_user_prompt(
                request,
            ),
            response_schema=self.build_output_format(
                request,
            ),
        )

    # -------------------------------------------------
    # System Prompt
    # -------------------------------------------------

    def build_system_prompt(
        self,
        request: PromptRequest,
    ) -> str:
        """
        Builds the system prompt.
        """

        return (
            "You are an expert presentation designer.\n"
            "Create professional, structured and visually "
            "balanced presentations.\n"
            "Follow the requested topic, language, audience "
            "and theme.\n"
            "Always return valid JSON only.\n"
            "Do not include Markdown, explanations or "
            "additional text outside the JSON object."
        )

    # -------------------------------------------------
    # User Prompt
    # -------------------------------------------------

    def build_user_prompt(
        self,
        request: PromptRequest,
    ) -> str:
        """
        Builds the user prompt from the current
        PromptRequest contract.
        """

        lines: list[str] = []

        # -------------------------------------------------
        # Presentation
        # -------------------------------------------------

        lines.append(
            "PRESENTATION"
        )

        lines.append(
            f"Topic: {request.topic}"
        )

        lines.append(
            f"Slide Count: {request.slide_count}"
        )

        lines.append(
            f"Language: {request.language}"
        )

        lines.append(
            f"Audience: "
            f"{request.audience or 'General audience'}"
        )

        lines.append(
            f"Theme: {request.theme}"
        )

        # -------------------------------------------------
        # Additional Notes
        # -------------------------------------------------

        if request.has_notes:

            lines.append("")

            lines.append(
                "ADDITIONAL NOTES"
            )

            lines.append(
                request.notes
            )

        # -------------------------------------------------
        # Provider Configuration
        # -------------------------------------------------

        lines.append("")

        lines.append(
            "AI CONFIGURATION"
        )

        lines.append(
            f"Provider: {request.provider}"
        )

        lines.append(
            "Online Providers: "
            f"{'Allowed' if request.online_enabled else 'Disabled'}"
        )

        lines.append(
            "Offline Only: "
            f"{'Yes' if request.offline_only else 'No'}"
        )

        # -------------------------------------------------
        # Metadata
        # -------------------------------------------------

        if request.metadata:

            lines.append("")

            lines.append(
                "ADDITIONAL CONFIGURATION"
            )

            for key, value in request.metadata.items():

                lines.append(
                    f"{key}: {value}"
                )

        # -------------------------------------------------
        # Output Requirements
        # -------------------------------------------------

        lines.append("")

        lines.append(
            "OUTPUT REQUIREMENTS"
        )

        lines.append(
            "- Return only valid JSON."
        )

        lines.append(
            "- Do not use Markdown."
        )

        lines.append(
            "- Do not add explanations before or after JSON."
        )

        lines.append(
            "- Generate exactly the requested number of slides."
        )

        lines.append(
            "- Every slide must have a layout and title."
        )

        lines.append(
            "- Content must be an array of strings."
        )

        lines.append(
            "- Use image_prompt when a visual is appropriate."
        )

        lines.append(
            "- Use speaker_notes when useful."
        )

        lines.append("")

        lines.append(
            self.build_output_format(
                request,
            )
        )

        return "\n".join(
            lines
        )

    # -------------------------------------------------
    # Output Format
    # -------------------------------------------------

    def build_output_format(
        self,
        request: PromptRequest,
    ) -> str:
        """
        Builds the required JSON output format.
        """

        return """
Return a JSON object using exactly this structure:

{
    "title": "Presentation title",
    "slides": [
        {
            "layout": "Title",
            "title": "Slide title",
            "subtitle": "Slide subtitle",
            "content": [
                "Content item 1",
                "Content item 2"
            ],
            "image_prompt": "Detailed image generation prompt",
            "speaker_notes": "Speaker notes"
        }
    ]
}

Rules:

- The root object must contain "title".
- The root object must contain "slides".
- "slides" must be an array.
- Every slide must have a "layout".
- Every slide must have a "title".
- "subtitle" must be a string.
- "content" must be an array of strings.
- "image_prompt" must be a string.
- "speaker_notes" must be a string.
- Do not add fields outside this structure.
- Return valid JSON only.
"""

    # -------------------------------------------------
    # Messages
    # -------------------------------------------------

    def build_messages(
        self,
        request: PromptRequest,
    ) -> list[dict[str, str]]:
        """
        Builds chat messages for AI providers.
        """

        return [
            {
                "role": "system",
                "content": self.build_system_prompt(
                    request,
                ),
            },
            {
                "role": "user",
                "content": self.build_user_prompt(
                    request,
                ),
            },
        ]

    # -------------------------------------------------
    # Shortcut
    # -------------------------------------------------

    def __call__(
        self,
        request: PromptRequest,
    ) -> PromptBundle:
        """
        Shortcut for build().
        """

        return self.build(
            request,
        )

    # -------------------------------------------------
    # Representation
    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return "<PromptBuilder>"

