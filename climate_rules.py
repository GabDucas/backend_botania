
from enum import Enum
from typing import List

# ======================================================
# ENUMS (états discrets)
# ======================================================

class TempRange(Enum):
    LOW = "<22"
    LOW_MID = "22-26"
    IDEAL = "26-30"
    HIGH_MID = "30-34"
    HIGH = ">34"

class HumRange(Enum):
    LOW = "<45"
    LOW_MID = "45-55"
    IDEAL = "55-65"
    HIGH_MID = "65-75"
    HIGH = ">75"


class Diff(Enum):
    PLUSPLUS = "++"
    PLUS = "+"
    MINUSMINUS = "--"
    MINUS = "-"



# ======================================================
# ACTIONNEURS (constantes)
# ======================================================

VRC_L   = "VRC_L"
VRC_M   = "VRC_M"
VRC_H   = "VRC_H"

VRC_L_B = "VRC_L_B"
VRC_M_B = "VRC_M_B"
VRC_H_B = "VRC_H_B"

VAP     = "VAP"
SP_CH   = "SP_CH"
SP_CLI  = "SP_CLI"


class Rule:
    def __init__(
        self,
        temp_range: TempRange,
        diff_t: Diff,
        hum_range: HumRange,
        diff_hr: Diff,
        actions: List[str]
    ):
         self.temp_range = temp_range
         self.diff_t = diff_t
         self.hum_range = hum_range
         self.diff_hr = diff_hr
         self.actions = actions

RULES: List[Rule] = [

    # ---------- T < 24 ----------
    Rule(TempRange.LOW, Diff.PLUS,  HumRange.LOW,  Diff.PLUS,  [VRC_L, VAP, SP_CH]),
    Rule(TempRange.LOW, Diff.PLUS,  HumRange.LOW,  Diff.MINUS, [VRC_H, SP_CH]),
    Rule(TempRange.LOW, Diff.PLUS,  HumRange.MID,  Diff.PLUS,  [VRC_L, SP_CH]),
    Rule(TempRange.LOW, Diff.PLUS,  HumRange.MID,  Diff.MINUS, [VRC_L, SP_CH]),
    Rule(TempRange.LOW, Diff.PLUS,  HumRange.HIGH, Diff.PLUS,  [VRC_H, SP_CH]),
    Rule(TempRange.LOW, Diff.PLUS,  HumRange.HIGH, Diff.MINUS, [VRC_L, SP_CH]),

    Rule(TempRange.LOW, Diff.MINUS, HumRange.LOW,  Diff.PLUS,  [VRC_L_B, VAP, SP_CH]),
    Rule(TempRange.LOW, Diff.MINUS, HumRange.LOW,  Diff.MINUS, [VRC_H_B, SP_CH]),
    Rule(TempRange.LOW, Diff.MINUS, HumRange.MID,  Diff.PLUS,  [VRC_L_B, SP_CH]),
    Rule(TempRange.LOW, Diff.MINUS, HumRange.MID,  Diff.MINUS, [VRC_L_B, SP_CH]),
    Rule(TempRange.LOW, Diff.MINUS, HumRange.HIGH, Diff.PLUS,  [VRC_H_B, SP_CH]),
    Rule(TempRange.LOW, Diff.MINUS, HumRange.HIGH, Diff.MINUS, [VRC_L_B, SP_CH]),

    # ---------- 24 ≤ T ≤ 34 ----------
    Rule(TempRange.MID, Diff.PLUS,  HumRange.LOW,  Diff.PLUS,  [VRC_L, VAP]),
    Rule(TempRange.MID, Diff.PLUS,  HumRange.LOW,  Diff.MINUS, [VRC_H]),
    Rule(TempRange.MID, Diff.PLUS,  HumRange.MID,  Diff.PLUS,  [VRC_L]),
    Rule(TempRange.MID, Diff.PLUS,  HumRange.MID,  Diff.MINUS, [VRC_L]),
    Rule(TempRange.MID, Diff.PLUS,  HumRange.HIGH, Diff.PLUS,  [VRC_H]),
    Rule(TempRange.MID, Diff.PLUS,  HumRange.HIGH, Diff.MINUS, [VRC_L]),

    Rule(TempRange.MID, Diff.MINUS, HumRange.LOW,  Diff.PLUS,  [VRC_L, VAP]),
    Rule(TempRange.MID, Diff.MINUS, HumRange.LOW,  Diff.MINUS, [VRC_H]),
    Rule(TempRange.MID, Diff.MINUS, HumRange.MID,  Diff.PLUS,  [VRC_L]),
    Rule(TempRange.MID, Diff.MINUS, HumRange.MID,  Diff.MINUS, [VRC_L]),
    Rule(TempRange.MID, Diff.MINUS, HumRange.HIGH, Diff.PLUS,  [VRC_H]),
    Rule(TempRange.MID, Diff.MINUS, HumRange.HIGH, Diff.MINUS, [VRC_L]),

    # ---------- T > 34 ----------
    Rule(TempRange.HIGH, Diff.PLUS,  HumRange.LOW,  Diff.PLUS,  [VRC_L_B, VAP, SP_CLI]),
    Rule(TempRange.HIGH, Diff.PLUS,  HumRange.LOW,  Diff.MINUS, [VRC_H_B, SP_CLI]),
    Rule(TempRange.HIGH, Diff.PLUS,  HumRange.MID,  Diff.PLUS,  [VRC_L_B, SP_CLI]),
    Rule(TempRange.HIGH, Diff.PLUS,  HumRange.MID,  Diff.MINUS, [VRC_L_B, SP_CLI]),
    Rule(TempRange.HIGH, Diff.PLUS,  HumRange.HIGH, Diff.PLUS,  [VRC_H_B, SP_CLI]),
    Rule(TempRange.HIGH, Diff.PLUS,  HumRange.HIGH, Diff.MINUS, [VRC_L_B, SP_CLI]),

    Rule(TempRange.HIGH, Diff.MINUS, HumRange.LOW,  Diff.PLUS,  [VRC_L, VAP, SP_CLI]),
    Rule(TempRange.HIGH, Diff.MINUS, HumRange.LOW,  Diff.MINUS, [VRC_H, SP_CLI]),
    Rule(TempRange.HIGH, Diff.MINUS, HumRange.MID,  Diff.PLUS,  [VRC_L, SP_CLI]),
    Rule(TempRange.HIGH, Diff.MINUS, HumRange.MID,  Diff.MINUS, [VRC_L, SP_CLI]),
    Rule(TempRange.HIGH, Diff.MINUS, HumRange.HIGH, Diff.PLUS,  [VRC_H, SP_CLI]),
    Rule(TempRange.HIGH, Diff.MINUS, HumRange.HIGH, Diff.MINUS, [VRC_L, SP_CLI]),
]


def get_temp_range(T: float) -> TempRange:
    if T < 22:
        return TempRange.LOW
    elif T <= 34:
        return TempRange.MID
    return TempRange.HIGH

def get_hum_range(HR: float) -> HumRange:
    if HR < 50:
        return HumRange.LOW
    elif HR <= 70:
        return HumRange.MID
    return HumRange.HIGH


def get_diff_t(int_t: float, ext_t: float) -> Diff:

    diff_t = int_t - ext_t

    if diff_t >= 10:
        return Diff.PLUSPLUS
    
    elif diff_t >= 0:
        return Diff.PLUS

    elif diff_t <= -10:
        return Diff.MINUSMINUS
    
    elif diff_t < 0:
        return Diff.MINUS
    
    return None

def get_diff_hum(int_hum: float, ext_hum: float) -> Diff:

    diff_hum = int_hum - ext_hum

    if diff_hum >= 15:
        return Diff.PLUSPLUS
    
    elif diff_hum >= 0:
        return Diff.PLUS
    
    elif diff_hum <= -15: 
        return Diff.MINUSMINUS
    
    elif diff_hum < 0:
        return Diff.MINUS
    
    return None


# ======================================================
# MOTEUR DE DÉCISION
# ======================================================

def compute_actions(
    T_int: float,
    T_ext: float,
    HR_int: float,
    HR_ext: float
) -> List[str]:

    t_range = get_temp_range(T_int)
    h_range = get_hum_range(HR_int)
    diff_t = get_diff_t(T_int, T_ext)
    diff_h = get_diff_hum(HR_int, HR_ext)

    print(f"Temp range: {t_range}, Hum range: {h_range}, Diff T: {diff_t}, Diff HR: {diff_h}")

    for rule in RULES:
        if (
            rule.temp_range == t_range and
            rule.diff_t == diff_t and
            rule.hum_range == h_range and
            rule.diff_hr == diff_h
        ):
            return rule.actions

    return []


