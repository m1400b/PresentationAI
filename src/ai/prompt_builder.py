"""
PresentationAI

Prompt Builder
"""

from __future__ import annotations

from src.ai.prompt_request import (
    PromptRequest,
)
from dataclasses import dataclass

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
    Builds AI prompts from
    PromptRequest objects.
    """

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
            "Always return valid JSON only.\n"
            "Do not include markdown, explanations or "
            "additional text."
        )
        # -------------------------------------------------

    # -------------------------------------------------
    # User Prompt
    # -------------------------------------------------

    def build_user_prompt(
        self,
        request: PromptRequest,
    ) -> str:
        """
        Builds the user prompt.
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

        if request.prompt:

            lines.append(
                f"Additional Instructions: "
                f"{request.prompt}"
            )

        lines.append(
            f"Slide Count: {request.slide_count}"
        )

        lines.append(
            f"Language: {request.language}"
        )

        lines.append(
            f"Audience: {request.audience}"
        )

        lines.append(
            f"Purpose: {request.purpose}"
        )

        lines.append(
            f"Style: {request.style}"
        )

        lines.append(
            f"Theme: {request.theme}"
        )

        # -------------------------------------------------
        # AI Configuration
        # -------------------------------------------------

        lines.append("")

        lines.append(
            "AI CONFIGURATION"
        )

        lines.append(
            f"Provider: {request.provider}"
        )

        lines.append(
            f"Model: {request.model or 'Auto'}"
        )

        lines.append(
            f"Creativity: {request.creativity}"
        )

        lines.append(
            f"Temperature: {request.temperature}"
        )

        lines.append(
            f"Maximum Tokens: {request.max_tokens}"
        )

        # -------------------------------------------------
        # Content Requirements
        # -------------------------------------------------

        lines.append("")

        lines.append(
            "CONTENT REQUIREMENTS"
        )

        if request.include_images:

            lines.append(
                "- Include image suggestions."
            )

        if request.include_charts:

            lines.append(
                "- Include charts where appropriate."
            )

        if request.include_tables:

            lines.append(
                "- Include tables where appropriate."
            )

        if request.include_notes:

            lines.append(
                "- Generate speaker notes."
            )

        if request.include_references:

            lines.append(
                "- Include references."
            )

            lines.append(
                f"- Citation style: "
                f"{request.citation_style}"
            )

        if request.include_agenda:

            lines.append(
                "- Include an agenda slide."
            )

        if request.include_summary:

            lines.append(
                "- Include a summary slide."
            )

        if request.include_thankyou:

            lines.append(
                "- Include a final thank-you slide."
            )

        # -------------------------------------------------
        # Visual Requirements
        # -------------------------------------------------

        lines.append("")

        lines.append(
            "VISUAL REQUIREMENTS"
        )

        if request.generate_images:

            lines.append(
                "- Generate image prompts "
                "for relevant slides."
            )

            lines.append(
                f"- Image provider: "
                f"{request.image_provider}"
            )

        if request.chart_style:

            lines.append(
                f"- Chart style: "
                f"{request.chart_style}"
            )

        if request.use_branding:

            lines.append(
                "- Apply company branding."
            )

        if request.use_company_template:

            lines.append(
                "- Use the company presentation template."
            )

        # -------------------------------------------------
        # Data Sources
        # -------------------------------------------------

        lines.append("")

        lines.append(
            "DATA SOURCES"
        )

        if request.use_local_documents:

            lines.append(
                "- Local documents may be used "
                "as source material."
            )

        if request.search_web:

            lines.append(
                "- Web search is allowed "
                "for additional information."
            )

        # -------------------------------------------------
        # Language / Direction
        # -------------------------------------------------

        lines.append("")

        lines.append(
            "LANGUAGE AND DIRECTION"
        )

        lines.append(
            f"- RTL: "
            f"{'Yes' if request.rtl else 'No'}"
        )

        # -------------------------------------------------
        # Additional Notes
        # -------------------------------------------------

        if request.extra:

            lines.append("")

            lines.append(
                "ADDITIONAL REQUIREMENTS"
            )

            lines.append(
                request.extra
            )

        # -------------------------------------------------
        # Output
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
            "- Do not add explanations "
            "before or after the JSON."
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
            "layout": "Title Slide",
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
    
    def build_messages(
        self,
        request: PromptRequest,
    ) -> list[dict[str, str]]:
        """
        Builds chat messages for
        AI providers.
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

    def __call__(
        self,
        request: PromptRequest,
    ) -> str:
        """
        Shortcut for build().
        """

        return self.build(
            request,
        )

    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return "<PromptBuilder>"