import sys, os, time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pvporcupine, random, pygame
import sounddevice as sd
import speech_recognition as sr
import webbrowser
import os

running_flag = False


def stop_jarvis():
    global running_flag
    running_flag = False


def start_jarvis():
    global running_flag
    running_flag = True

    pygame.mixer.init()

    Hi_ser = pygame.mixer.Sound('Audio\\Hi_sir.mp3')
    Yes_ser = [
        'Audio\\Yes_sir.mp3',
        'Audio\\Yes_sir2.mp3',
        'Audio\\Yes_sir3.mp3'
    ]
    Bye_sir = pygame.mixer.Sound('Audio\\bye_sir.mp3')
    Ok_sir = pygame.mixer.Sound('Audio\\ok_sir.mp3')
    Hi_ser.play()
    sd.wait(Hi_ser)

    handler = pvporcupine.create(
        access_key='q+ZjIphUWl1mPiAvhU9MiB7wrkS3OTmG+O49Ed7dSPMRRpr2xHaXBQ==',
        keyword_paths=[r'Models\\Jarvis_wake_word.ppn'],
        sensitivities=[1]
    )

    recognizer = sr.Recognizer()

    active = False
    active_until = 0
    active_session_end = 0

    def listen_command_sr(timeout_sec=15, phrase_limit_sec=15):
        global running_flag
        if not running_flag:
            return None

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

        if not running_flag:
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

    def execute_command(command_text):
        global running_flag

        if not command_text:
            return

        text = command_text.lower()

        if "знайди" in text:
            Ok_sir.play()
            query = text.split("знайди", 1)[1].strip()
            if query:
                url = "https://www.google.com/search?q=" + query.replace(" ", "+")
                webbrowser.open(url)

        elif "браузер" in text or "хром" in text or "chrome" in text:
            Ok_sir.play()
            webbrowser.open("https://www.google.com")

        elif "стім" in text or "steam" in text:
            Ok_sir.play()
            os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")

        elif "діскорд" in text or "discord" in text:
            Ok_sir.play()
            os.startfile(r"C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk")

        elif "саундклауд" in text or "soundcloud" in text or "музика" in text:
            Ok_sir.play()
            webbrowser.open(r"C:\SoundCloud.lnk")

        elif "вимкнись" in text or "стоп" in text or "припини" in text:
            Bye_sir.play()
            sd.wait(Bye_sir)
            running_flag = False

    def callback(indata, frames, time_info, status):
        global running_flag
        nonlocal active, active_until, active_session_end

        if not running_flag:
            raise sd.CallbackStop()

        pcm = indata[:, 0]
        now = time.time()

        if active and now >= active_session_end:
            print("Час сесії 30 секунд минув, повертаюсь до wake-word.")
            active = False

        if active and now < active_until:
            command_text = listen_command_sr(timeout_sec=15, phrase_limit_sec=15)
            print("Команда:", command_text)
            execute_command(command_text)
            if not running_flag:
                raise sd.CallbackStop()
            active_until = time.time() + 30
            return

        if now >= active_until:
            active = False

        if handler.process(pcm) >= 0:
            Random_sound = random.choice(Yes_ser)
            sound = pygame.mixer.Sound(Random_sound)
            sound.play()

            time.sleep(sound.get_length())

            active = True
            now = time.time()
            active_until = now + 30          # таймаут між командами
            active_session_end = now + 30    # вся сесія максимум 30 сек

            command_text = listen_command_sr(timeout_sec=15, phrase_limit_sec=15)
            print("Перша команда:", command_text)
            execute_command(command_text)
            if not running_flag:
                raise sd.CallbackStop()

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


