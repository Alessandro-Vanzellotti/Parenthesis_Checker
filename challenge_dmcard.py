OPEN_PARENTHESIS = "("
CLOSE_PARENTHESIS = ")"


def parenthesis_checker(word):
    open_count = 0

    for c in word:
        if (c == OPEN_PARENTHESIS):
            open_count += 1

        elif (c == CLOSE_PARENTHESIS) and (open_count > 0):
            open_count -= 1
        
        elif (c == CLOSE_PARENTHESIS) and (open_count == 0):
            return "incorrect"

    if (open_count == 0):
        return "correct"
    
    return "incorrect"