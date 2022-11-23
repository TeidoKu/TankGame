import pygame

SCREEN_SIZE = (500, 500)


class Mushroom(pygame.sprite.Sprite):
    """This is the class for a falling mushroom"""

    base_image = pygame.image.load("wall-icon.png")

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(self.base_image, (50, 50))
        self.rect = self.image.get_rect()
        # Starting position = top of the screen
        # self.rect.x = SCREEN_SIZE[0] / 2
        # self.rect.y = 0

    # def update(self):
    #     self.rect.y += 5
    #     # The mushroom cannot go below the screen
    #     if self.rect.bottom > SCREEN_SIZE[1]:
    #         self.rect.bottom = SCREEN_SIZE[1]


class Tank(pygame.sprite.Sprite):
    """This is the main player Class"""

    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("t34.png")
        self.grow_factor = 1
        self.image = pygame.transform.scale(self.original_image, (100, 95))
        self.rect = self.image.get_rect()

        # Starting position = middle of the screen, bottom
        self.rect.x = SCREEN_SIZE[0] / 2
        self.rect.bottom = SCREEN_SIZE[1]

    def grow(self):
        """Increase Mario's size"""

        self.grow_factor += 1
        self.resize()

    def resize(self):
        """Recreate the sprite with the updated dimensions"""

        old_rect = self.rect
        new_size = (100 * self.grow_factor, 95 * self.grow_factor)
        self.image = pygame.transform.scale(self.original_image, new_size)
        self.rect.x = old_rect[0] - (new_size[0] - old_rect[2])
        self.rect.y = old_rect[1] - (new_size[1] - old_rect[2])


def main():
    """Main function to run the game"""

    pygame.init()

    # Screen is 500x500 pixels
    window = pygame.display.set_mode((500, 500))
    window.set_colorkey((255, 255, 255))
    clock = pygame.time.Clock()

    # New player
    tank = Tank()

    # Mushroom sprite group
    mushrooms = pygame.sprite.Group()
    mushroom = Mushroom()
    mushrooms.add(mushroom)

    running = True
    while running:
        # Paint the screen white
        window.fill((255, 255, 255))

        # Create a new Clock object
        clock.tick(30)

        # Update all the mushrooms
        mushrooms.update()

        # Mario touched a mushroom!
        if pygame.sprite.spritecollide(tank, mushrooms, dokill=True):
            tank.grow()

        # Event loop - quit if closed or 'escape' is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = event.pos
                if tank.rect.collidepoint(mouse):
                    print("You clicked Mario!")

        # Get the keys outside of the event loop (!)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            # Move the player right by 20 pixels
            # We have to make sure it does not go "off" the screen
            tank.rect.right = min(tank.rect.right + 20, 0)
        if keys[pygame.K_LEFT]:
            # Move the player left by 20 pixels
            tank.rect.left = max(tank.rect.left - 20, 0)

        # Update the player image
        window.blit(tank.image, tank.rect)
        mushrooms.draw(window)

        # Update the screen
        pygame.display.update()


if __name__ == "__main__":
    main()
