import arcade
from arcade import key


class Ball:
    def __init__(self, x, y, size, color, speed_x, speed_y):
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, (0, 240, 240))

    def on_update(self):
        self.x = self.x+self.speed_x
        self.y = self.y+self.speed_y


class Game1(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball(100, 250, 100, (0, 240, 240), 0, 0)
        arcade.set_background_color(arcade.color.DARK_SKY_BLUE)

    def on_update(self, delta_time: float):
        self.ball.on_update()

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def on_key_press(self, symbol: int, modifiers: int, ):
        if symbol == arcade.key.RIGHT:
            self.ball.speed_x+=3
        if symbol == arcade.key.LEFT:
            self.ball.speed_x-=3
        if symbol == arcade.key.UP:
            self.ball.speed_y+=3
        if symbol == arcade.key.DOWN:
            self.ball.speed_y-=3

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.ball.speed_x = 0
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.ball.speed_y = 0


    # !TODO Добавить on_key_press, on_key_release


HEIGHT = 500
WIDTH = 750


def main():
    game = Game1(WIDTH, HEIGHT, "Something_1")
    game.run()


main()
