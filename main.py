# from typing
import pygame
import random
import sys
import sorters


WIDTH: int = 700
HEIGHT: int = 500


def run_visualization(sorter: sorters.Sorter) -> None:
    '''
    Run a real-time sorting visualization for sorting algorithm.

    The sorter is expected to render the initial state via 
    `init_render()` and advance the visualization each frame via 
    `transition_render()`.
    '''

    pygame.init()
    window: pygame.Surface = pygame.display.set_mode(
        size=(WIDTH, HEIGHT),
        flags=pygame.RESIZABLE
    )
    clock = pygame.time.Clock()

    window.fill('Black')
    sorter.init_render(window) #This
    
    while "True and REAL":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        keystate = pygame.key.get_pressed()
        modstate: int = pygame.key.get_mods()

        if keystate[pygame.K_w] and (modstate & pygame.KMOD_CTRL):
            sys.exit(0)

        sorter.transition_render(window) #This
        clock.tick(60)


def main() -> int:

    n: int = 50
    nums: list[int] = [random.randint(11, 200) for _ in range(n)]
    run_visualization(sorters.FunnySort(nums))

    return 0


if __name__ == '__main__':

    main()