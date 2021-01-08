##Filtering Buttons in Graph##

from pyvis.network import Network
from pyvis.options import Options
import json

file = "./json_files/combined_data.json"



def get_data():
    with open (file, "r") as json_file:
        data = json.load(json_file)
        return(data)

def map_algs(g, alg="barnes"):
    if alg=="barnes":
        g.barnes_hut()
    if alg=="forced":
        g.force_atlas_2based()
    if alg=="hr":
        g.hrepulsion()

def map_data(letter_data, ep_color="#03DAC6", ms_color="#da03b3", edge_color="#018786", ep_shape="triangle", ms_shape="box", alg="barnes", buttons=False, recipient_color="#FFA300", recipient_shape="ellipse", cited_color="#DFEE9A", cited_shape="square"):
    g = Network(height="1500px", width="100%", bgcolor="#222222", font_color="white", directed=True)
    if buttons==True:
        g.width = "75%"
        # g.show_buttons(filter_=["interaction"])
        g.set_options('''
        var options = {
  "interaction": {
    "tooltipDelay": 450
  }
}
        ''')
        # "nodes", "layout", "interaction", "manipulation", "selection", "renderer", "physics"
    for letter in letter_data[0:10]:
        ep = (letter["ep_num"])[0]
        mss = (letter["mss"])
        recipients = (letter["recipients"])
        people_cited = (letter["people_cited"])
        g.add_node(ep, color=ep_color, shape=ep_shape)
        for ms in mss:
            g.add_node(ms, color=ms_color, shape=ms_shape)
            g.add_edge(ep, ms, color=edge_color)



    # map_algs(g, alg=alg)
    g.show("letters2.html")


epp_data = get_data()
map_data(letter_data=epp_data, ms_shape="triangle", ep_shape="box", alg="barnes", buttons=True)
