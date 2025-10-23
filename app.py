import os
import sys
import asyncio
import yaml
from dotenv import load_dotenv

load_dotenv()
with open("config.yaml") as f:
    config = yaml.safe_load(f)

print("✅ Bybit Bot Template запущено!")
print(f"Режим: {config['mode']}")
print(f"Активи: {', '.join(config['symbols'])}")
print("Наступним кроком: додамо стратегію та WebSocket-підключення.")
