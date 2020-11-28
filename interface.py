import tkinter as tk
from byteread import DaFile
import numpy as np
fl = open('3.jpg', 'rb')
da_f = DaFile()
da_f.f_use(fl)
print(da_f.df_rows)
fl .close()
df_page = da_f.page_load(20)



def str_hex(num):
    num = str(hex(num))
    
    return '0' +num
    
def InFocus(event):
    print(event.widget)
    event.widget.configure({"background": 'LightYellow2'})
   
    
def OutOfFocus(event):
    
    event.widget.configure({"background": 'white'})
    

def EntryClick(event): 
    # честно спзженно отсюда: https://www.geeksforgeeks.org/python-tkinter-grid_location-and-grid_size-method/
    # ф-я нахождения координаты 

    # Widget.winfo_rootx() - положение  фрейма отн всего экрана монитора
    # event.x_root - координата мыши отн всего экрана монитора
    global COLS, ROWS
    global eX, eY
    
    # Here retrieving the size of the parent 
    # widget relative to master widget
    x = event.x_root  -frame_hex_text.winfo_rootx()  
    y = event.y_root  - frame_hex_text.winfo_rooty()  

    print(frame_hex_text.winfo_rootx(), end=' - ')
    print(frame_hex_text.winfo_rooty() )
    print(event.x_root, end=' ~ ')
    print(event.y_root)

    # Here grid_location() method is used to 
    # retrieve the relative position on the 
    # parent widget 
    x, y = frame_hex_text.grid_location(x, y)
    #'!entry'
    x-=1
    y-=1
    print(x, end = ' ')
    print(y)

    
    if x== 0 and y == 0:
        
        frame_hex_text.children['!entry'].focus()
        eX = x
        eY = y
    elif x < 0 or y < 0 or x > COLS or y > ROWS:
        pass
    else:
        eX = x
        eY = y
        frame_hex_text.children['!entry'+ str(x + (COLS+1)*y+1)].focus()
    
    
def e_fill(df_page):
    global COLS, ROWS
    for i in range(ROWS+1):
        for j in range(COLS+1):
            if i== 0 and j == 0:
                frame_hex_text.children['!entry'].delete(0, 'end')
                try:
                    frame_hex_text.children['!entry'].insert(0,int(df_page[i][j]))
                except:
                    frame_hex_text.children['!entry'].insert(0,'')
                        
            else:
                frame_hex_text.children['!entry'+ str(j + (COLS+1)*i+1)].delete(0, 'end')
                try:
                    frame_hex_text.children['!entry'+ str(j + (COLS+1)*i+1)].insert(0,int(df_page[i][j]))
                except:
                    frame_hex_text.children['!entry'].insert(0,'')


def MoveLeft(event):
    global COLS, ROWS
    global eX, eY
        
    if event.widget.index(tk.INSERT)  == 0:
        eX -=1
        if eX < 0:
            eX = COLS
        if eX== 0 and eY == 0:
            frame_hex_text.children['!entry'].focus()
            frame_hex_text.children['!entry'].icursor(3)
        else:
            frame_hex_text.children['!entry'+ str(eX + (COLS+1)*eY+1)].focus()
            frame_hex_text.children['!entry'+ str(eX + (COLS+1)*eY+1)].icursor(4)
            
        

def MoveRight(event):
    global COLS, ROWS
    global eX, eY

    if event.widget.index(tk.INSERT)  == len(event.widget.get()):
        eX +=1
        if eX > COLS:
            eX = 0
        if eX== 0 and eY == 0:
            frame_hex_text.children['!entry'].focus()
            frame_hex_text.children['!entry'].icursor(3)
            frame_hex_text.children['!entry'+ str(eX + (COLS+1)*eY+1)].icursor(0)
        else:
            frame_hex_text.children['!entry'+ str(eX + (COLS+1)*eY+1)].focus()
            frame_hex_text.children['!entry'+ str(eX + (COLS+1)*eY+1)].icursor(4)
            frame_hex_text.children['!entry'+ str(eX + (COLS+1)*eY+1)].icursor(0)


        
def MoveUp(event):
    global COLS, ROWS
    global eX, eY
    
    eY -=1
    if eY < 0:
        eY +=1
        
        df_page = da_f.pg_up()
        
        e_fill(df_page)

    if eX== 0 and eY == 0:
        frame_hex_text.children['!entry'].focus()
        frame_hex_text.children['!entry'].icursor(event.widget.index(tk.INSERT))
    else:
        frame_hex_text.children['!entry'+ str(eX + (COLS+1)*eY+1)].focus()
        frame_hex_text.children['!entry'+ str(eX + (COLS+1)*eY+1)].icursor(event.widget.index(tk.INSERT))
        

def MoveDown(event):
    global COLS, ROWS
    global eX, eY
    
    eY +=1
    if eY > ROWS:
        eY -=1
        
        df_page = da_f.pg_down()
        
        e_fill(df_page)
                    #frame_hex_text.children['!entry'+ str(eX + (COLS+1)*eY+1)].icursor(event.widget.index(tk.INSERT))


            
    if eX== 0 and eY == 0:
        frame_hex_text.children['!entry'].focus()
        frame_hex_text.children['!entry'].icursor(event.widget.index(tk.INSERT))
    else:
        frame_hex_text.children['!entry'+ str(eX + (COLS+1)*eY+1)].focus()
        frame_hex_text.children['!entry'+ str(eX + (COLS+1)*eY+1)].icursor(event.widget.index(tk.INSERT))
        
def testVal(inStr,acttyp):
    #https://www.cyberforum.ru/python-graphics/thread2392322.html
    if acttyp == '1':
        if not inStr.isdigit():
            return False
    return True



    
root = tk.Tk()

global eX, eY
eX = 0
eY = 0
global COLS, ROWS
ROWS = 19
COLS = 15

frame_hex_text = tk.Frame(
            master=root,
            relief=tk.RAISED,
            borderwidth=1
        )
frame_hex_text.pack()


for i in range(ROWS+2):
    for j in range(COLS+2):
        
        if i == 0 and j != 0:
            
            label = tk.Label( master=frame_hex_text,
                                       text=str_hex(j-1),
                                       width=4,
                                       font="Courier 12",
                                       justify='center')
            label.grid(row=i, column=j,padx=1, pady=1)
            
        elif j == 0 and i != 0:
            
            label = tk.Label( master=frame_hex_text,
                                      text=str_hex(i-1),
                                      width=4,
                                      font="Courier 12",
                                      justify='center')
            label.grid(row=i, column=j,padx=1, pady=1)
            
        elif j == 0 and i == 0:
            pass
        else:
            entry_bytes =tk.Entry(
                                                        master=frame_hex_text,
                                                        width=4,
                                                        
                                                        font="Courier 12",
                                                        justify='center',
                                                        validate='key'
                                                        )
            
            #entry_bytes.insert(0,str(i) + ' '+ str(j))
            try:
                entry_bytes.insert(0,int(df_page[i-1][j-1]))
            except:
                entry_bytes.insert(0,'')
            
            entry_bytes.grid(row=i, column=j,padx=1, pady=1)
            
            entry_bytes['validatecommand'] = (entry_bytes.register(testVal),'%P','%d')

            entry_bytes.bind("<FocusIn>", lambda event: InFocus(event) )
            entry_bytes.bind("<FocusOut>",lambda event: OutOfFocus(event) )
            entry_bytes.bind("<Left>", lambda event: MoveLeft(event) )
            entry_bytes.bind("<Right>", lambda event: MoveRight(event) )
            entry_bytes.bind("<Up>", lambda event: MoveUp(event))
            entry_bytes.bind("<Down>", lambda event: MoveDown(event) )
            
            root.bind('<Button-1>', EntryClick)        


frame_hex_text.children['!entry'].focus()
frame_hex_text.children['!entry'].icursor(10)
print(frame_hex_text.children['!entry'].index(tk.INSERT))
root.mainloop()
