import arcade

HEIGHT=500
WIDTH=750


class Game1 (arcade.Window):
    def __init__(self,width,height,title):
        ball_1=ball(arcade.color.BLUE,140,50,70,70,12,12)
        super().__init__(width,height,title)
        self.ball=ball((0,195,200),100,5,20,20,15,15)
        arcade.set_background_color(arcade.color.DARK_SKY_BLUE)
        ball_0=ball(arcade.color.BITTER_LIME,120,70,70,70,14,14)
        ball_2 = ball(arcade.color.DARK_VIOLET,100,20,70,70,9,9)
        ball_3 = ball(arcade.color.DEER,200,180,70,70,17,17)
        ball_4 = ball(arcade.color.DEBIAN_RED, 10, 180, 70, 70, 5, 5)
        self.balls=[ball_0,ball_1,ball_2,ball_3,ball_4]

    def on_draw(self):
        arcade.start_render()
        for i in range(len(self.balls)):
            self.balls[i].on_draw()


    def on_update(self, delta_time: float):
        for i in range(len(self.balls)):
            self.balls[i].on_update(delta_time)

class ball:
    def __init__(self, color, x, y, width, height, speed_x, speed_y):
        self.x=x
        self.y=y
        self.color=color
        self.width=width
        self.height=height
        self.speed_x=speed_x
        self.speed_y=speed_y
    def on_update(self, delta_time: float):
        self.x+=self.speed_x
        self.y+=self.speed_y
        if self.x>=WIDTH:
            self.speed_x*=(-1)
        if self.y>=HEIGHT:
            self.speed_y*=(-1)
        if self.x<=0:
            self.speed_x*=(-1)
        if self.y<=0:
            self.speed_y*=(-1)
    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, 100, 100, (self.color))















def main():
    game=Game1(WIDTH,HEIGHT,"Something_1")
    game.run()

main()