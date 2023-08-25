from st3m.application import Application, ApplicationContext
import st3m.run
import leds

NUM_LEDs = 40
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
NUM_COLORS = 3

class LEDs(Application):
    def __init__(self, app_ctx: ApplicationContext) -> None:
        super().__init__(app_ctx)
        self.image_path = ""
        self.led = 0
        self.color_idx = 0
        self.color = COLORS[self.color_idx]


    def draw(self, ctx: Context) -> None:
        # Paint the background black
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()



    def think(self, ins: InputState, delta_ms: int) -> None:
        super().think(ins, delta_ms) # Let Application do its thing

        red = self.color[0]
        green = self.color[1]
        blue = self.color[2]

        leds.set_rgb(self.led, red, green, blue)
        leds.update()

        self.led += 1
        if self.led == 40:
            self.led = 0
            self.color_idx = (self.color_idx + 1) % NUM_COLORS
            self.color = COLORS[self.color_idx]


if __name__ == '__main__':
    st3m.run.run_view(LEDs(ApplicationContext()))
