# returns cost of the given level
# when level = 12 the returned cost is from level 11 -> 12
def get_level_cost(level: int) -> int:
    return int(round((0.02 * pow(level, 3)) + (3.06 * pow(level, 2)) + (105.6 * level) - 895, 0))

# returns the amount of possible levelups
# takes the current level and the amount of held souls
# a boolean can be given as last parameter to supress print statement
def get_possible_ups(currentLevel: int, souls: int, silent: bool = False) -> int:
    level: int = currentLevel + 1
    cost: int = get_level_cost(level)
    ups: int = 0
    while (souls >= cost):
        if (silent == False):
            print(f"Cost from level {level-1} to {level}: {cost} Souls.")
        souls -= cost
        level += 1
        ups += 1
        cost = get_level_cost(level)
    return ups

# takes the current level and amount of souls from user input
# then prints the amount of possible level ups
def start():
    try:
        print("Enter your starting level.")
        currentLevel: int = int(input("> "))
        print("Enter the amount of souls you have.")
        souls: int = int(input("> "))
        ups: int = get_possible_ups(currentLevel, souls)
        print(ups)
    except:
        print("Something happened :c, try entering real numbers.")


start()
