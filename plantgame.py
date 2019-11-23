#Authors: Lucklita Theng and Izzy Charlton
from arcade import *

screen_width = 400
screen_height = 600

#creating a class for the main menu of the game
class mainGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.GREEN)

    def setUp(self):

        # setting the game environment
        self.player_list = arcade.SpriteList()
        self.insect_list = arcade.SpriteList()
        self.obstacles_list = arcade.SpriteList()

        # game score
        self.score = 0

        # Level 1: create seed, and seedshell to break
        SpriteScale = 2
        self.seed_sprite = arcade.Sprite("seed.png", SpriteScale)
        self.seed_sprite.center_x = 200
        self.seed_sprite.center_y = 100
        self.player_list.append(self.seed_sprite)

        self.seedshell_sprite = arcade.Sprite("seedshell.png", SpriteScale)
        self.seedshell_sprite.center_x = 200
        self.seedshell_sprite.center_y = 100
        self.player_list.append(self.seed_sprite)

        # Level 2: create insects as obstacles
        self.insect1_sprite = arcade.Sprite("insect.png", SpriteScale)
        elf.insect1_sprite.center_x = 50
        self.insect1_sprite.center_y = 100
        self.obstacle_list.append(self.insect1_sprite)

        self.insect2_sprite = arcade.Sprite("insect.png", SpriteScale)
        elf.insect2_sprite.center_x = 350
        self.insect2_sprite.center_y = 200
        self.obstacle_list.append(self.insect2_sprite)

        self.insect3_sprite = arcade.Sprite("insect.png", SpriteScale)
        elf.insect3_sprite.center_x = 50
        self.insect3_sprite.center_y = 300
        self.obstacle_list.append(self.insect3_sprite)

        self.insect4_sprite = arcade.Sprite("insect.png", SpriteScale)
        elf.insect4_sprite.center_x = 350
        self.insect4_sprite.center_y = 400
        self.obstacle_list.append(self.insect4_sprite)

        self.insect5_sprite = arcade.Sprite("insect.png", SpriteScale)
        self.insect5_sprite.center_x = 50
        self.insect5_sprite.center_y = 500
        self.obstacle_list.append(self.insect5_sprite)

        # Level 3: create raindrops to catch and lightnings to avoid
        raindrop_counts =
        lightning_counts =

        # create raindrops to fall randomly from the sky
        for i in range(raindrops_count):
            raindrops = arcade.Sprite("", SpriteScale)

            raindrops.center_x =

        pass

    def draw(self):
        arcade.start_render()
        # drawing objects appearing on screen of game
        pass

    def updateGame(self, delta_time):
        # coding of movements and the game logic
        pass

def main():
    game = mainGame(screen_width, screen_height)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
