import psutil
import curses
import time

def draw_menu(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()

    while True:
        stdscr.addstr(0, 0, "System Monitor - Press 'q' to exit", curses.A_BOLD)
        stdscr.addstr(2, 0, "CPU Usage:", curses.A_BOLD)
        stdscr.addstr(4, 0, "Memory Usage:", curses.A_BOLD)

        # Get CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        stdscr.addstr(2, 15, f"{cpu_percent:.2f}%", curses.color_pair(1))

        # Get memory usage
        mem = psutil.virtual_memory()
        mem_percent = mem.percent
        stdscr.addstr(4, 15, f"{mem_percent:.2f}%", curses.color_pair(2))

        stdscr.refresh()

        # Check for user input to exit
        user_input = stdscr.getch()
        if user_input == ord('q'):
            break

def main():
    try:
        curses.wrapper(draw_menu)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
