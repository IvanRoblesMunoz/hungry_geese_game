#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 20:23:21 2021

@author: roblesi

Make background
"""
# pylint: disable=E0401
# =============================================================================
# imports
# =============================================================================
import os
from pathlib import Path
from PIL import Image

from src.draw_sprite.image_statics import (
    PADDING_TOP,
    PADDING_BOTTOM,
    PADDING_LEFT,
    PADDING_RIGHT,
    CELL_WIDTH,
    CELL_RESIZE,
    GRID_RESIZE,
    LETTER_RESIZE,
)

# =============================================================================
# Statics
# =============================================================================
REPO_PATH = Path(os.getcwd())
ASSETS_PATH = REPO_PATH / "src/draw_sprite/assets"
BASE_IMAGE_PATH = ASSETS_PATH / "hungry_geese_image.png"
LETTER_IMAGE_PATH = ASSETS_PATH / "hungry_geese_game_letters.png"

SAVE_SPRITE_PATH = REPO_PATH / "src/game/assets/background_sprite.png"

# =============================================================================
# Functions
# =============================================================================


def _load_cell_image(path_to_image=BASE_IMAGE_PATH):
    original = Image.open(path_to_image)
    cell = original.crop((191, 191 + CELL_WIDTH, 326.5, 326.5 + CELL_WIDTH))
    return cell


def _load_letters_header(path_to_image=LETTER_IMAGE_PATH):
    letters = Image.open(path_to_image)
    return letters


def _resize_image(img, percentage):
    size = img.size
    img = img.resize(
        (int(size[0] * percentage), int(size[1] * percentage)), Image.ANTIALIAS
    )
    return img


def make_background_grid(
    n_cells_width=11,
    n_cells_height=7,
    padding_top=PADDING_TOP,
    padding_bottom=PADDING_BOTTOM,
    padding_left=PADDING_LEFT,
    padding_right=PADDING_RIGHT,
):
    """Make background image for game."""

    cell = _resize_image(_load_cell_image(), CELL_RESIZE)
    letters = _resize_image(_load_letters_header(), LETTER_RESIZE)

    cell_width = cell.size[0]
    cell_height = cell.size[1]

    grid_width = cell_width * n_cells_width + padding_left + padding_right
    grid_height = cell_height * n_cells_height + padding_top + padding_bottom

    grid = Image.new("RGB", (grid_width, grid_height), (0, 0, 0),)

    for i in range(n_cells_width):
        for j in range(n_cells_height):
            grid.paste(
                cell, (i * cell_width + padding_left, j * cell_width + padding_top)
            )

    letters_pos_x = int((grid_width - letters.size[0]) / 2)
    letters_pos_y = int((padding_top - letters.size[1]) / 2)
    grid.paste(letters, (letters_pos_x, letters_pos_y))

    grid = grid.resize(
        (int(grid.size[0] * GRID_RESIZE), int(grid.size[1] * GRID_RESIZE)),
        Image.ANTIALIAS,
    )
    grid.save(SAVE_SPRITE_PATH)

    grid.show()


if __name__ == "__main__":
    make_background_grid()
