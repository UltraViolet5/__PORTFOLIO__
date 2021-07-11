import winsound


def play_input_beep():
    """Play Beep sound."""
    winsound.Beep(500, 200)


def play_step_beep():
    """Play Beep sound."""
    winsound.Beep(50, 50)


def attack_beep():
    winsound.Beep(1000, 50)


def dead_beep():
    winsound.Beep(600, 1500)
