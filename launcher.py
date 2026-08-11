"""
PresentationAI Launcher
"""

import sys

from src.core.application import Application


def main():

    application = Application()

    exit_code = application.run()

    sys.exit(exit_code)


if __name__ == "__main__":
    main()