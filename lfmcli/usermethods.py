from lastfmget import *
from config.userinfo import USER
from prettytable import PrettyTable

def getTopAlbums(user=USER, period="7day", limit=10):
    return

def getTopArtists(user=USER, period="7day", limit=10):

    response = lastfmGet({
        "user": user,
        "method": "user.gettopartists",
        "period": period,
        "limit": limit
    })

    table = PrettyTable()
    table.field_names = ["Artist", "Playcount"]

    for artist in response.json()["topartists"]["artist"]:
        table.add_row([artist["name"], artist["playcount"]])
    
    print(user + "'s " + "top " + str(limit) + " artists for the past " + period + " period")
    print("\n")
    print(table)


def getTopTracks():
    return
