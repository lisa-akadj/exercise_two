def check_grammar(text):
    chars_list = list(text)
    cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punc_marks = ['.', '?', '!']
    if chars_list[0] in cap_letters and chars_list[-1] in punc_marks:
        return True
    # elif chars_list[0] in cap_letters and chars_list[-1, -4] == ['.', '.', '.']:
    #     return True
    # elif chars_list[0] in cap_letters and chars_list[-1, -3] == ['?', '!']:
        return True
    else:
        return False
