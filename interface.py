import tkinter as tk

def str_hex(num):
    num = str(hex(num))
    
    return '0' +num
    
def callback(e):
    e.widget.configure({"background": 'LightYellow2'})
def OutOfFocus(e):
    e.widget.configure({"background": 'white'})
root = tk.Tk()


rows = 20
cols = 16
entry_bytes = [[None]*(cols + 1)]*(rows +1) #contanis widgets entry
labels_row = [None]*(rows+1) #contanis widgets label
for i in range(rows+1):
    for j in range(cols+1):
        
        frame_hex_text = tk.Frame(
            master=root,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame_hex_text.grid(row=i, column=j,padx=1, pady=1)
        if i == 0 and j != 0:
            
            label = tk.Label(master=frame_hex_text, text=str_hex(j-1),width=4, font="Courier 12", justify='center')
            label.pack()
        elif j == 0 and i != 0:
            
            label = tk.Label(master=frame_hex_text, text=str_hex(i-1),width=4, font="Courier 12",justify='center')
            label.pack()
        elif j == 0 and i == 0:
            pass
        else:
            entry_bytes[i][j] = tk.Entry(master=frame_hex_text, width=4,font="Courier 12",justify='center')
            entry_bytes[i][j].bind("<FocusIn>", callback)
            entry_bytes[i][j].bind("<FocusOut>", OutOfFocus)
             
            entry_bytes[i][j].pack()
frame_hex_text = tk.Frame(master=root)
#frame_hex_text.pack()


root.mainloop()
