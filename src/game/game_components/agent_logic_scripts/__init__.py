#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 20:09:40 2021

@author: roblesi

Module to import Agents from same module.
"""
# pylint: disable=E0401
try:
    from torch.multiprocessing import set_start_method
except RuntimeError:
    pass

set_start_method("spawn")
from src.game.game_components.agent_logic_scripts.alpha_geese_agent_13378 import (
    alphageese_agent_13378,
)
from src.game.game_components.agent_logic_scripts.alpha_geese_agent_18138 import (
    alphageese_agent_18138,
)
from src.game.game_components.agent_logic_scripts.crazy_goose import crazy_goose_agent
from src.game.game_components.agent_logic_scripts.boilergoose import boilergoose_agent
from src.game.game_components.agent_logic_scripts.risk_adverse_greedy import (
    risk_averse_greedy_agent,
)
