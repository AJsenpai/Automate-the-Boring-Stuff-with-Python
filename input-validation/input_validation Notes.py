
"""
####    input validation    ####
"""

####    The PyInputPlus Module    ####

# reference - https://pyinputplus.readthedocs.io/.
# pyinputplus is not a part of python standard library ; you need to install it seprately 
# using pip install --user modulename . PyInputPlus has several functions for different kinds of input:

# The following parameters are available for all of the input*() functions. 
# You can see this documentation by calling help(pyip.parameters):
  import pyinputplus as pyip

  response = pyip.inputInt("enter number")
  print(response)
  print(help(pyip.parameters))
# over your mouse to any Input*() and you'll see the list of parameters in docs

#=================================================
""" Common input*() functions in PyInputPlus  """
#=================================================


'''
### 1. inputStr()
'''
  pyinputplus.inputStr(prompt='', default=None, blank=False, timeout=None, limit=None, strip=None, allowRegexes=None,
                          blockRegexes=None, applyFunc=None, postValidateApplyFunc=None)

# Prompts the user to enter any string input. This is similar to Python’s input() and raw_input() functions, 
# but with PyInputPlus’s additional features such as timeouts, retry limits, stripping, allowlist/blocklist, etc.

# Run help(pyinputplus.parameters) for an explanation of the common parameters
  >>> result = inputStr('Enter name> ')
  Enter name> Al
  >>> result
  'Al'

'''
### 2. inputCustom()
'''
  pyinputplus.inputCustom(customValidationFunc, prompt='', default=None, blank=False, timeout=None, limit=None, strip=None,
                                          allowRegexes=None, blockRegexes=None, applyFunc=None, postValidateApplyFunc=None)

# Validation can be performed by the customValidationFunc argument, which raises an exception if the input is invalid. 
# The exception message is used to tell the user why the input is invalid.                                          

  >>> def raiseIfUppercase(text):
  ...     if text.isupper():
  ...         raise Exception('Input cannot be uppercase.')
  ...
  >>> inputCustom(raiseIfUppercase)
  HELLO
  Input cannot be uppercase.
  Hello
  'Hello'


'''
### 3. inputNum()
'''
  pyinputplus.inputNum(prompt='', default=None, blank=False, timeout=None, limit=None, strip=None, allowRegexes=None,
  blockRegexes=None, applyFunc=None, postValidateApplyFunc=None, min=None, max=None, greaterThan=None, lessThan=None)

# Prompts the user to enter a number, either an integer or a floating - point value.Returns an int or float value
# (depending on if the user entered a decimal in their input.)
  >>> response = pyip.inputNum(min=4)
  3
  Number must be at minimum 4.
  4
  >>> response
  4
  >>> response = pyip.inputNum(greaterThan=4)
  4
  Number must be greater than 4.
  4.1

'''
### 4. inputInt()
'''
  pyinputplus.inputInt(prompt='', default=None, blank=False, timeout=None, limit=None, strip=None, allowRegexes=None,
  blockRegexes=None, applyFunc=None, postValidateApplyFunc=None, min=None, max=None, lessThan=None, greaterThan=None)

# Prompts the user to enter an integer value. Returns the integer as an int value.
  >>> response = pyip.inputInt(min=4)
  3
  Number must be at minimum 4.
  -5
  Number must be at minimum 4.
  5
  >>> response
  5
  >>> response = pyip.inputInt(blockRegexes=[r'[13579]$'])
  43
  This response is invalid.
  41
  This response is invalid.
  42
  >>> response
  42
  >>> response = pyip.inputInt()
  42.0
  >>> response
  42

'''
### 5. inputFloat()
'''
  pyinputplus.inputFloat(prompt='', default=None, blank=False, timeout=None, limit=None, strip=None, allowRegexes=None,
  blockRegexes=None, applyFunc=None, postValidateApplyFunc=None, min=None, max=None, lessThan=None, greaterThan=None)

  >>> import pyinputplus as pyip
  >>> response = pyip.inputFloat()
  42
  >>> response
  42.0

'''
### 6. inputChoice()
'''
  pyinputplus.inputChoice(choices, prompt='_default', default=None, blank=False, timeout=None, limit=None, strip=None,
  allowRegexes=None, blockRegexes=None, applyFunc=None, postValidateApplyFunc=None, caseSensitive=False)

  # choices (Sequence): A sequence of strings, one of which the user must enter.
  # caseSensitive (bool): If True, the user must enter a choice that matches the case of the string in choices. Defaults to False.
  >>> import pyinputplus as pyip
  >>> response = pyip.inputChoice(['dog', 'cat'])
  Please select one of: dog, cat
  dog
  >>> response
  'dog'
  >>> response = pyip.inputChoice(['dog', 'cat'])
  Please select one of: dog, cat
  CAT
  >>> response
  'cat'
  >>> response = pyip.inputChoice(['dog', 'cat'])
  Please select one of: dog, cat
  mouse
  'mouse' is not a valid choice.
  Please select one of: dog, cat
  Dog
  >>> response
  'dog'

'''
### 7. inputMenu()
'''
  pyinputplus.inputMenu(choices, prompt='_default', default=None, blank=False, timeout=None, limit=None, strip=None, allowRegexes=None,
  blockRegexes=None, applyFunc=None, postValidateApplyFunc=None, numbered=False, lettered=False, caseSensitive=False)
  >>> import pyinputplus as pyip
  >>> response = pyip.inputMenu(['dog', 'cat'])
  Please select one of the following:
  * dog
  * cat
  DOG
  >>> response
  'dog'
  >>> response = pyip.inputMenu(['dog', 'cat'], numbered=True)
  Please select one of the following:
  1. dog
  2. cat
  2
  >>> response
  'cat'
  >>> response = pyip.inputMenu(['dog', 'cat'], lettered=True)
  Please select one of the following:
  A. dog
  B. cat
  B
  >>> response
  'cat'

'''
### 8. inputDate()
'''
  pyinputplus.inputDate(prompt='', formats=None, default=None, blank=False, timeout=None, limit=None, strip=None, allowRegexes=None,
  blockRegexes=None, applyFunc=None, postValidateApplyFunc=None)

  >>> import pyinputplus as pyip
  >>> response = pyip.inputDate()
  2019/10/31
  >>> response
  datetime.date(2019, 10, 31)
  >>> response = pyip.inputDate()
  Oct 2019
  'Oct 2019' is not a valid date.
  10/31/2019
  >>> response
  datetime.date(2019, 10, 31)
  >>> response = pyip.inputDate(formats=['%b %Y'])
  Oct 2019
  >>> response
  datetime.date(2019, 10, 1)

'''
### 9. inputDatetime()
'''
  pyinputplus.inputDatetime(prompt='',
  formats=('%m/%d/%Y %H:%M:%S', '%m/%d/%y %H:%M:%S', '%Y/%m/%d %H:%M:%S', '%y/%m/%d %H:%M:%S', '%x %H:%M:%S', '%m/%d/%Y %H:%M',
  '%m/%d/%y %H:%M', '%Y/%m/%d %H:%M', '%y/%m/%d %H:%M', '%x %H:%M', '%m/%d/%Y %H:%M:%S', '%m/%d/%y %H:%M:%S', '%Y/%m/%d %H:%M:%S',
  '%y/%m/%d %H:%M:%S', '%x %H:%M:%S'),
  default=None, blank=False, timeout=None, limit=None, strip=None, allowRegexes=None, blockRegexes=None,
  applyFunc=None, postValidateApplyFunc=None)

  >>> import pyinputplus as pyip
  >>> response = pyip.inputDatetime()
  2019/10/31 12:00:01
  >>> response
  datetime.datetime(2019, 10, 31, 12, 0, 1)
  >>> response = pyip.inputDatetime(formats=['hour %H minute %M'])
  hour 12 minute 1
  >>> response
  datetime.datetime(1900, 1, 1, 12, 1)



'''
### 10. inputtime()
'''
  pyinputplus.inputTime(prompt='', formats=('%H:%M:%S', '%H:%M', '%X'), default=None, blank=False, timeout=None, limit=None,
  strip=None, allowRegexes=None, blockRegexes=None, applyFunc=None, postValidateApplyFunc=None)
  
  >>> import pyinputplus as pyip
  >>> response = pyip.inputTime()
  12:00:01
  >>> response
  datetime.time(12, 0, 1)
  >>> response = pyip.inputTime()
  12:00
  >>> response
  datetime.time(12, 0)
  >>> response = pyip.inputTime(formats=['hour %H minute %M'])
  hour 12 minute 1
  >>> response
  datetime.time(12, 1)

'''
### 11. inputUSState()
'''
  >>> import pyinputplus as pyip
  >>> response = pyip.inputUSState()
  ca
  >>> response
  'CA'
  >>> response = pyip.inputUSState()
  California
  >>> response
  'CA'
  >>> response = pyip.inputUSState(returnStateName=True)
  ca
  >>> response
  'California'`

'''
### 12. inputMonth()
'''
  >>> import pyinputplus as pyip
  >>> response = pyip.inputMonth()
  3
  >>> response
  'March'
  >>> response = pyip.inputMonth()
  Mar
  >>> response
  'March'
  >>> response = pyip.inputMonth()
  MARCH
  >>> response
  'March'

'''
### 13. inputDayOfWeek()
'''
  >>> import pyinputplus as pyip
  >>> response = pyip.inputDayOfWeek()
  mon
  >>> response
  'Monday'
  >>> response = pyip.inputDayOfWeek()
  FRIDAY
  >>> response
  'Friday'

'''
### 14. inputDayOfMonth()
'''
  >>> import pyinputplus as pyip
  >>> response = pyip.inputDayOfMonth(2019, 10)
  31
  >>> response
  31
  >>> response = pyip.inputDayOfMonth(2000, 2)
  29
  >>> response
  29
  >>> response = pyip.inputDayOfMonth(2001, 2)
  29
  '29' is not a day in the month of February 2001
  1
  >>> response
  1

'''
### 15. pyinputplus.inputIp()
'''
  pyinputplus.inputIp(prompt='', default=None, blank=False, timeout=None, limit=None, strip=None, allowRegexes=None,
  blockRegexes=None, applyFunc=None, postValidateApplyFunc=None)

'''
### 16. inputURL()
'''
  pyinputplus.inputURL(prompt='', default=None, blank=False, timeout=None, limit=None, strip=None, allowRegexes=None,
  blockRegexes=None, applyFunc=None, postValidateApplyFunc=None)

'''
### 17. inputYesNo()
'''
  pyinputplus.inputYesNo(prompt='', yesVal='yes', noVal='no', caseSensitive=False, default=None, blank=False, timeout=None,
  limit=None, strip=None, allowRegexes=None, blockRegexes=None, applyFunc=None, postValidateApplyFunc=None)
  >>> import pyinputplus as pyip
  >>> response = pyip.inputYesNo()
  yes
  >>> response
  'yes'
  >>> response = pyip.inputYesNo()
  NO
  >>> response
  'no'
  >>> response = pyip.inputYesNo()
  Y
  >>> response
  'yes'
  >>> response = pyip.inputYesNo(yesVal='oui', noVal='no')
  oui
  >>> response
  'oui'

'''
### 18. inputPassowrd()
'''
  pyinputplus.inputPassword(prompt='', mask='*', default=None, blank=False, timeout=None, limit=None, strip='', allowRegexes=None,
  blockRegexes=None, applyFunc=None, postValidateApplyFunc=None)
# Prompts the user to enter a password.Mask characters will be displayed instead of the actual characters.
# If correctPassword is None, then any input is accepted and returned by inputPassword().
# The default for strip is '' so that no whitespace striping occurs.

# By default, limit is set to 1, so an incorrect password attempt results in raising RetryLimitException.
# If limit is set to None, then user is asked again for a correct password forever.
# The wrongPasswordMsg string is displayed whenever the user enters an incorrect password.




#====================================================================
""" Common parameters for all input*() functions in PyInputPlus """
#====================================================================

'''
1.  prompt (str): The text to display before each prompt for user input. 
    Identical to the prompt argument for Python’s raw_input() and input() functions.

2.  default (str, None): A default value to use if the user time out or exceed the number of tries to enter valid input.

3.  blank (bool): If True, a blank string will be accepted. Defaults to False.

4.  timeout (int, float): The number of seconds since the first prompt for input after which a T
    imeoutException is raised the next time the user enters input.

5.  limit (int): The number of tries the user has to enter valid input before the default value is returned.

6.  strip (bool, str, None): If None, whitespace is stripped from value. If a str, the characters in it are stripped from value. 
    If False, nothing is stripped.

7.  allowlistRegexes (Sequence, None): A sequence of regex str that will explicitly pass validation.

8.  blocklistRegexes (Sequence, None): A sequence of regex str or (regex_str, error_msg_str) tuples that, 
    if matched, will explicitly fail validation.

9.  applyFunc (Callable, None): An optional function that is passed the user’s input, and returns the new value to use as the input.

10. postValidateApplyFunc (Callable, None): An optional function that is passed the user’s input after 
    it has passed validation, and returns a transformed version for the input*() function to return.

'''

'''
there are few more but not very common, check on docs online
'''
