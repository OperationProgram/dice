import random


def draw_dice(i):
    diceGraphics = [
        """|1|""",
        """|2|""",
        """|3|""",
        """|4|""",
        """|5|""",
        """|6|""",
                    ]
    return diceGraphics[i]


def roll_dice():
    dice_sides = [0, 1, 2, 3, 4, 5]
    roll = random.choice(dice_sides)
    return roll


def main():
    print(draw_dice(roll_dice()))


main()
