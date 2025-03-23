import pygame

def get_tileset(path: str, col: int, row: int, width: int, height: int, scale: float) -> list[pygame.Surface]:
    image = pygame.image.load(path).convert_alpha()
    tiles = []
    for y in range(row):
        for x in range(col):
            tile = pygame.Surface((width, height))
            tile.blit(image, (width * -x, height * -y))
            tile = pygame.transform.scale(tile, (width * scale, height * scale))
            tiles.append(tile)
    return tiles