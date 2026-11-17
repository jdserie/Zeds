"""Play Zeds, a branching survival story, in a terminal or desktop window."""
import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Scene:
    title: str
    text: str
    choices: tuple[tuple[str, str], ...] = ()


SCENES = {
    'start': Scene('The outbreak', '{player}, the city is falling. Bob needs your help crossing downtown to the CDC safe zone.', (
        ('Cross the rooftops', 'roof'),
        ('Take the streets', 'road'),
    )),
    'roof': Scene('The last rooftop', 'You and Bob can see the safe zone. The street below looks quiet.', (
        ('Jump down', 'jump'),
        ('Climb down the fire ladder', 'ladder'),
    )),
    'road': Scene('An abandoned car', 'The engine is running. A crowd of Zeds is closing in.', (
        ('Take the car', 'car'),
        ('Run for the safe zone', 'run'),
    )),
    'jump': Scene('One survivor', 'The jump alerts the Zeds and Bob breaks his leg. {player} reaches the safe zone alone.'),
    'ladder': Scene('Both survived', 'You and Bob climb down quietly and make it across the field together.'),
    'car': Scene('Dead end', 'A Zed is hiding in the backseat. Neither of you reaches the safe zone.'),
    'run': Scene('Overrun', 'There are too many Zeds in the street. The safe zone is out of reach.'),
}


def scene_text(scene, player):
    return scene.text.format(player=player.strip() or 'Survivor')


def play_terminal():
    player = input('Your name: ')
    scene = SCENES['start']
    while True:
        print(f'\n{scene.title}\n{scene_text(scene, player)}')
        if not scene.choices:
            if input('Play again? [y/N] ').strip().lower() != 'y':
                return
            scene = SCENES['start']
            continue
        for number, (label, _) in enumerate(scene.choices, 1):
            print(f'{number}. {label}')
        choice = input('Choose 1 or 2: ').strip()
        if choice in ('1', '2'):
            scene = SCENES[scene.choices[int(choice) - 1][1]]
        else:
            print('Choose one of the listed routes.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gui', action='store_true', help='Open the graphical edition.')
    args = parser.parse_args()
    try:
        if args.gui:
            from graphical import play_graphical
            play_graphical(SCENES, scene_text)
        else:
            print('== ZEDS ==')
            play_terminal()
    except (EOFError, KeyboardInterrupt):
        print('\nRun ended.')


if __name__ == '__main__':
    main()
