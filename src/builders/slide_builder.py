from src.models.slide import Slide

from src.models.elements.text_element import TextElement

from src.models.elements.image_element import ImageElement


class SlideBuilder:

    def build(self, draft):

        slide = Slide()

        slide.title = draft.title

        slide.layout = draft.layout

        slide.image_prompt = draft.image_prompt

        slide.bullets = draft.bullets.copy()

        slide.notes = draft.notes

        # ---------- Title ----------

        slide.elements.append(

            TextElement(

                text=draft.title,

                x=1,

                y=0.5,

                width=24,

                height=1,

                font_size=30,

                bold=True,

                align="center",

            )

        )

        # ---------- Content ----------

        body = "\n".join(

            "• " + b

            for b in draft.bullets

        )

        slide.elements.append(

            TextElement(

                text=body,

                x=1,

                y=2,

                width=12,

                height=8,

                font_size=22,

            )

        )

        # ---------- Image ----------

        if draft.image_prompt:

            slide.elements.append(

                ImageElement(

                    x=14,

                    y=2,

                    width=8,

                    height=8,

                    caption=draft.image_prompt,

                )

            )

        return slide