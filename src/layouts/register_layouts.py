from src.ai.layout_registry import LayoutRegistry

from src.layouts.title_slide_layout import (
    TitleSlideLayout,
)

from src.layouts.title_content_layout import (
    TitleContentLayout,
)
from src.layouts.two_columns_layout import (
    TwoColumnsLayout,
)

def create_default_layout_registry():

    registry = LayoutRegistry()

    registry.register(
        TitleSlideLayout()
    )

    registry.register(
        TitleContentLayout()
    )
    registry.register(
    TwoColumnsLayout()
)

    return registry