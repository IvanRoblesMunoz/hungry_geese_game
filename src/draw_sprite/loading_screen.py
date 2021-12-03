#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 23:34:46 2021

@author: roblesi
"""
# pylint: disable=E0401
# =============================================================================
# imports
# =============================================================================
import os
from pathlib import Path
from PIL import Image

from src.draw_sprite.background import _resize_image

# =============================================================================
# Statics
# =============================================================================
REPO_PATH = Path(os.getcwd())
ASSETS_PATH = REPO_PATH / "src/draw_sprite/assets"
LOADING_SCREEN_PATH = ASSETS_PATH / "loading_screen.png"

GRID_PATH = REPO_PATH / "src/game/assets/background_sprite.png"
SAVE_SPRITE_PATH = REPO_PATH / "src/game/assets/loading_screen.png"

# =============================================================================
# Functions
# =============================================================================


def _load_original_loading_screen(path_to_image=LOADING_SCREEN_PATH):
    loading_screen = Image.open(path_to_image)
    return loading_screen


def _resize_image(img, percentage):
    size = img.size
    img = img.resize(
        (int(size[0] * percentage), int(size[1] * percentage)), Image.ANTIALIAS
    )
    return img


def make_loading_screen():
    """Make loading screen."""
    loading_screen = _load_original_loading_screen()
    loading_screen = _resize_image(loading_screen, 0.825)

    loading_screen.save(SAVE_SPRITE_PATH)
    loading_screen.show()


if __name__ == "__main__":
    make_loading_screen()
