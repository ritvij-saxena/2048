import pygame
from game_logic import move, spawn_tile, check_game_over, reset_game
from ui import draw_grid, draw_overlay

pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 Game")


def main():
    def reset():
        grid = reset_game()
        spawn_tile(grid)
        spawn_tile(grid)
        return grid

    grid = reset()
    running = True
    game_over = False

    key_mapping = {
        pygame.K_LEFT: 'left',
        pygame.K_RIGHT: 'right',
        pygame.K_UP: 'up',
        pygame.K_DOWN: 'down'
    }

    while running:
        draw_grid(screen, grid)
        pygame.display.flip()
        if game_over:
            draw_overlay(screen, "You Win! Press R to Restart" if game_over == "win" else "Game Over! Press R to Restart")

        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                running = False

            # Reset logic
            if event.key == pygame.K_r and game_over:
                grid = reset()
                game_over = False

            # Movement logic
            elif event.type == pygame.KEYDOWN and not game_over and event.key in key_mapping:
                new_grid = move(grid, key_mapping[event.key])
                if new_grid != grid:
                    grid = new_grid
                    spawn_tile(grid)
                    status = check_game_over(grid)
                    if status:
                        game_over = status
    pygame.quit()

if __name__ == "__main__":
    main()
