# Dark Souls 1 Soul Level Calculator
## Description
This is a little script I wrote [with the information on this Wikidot page](http://darksouls.wikidot.com/soul-level) and python to calculate the amount of levelups I can get in Dark Souls: <b>Prepare to Die Edition</b> and <b>Dark Souls: Remastered</b>. There are more practical solutions for this like [Dakota Madden-Fong's web calculator](https://trifectaiii.github.io/DS1-Soul-Level-Calculator/) but it was still fun quickly writing this mini-script.
<br>
<b>Disclaimer:</b> level calculation is accurate level 12 and up.

## How to use
Simply run
```
python soullevelcalc.py
```
and you will be asked for your current level and your amount of souls then you will be told how many level ups you can get and how much each would cost.

## Functions

### 
```py 
# returns cost of the given level
# when level = 12 the returned cost is from level 11 -> 12
def get_level_cost(level: int) -> int:

# returns the amount of possible levelups
# takes the current level and the amount of held souls
# a boolean can be given as last parameter to supress print statement
def get_possible_ups(currentLevel: int, souls: int, silent: bool = False) -> int:

# takes the current level and amount of souls from user input
# then prints the amount of possible level ups
def start():
```

## Formula
The formula is:
`y = 0.02x^3 + 3.06x^2 + 105.6x - 895`
Where <b>x</b> is your level and <b>y</b> the calculated cost.
<br>
Formula and level chart can be found [on the Dark Souls Wikidot page](http://darksouls.wikidot.com/soul-level)
