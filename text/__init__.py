from st3m.application import Application, ApplicationContext
from st3m.ui.colours import RED, GO_GREEN, BLACK
import st3m.run
import leds

"""
see python_payload/st3m/ui/colours.py for pre-definec colors
see components/ctx/ctx_config.h for pre-defined fonts
"""

class FontSwitcher(Application):
    def __init__(self, app_ctx: ApplicationContext) -> None:
        super().__init__(app_ctx)
        self.delta_ms = 0
        self.font_idx = 0
        self.font = ""
        self.init_done = False
        self.fonts = []

        leds.set_all_rgb(*GO_GREEN)
        # leds.set_all_rgb(255, 0, 0)
        leds.update()

    def draw(self, ctx: Context) -> None:
        if not self.init_done:
            i = 0
            try: 
                while True:
                    f = ctx.get_font_name(i)
                    # print(f)
                    self.fonts.append(f)
                    i += 1
            except ValueError as ve:
                pass
            self.num_fonts = i
            # print(f"we have {i} fonts available")
            self.font = self.fonts[0]
            self.init_done = True

        # Paint the background red
        # ctx.rgb(255, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.rgb(*RED).rectangle(-120, -120, 240, 240).fill()

        ctx.text_align = ctx.CENTER
        ctx.text_baseline = ctx.MIDDLE
        ctx.rgb(*BLACK)
        ctx.font_size = 30
        ctx.font = self.font
        ctx.move_to(0, 0)
        ctx.save()
        ctx.text(self.font)


    def think(self, ins: InputState, delta_ms: int) -> None:
        super().think(ins, delta_ms) # Let Application do its thing
        self.delta_ms += delta_ms

        if self.delta_ms >= 250:
            self.delta_ms = 0
            if ins.buttons.app == ins.buttons.PRESSED_RIGHT:
                self.font_idx = (self.font_idx + 1) % len(self.fonts)
            if ins.buttons.app == ins.buttons.PRESSED_LEFT:
                self.font_idx = self.font_idx - 1
                if self.font_idx < 0: self.font_idx = len(self.fonts) - 1

            self.font = self.fonts[self.font_idx]

if __name__ == '__main__':
    st3m.run.run_view(FontSwitcher(ApplicationContext()))
