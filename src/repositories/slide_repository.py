"""
PresentationAI

Slide Repository
"""

#from __future__ import annotations

from src.database.database_service import DatabaseService

import json


class SlideRepository:
    """
    Handles persistence of Slide objects.
    """

    # -------------------------------------------------

    def __init__(self, database: DatabaseService):

        self.database = database

    # -------------------------------------------------

    def save(self, slide):

        if self.exists(slide.id):

            self._update_slide(slide)

        else:

            self._insert_slide(slide)

        #
        # Save Elements (Next Release)
        #

        # self._save_elements(slide)

        self.database.commit()
    # -------------------------------------------------

    def _insert_slide(self, slide):

        self.database.execute(
            """
            INSERT INTO slides
            (
                id,
                title,
                subtitle,
                content,
                prompt,
                notes,
                layout,
                tags,
                status,
                ai_model,
                slide_order,
                created_at,
                modified_at
            )
            VALUES
            (
                ?,?,?,?,?,?,?,?,?,?,?,?,?
            )
            """,
            (
                slide.id,
                slide.title,
                slide.subtitle,
                slide.content,
                slide.prompt,
                slide.notes,
                slide.layout,
                slide.tags,
                slide.status,
                slide.ai_model,
                slide.order,
                slide.created_at,
                slide.modified_at,
            ),
        )

    # -------------------------------------------------

    def _update_slide(self, slide):

        self.database.execute(

            """
            UPDATE slides
            SET

                title=?,

                subtitle=?,

                content=?,

                prompt=?,

                notes=?,

                layout=?,

                tags=?,

                status=?,

                ai_model=?,

                slide_order=?,

                modified_at=?

            WHERE id=?
            """,

            (

                slide.title,

                slide.subtitle,

                slide.content,

                slide.prompt,

                slide.notes,

                slide.layout,

                slide.tags,

                slide.status,

                slide.ai_model,

                slide.order,

                slide.modified_at,

                slide.id,

            ),

        )


    # -------------------------------------------------

    def get(self, slide_id):

        return self.database.query_one(

            """
            SELECT
                id,
                title,
                subtitle,
                content,
                prompt,
                notes,
                layout,
                tags,
                status,
                ai_model,
                slide_order,
                created_at,
                modified_at
            FROM slides
            WHERE id=?
            """,

            (slide_id,),

        )

    # -------------------------------------------------

    def get_all(self):

        return self.database.query(

            """
            SELECT

                id,

                title,

                subtitle,

                content,

                prompt,

                notes,

                layout,

                tags,

                status,

                ai_model,

                slide_order,

                created_at,

                modified_at

            FROM slides

            ORDER BY slide_order
            """

        )

    # -------------------------------------------------

    def delete(self, slide_id):

        self.database.execute(

            "DELETE FROM slides WHERE id=?",

            (slide_id,)

        )


        self.database.commit()

    # -------------------------------------------------

    def clear(self):

        self.database.execute(

            "DELETE FROM slides"

        )

        self.database.commit()

    # -------------------------------------------------
    
    def _save_elements(self, slide):

        """
        Saves all slide elements.

        Implement in Release 0.8
        """

        pass
    
    def _load_elements(self, slide_id):

        """
        Loads all elements of one slide.

        Implement in Release 0.8
        """

        return []

    def count(self):

        row = self.database.query_one(

            """
            SELECT COUNT(*) AS total
            FROM slides
            """

        )

        return row["total"] if row else 0

    # -------------------------------------------------

    def exists(self, slide_id):

        row = self.database.query_one(

            "SELECT id FROM slides WHERE id=?",

            (slide_id,),

        )

        return row is not None
    
    
    
    def save_all(self, slides):

        self.clear()

        for slide in slides:

            if self.exists(slide.id):

                self._update_slide(slide)

            else:

                self._insert_slide(slide)

            # self._save_elements(slide)

        self.database.commit()