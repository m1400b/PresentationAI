"""
PresentationAI

Slides List Model
"""

from PySide6.QtCore import (
    Qt,
    QAbstractListModel,
    QModelIndex,
)

from src.services.slide_service import SlideService


class SlidesModel(QAbstractListModel):

    # -------------------------------------------------

    def __init__(

        self,

        slide_service: SlideService,

    ):

        super().__init__()

        self.slide_service = slide_service

    # -------------------------------------------------

    def rowCount(

        self,

        parent=QModelIndex(),

    ):

        return self.slide_service.count()

    # -------------------------------------------------

    def data(

        self,

        index,

        role=Qt.DisplayRole,

    ):

        if not index.isValid():

            return None

        slide = self.slide_service.get(

            index.row()

        )

        if slide is None:

            return None

        if role == Qt.DisplayRole:

            return (

                f"{slide.order}. "

                f"{slide.title}"

            )

        return None

    # -------------------------------------------------

    def refresh(self):

        self.beginResetModel()

        self.endResetModel()