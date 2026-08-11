"""
PresentationAI

Element Repository
"""

from __future__ import annotations

import json
from dataclasses import asdict

from src.database.database_service import DatabaseService

from src.models.elements.text_element import TextElement
from src.models.elements.image_element import ImageElement
from src.models.elements.chart_element import ChartElement


class ElementRepository:
    """
    Handles persistence of slide elements.
    """

    # -------------------------------------------------

    def __init__(
        self,
        database: DatabaseService,
    ):

        self.database = database

    # -------------------------------------------------

    def save(
        self,
        slide_id: str,
        element,
    ):

        row = self.database.query_one(

            "SELECT id FROM elements WHERE id=?",

            (element.id,),

        )

        if row:

            self._update(slide_id, element)

        else:

            self._insert(slide_id, element)

    # -------------------------------------------------

    def _insert(
        self,
        slide_id: str,
        element,
    ):

        self.database.execute(

            """
            INSERT INTO elements
            (
                id,
                slide_id,
                type,
                name,
                x,
                y,
                width,
                height,
                rotation,
                z_index,
                visible,
                locked,
                opacity,
                data,
                created_at,
                modified_at
            )
            VALUES
            (
                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
            )
            """,

            (

                element.id,

                slide_id,

                element.type,

                element.name,

                element.x,

                element.y,

                element.width,

                element.height,

                element.rotation,

                element.z_index,

                int(element.visible),

                int(element.locked),

                element.opacity,

                json.dumps(
                    self._extra_data(element),
                    ensure_ascii=False,
                ),

                element.created_at,

                element.modified_at,

            ),

        )

        self.database.commit()
    # -------------------------------------------------
    
    def _update(
        self,
        slide_id: str,
        element,
    ):

        self.database.execute(

            """
            UPDATE elements
            SET

                slide_id=?,

                type=?,

                name=?,

                x=?,

                y=?,

                width=?,

                height=?,

                rotation=?,

                z_index=?,

                visible=?,

                locked=?,

                opacity=?,

                data=?,

                modified_at=?

            WHERE id=?
            """,

            (

                slide_id,

                element.type,

                element.name,

                element.x,

                element.y,

                element.width,

                element.height,

                element.rotation,

                element.z_index,

                int(element.visible),

                int(element.locked),

                element.opacity,

                json.dumps(
                    self._extra_data(element),
                    ensure_ascii=False,
                ),

                element.modified_at,

                element.id,

            ),

        )

        self.database.commit()
    # -------------------------------------------------

    def load_by_slide(
        self,
        slide_id,
    ):

        rows = self.database.query(

            """
            SELECT *
            FROM elements
            WHERE slide_id=?
            ORDER BY rowid
            """,

            (slide_id,),

        )

        elements = []

        for row in rows:

            element = self._create_element(row)

            if element:

                elements.append(element)

        return elements

    # -------------------------------------------------

    def delete(
        self,
        element_id,
    ):

        self.database.execute(

            "DELETE FROM elements WHERE id=?",

            (element_id,),

        )

        self.database.commit()

    # -------------------------------------------------

    def delete_by_slide(
        self,
        slide_id,
    ):

        self.database.execute(

            "DELETE FROM elements WHERE slide_id=?",

            (slide_id,),

        )

        self.database.commit()

    # -------------------------------------------------

    def _create_element(
        self,
        row,
    ):
    
        element_type = row["type"]
    
        if element_type == "Text":
            element = TextElement()
    
        elif element_type == "Image":
            element = ImageElement()
    
        elif element_type == "Chart":
            element = ChartElement()
    
        else:
            return None
    
        # -------------------------------------------------
        # Base properties
        # -------------------------------------------------
    
        element.id = row["id"]
    
        element.type = row["type"]
    
        element.x = row["x"]
    
        element.y = row["y"]
    
        element.width = row["width"]
    
        element.height = row["height"]
    
        element.rotation = row["rotation"]
    
        element.name = row["name"] or ""

        element.z_index = row["z_index"]
        
        element.opacity = row["opacity"]

        element.visible = bool(row["visible"])
    
        element.locked = bool(row["locked"])
    
        element.created_at = row["created_at"]
    
        element.modified_at = row["modified_at"]
    
        # -------------------------------------------------
        # Extra properties
        # -------------------------------------------------
    
        try:
        
            data = json.loads(row["data"] or "{}")
    
        except Exception:
        
            data = {}
    
        for key, value in data.items():
        
            if hasattr(element, key):
            
                setattr(
                    element,
                    key,
                    value,
                )
    
        return element
    # -------------------------------------------------

    def _extra_data(
        self,
        element,
    ):

        data = asdict(element)

        ignored = {

            # -------------------------------------------------
            # Base Element
            # -------------------------------------------------

            "id",

            "type",

            "name",

            "x",

            "y",

            "width",

            "height",

            "rotation",

            "z_index",

            "visible",

            "locked",

            "opacity",

            "selected",

            "created_at",

            "modified_at",

        }

        return {

            key: value

            for key, value in data.items()

            if key not in ignored

        }