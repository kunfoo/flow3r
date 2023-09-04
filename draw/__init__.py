from st3m.application import Application, ApplicationContext
from st3m.ui.colours import RED, BLACK, BLUE, GREEN, WHITE
import st3m.run
import leds
import math

class DrawSomething(Application):
    def __init__(self, app_ctx: ApplicationContext) -> None:
        super().__init__(app_ctx)
        self.x = 0
        self.y = 120
        self.rotation = 0
        self.rotate_left = True
        self.delta_ms = 0

        leds.set_all_rgb(*RED)
        leds.update()

    def draw(self, ctx: Context) -> None:
        # Paint the background black
        ctx.rgb(*BLACK).rectangle(-120, -120, 240, 240).fill()

        ctx.rotate(self.rotation)
        ctx.rgb(*RED)
        ctx.move_to(0, ctx.height/2).line_to(0, -ctx.height/2).stroke()
        ctx.rgb(*BLUE)
        ctx.move_to(ctx.width/2, 0).line_to(-ctx.width/2, 0).stroke()
        ctx.rgb(*GREEN)
        ctx.move_to(ctx.width/2, ctx.height/2).line_to(-ctx.width/2, -ctx.height/2).stroke()
        ctx.rgb(*WHITE)
        ctx.move_to(-ctx.width/2, ctx.height/2).line_to(ctx.width/2, -ctx.height/2).stroke()


    def think(self, ins: InputState, delta_ms: int) -> None:
        super().think(ins, delta_ms) # Let Application do its thing

        if ins.buttons.app == ins.buttons.PRESSED_RIGHT:
            self.rotate_left = False
        elif ins.buttons.app == ins.buttons.PRESSED_LEFT:
            self.rotate_left = True

        # rotate 1 degree
        if self.rotate_left:
            self.rotation -= math.pi / 180
        else:
            self.rotation += math.pi / 180


if __name__ == '__main__':
    st3m.run.run_view(DrawSomething(ApplicationContext()))
