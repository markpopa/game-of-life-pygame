import asyncio
import pygame
import numpy as np

BG = (10, 10, 10)
GRID = (40, 40, 40)
DIE = (170, 23, 10)
ALIVE = (255, 255, 255)
SIZE = 10

async def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = BG if cells[row, col] == 0 else ALIVE
        
        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = DIE
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = ALIVE
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = ALIVE
                    
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
        
    return updated_cells

async def main():
    pygame.init()
    screen = pygame.display.set_mode((128 * SIZE, 72 * SIZE))
    cells = np.zeros((72, 128))
    screen.fill(GRID)
    await update(screen, cells, SIZE)
    
    pygame.display.flip()
    
    running = False
    speed = 0.1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    await update(screen, cells, SIZE)
                    pygame.display.update()
                elif event.key == pygame.K_RIGHT:
                    speed = max(0.001, speed - 0.01)
                elif event.key == pygame.K_LEFT:
                    speed = min(1.0, speed + 0.01)
                elif event.key == pygame.K_DOWN:
                    speed = 0.1
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // SIZE, pos[0] // SIZE] = 1
                await update(screen, cells, SIZE)
                pygame.display.update()
        
        screen.fill(GRID)
        
        if running:
            cells = await update(screen, cells, SIZE, with_progress=True)
            pygame.display.update()
        
        await asyncio.sleep(speed)

if __name__ == '__main__':
    asyncio.run(main())
