from IPython.display import HTML
from urllib.request import urlopen
import matplotlib.pyplot as plt


def menon_headings():
    html = urlopen("https://raw.githubusercontent.com/kristomi/offentlige_ting/master/Menon-farger/menon_headings.css")
    HTML(html.read().decode('utf-8'))


def menon_logo():
    html = urlopen("https://raw.githubusercontent.com/kristomi/offentlige_ting/master/Menon-farger/menon_logo.css")
    HTML(html.read().decode('utf-8'))


def menon_matplotlib():
    from cycler import cycler
    color_url = "https://raw.githubusercontent.com/kristomi/offentlige_ting/master/Menon-farger/menon_farger.json"
    menon_farger = json.loads(requests.get(color_url).text, object_pairs_hook=collections.OrderedDict)
    plt.style.use('bmh')
    plt.rcParams['axes.prop_cycle'] = cycler(color=[color for _, color in menon_farger.items()])


if __name__ == '__main__':
    menon_headings()
    menon_logo()
    menon_matplotlib()
