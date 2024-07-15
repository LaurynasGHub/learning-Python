# import GUI library
import PySimpleGUI as sg

# define class
class Hangman:
    # define apps window using window class
    def __init__(self) -> None:
        self._window = sg.Window(
            title="Hangman game tutorial",
            layout=[[]],
            # if set to true, can't modify game window after creation
            finalize=True,
            margins=(100, 100),
        )
    # define read event, it catches events like clicks etc.
    def read_event(self):
        event = self._window.read()
        event_id = event[0] if event is not None else None
        return event_id

    # let's to close app and terminate
    def close(self):
        self._window.close()

# define games loop
if __name__ == "__main__":
    # create instance of the games class
    game = Hangman()
    # event loop, while true game runs
    while True:
        # first init read to catch players actions
        event_id = game.read_event()
        if event_id in {sg.WIN_CLOSED}:
            break
        game.close()