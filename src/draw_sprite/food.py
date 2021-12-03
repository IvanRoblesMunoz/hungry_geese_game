#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 17:22:14 2021

@author: roblesi
"""
# pylint: disable=E0401
# =============================================================================
# imports
# =============================================================================
import os
from pathlib import Path
from PIL import Image


from src.draw_sprite.background import _load_cell_image
from src.draw_sprite.image_statics import GRID_RESIZE

GRID_RESIZE = 0.25
# =============================================================================
# Statics
# =============================================================================
REPO_PATH = Path(os.getcwd())
ASSETS_PATH = REPO_PATH / "src/draw_sprite/assets"
FOOD_PATH = ASSETS_PATH / "pizza.png"

SAVE_SPRITE_PATH = REPO_PATH / "src/game/assets/food_sprite.png"


def _load_food_image(path_to_image=FOOD_PATH, percentage=0.9):
    food = Image.open(path_to_image)
    width, height = _load_cell_image().size

    food = food.resize(
        (int(width * percentage * GRID_RESIZE), int(height * percentage * GRID_RESIZE)),
        Image.ANTIALIAS,
    )
    return food


def make_food_image():
    """Make food image."""
    food = _load_food_image()
    food.save(SAVE_SPRITE_PATH)
    food.show()


if __name__ == "__main__":
    make_food_image()
