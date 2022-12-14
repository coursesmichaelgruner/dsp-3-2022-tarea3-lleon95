#!/usr/env python3

import pyaudio
import sys

sample_format = pyaudio.paInt16  # 16 bits per sample
fs = 44100  # Record at 44100 samples per second
channels = 1
chunk = 1  # Record in chunks of 1 sample
seconds = 60
intconst = 32767

def ms_to_sample(ms):
    '''
    Converts the sample to 
    '''
    return int(fs * ms / 1000)

def system_function(current, a, former):
    b = 0.5
    c = 0.5

    inputsig = int(current * b)
    formersig = int(former[a] * c)
    return inputsig + formersig

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("ERROR: requires the delay as argument")
        print("\t python3 ex1.py DELAY")
        exit()
    
    delay = sys.argv[1]
    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    print('Recording')
    stream_mic = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    stream_speak = p.open(format = sample_format,
                    channels = channels,
                    rate = fs,
                    output = True)

    a = ms_to_sample(int(delay))

    # Store data in chunks for 3 seconds
    memory = [0 for i in range(a + 1)]
    for i in range(0, int(fs / chunk * seconds)):
        # Get the input sample
        inputdata = stream_mic.read(chunk)

        inputsample = int.from_bytes(inputdata, byteorder='little', signed=True)
        #print('inp', inputdata, inputsample)
        # Process the sample through the plant
        outputsample = system_function(inputsample, a, memory)
        # Process the output sample
        memory.insert(0, outputsample)
        memory.pop()
        outputdata = outputsample.to_bytes(2, byteorder='little', signed=True)
        #print('out', outputdata, outputsample)
        stream_speak.write(outputdata)

    # Stop and close the stream 
    stream_mic.stop_stream()
    stream_mic.close()
    stream_speak.stop_stream()
    stream_speak.close()
    # Terminate the PortAudio interface
    p.terminate()

print('Finished recording')
