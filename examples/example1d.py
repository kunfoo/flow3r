from st3m.reactor import Responder
from st3m.input import InputController
from st3m.utils import tau

import st3m.run

class Example(Responder):
    def __init__(self) -> None:
        self.input = InputController()
        self._x = -20.
        self._draw_rectangle = True
        self.delta = 0

    def draw(self, ctx: Context) -> None:
        # Paint the background black
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()

        # Paint a red square in the middle of the display
        if self._draw_rectangle:
            ctx.rgb(255, 0, 0).rectangle(self._x, -20, 40, 40).fill()
        else:
            ctx.rgb(255, 0, 0).arc(self._x, -20, 40, 0, tau, 0).fill()

    def think(self, ins: InputState, delta_ms: int) -> None:
        direction = ins.buttons.app # -1 (left), 1 (right), or 2 (pressed)
        direct = ins.buttons.os # -1 (left), 1 (right), or 2 (pressed)

        self.delta += delta_ms
        if self.delta > 500:
            self.delta = 0
            if direct == ins.buttons.PRESSED_DOWN:
                self._draw_rectangle = not self._draw_rectangle

        if direction == ins.buttons.PRESSED_LEFT:
            self._x -= 20 * delta_ms / 1000
        elif direction == ins.buttons.PRESSED_RIGHT:
            self._x += 20 * delta_ms / 1000

    """
    def think(self, ins: InputState, delta_ms: int) -> None:
        self.input.think(ins, delta_ms) # let the input controller to its magic

        if self.input.buttons.os.middle.pressed:
            self._draw_rectangle = not self._draw_rectangle

        if self.input.buttons.app.left.pressed:
            self._x -= 20 * delta_ms / 1000
        elif self.input.buttons.app.right.pressed:
            self._x += 20 * delta_ms / 1000
    """


st3m.run.run_responder(Example())
