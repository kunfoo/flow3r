from st3m.reactor import Responder
import st3m.run

class Example(Responder):
    def __init__(self) -> None:
        self._x = -20

    def draw(self, ctx: Context) -> None:
        # Paint the background black
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()

        # Paint a red square in the middle of the display
        ctx.rgb(255, 0, 0).rectangle(self._x, -20, 40, 40).fill()

    def think(self, ins: InputState, delta_ms: int) -> None:
        direction = ins.buttons.app

        if direction == ins.buttons.PRESSED_LEFT:
            self._x -= 1
        elif direction == ins.buttons.PRESSED_RIGHT:
            self._x += 1


st3m.run.run_responder(Example())
