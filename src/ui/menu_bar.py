"""
PresentationAI

Menu Bar
"""

from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMenuBar


def build_menu_bar(window):

    menu_bar = QMenuBar()

    # ----------------------------------------------------
    # File
    # ----------------------------------------------------

    file_menu = menu_bar.addMenu("&File")

    action_new = QAction("New Project", window)
    action_new.setShortcut(QKeySequence.New)

    action_open = QAction("Open Project", window)
    action_open.setShortcut(QKeySequence.Open)

    action_save = QAction("Save Project", window)
    action_save.setShortcut(QKeySequence.Save)

    action_exit = QAction("Exit", window)
    action_exit.setShortcut(QKeySequence.Quit)

    action_new.triggered.connect(window.new_project)
    action_open.triggered.connect(window.open_project)
    action_save.triggered.connect(window.save_project)
    action_exit.triggered.connect(window.close)

    file_menu.addAction(action_new)
    file_menu.addAction(action_open)

    file_menu.addSeparator()

    file_menu.addAction(action_save)

    file_menu.addSeparator()

    file_menu.addAction(action_exit)

    # ----------------------------------------------------
    # Edit
    # ----------------------------------------------------

    menu_bar.addMenu("&Edit")

    # ----------------------------------------------------

    menu_bar.addMenu("&View")

    # ----------------------------------------------------

    menu_bar.addMenu("&Insert")

    # ----------------------------------------------------

    menu_bar.addMenu("&Tools")

    # ----------------------------------------------------

    menu_bar.addMenu("&Help")

    return menu_bar