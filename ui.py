import pygame

WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE
BACKGROUND_COLOR = (187, 173, 160)
LINE_COLOR = (50, 50, 50)
TILE_COLORS = {
    0: (205, 193, 180), 2: (238, 228, 218), 4: (237, 224, 200), 8: (242, 177, 121),
    16: (245, 149, 99), 32: (246, 124, 95), 64: (246, 94, 59), 128: (237, 207, 114),
    256: (237, 204, 97), 512: (237, 200, 80), 1024: (237, 197, 63), 2048: (237, 194, 46)
}

def draw_grid(screen, grid):
    """Draws the 2048 grid and tiles."""
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 36)  # Move font initialization here
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = grid[row][col]
            color = TILE_COLORS.get(value, (60, 58, 50))
            pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, LINE_COLOR, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)
            if value:
                text = font.render(str(value), True, (0, 0, 0))
                text_rect = text.get_rect(center=(col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)

def draw_overlay(screen, text):
    """Displays a semi-transparent overlay with a message."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    font = pygame.font.Font(None, 36)  # Move font initialization here
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    overlay.blit(text_surface, text_rect)
    screen.blit(overlay, (0, 0))
    pygame.display.flip()
    pygame.time.wait(2000)
