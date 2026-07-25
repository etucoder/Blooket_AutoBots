import pyautogui
from time import sleep
from blooket_question_bot import answer_questions
ball_image = "ball.png"
question_screen_image = "question_screen.png"
pyautogui.PAUSE = 0
while True:
    try:
        location = pyautogui.locateOnScreen(ball_image,confidence=0.8)
        if location is not None:
            centerx , centery = pyautogui.center(location)
            pyautogui.moveTo(centerx,centery)
        else:
            print("Image not on screen")

    except:
        try:
            location = pyautogui.locateOnScreen(question_screen_image,confidence=0.8)
            answer_questions(3)
        except:
            print("Error")
