from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "https://politicalvigilante.libsyn.com/rss"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/f/f/8/4/ff840dcce3559a06/The_Political_Vigilante_Podcast.png"},
   {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('latest_episodes'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/f/f/8/4/ff840dcce3559a06/The_Political_Vigilante_Podcast.png"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/latest_episodes/')
def latest_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

if __name__ == '__main__':
    plugin.run()
