from riotwatcher import LolWatcher

key = 'RGAPI-d2347ac6-9736-49f7-b191-1b081f1ba264'
watcher = LolWatcher(key)


def printStats(summonerName):
    summoner = watcher.summoner.by_name('na1',summonerName)
    stats = watcher.league.by_summoner('na1', summoner['id'])
    num = 0
    if (stats[0]['queueType'] == 'RANKED_SOLO_5x5'):
        num = 0
    else:
        num = 1

    tier = stats[num]['tier']
    rank = stats[num]['rank']
    lp = stats[num]['leaguePoints']

    wins= int(stats[num]['wins'])
    losses = int(stats[num]['losses'])
    wr = int((wins/(wins+losses))* 100)
    print(stats)
    print(summonerName +" is currently ranked in " + str(tier), str(rank) +" with " + str(lp) + "LP and a " + str(wr) + "% winrate.")

