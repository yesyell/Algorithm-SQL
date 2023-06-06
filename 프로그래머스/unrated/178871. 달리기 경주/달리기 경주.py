def solution(players, callings):
    player_dict = {player: n for n, player in enumerate(players)}
    for calling in callings:
        i = player_dict[calling]
        players[i-1], players[i] = players[i], players[i-1]
        player_dict[players[i-1]], player_dict[players[i]] = i-1, i
    return players