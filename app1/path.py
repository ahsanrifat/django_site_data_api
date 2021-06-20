import pandas as pd

data = None
edges_list = []
edges_count = 0
nodes_list = []
nodes_count = 0
visited_dict = {}


def get_child_list(site_name):
    global data
    df = data[data.SiteA == site_name]
    return pd.Series(df.LinkB.values, index=df.SiteB).to_dict()


def DFS(start_site):
    child_list = get_child_list(start_site)
    global edges_list, edges_count, nodes_list, nodes_count, visited_dict
    if start_site in visited_dict:
        return
    else:
        visited_dict[start_site] = True
    nodes_count = nodes_count + 1
    nodes_list.append({"id": start_site, "label": start_site})

    for child in child_list:
        # print(child_list[child])
        if child != None or child != "":
            edges_list.append(
                {
                    "source": start_site,
                    "target": child,
                    "label": child_list[child],
                }
            )
            DFS(child)
    return None


def make_tree(start_site):
    global edges_list, nodes_list, nodes_count, data
    data = pd.read_json(r"C:\Users\syedr\Documents\django_api\api\app1\path.json")
    DFS(start_site)
    return_data = {"nodes": nodes_list, "edges": edges_list}
    return return_data


# make_tree("WR-3203-TN1")
