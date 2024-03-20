def solution(record):
    
    nickname = dict()
    answer = []
    
    for line in record:
        commands = line.split()
        command = commands[0]
        if(command == "Enter" or command == "Change"):
            uid, nick = commands[1:]
            nickname[uid] = nick
    
    for line in record:
        commands = line.split()
        command = commands[0]
        if(command == "Enter"):
            uid = commands[1]
            answer.append(nickname[uid] +"님이 들어왔습니다.")
        elif(command == "Leave"):
            uid = commands[1]
            answer.append(nickname[uid] +"님이 나갔습니다.")
    
    
    return answer