import math
import pyaudio

PyAudio = pyaudio.PyAudio

bit_rate = 16000
frequency = 500 + 100
input_data = "• • • —".split()
wave_data = ""
length = len(input_data)

bit_rate = max(bit_rate, frequency + 100)
number_of_frames = int(bit_rate)
rest_frames = number_of_frames % bit_rate

for i in range(length):
    el = input_data.pop(0)
    if el == "•":
        for x in range(number_of_frames // 15):
            wave_data += chr(int(math.cos(x /
                             ((bit_rate / frequency) / math.pi))))
    elif el == "—":
        for x in range(number_of_frames // 5):
            wave_data += chr(int(math.sin(x) + 127))
    for x in range(number_of_frames // 12):
        wave_data += chr(0)
# for x in range(rest_frames):
#    wave_data = wave_data + chr(128)

p = PyAudio()
stream = p.open(
    format=p.get_format_from_width(1), channels=1, rate=bit_rate, output=True
)

stream.write(wave_data)
stream.stop_stream()
stream.close()
p.terminate()
