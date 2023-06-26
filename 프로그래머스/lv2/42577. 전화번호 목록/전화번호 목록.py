def solution(phone_book):
    answer = True
    phone_book = set(phone_book)
    for phone in phone_book:
        for i in range(len(phone)):
            if(phone[:i] in phone_book):
                answer = False
    return answer