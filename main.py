import curses

def main(stdscr):
    s = stdscr

    #limpa
    s.clear()

    #tira o cursor
    curses.curs_set(0)

    #msg
    s.addstr(8,8, 'bom dia')

    #bota a msg
    s.refresh()

    # q pra fechar
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(main)