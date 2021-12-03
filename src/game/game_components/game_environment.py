#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 11:56:00 2021

@author: roblesi
"""
# pylint: disable=E0401
# =============================================================================
# Imports
# =============================================================================
from kaggle_environments import make
from src.game.game_components.agent_logic_scripts import (
    alphageese_agent_13378,
    alphageese_agent_18138,
    crazy_goose_agent,
    # boilergoose_agent,
    # risk_averse_greedy_agent,
)

# =============================================================================
# Functions
# =============================================================================


class GameEnvironment:
    """Class used to process the game."""

    def __init__(self):
        self.env = make("hungry_geese", debug=True)
        self.trainer = self.env.train(
            [None, alphageese_agent_13378, crazy_goose_agent, alphageese_agent_18138]
        )

    def start_game(self):
        """Start game environment."""
        obs = self.trainer.reset()
        return obs

    def process_step(self, action):
        """Process action and return new observation."""
        self.env.render()
        obs, _, done, _ = self.trainer.step(action)
        return obs, done
