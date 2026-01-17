# from typing
import pygame
import random
import sys
import sorters


WIDTH: int = 1200
HEIGHT: int = 500


def run_visualization(sorter: sorters.Sorter) -> None:
    '''
    Run a real-time sorting visualization for sorting algorithm.

    The sorter is expected to render the initial state via 
    `init_render()` and advance the visualization each frame via 
    `transition_render()`.
    '''

    window: pygame.Surface = pygame.display.set_mode(
        size=(WIDTH, HEIGHT),
        flags=pygame.RESIZABLE
    )
    clock = pygame.time.Clock()

    window.fill('Black')
    # pygame.display.update()
    sorter.init_render(window) #This
    
    while "True and REAL":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keystate = pygame.key.get_pressed()
        modstate: int = pygame.key.get_mods()

        if keystate[pygame.K_w] and (modstate & pygame.KMOD_CTRL):
            return

        sorter.transition_render(window) #This
        clock.tick(300)


def main() -> int:

    pygame.init()

    n: int = WIDTH // 2
    nums: list[int] = [random.randint(11, 200) for _ in range(n)]

    run_visualization(sorters.FunnySort(nums))
    run_visualization(sorters.MergeSort(nums))

    pygame.quit()

    return 0


if __name__ == '__main__':

    main()