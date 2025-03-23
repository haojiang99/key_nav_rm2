import curses
import key_nav_rm2.swipe as swipe

def on_key_event(event):
    if event.name == 'j':
        print("key pressed")

# Main function to listen for keyboard inputs
def main(stdscr):

    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()
    stdscr.addstr("Press key")
    stdscr.refresh()

    while True:
        key = stdscr.getch()

        if key == ord('j'):
            swipe.swipe("right")
        if key == ord('k'):
            swipe.swipe("left")
        if key == curses.KEY_LEFT:
            swipe.swipe("right")
        if key == curses.KEY_RIGHT:
            swipe.swipe("left")
        if key == 27:
            swipe.swipe("top")

        stdscr.refresh()

    keyboard.wait('esc')

if __name__ == "__main__":
    curses.wrapper(main)

