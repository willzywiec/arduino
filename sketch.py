# sketch.py

import pandas as pd
import serial
import time

pd.set_option('precision', 15) # double precision

port = 'COM3'
rate = 9600

def main():
    start = time.time()
    output = []
    ser = serial.Serial(port, rate)
    while True:
        read = ser.readline() # .decode('utf-8')
        mark = time.time() - start
        print(mark)
        output.append(mark)
        dictionary = {'output':output}
        df = pd.DataFrame(dictionary)
        df.to_csv('output.csv', index = False)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('stopped')
