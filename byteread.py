import numpy as np
import pandas as pd

#int.from_bytes(b'\xff', 'big') << ! >> bytes([255])


class DaFile:
    def __init__(self):
        
        # dataframe contains bytes of image 
        self.df = pd.DataFrame(index=[hex(0)], columns=[hex(i) for i in range(16)])

        #self.df_da_page = np.nan

        
    def f_use(self, f):
        #
        
        TR = True

        # rows in df
        self.df_rows = 0


        while TR:
            sxtnBytes,TR, self.cut = self.SixteenBytes(f)


            # why it's faster
            ## TO DO: check the speed
            
            #for j in range( len(sxtnBytes)-cut ):
            #    fb.write(bytes([sxtnBytes[j]]))
        
            #df.write(bytes(sxtnBytes[0:cut]))       
        
            self.df.loc[hex(self.df_rows)] = sxtnBytes
            
            self.df_rows +=1
        

    def page_load(self, ROWS=16, start_row = 0):
        # load first page
        
        # maybe i do it next time
        
        #COLS = 15, 
        #kt_df_rows = COLS * ROWS / 16
        #if kt_df_rows%16 != 0:
            #kt_df_rows += 1
            #kt_df_rows=int(kt_df_rows)


        ###
        #self.df_da_page = self.df[ 0 :ROWS ].to_numpy()
        self.start_row = start_row
        self.ROWS = ROWS
        return self.df[ self.start_row :self.start_row + self.ROWS ].to_numpy()
        
    def pg_down(self):
        self.start_row +=1
        return self.df[ self.start_row :self.start_row + self.ROWS ].to_numpy()

    def pg_up(self):
        self.start_row -=1
        if self.start_row < 0:
            self.start_row = self.df_rows - self.ROWS+1
        return self.df[ self.start_row :self.start_row + self.ROWS ].to_numpy()
    def save_to_csv(self, name = '0ut'):
        self.df.to_csv(name +'.csv')

    def save_to_im(self, fw=open('end.jpg', 'wb') ):
        #T0 D0: this
        pass

    def SixteenBytes(self, f):
        # actually it must be a function
        # it's returns list of next 16 bytes of file [ ret ]
        # if it's end of file, fills list with NaNs to the end, set TR as False and counts quantity of NaNs in cut

        ret = []
        TR = True
        
        # counter of NaNs in dadaframe
        self.cut = 0
        
        for i in range(16):
            byte = f.read(1)
            if byte: 
                if byte!=np.nan:     
                    ret.append(int.from_bytes(byte, 'big') )              
            else:
                TR = False
                ret.append(np.nan)
                self.cut +=1
        
        return ret, TR, self.cut



# testing...
fl = open('2.jpg', 'rb')


#da_f = DaFile()
#da_f.f_use(fl)
#da_f.page_load(32)

#fl .close()
#print(da_f.df)
#__________________________________
