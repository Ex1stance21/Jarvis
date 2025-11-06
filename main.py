import pvporcupine
import sounddevice as sd
import struct

class WakeWordDetector:
    def __init__(self, access_key, keyword_paths, sensitivities=0.7):
        self.access_key = access_key
        self.keyword_paths = keyword_paths
        self.sensitivities = sensitivities

    def listener(self):
        self.handler = pvporcupine.create(
            access_key=self.access_key,
            keyword_paths=self.keyword_paths,
            sensitivities=self.sensitivities,
        )

    def callback(self, indata, frames, time, status):
        pcm = struct.unpack_from("h" * self.handler.frame_length, indata)
        if self.handler.process(pcm) >= 0:
            print("Detected")
    def mic_on(self):
        with sd.InputStream(
                samplerate=self.handler.sample_rate,
                blocksize=self.handler.frame_length,
                channels=1,
                callback=self.callback
        ):
            input("Натисніть Enter для завершення...\n")

    def start(self):
        self.listener()
        self.mic_on()
detector = WakeWordDetector('q+ZjIphUWl1mPiAvhU9MiB7wrkS3OTmG+O49Ed7dSPMRRpr2xHaXBQ=='
                            , [r'Models\Jarvis_wake_word.ppn'], [0.7])
detector.start()

