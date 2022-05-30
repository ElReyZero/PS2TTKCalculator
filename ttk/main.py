from ttk import getTTK
from modules import config as cfg

def main(weapon_name: str, shots: int, distance: float):
    cfg.get_config()
    return getTTK(weapon_name, shots, distance)

def setConfig():
    cfg.get_config()

