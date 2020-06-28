"""
Multiplication Quiz using pyinputplus module for input validation
"""

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f"#{questionNumber}: {num1} X {num2} "
    try:

        # Right answers are handled by allowed regex
        # wrong answers are handled by block reges, with custom message
        pyip.inputStr(
            prompt,
            allowRegexes=["^%s$" % (num1 * num2)],
            blockRegexes=[(".*", "Incorrect!")],
            timeout=8,
            limit=3,
        )

    except pyip.TimeoutException:
        print("Time Out!!")

    except pyip.RetryLimitException:
        print("Out of Tries!!")

    else:
        print("Correct!")
        correctAnswers += 1
    time.sleep(1)
print(f"Score: {correctAnswers}/ {numberOfQuestions}")
