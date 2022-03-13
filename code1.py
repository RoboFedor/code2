import arcade


class ball:
    def __init__(self, x, y, size, color):
        self.size = size
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, (0, 240, 240))


class Game1(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        self.ball = ball(50, 50, 100, (0, 240, 240))
        arcade.set_background_color(arcade.color.DARK_SKY_BLUE)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.size += 20
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.ball.size -= 20

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.ball.x = x
        self.ball.y = y

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()


HEIGHT = 500
WIDTH = 750


def main():
    game = Game1(WIDTH, HEIGHT, "Something_1")
    game.run()


main()
