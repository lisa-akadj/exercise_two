from lib.check_grammar import check_grammar

def test_true_for_capital_letter_and_full_stop():
    result = check_grammar("Good morning.")
    assert result == True 

def test_true_for_capital_letter_and_exclm_mark():
    result = check_grammar("Good morning!")
    assert result == True

def test_true_for_capital_letter_and_question_mark():
    result = check_grammar("How are you?")
    assert result == True

# def test_true_for_capital_letter_and_elipses():
#     result = check_grammar("I don't know...")
#     assert result == True

# def test_true_for_capital_letter_and_interrobang():
#     result = check_grammar("Are you serious?!")
#     assert result == True

def test_false_for_capital_letter_no_punc_mark():
    result = check_grammar("How are you")
    assert result == False

def test_false_for_lower_letter_punc_mark():
    result = check_grammar("how are you?")
    assert result == False

def test_false_for_lower_letter_no_punc_mark():
    result = check_grammar("i am fine")
    assert result == False