from st3m.application import Application, ApplicationContext
import st3m.run
import captouch


class CapTouch(Application):
    def __init__(self, app_ctx: ApplicationContext) -> None:
        super().__init__(app_ctx)
        captouch.calibration_request()
        self.delta = 0


    def draw(self, ctx: Context) -> None:
        # Paint the background black
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()



    def think(self, ins: InputState, delta_ms: int) -> None:
        super().think(ins, delta_ms) # Let Application do its thing

        self.delta += delta_ms
        if self.delta >= 1000:
            self.delta = 0
            petals = captouch.read().petals
            for i, p in enumerate(petals):
                if p.pressed:
                    pads = p.pads
                    distance, angle = p.position
                    if p.top:
                        print(f"top petal {i} pressed.")
                        print(f"pad.cw: {pads.cw}")
                        print(f"pad.ccw: {pads.ccw}")
                    elif p.bottom:
                        print(f"bottom petal {i} pressed.")
                        if pads.tip: print("pad tip touched")
                    if pads.base: print("pad base touched")
                    print(f"distance: {distance}")
                    print(f"angle: {angle}")


if __name__ == '__main__':
    st3m.run.run_view(CapTouch(ApplicationContext()))
