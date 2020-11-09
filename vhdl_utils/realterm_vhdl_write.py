import numpy as np

__endline = '\r'

def __create_comment(cnt):
    s = '-- [{0}]'.format(cnt)
    s += __endline
    return s

def __create_array_def(data):
    n = int(len(data)/2) - 1
    s = '-- le_byte_array(0 to {0})'.format(n)
    s += __endline
    return s    
    
def __create_data(data):
    
    line_list = []
    ind = np.arange(0, len(data), 2)
    
    def write_hex_byte(x):
        return "x\"" + x + "\""
        
    for n in ind:
        # get the string for the byte
        s = write_hex_byte(data[n:n+2])
        # append to the list
        line_list.append(s)
    #
        
    line = ",".join(line_list)
    return line

def write_dict(dict_data, fpath):
    try:
        f = open(fpath,'w')
        
        for key in dict_data:
            
            cnt = dict_data[key]
            if (1 == cnt) :
                continue
            #   
            # Write the comment line
            comment = __create_comment(cnt)
            f.write( comment)
            
            f.write( __create_array_def(key))

            # Print the frame on the following line
            f.write( __create_data(key))
            f.write( __endline)
        #
    except:
        print('Error occured while writing unique lines')
    finally:
        f.close()
    #
    return
