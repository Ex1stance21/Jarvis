import sys, os, time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pvporcupine, random, pygame
import sounddevice as sd
import speech_recognition as sr
import webbrowser
import subprocess
import os


def start_jarvis():
    pygame.mixer.init()

    Hi_ser = pygame.mixer.Sound('Audio\\Hi_sir.mp3')
    Yes_ser = [
        'Audio\\Yes_sir.mp3',
        'Audio\\Yes_sir2.mp3',
        'Audio\\Yes_sir3.mp3'
    ]

    Hi_ser.play()
    sd.wait(Hi_ser)

    handler = pvporcupine.create(
        access_key='q+ZjIphUWl1mPiAvhU9MiB7wrkS3OTmG+O49Ed7dSPMRRpr2xHaXBQ==',
        keyword_paths=[r'Models\Jarvis_wake_word.ppn'],
        sensitivities=[1]
    )

    recognizer = sr.Recognizer()

    active = False
    active_until = 0

    # Слухання команди через SpeechRecognition
    def listen_command_sr(timeout_sec=15, phrase_limit_sec=15):
        print(f"SR: слухаю команду до {timeout_sec} сек...")

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)

            try:
                audio = recognizer.listen(
                    source,
                    timeout=timeout_sec,
                    phrase_time_limit=phrase_limit_sec
                )
            except sr.WaitTimeoutError:
                print("Ніхто не говорить, час вичерпано.")
                return None

        try:
            text = recognizer.recognize_google(audio, language='uk-UA')
            return text
        except sr.UnknownValueError:
            print("Не вдалося розпізнати мову.")
            return None
        except sr.RequestError as e:
            print(f"Помилка запиту до сервісу розпізнавання: {e}")
            return None

    # Виконання команд
    def execute_command(command_text):
        if not command_text:
            return

        text = command_text.lower()

        if "браузер" in text or "хром" in text or "chrome" in text:
            webbrowser.open("https://www.google.com")

        else:
            print("Команда не розпізнана, поки що нічого не роблю.")

    # Callback Porcupine
    def callback(indata, frames, time_info, status):
        nonlocal active, active_until

        pcm = indata[:, 0]
        now = time.time()

        # Якщо вже в активному режимі і 30 секунд ще не минули —
        # одразу слухаємо команду, без wake-word.
        if active and now < active_until:
            command_text = listen_command_sr(timeout_sec=15, phrase_limit_sec=15)
            print("Команда:", command_text)
            execute_command(command_text)

            # продовжуємо ще на 30 секунд
            active_until = time.time() + 30
            return

        if now >= active_until:
            active = False

        # Тут працює wake-word
        if handler.process(pcm) >= 0:
            Random_sound = random.choice(Yes_ser)
            sound = pygame.mixer.Sound(Random_sound)
            sound.play()

            time.sleep(sound.get_length())

            # Вмикаємо режим команд на 30 секунд
            active = True
            active_until = time.time() + 30

            command_text = listen_command_sr(timeout_sec=15, phrase_limit_sec=15)
            print("Перша команда:", command_text)
            execute_command(command_text)

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
