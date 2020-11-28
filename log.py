"""
Created on Sun Nov  8 16:46:40 2020

@author: Danni
"""
import logging
import logging.handlers
import os

def startlogging(filename, filemode='w', level=logging.INFO, 
                 format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'): 
    """
    record console ouptut

    Parameters
    ----------
    filename : string
        name of your log.
    filemode : string, optional
        write or read. The default is 'w'.
    level : int or string , optional
        logging level. The default is logging.WARNING.
    format : string, optional
        the time format. The default is '%(asctime)s %(filename)s 
        [line:%(lineno)d] %(levelname)s %(message)s'.

    Returns
    -------
    None.

    """
    formatter = logging.Formatter(format)
    mylog = logging.getLogger()
    mylog.setLevel(level)
#write to log
    path = os.path.dirname(filename)
    if not os.path.isdir(path):
        os.makedirs(path)
    fh = logging.FileHandler(filename + ".log.wf")  
    ih = logging.FileHandler(filename + ".log")
    fh.setLevel(logging.WARNING)
    ih.setLevel(level)
    #console output
    ch = logging.StreamHandler()
    #record errors and warning messages
    ch.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    ih.setFormatter(formatter)
    ch.setFormatter(formatter)
    mylog.addHandler(fh)
    mylog.addHandler(ch)
    mylog.addHandler(ih)