#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 18:03:25 2021

@author: roblesi

This module makes the visuals for the game.

"""
# pylint: disable=E0401
# =============================================================================
# Imports
# =============================================================================
import os
from pathlib import Path
from typing import Tuple

import pygame
from pygame import display

# =============================================================================
# Statics
# =============================================================================
from src.game.visualisation.visualisation_statics import (
    START_HEIGHT,
    START_WIDTH,
    WIDTH_STEP,
    HEIGHT_STEP,
)

REPO_PATH = Path(os.getcwd())
ASSETS_PATH = REPO_PATH / "src/game/assets"


BACKGROUND = pygame.image.load(ASSETS_PATH / "background_sprite.png")
LOADING_SCREEN = pygame.image.load(ASSETS_PATH / "loading_screen.png")
FOOD = pygame.image.load(ASSETS_PATH / "food_sprite.png")

OBJECT_WIDTH = FOOD.get_width()

COLOR_GEESE = {
    0: (255, 255, 255),  # White
    1: (255, 0, 0),  # Red
    2: (0, 255, 0),  # Green
    3: (0, 0, 255),  # Blue
}


# =============================================================================
# Function
# =============================================================================


def cell_to_coordinates(cell: int) -> Tuple[float]:
    """Convert cell number to x,y coordinates."""
    cells_width = (cell) % 11
    cells_height = (cell) // 11

    x_coord = START_WIDTH + cells_width * WIDTH_STEP
    y_coord = START_HEIGHT + cells_height * HEIGHT_STEP

    return x_coord, y_coord


def draw_goose(dis: display, goose_pos: list, goose_idx: int) -> None:
    for body_idx, goose_part in enumerate(goose_pos):
        x_coord, y_coord = cell_to_coordinates(goose_part)

        # Draw head
        if body_idx == 0:
            pygame.draw.polygon(
                surface=dis,
                color=COLOR_GEESE[goose_idx],
                points=[
                    (x_coord + HEIGHT_STEP / 3, y_coord),
                    (x_coord, y_coord + HEIGHT_STEP / 3),
                    (x_coord + WIDTH_STEP / 3, y_coord + HEIGHT_STEP * 2 / 3),
                    (x_coord + WIDTH_STEP * 2 / 3, y_coord + HEIGHT_STEP / 3),
                ],
            )
        # Draw tail
        elif body_idx == len(goose_pos) - 1:
            pygame.draw.circle(
                surface=dis,
                color=COLOR_GEESE[goose_idx],
                center=(x_coord + WIDTH_STEP / 3, y_coord + HEIGHT_STEP / 3),
                radius=WIDTH_STEP / 3,
            )
        # Draw bpdy
        else:
            pygame.draw.rect(
                dis,
                COLOR_GEESE[goose_idx],
                (x_coord, y_coord, OBJECT_WIDTH, OBJECT_WIDTH),
            )


def draw_step(dis: display, obs: dict) -> None:
    """
    Draws step of game.

    Parameters
    ----------
    dis : display
        Game display.
    obs : dict
        Observation representing the current state of the game.

    Returns
    -------
    None

    """
    # Draw background
    # dis.blit(BACKGROUND, (0, 0))
    dis.blit(BACKGROUND, (0, 0))

    # Draw food
    for food_cell in obs["food"]:
        dis.blit(FOOD, cell_to_coordinates(food_cell))

    # Draw geese
    for goose_idx in range(4):
        goose_pos = obs["geese"][goose_idx]

        draw_goose(dis, goose_pos, goose_idx)

    # Update
    pygame.display.flip()
    pygame.display.update()


def draw_loading_screen(dis: display) -> None:
    """Draw loading screen."""

    msg1 = "Welcome to Hungry Geese!!!"
    msg2 = "Please press any key to start."
    msg3 = "You will play the white character, you can control it"
    msg4 = "using the direction keys. After each input, the NPCs"
    msg5 = "will take a second to submit their direction."

    # Draw background
    dis.blit(LOADING_SCREEN, (0, 0))

    # Write message
    font_style1 = pygame.font.SysFont("bahnschrift", 40)
    dis.blit(font_style1.render(msg1, True, (0, 196, 151)), [40, 40])

    font_style2 = pygame.font.SysFont("bahnschrift", 35)
    dis.blit(font_style2.render(msg2, True, (0, 196, 151)), [40, 80])

    font_style3 = pygame.font.SysFont("bahnschrift", 25)
    dis.blit(font_style3.render(msg3, True, (0, 196, 151)), [30, 175])
    dis.blit(font_style3.render(msg4, True, (0, 196, 151)), [30, 200])
    dis.blit(font_style3.render(msg5, True, (0, 196, 151)), [30, 225])

    # Update
    pygame.display.flip()
    pygame.display.update()


def draw_endgame_screen(dis: display, position: int) -> None:
    """Draw end game screen."""

    msg1 = f"Game ended, you placed {position} of 4!!!"
    msg2 = "Please press any key to start."
    msg3 = "You will play the white character, you can control it"
    msg4 = "using the direction keys. After each input, the NPCs"
    msg5 = "will take a second to submit their direction."

    # Draw background
    dis.blit(LOADING_SCREEN, (0, 0))

    # Write message
    font_style1 = pygame.font.SysFont("bahnschrift", 40)
    dis.blit(font_style1.render(msg1, True, (0, 196, 151)), [40, 50])

    font_style2 = pygame.font.SysFont("bahnschrift", 35)
    dis.blit(font_style2.render(msg2, True, (0, 196, 151)), [40, 90])

    font_style3 = pygame.font.SysFont("bahnschrift", 25)
    dis.blit(font_style3.render(msg3, True, (0, 196, 151)), [30, 175])
    dis.blit(font_style3.render(msg4, True, (0, 196, 151)), [30, 200])
    dis.blit(font_style3.render(msg5, True, (0, 196, 151)), [30, 225])

    # Update
    pygame.display.flip()
    pygame.display.update()
