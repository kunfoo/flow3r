from st3m.application import Application, ApplicationContext
from st3m.ui.colours import RED
import st3m.run
import leds

"""
see python_payload/st3m/ui/colours.py for pre-definec colors
see components/ctx/ctx_config.h for pre-defined fonts
"""

class CatImage(Application):
    def __init__(self, app_ctx: ApplicationContext) -> None:
        super().__init__(app_ctx)
        self.delta_ms = 0
        self.image_path = "/sd/apps/image/cat.png"

        leds.set_all_rgb(*RED)
        leds.update()

    def draw(self, ctx: Context) -> None:
        # Paint the background red
        # ctx.rgb(255, 0, 0).rectangle(-120, -120, 240, 240).fill()
        # ctx.rgb(*RED).rectangle(-120, -120, 240, 240).fill()

        ctx.image(self.image_path, -120, -120, 240, 240)


    def think(self, ins: InputState, delta_ms: int) -> None:
        super().think(ins, delta_ms) # Let Application do its thing
        self.delta_ms += delta_ms

        if self.delta_ms >= 250:
            self.delta_ms = 0
            if ins.buttons.app == ins.buttons.PRESSED_RIGHT:
                pass
            elif ins.buttons.app == ins.buttons.PRESSED_LEFT:
                pass
            elif ins.buttons.app == ins.buttons.PRESSED_DOWN:
                pass


if __name__ == '__main__':
    st3m.run.run_view(CatImage(ApplicationContext()))
