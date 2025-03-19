# uselessString Package

## Basic intro
This package aims to provide programmers some variants and interesting capabilities of string, including palindrome (characters reversal), words reversal, customized repetitiveness, emotion expression, etc...

Project available on PyPI through: 
[PyPI]


## Badge
![Build Status](https://github.com/software-students-spring2025/3-python-package-goodgood/actions/workflows/build.yaml/badge.svg)

## Documentation

1. To import the project, you need to install the package from pip through terminal or PyPI. 
```bash
pip install uselessString
```

And you may upgrade the package. 
```bash
pip install --upgrade uselessString
```

2. Package function. 
(1) .palindrome(s)
Convert a string to its palindrome
```python
def palindrome(text: str) -> str:
    """
    :param s: A random string
    :raises TypeError: If the input is not a string.
    """

result = uselessString.palindrome("Hello World") # return "dlrow olleH”
print(result)
```

(2).reverse(s)
Reverse all the words in a string. 
```python
def reverse(text: str) -> str: 
    """
    :param text: A random string
    :raises TypeError: If the input is not a string.
    """
result = uselessString.reverse("Hello World") # return "World Hello" 
print(result)
```

(3).echo(s, i)
Repeat the word s i times. 
```python
def echo(s: str, i: int) -> str:
    """
    :param s: A random string
    :param i: A random int
    :raises TypeError: If s is not a string or i is not an int. 
    """
result = uselessString.echo("Hello World", 3) # return "Hello World Hello World Hello World"
print(result)

```

(4).angry(s)
This function randomly adds some special characters, such as @, %, !, *, etc... , to express angryness and bad words. These special characters will be added between each word. 
```python
def angry(s: str) -> str: 
    """
    :param s: A random string
    :raises TypeError: If s is not a string. 
    """
result = uselessString.angry("Hello World")# return "Hello @!%%* World @&**!%@@%@" 
print(result)
```

(5).mocking(s)
This function turns a string into "camel strcture", which means characters in the word s will be repetitively upper case and lower case. 
```python
def mocking(s: str) -> str: 
    """
    :param s: A random string
    :raises TypeError: If s is not a string
    """
result = uselessString.mocking("Hello World") # return "HeLlO wOrLd" 
print(result)

```

(6).emoji(s, emotion)
This function will add emoji corresponding to input emotion at the end of the string. 
```python
def emoji(s: str, emotion: str) -> str:
    """
    :param s: A random string
    :param emotion: A random emotion (if emotion not in our built-in list, we will return a default emoji)
    :raises TypeError: if s or emotion is not a string. 
    """
result = uselessString.emoji("Hello World", "happy") # return "Hello World 😄"
print(result)
```

(7).random(s)
This function shuffles the order of characters in the string s. 

```python
def random(s: str) -> str: 
    """
    :param s: A random string
    :raises TypeError: if s is not a string. 
    """
result = uselessString.random("Hello World") # return "eolW rlHodl" 
print(result)
```

## Project contribution
We really appreciate any form of technical contribution and capability extension. Here, we provide a standard setup workflow. 

## Contributers
Tim Yan: [Github](https://github.com/T1mmmmm)

Bill Feng: [Github](https://github.com/BillBBle)

Warren Wu: [Github](https://github.com/W0rren12)

Marcos Huh: [Github](https://github.com/mh6355)

## Package setup

