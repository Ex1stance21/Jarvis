import pvporcupine
import sounddevice as sd
import numpy as np
import time

class WakeWordDetector:
    def __init__(self, access_key, keyword_paths, sensitivities):
        self.porcupine = pvporcupine.create(
            access_key=access_key,
            keyword_paths=keyword_paths,
            sensitivities=sensitivities,
        )

    def callback(self, indata, frames, time, status):
        pcm = indata[:, 0]
        if self.porcupine.process(pcm) >= 0:
            print("Detected")

    def mic_on(self):
        with sd.InputStream(
                samplerate=self.porcupine.sample_rate,
                blocksize=self.porcupine.frame_length,
                channels=1,
                dtype='int16',
                callback=self.callback
        ):
            input("Натисніть Enter для завершення...\n")

    def start(self):
        self.mic_on()

detector = WakeWordDetector(
    'q+ZjIphUWl1mPiAvhU9MiB7wrkS3OTmG+O49Ed7dSPMRRpr2xHaXBQ==',
    [r'Models\Jarvis_wake_word.ppn'],
    [1]
)
detector.start()

