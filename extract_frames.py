"""
This is a python script to extract a set of unique
telemetry frames from an ascii file and create a
file with the list of unique frames.
  
@author Nicholas St. Hill <nicholas.sthill@keiky.com>
"""
import os

filepath = "./test_data_20201021/ch1_20201021_17_swap.txt"
output_fpath = 'ch1_20201021_17_swap_list.txt'

# string used at the end of lines in the output file
endline = '\n'

unique_list = []
full_filepath = os.path.join(os.path.dirname(__file__),filepath)

try:
    f = open(full_filepath, "r")
    
    byte1 = f.read(2)
    byte2 = byte1
    frame = ''
    while byte1:
        byte2 = byte1
        byte1 = f.read(2)
        
        # Find the frame start
        if (byte2=='7E') and (byte1 != '7E') :
            # frame start
            frame = byte2 + byte1;

        elif (byte1=='7E') and (byte2 != '7E'):
            # frame end
            frame += byte1;
            
            if frame not in unique_list: 
                unique_list.append(frame)
            # 
            frame = '' # clear frame
        else:
             frame += byte1
       
        # 
    #
   
except:
    print("issue reading the file")
finally:
    f.close()
#

#%% Function to write a unique list to file   
def write_output_list_file(fpath, unique_list):
    """Write a unique list of frames to a text file"""
    try:
        f = open(fpath,'w')
        
        for line in unique_list:
            f.write(line)
            f.write(endline)
        #
    except:
        print('Error occured while writing unique lines')
    finally:
        f.close()
    #
    return
#
#%%
write_output_list_file(output_fpath, unique_list)