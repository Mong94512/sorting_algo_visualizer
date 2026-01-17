import math
import pygame
from typing import Any, Generator, Union, TypeVar, Generic, Protocol


'''Protocol'''
class IsSortable(Protocol):
    def __lt__(self, other: object) -> bool: ...
    def __int__(self) -> int: ...


'''
Type alises
'''
funny_sort_gen = Union[
    Generator[tuple[int, int, pygame.Color], Any, None] | 
    None
]

T = TypeVar("T", bound=IsSortable)
BASE_COLOR = pygame.Color('Blue')
SORTED_COLOR = pygame.Color('Pink')
OUTLINE_COLOR = pygame.Color('Red')
SWAP_COLOR = pygame.Color('Green')


class FunnySort(Generic[T]):
    '''
    Class that sort the list[T] while visualizing the sorting process.

    It use an algorithm called 'funny sort'.
    '''
    def __init__(self, nums: list[T]) -> None:
        self.nums = list(nums)
        self.n = len(self.nums)
        self.gen: funny_sort_gen = self.__make_generator()
    

    def init_render(self, window: pygame.Surface) -> None:
        '''
        Render the initial state of list
        '''
        
        for i in range(self.n):
            self.point_render(window, i, BASE_COLOR)

        pygame.display.update()


    def __make_generator(self) -> funny_sort_gen:
        '''
        Run the sorting algorithm with yielding.

        WARNING: Not for external usage.
        '''

        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.nums[j] < self.nums[i]:
                    self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                    yield i, j, SWAP_COLOR
                    yield i, j, BASE_COLOR

        for i in range(self.n):
            yield i, -1, SORTED_COLOR


    def point_render(
        self,
        window: pygame.Surface,
        pos: int,
        color: pygame.Color) -> None:
        '''
        Render the visual of element at position(pos) in list.
        '''

        val_mag: int = int(self.nums[pos])
        w: int = math.ceil(window.get_width() / self.n)
        x: int = pos * w
        y: int = window.get_height() - 100 - val_mag

        pygame.draw.rect(
            surface=window,
            color='Black',
            rect=pygame.Rect(x, 0, w, window.get_height()),
        )

        pygame.draw.rect(
            surface=window,
            color=color,
            rect=pygame.Rect(x, y, w, val_mag),
        )

        if w // 10 > 0:
            pygame.draw.rect(
                surface=window,
                color=OUTLINE_COLOR,
                rect=pygame.Rect(x, y, w, val_mag),
                width=w // 10
            )


    def transition_render(self, window: pygame.Surface) -> 'FunnySort':
        '''
        Render the intermediate state of list.

        Do nothing if the list already sorted.
        '''

        if not self.gen:
            return self

        try:
            u, v, color = next(self.gen)
            self.point_render(window, u, color)
            if v != -1:
                self.point_render(window, v, color)
        except:
            self.gen = None

        pygame.display.update()

        return self
