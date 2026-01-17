import math
import pygame


BASE_COLOR = pygame.Color('Blue')
SORTED_COLOR = pygame.Color('Pink')
OUTLINE_COLOR = pygame.Color('Red')
SWAP_COLOR = pygame.Color('Green')


class MergeSort:
    def __init__(self, nums: list[int]) -> None:
        self.n = len(nums)
        self.nums = nums.copy()
        self.gen = self.__make_generator()


    def init_render(self, window: pygame.Surface) -> None:
        
        for i, val in enumerate(self.nums):
            self.point_render(window, val, i, BASE_COLOR)

        pygame.display.update()


    def __make_generator(self):
        
        def dfs(left: int, right: int):
            if left == right:
                return
            
            mid: int = (left + right) // 2
            yield from dfs(left, mid)
            yield from dfs(mid + 1, right)
            yield from merge(left, mid, right)

            if right - left + 1 != self.n:
                return
            
            for i, val in enumerate(self.nums):
                yield val, i, SORTED_COLOR


        def merge(left: int, mid: int, right: int):

            lhs: list[int] = self.nums[left : mid + 1]
            rhs: list[int] = self.nums[mid + 1: right + 1]
            i: int = 0
            j: int = 0
            k: int = left

            while i < len(lhs) and j < len(rhs):
                if lhs[i] <= rhs[j]:
                    yield lhs[i], k, SWAP_COLOR
                    self.nums[k] = lhs[i]
                    i += 1
                else:
                    yield rhs[j], k, SWAP_COLOR
                    self.nums[k] = rhs[j]
                    j += 1
                k += 1

            while i < len(lhs):
                yield lhs[i], k, SWAP_COLOR
                self.nums[k] = lhs[i]
                i += 1
                k += 1
                
            while j < len(rhs):
                yield rhs[j], k, SWAP_COLOR
                self.nums[k] = rhs[j]
                j += 1
                k += 1

            for i in range(left, right + 1):
                yield self.nums[i], i, BASE_COLOR

        return dfs(0, self.n - 1)
    

    def point_render(
            self, 
            window: pygame.Surface, 
            val_mag: int,
            pos: int, 
            color: pygame.Color) -> None:

        # w: int = math.ceil(window.get_width() / self.n)
        w: int = window.get_width() // self.n
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

    
    def transition_render(self, window: pygame.Surface) -> 'MergeSort':
        if self.gen == None:
            return self

        try:
            val, pos, color = next(self.gen)
            self.point_render(window, val, pos, color)
        except:
            self.gen = None

        pygame.display.update()

        return self