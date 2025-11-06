import os, pvporcupine, random, pygame
import sounddevice as sd
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

pygame.mixer.init()
Hi_ser = pygame.mixer.Sound('Audio\\Hi_sir.mp3')
Yes_ser = ['Audio\\Yes_sir.mp3',
           'Audio\\Yes_sir2.mp3',
           'Audio\\Yes_sir3.mp3']
Hi_ser.play()
sd.wait()

handler = pvporcupine.create(
    access_key='q+ZjIphUWl1mPiAvhU9MiB7wrkS3OTmG+O49Ed7dSPMRRpr2xHaXBQ==',
    keyword_paths=[r'Models\Jarvis_wake_word.ppn'],
    sensitivities=[1]
)

start_time = None

def callback(indata, frames, time_info, status):
    pcm = indata[:, 0]

    if handler.process(pcm) >= 0:
        Random_sound = random.choice(Yes_ser)
        sound = pygame.mixer.Sound(Random_sound)
        sound.play()

def mic_on():
    with sd.InputStream(
            samplerate=handler.sample_rate,
            blocksize=handler.frame_length,
            channels=1,
            dtype='int16',
            latency='low',
            callback=callback
    ):
        input("Натисніть Enter для завершення...\n")

mic_on()

handler.delete()

