#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 20:09:40 2021

@author: roblesi
"""
# pylint: disable=E1101
# =============================================================================
# Imports
# =============================================================================
import sys
import pygame


from src.game.game_components.game_environment import GameEnvironment
from src.game.visualisation.visualise_step import (
    draw_step,
    draw_loading_screen,
    draw_endgame_screen,
    BACKGROUND,
)

pygame.init()

# =============================================================================
# Colors
# =============================================================================


WIDTH = BACKGROUND.get_width()
HEIGHT = BACKGROUND.get_height()

# Make display
DIS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hungry geese game AI")


def game_loop():
    """Loop over game."""
    game_environment = GameEnvironment()
    obs = game_environment.start_game()
    draw_step(DIS, obs)

    game_over = False
    while not game_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    obs, game_over = game_environment.process_step("WEST")
                elif event.key == pygame.K_RIGHT:
                    obs, game_over = game_environment.process_step("EAST")
                elif event.key == pygame.K_UP:
                    obs, game_over = game_environment.process_step("NORTH")
                elif event.key == pygame.K_DOWN:
                    obs, game_over = game_environment.process_step("SOUTH")

            if game_over:
                print(obs)
                end_game(obs)

            else:
                draw_step(DIS, obs)

    pygame.quit()
    sys.exit()


def find_final_position(obs: dict) -> int:
    """Find final player position."""
    if len(obs["geese"][0]) == 0:
        pos = 4 - sum([1 if len(i) == 0 else 0 for i in obs["geese"][1:]])

    else:
        geese = [0, 1, 2, 3]
        length = [len(i) for i in obs["geese"]]
        order = list(zip(*sorted(zip(length, geese))))[1]

        pos = 4 - order.index(0)

    return pos


def start_game() -> None:
    """Start game function. Draws loading screen."""
    game_over = False
    while not game_over:

        draw_loading_screen(DIS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game_loop()


def end_game(obs: dict) -> None:
    """End game function. Draws loading screen."""
    game_over = False
    while not game_over:

        pos = find_final_position(obs)
        draw_endgame_screen(DIS, pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game_loop()


if __name__ == "__main__":
    start_game()
