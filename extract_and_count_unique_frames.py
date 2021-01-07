"""
This is a python script to extract and count the set of unique
telemetry frames from an ascii file and create a
file with the list of unique frames.
"""
import os
from pathlib import Path

import vhdl_utils.realterm_vhdl_write as realterm_vhdl_write

filepath = "./test_data_20201021/ch0_20201021_0.txt"
output_file_suffix = '_list'

# string used at the end of lines in the output file
endline = '\n'

ignore_singles = True

unique_list = []
frame_dict = dict()
full_filepath = os.path.join(os.path.dirname(__file__),filepath)

#%%
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
                
                # Initialize frame count
                frame_dict[frame] = 1
            else:
                # increment count
                frame_dict[frame] = frame_dict[frame] + 1
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
def write_frame_count_list_file(fpath, frame_dict):
    """Write a unique list of frames to a text file"""
    try:
        f = open(fpath,'w')
        
        for key in frame_dict:
            
            cnt = frame_dict[key]
            if ignore_singles==True and (1 == cnt) :
                continue
            #   
            # Create a count string
            cnt_str = '[{}]'.format(cnt)
            # Print the count on one line
            f.write(cnt_str)
            f.write(endline)
            # Print the frame on the following line
            f.write(key)
            f.write(endline)
        #
    except:
        print('Error occured while writing unique lines')
    finally:
        f.close()
    #
    return
#

#%% Create the output file name
def create_output_filepath(fpath, suffix='_list', ext=".txt"):
    """Create the output file path"""
    name = Path(fpath).name
    s = os.path.splitext(name)[0]
    s += suffix + ext
    return s

#%% Output the text version
output_fpath = create_output_filepath(full_filepath, suffix=output_file_suffix)
write_frame_count_list_file(output_fpath, frame_dict)

#%% Write a VHDL output file
vhdl_fpath = create_output_filepath(full_filepath, suffix='',ext='.vhd')
realterm_vhdl_write.write_dict(frame_dict, vhdl_fpath)

