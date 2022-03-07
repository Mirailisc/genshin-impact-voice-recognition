import speech_recognition as sr
import pyautogui

r = sr.Recognizer()


with sr.Microphone() as source:
    while True:
        print('Speak Anything: ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('You said : {}'.format(text))

            if text.lower() == "1":
                print('1 recognized')
                pyautogui.press('1')

            elif text.lower() == "2":
                print('2 recognized')
                pyautogui.press('1')

            elif text.lower() == "3":
                print('3 recognized')
                pyautogui.press('3')

            elif text.lower() == "4":
                print('4 recognized')
                pyautogui.press('4')

            elif text.lower() == "never gonna give you up":
                print('never gonna give you up recognized')
                pyautogui.press('e')

            elif text.lower() == "never gonna let you down":
                print('never gonna let you down recognized')
                pyautogui.press('q')
            
            elif text.lower() == "joe biden":
                print('attack recognized')
                pyautogui.click(clicks=1, button='left')

            elif text.lower() == "exit":
                break

        except:
            print('Sorry could not recognize your voice')
