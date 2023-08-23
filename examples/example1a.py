from st3m.reactor import Responder
import st3m.run

class Example(Responder):
    def __init__(self) -> None:
        pass

    def draw(self, ctx: Context) -> None:
        # Paint the background black
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()

        # Paint a red square in the middle of the display
        ctx.rgb(255, 0, 0).rectangle(-20, -20, 40, 40).fill()

    def think(self, ins: InputState, delta_ms: int) -> None:
        pass


st3m.run.run_responder(Example())
