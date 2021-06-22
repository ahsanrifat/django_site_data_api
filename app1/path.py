import pandas as pd
import random

data = None
edges_list = []
edges_count = 0
nodes_list = []
nodes_count = 0
nodes_track = {}
visited_dict = {}


def get_child_list(site_name):
    global data
    df = data[data.SiteA == site_name]
    return_dict = {}
    move_forward_flag = True
    for index, row in df.iterrows():
        return_dict[row.SiteB] = "{} -> {}".format(row.LinkA, row.LinkB)
        if "UPE" in row.SiteB:
            print(row.SiteB)
            move_forward_flag = False
    return (return_dict, move_forward_flag)


def DFS(start_site):
    global edges_list, edges_count, nodes_list, nodes_count, visited_dict
    if start_site in visited_dict:
        return
    else:
        visited_dict[start_site] = True
    if nodes_count == 0:
        nodes_count = nodes_count + 1
        nodes_list.append(
            {"nodes_count": nodes_count, "id": start_site, "label": start_site}
        )
        nodes_track[start_site] = True
    child_list, move_forward_flag = get_child_list(start_site)
    print(move_forward_flag)
    for child in child_list:
        if child != None or child != "":
            if child not in nodes_track:
                nodes_count = nodes_count + 1
                nodes_list.append(
                    {"nodes_count": nodes_count, "id": child, "label": child}
                )
                nodes_track[child] = True
            edges_count = edges_count + 1
            edges_list.append(
                {
                    "edge_count": edges_count,
                    "width": random.randint(1, 4),
                    "source": start_site,
                    "target": child,
                    "label": child_list[child],
                }
            )
            if move_forward_flag:
                DFS(child)
    return None


def make_tree(start_site):
    global edges_list, nodes_list, nodes_count, data
    data = pd.read_json(r"C:\Users\syedr\Documents\django_api\api\app1\path.json")
    DFS(start_site)
    return_data = {"nodes": nodes_list, "edges": edges_list}
    return return_data


# make_tree("WR-3203-TN1")
