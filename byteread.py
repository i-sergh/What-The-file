import numpy as np
import pandas as pd

#int.from_bytes(b'\xff', 'big') << ! >> bytes([255])


class DaFile:
    def __init__(self):
        
        # dataframe contains bytes of image 
        self.df = pd.DataFrame(index=[hex(0)], columns=[hex(i) for i in range(16)])

        

        
    def f_use(self, f):
        #
        
        TR = True

        # rows in df
        i = 0


        while TR:
            sxtnBytes,TR, self.cut = self.SixteenBytes(fl)


            # why it's faster
            ## TO DO: check the speed
            
            #for j in range( len(sxtnBytes)-cut ):
            #    fb.write(bytes([sxtnBytes[j]]))
        
            #df.write(bytes(sxtnBytes[0:cut]))       
        
            self.df.loc[hex(i)] = sxtnBytes
            
            i +=1

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
fl = open('1.jpg', 'rb')


da_f = DaFile()
da_f.f_use(fl)
da_f.save_to_csv()

#print(da_f.df)
#__________________________________
