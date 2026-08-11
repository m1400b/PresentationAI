"""
PresentationAI

Slide Renderer
"""

from src.models.slide import Slide
from src.models.elements.text_element import TextElement
from src.models.elements.image_element import ImageElement


class SlideRenderer:
    """
    Converts Slide data into drawable elements.

    This renderer is idempotent.
    Calling render() multiple times produces
    the same visual result.
    """

    # -------------------------------------------------

    def render(self, slide: Slide):

        slide.elements.clear()

        layout = slide.layout

        if layout == "Title":

            self._render_title(slide)

        elif layout == "Title + Content":

            self._render_title_content(slide)

        elif layout == "Two Columns":

            self._render_two_columns(slide)

        elif layout == "Blank":

            pass

        else:

            self._render_title_content(slide)

    # -------------------------------------------------

    def render_all(self, slides):

        for slide in slides:

            self.render(slide)

    # -------------------------------------------------

    def _render_title(self, slide):

        title = TextElement()

        title.text = slide.title

        title.x = 40
        title.y = 40

        title.width = 840
        title.height = 60

        title.font_size = 30
        title.bold = True

        slide.elements.append(title)

    # -------------------------------------------------

    def _render_title_content(self, slide):

        title = TextElement()

        title.text = slide.title

        title.x = 40
        title.y = 30

        title.width = 840
        title.height = 60

        title.font_size = 28
        title.bold = True

        slide.elements.append(title)

        body = TextElement()

        body.text = "\n".join(

            f"• {x}"

            for x in slide.bullets

        )

        body.x = 60
        body.y = 120

        body.width = 820
        body.height = 320

        body.font_size = 20

        slide.elements.append(body)

        if slide.image_prompt:

            image = ImageElement()

            image.x = 640
            image.y = 120

            image.width = 220
            image.height = 220

            image.caption = slide.image_prompt

            slide.elements.append(image)

    # -------------------------------------------------

    def _render_two_columns(self, slide):

        title = TextElement()

        title.text = slide.title

        title.x = 40
        title.y = 30

        title.width = 840
        title.height = 60

        title.font_size = 28
        title.bold = True

        slide.elements.append(title)

        half = len(slide.bullets) // 2

        left = TextElement()

        left.text = "\n".join(

            f"• {x}"

            for x in slide.bullets[:half]

        )

        left.x = 50
        left.y = 120

        left.width = 360
        left.height = 320

        slide.elements.append(left)

        right = TextElement()

        right.text = "\n".join(

            f"• {x}"

            for x in slide.bullets[half:]

        )

        right.x = 470
        right.y = 120

        right.width = 360
        right.height = 320

        slide.elements.append(right)