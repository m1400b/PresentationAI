"""
PresentationAI

Base Renderer
"""


class BaseRenderer:

    def render(
        self,
        ppt_slide,
        element
    ):

        raise NotImplementedError()