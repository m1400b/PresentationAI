"""
PresentationAI

Slide Renderer
"""

from __future__ import annotations

from src.models.slide import Slide

from src.models.elements.text_element import TextElement
from src.models.elements.image_element import ImageElement
from src.models.elements.chart_element import ChartElement

from src.renderers.text_renderer import TextRenderer
from src.renderers.image_renderer import ImageRenderer
from src.renderers.chart_renderer import ChartRenderer


class SlideRenderer:
    """
    Renders one Slide into a PowerPoint slide.
    """

    # -------------------------------------------------

    def __init__(self):

        self.renderers = {

        TextElement: TextRenderer(),

        ImageElement: ImageRenderer(),

        ChartElement: ChartRenderer(),

    }

    # -------------------------------------------------

    def render(
        self,
        ppt_slide,
        slide: Slide,
    ):

        if slide is None:

            return

        for element in slide.elements:

            self.render_element(
                ppt_slide,
                element,
            )

    # -------------------------------------------------

    def render_element(
    self,
    ppt_slide,
    element,
):

        renderer = self.renderers.get(type(element))

        if renderer is None:

            return

        renderer.render(
            ppt_slide,
            element,
        )

    def register_renderer(
    self,
    element_type,
    renderer,
):

        self.renderers[element_type] = renderer
        
        #
        # Future:
        #
        # ShapeElement
        # TableElement
        # IconElement
        # VideoElement
        #