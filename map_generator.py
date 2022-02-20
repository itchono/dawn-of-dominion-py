import random
from enums import Terrain

def terrain_generator(size: int) -> list[list[int]]:
    '''
    Generates an island of random terrain surrounded by the ocean.

    RULES:
    - The island is a randomly sized ellipse between size/2 and 3*size/4.
    - The island's inside edge is smaller than the island by between 1
        and 1/4 the size of the island
    - The outside edge of the island is made of loose ground.
    - The inside of the island is made of firm ground.
    - The center of the island is made of mountainous terrain.
    - Inland water is calm sea.
    - Water around the island is rough sea.
    '''

    island_array = [[Terrain.ROUGH_SEA] * size for _ in range(size)]  # Create the surrounding ocean

    ellipse_height = random.randint(size // 2, 3*size // 4)
    ellipse_width = random.randint(size // 2, 3*size // 4)

    # fill in the ellipse with loose ground as a first pass
    for i in range(size):
        for j in range(size):
            if (i - size // 2) ** 2 + (j - size // 2) ** 2 <= (ellipse_width ** 2 + ellipse_height ** 2) / 4:
                island_array[i][j] = Terrain.LOOSE_GROUND

    interior_ellipse_height = ellipse_height - random.randint(1, ellipse_height // 4)
    interior_ellipse_width = ellipse_width - random.randint(1, ellipse_width // 4)

    # Fill the interior of the island with firm ground and other terrain details
    for i in range(size):
        for j in range(size):
            if (i - size // 2) ** 2 + (j - size // 2) ** 2 <= (interior_ellipse_width ** 2 + interior_ellipse_height ** 2) / 4:
                island_array[i][j] = Terrain.FIRM_GROUND

                # Add some mountainous terrain (30% chance)
                if (i - size // 2) ** 2 + (j - size // 2) ** 2 <= (interior_ellipse_width ** 2 + interior_ellipse_height ** 2) / 8 \
                    and random.randint(1, 100) <= 30:
                    island_array[i][j] = Terrain.MOUNTAINOUS

                # Generate random inland sea (2x1 or 1x2) (3% chance each)
                elif random.randint(1, 100) <= 3 and j > 0 and j < size - 1:
                    island_array[i][j] = Terrain.CALM_SEA
                    island_array[i][j + 1] = Terrain.CALM_SEA
                elif random.randint(1, 100) <= 3 and i > 0 and i < size - 1:
                    island_array[i][j] = Terrain.CALM_SEA
                    island_array[i + 1][j] = Terrain.CALM_SEA

    return island_array

if __name__ == "__main__":
    terrain = terrain_generator(15)
    # Pretty-print raw number values

    for row in terrain:
        print([value.value for value in row])
