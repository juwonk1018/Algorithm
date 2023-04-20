def solution(players, callings):
    pos = dict()
    for i in range(len(players)):
        pos[players[i]] = i
        
    for call in callings:
        idx = pos[call]; prevPlayer = players[idx-1]
        pos[call], pos[prevPlayer] = pos[prevPlayer], pos[call]
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players