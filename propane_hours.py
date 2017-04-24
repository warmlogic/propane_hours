import sys
from math import floor

def propane_hours(tank_wt_lbs_current, TANK_WT_LBS_EMPTY=None, BURNER_BTU=None):
    '''Estimate the number of hours left in a propane tank based on its weight.

    On my burner, I get about 75% efficiency.

    Brew beer and be merry!
    '''

    if TANK_WT_LBS_EMPTY is None:
        TANK_WT_LBS_EMPTY = 16.6

    if BURNER_BTU is None:
        BURNER_BTU = 55000.0

    # BTUs in a pound of liquid propane
    BTU_PER_LB_PROP = 21591.0

    prop_lbs = tank_wt_lbs_current - TANK_WT_LBS_EMPTY
    btu = prop_lbs * BTU_PER_LB_PROP

    # time based on 100% efficiency
    time_hours_100 = btu / BURNER_BTU
    time_minutes_100 = time_hours_100 * 60
    hours_part_100   = floor(time_hours_100)
    minutes_part_100 = floor(time_minutes_100 % 60)

    # time based on 75% efficiency
    time_hours_75 = time_hours_100 * 0.75
    time_minutes_75 = time_hours_75 * 60
    hours_part_75   = floor(time_hours_75)
    minutes_part_75 = floor(time_minutes_75 % 60)

    # time based on 50% efficiency
    time_hours_50 = time_hours_100 * 0.5
    time_minutes_50 = time_hours_50 * 60
    hours_part_50   = floor(time_hours_50)
    minutes_part_50 = floor(time_minutes_50 % 60)

    print('{:.2f} lbs. of propane in {:.2f} lb. tank ({:.2f} lbs. together)'.format(prop_lbs, TANK_WT_LBS_EMPTY, tank_wt_lbs_current))
    print('Burner BTU: {:.1f}'.format(BURNER_BTU))

    print('At full blast:')
    print('\tAssuming 100% efficiency: {} hours {} minutes'.format(hours_part_100, minutes_part_100))
    print('\tAssuming 75% efficiency:  {} hours {} minutes'.format(hours_part_75, minutes_part_75))
    print('\tAssuming 50% efficiency:  {} hours {} minutes'.format(hours_part_50, minutes_part_50))

if __name__ == "__main__":
    args = sys.argv[1:]
    tank_wt_lbs_current = float(args[0])

    if len(args) == 2:
        TANK_WT_LBS_EMPTY = float(args[1])
    else:
        TANK_WT_LBS_EMPTY = None

    if len(args) == 3:
        BURNER_BTU = float(args[2])
    else:
        BURNER_BTU = None

    propane_hours(tank_wt_lbs_current, TANK_WT_LBS_EMPTY, BURNER_BTU)
