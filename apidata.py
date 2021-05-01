import requests
import os
import json

def get_user_data(username):
    res = requests.get(f"https://api.jikan.moe/v3/user/{username}/profile").json()
    string = json.dumps(res)
    profilestats = json.loads(string)
    return profilestats

def required_stats(username):
    result = ""
    stats = get_user_data(username)
    name = stats['username']
    anime_stats = stats['anime_stats']
    days = anime_stats['days_watched']
    total_entries = anime_stats['total_entries']
    mean_score = anime_stats['mean_score']
    
    result += f"""
    Username👤 :: {name}
    Total Anime Known📖 :: {total_entries}
    Days Wasted📖 :: {days}

    About You ::
    """

    if mean_score>8 :
        result += """Sometimes Either you dont't put brain while rating Or You watch only good anime """
    elif mean_score<5 : 
        result += """Sometimes You are a true critic among weebs """
    else :
        result += """Sometimes You are a adult who enjoys and sees anime the right way """
    
    if days < 20 or total_entries < 20 : 
        result += """A kid weeb or a weak weeb is what we call you. Also u like cosplays """
    elif days>50 or total_entries > 50 :
        result += """You sir are weeb and have acquired basics of japanese """
    elif days>100 or total_entries > 100 :
        result += """You are a god weeb, a rare sight in our degenrate-generation """
    else : 
        result += """ You are a average man """
    return result


if __name__ == "__main__":
    inp = input("name please")
    string = required_stats(inp)
    print(string)
