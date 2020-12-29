def solution(phone_book):
    phone_book.sort()
    pv = phone_book.pop(0)
    for i in phone_book:
        if i.startswith(pv):
            return False
    return True