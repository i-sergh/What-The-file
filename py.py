import numpy as np
import pandas as pd

fl = open('1.jpg', 'rb')
fb = open('end.jpg', 'wb')
#fb.close()
#fb = open('end.jpg', 'ab')
def SixteenBytes(f):
    ret = []
    TR = True
    for i in range(16):
        byte = f.read(1)
        if byte:
            if int.from_bytes(byte, 'big')== 133:
                ret.append(int.from_bytes(byte, 'big') - 10)
        
            elif int.from_bytes(byte, 'big')== 123:
                ret.append(int.from_bytes(byte, 'big') - 105)
            elif int.from_bytes(byte, 'big')> 80 and int.from_bytes(byte, 'big')< 100:
                ret.append(int.from_bytes(byte, 'big') - 15)
            else:
                ret.append(int.from_bytes(byte, 'big') )
            
        else:
            ret.append(np.nan)
            TR = False
    return ret, TR
    
  
df = pd.DataFrame(index=[hex(0)], columns=[hex(i) for i in range(16)])    
#int.from_bytes(b'\xff', 'big') << ! >> bytes([255])

TR = True
i = 0


while TR:
    sxtnBytes,TR = SixteenBytes(fl)
    
    for j in range(len(sxtnBytes)):
        try:
            if sxtnBytes != np.nan:
                fb.write(bytes([sxtnBytes[j]]))
        except:
            print(sxtnBytes[j])
    df.loc[hex(i)] = sxtnBytes
    i +=1
    
print(df)
df.to_csv('out.csv')

fl.close()
fb.close()
