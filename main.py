"""
Flappy Bird Game
Developed by: Phạm Lê Ngọc Sơn
Version: 1.0.0
License: MIT
"""

import asyncio

from src.flappy import Flappy

if __name__ == "__main__":
    asyncio.run(Flappy().start())
