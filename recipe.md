# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_grammar(text):
    """Checks that the text begins with a capital letter and that it ends with "." or "?" or "!" or "..." or "?!"

    Parameters: (list all parameters and their types)
        text: a string of text with sentence finishing punctuation mark
        (e.g. "Good morning!")

    Returns: (state the return value and its type)
        True
        False - if either is missing

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a sentence 
It returns True if the sentence starts with a capital letter and ends with full stop. 
"""
check_grammar("Good morning.") => True

"""
Given a sentence 
It returns True if it starts with a capital letter and ends with an exclamation mark. 
"""
check_grammar("Good morning!") => True

"""
Given a sentence
It returns True if the sentence starts with a capital letter and ends with a question mark. 
"""
check_grammar("How are you?") => True

"""
Given a sentence 
It returns True if the sentence starts with a capital letter and ends with an elipses.
"""
check_grammar("I don't know...") => True

"""
Given a sentence 
It returns True if the sentence starts with a capital letter and ends with an 'interrobang'(?!)
"""
check_grammar("Are you serious?!") => True 

"""
Given a sentence 
It returns False if the sentence starts with a capital letter and has no ending punctuation mark
"""
check_grammar("How are you") => False

"""
Given a sentence
It returns False if the sentence starts with a lower case letter and finishes with a punctuation mark
"""
check_grammar("how are you?") => False

"""
Given a sentence
It returns False if the sentence starts with a lower case letter and does not have an ending punctuation mark.
"""
check_grammar("i am fine") => False
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
