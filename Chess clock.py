"""A simple chess timer. Default time is 5 minutes, minimum time is 1 minute, can only
accept whole numbers."""

import tkinter as T
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta
    
global white, black, white_moove, white_time, black_time, game_on, mins, hours
game_on = 1

while game_on == 1:
    time_root = T.Tk()
    h = int(time_root.winfo_reqheight()*3)
    w = int(time_root.winfo_reqwidth())
    size_pos = f'+{h}+{w}'
    mins = T.Entry(time_root, textvariable=T.StringVar)
    hours = T.Entry(time_root, textvariable=T.StringVar)
    min_label = T.Label(time_root, text='Minutes')
    hour_label = T.Label(time_root, text='Hours')
    label = T.Label(time_root,text='♔♕ ♛♚ ♔♕ ♛♚ ♔♕ ♛♚ ♔♕ ♛♚ ♔♕ ♛♚')
    mins.grid(row=0, column=1)  
    hours.grid(row=1, column=1)
    min_label.grid(row=0, column=0)
    hour_label.grid(row=1, column=0)
    label.grid(row=3, column=0, columnspan=3)
    time_root.geometry(f'{size_pos}')

    def start():
        """Validiate time input and start game or take input again"""
        global mins, hours, game_on
        hours = hours.get()
        mins = mins.get()
        if len(hours) == 0 or len(mins) == 0:
            messagebox.showinfo('NOTICE', 'No time frame defined, default is 5 minute blitz.')
            hours = '0'
            mins = '5'
        try:
            time_check = int(mins) + int(hours)
        except:
            messagebox.showinfo('FAIL', 'Can only accept whole numbers (no strings or signs)')
            hours = '0'
            mins = '1'
            game_on = 2
        time_root.destroy()
        return None

    start = T.Button(time_root, text='Start game', command=start).grid(column=1, row=4, sticky=T.W, pady=4)
    time_root.title("Set time")
    time_root.mainloop()

    time_input = '{}:{}:00'.format(hours, mins)
    game_time = datetime.strptime(time_input, '%H:%M:%S')
    white_time = game_time
    black_time = game_time
    white = datetime.strftime(game_time, '%H:%M:%S')
    black = datetime.strftime(game_time, '%H:%M:%S')
    white_moove = 0
    root = T.Tk()
    root.geometry(size_pos)
    root.title("Game on!")

    def pass_turn():
        """Passes the turn between players"""
        global white_moove
        if white_moove == 0:
            white_moove = 1
        else:
            white_moove = 0
        return None
    
    def restart():
        """Restart the game for any reason"""
        global game_on
        game_on = 2
        return None

    root.bind('<Return>', pass_turn)
    pass_button = T.Button(root, text='Press ENTER to pass turn', command=pass_turn)
    restart_button = T.Button(root, text='Restart', command=restart)
    timer = T.Label(root, text=f'White: {white} Black: {black}')
    timer.pack()
    pass_button.pack() 
    restart_button.pack()

    def start_timer():
        """Start the timer, white opens. If input was invalid timer will not start."""
        global white, black, white_time, black_time, game_on
        if game_on == 1:
            if white_moove == 0:
                interval = 1
                white_time = white_time - timedelta(seconds=interval)
                white = datetime.strftime(white_time, '%H:%M:%S')
                timer.config(text=f'White: {white}    Black: {black}')
            else:
                interval = 1
                black_time = black_time - timedelta(seconds=interval)
                black = datetime.strftime(black_time, '%H:%M:%S')
                timer.config(text=f'White: {white}    Black: {black}')
        if game_on == 2:
            game_on = 1
            root.destroy()                
        if white == '00:00:00':
            game_on = 0
            root.destroy()
            win = T.Tk()
            win.geometry(size_pos)
            msg = T.Label(win, text=f'Times up for white!\nBlack is left with {black}')
            fin = T.Button(win, text='Exit', command=quit)

            def restart():
                global game_on
                game_on=1
                win.destroy()
                return None

            another_game = T.Button(win, text='Play again', command=restart)
            msg.pack()
            fin.pack()
            another_game.pack()
            win.mainloop()
        elif black_time.strftime('%H:%M:%S') == '00:00:00':
            game_on = 0
            root.destroy()
            win = T.Tk()
            win.geometry(size_pos)
            msg = T.Label(win, text=f'Times up for black!\nWhite is left with {white}')
            msg.pack()
            fin = T.Button(win, text='Exit', command=quit)

            def restart():
                global game_on
                game_on=1
                win.destroy()
                return None

            another_game = T.Button(win, text='Play again', command=restart)
            msg.pack()
            fin.pack()
            another_game.pack()
            win.mainloop()

        root.after(1000,start_timer)

    start_timer()
    root.mainloop()