import numpy as np
from models.duo import Duo

def calculate_winchance_red(duo_red:Duo,duo_green:Duo) -> float:
    cor_winrate_red = correct_winrate(duo_red)
    cor_winrate_gre = correct_winrate(duo_green)
    return 1/(1+np.power(10,cor_winrate_gre-cor_winrate_red))

def correct_winrate(duo:Duo):
    wr = duo.winrate
    nog = duo.number_of_games
    cor_wr = wr
    
    if (wr == 0 and nog < 4) or(wr == 1 and nog < 4): cor_wr = 0.5
    elif wr < 0.35 and nog > 3: cor_wr = 0.35
    elif wr > 0.65 and nog > 3: cor_wr = 0.65

    return cor_wr