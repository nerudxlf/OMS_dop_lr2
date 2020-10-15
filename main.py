import cairocffi
import igraph as ig
import time


def community_walktrap_plot(g: object) -> dict:
    start_time = time.monotonic()
    wtrap = g.community_walktrap(steps=8)
    stop_time = time.monotonic() - start_time
    clust = wtrap.as_clustering()
    max_size = max(clust.sizes())
    len_clust = len(clust.sizes())
    modularity = clust.recalculate_modularity()
    ig.plot(wtrap) # draw dendogram
    ig.plot(clust, mark_groups=True) # draw graph
    return {
        "размер максимального сообщества": max_size,
        "число сообществ": len_clust,
        "модулярность": modularity,
        "время работы": stop_time
    }


def community_label_propagation_plot(g: object) -> dict:
    start_time = time.monotonic()
    label_prop = g.community_label_propagation()
    stop_time = time.monotonic() - start_time
    max_size = max(label_prop.sizes())
    len_clust = len(label_prop.sizes())
    modularity = label_prop.recalculate_modularity()
    ig.plot(label_prop, mark_groups=True) # draw graph
    return {
        "размер максимального сообщества": max_size,
        "число сообществ": len_clust,
        "модулярность": modularity,
        "время работы": stop_time
    }


def community_spinglass_plot(g: object) -> dict:
    start_time = time.monotonic()
    spinglass = g.community_spinglass()
    stop_time = time.monotonic() - start_time
    max_size = max(spinglass.size())
    len_clust = len(spinglas.size())
    modularity = spinglass.recalculate_modularity()
    ig.plot(spinglass, mark_groups=True)
    return {
        "размер максимального сообщества": max_size,
        "число сообществ": len_clust,
        "модулярность": modularity,
        "время работы": stop_time
    }


def community_edge_betweenness_plot(g: object):
    #!!!long counts
    edge_bet = g.community_edge_betweenness()
    print(type(edge_bet))


def community_fastgreedy_plot(g: object) -> dict:
    start_time = time.monotonic()
    fastgreedy = g.community_fastgreedy()
    stop_time = time.monotonic() - start_time
    clust = fastgreedy.as_clustering()
    max_size = max(clust.sizes())
    len_clust = len(clust.sizes())
    modularity = clust.recalculate_modularity()
    ig.plot(fastgreedy) # draw dendogram
    ig.plot(clust, mark_groups=True) # draw graph
    return {
        "размер максимального сообщества": max_size,
        "число сообществ": len_clust,
        "модулярность": modularity,
        "время работы": stop_time
    }


def community_leading_eigenvector_plot(g: object) -> dict:
    start_time = time.monotonic()
    leading_eigenvector = g.community_leading_eigenvector()
    stop_time = time.monotonic() - start_time
    max_size = max(leading_eigenvector.sizes())
    len_clust = len(leading_eigenvector.sizes())
    modularity = leading_eigenvector.recalculate_modularity()
    ig.plot(leading_eigenvector, mark_groups=True)
    return {
        "размер максимального сообщества": max_size,
        "число сообществ": len_clust,
        "модулярность": modularity,
        "время работы": stop_time
    }


def main():
    g = ig.Graph.Read_Ncol("facebook_combined.txt",
                           directed=True).as_undirected()
    # print("walktrap:\n")
    # print(community_walktrap_plot(g))
    # print("label propagation:\n") 
    # print(community_label_propagation_plot(g))
    # print("edge betweeness:\n")
    # print(community_edge_betweenness_plot(g))
    # print("spinglass_plot:\n") 
    # print(community_spinglass_plot(g))
    # print("fastgreedy:\n")
    # print(community_fastgreedy_plot(g))
    # print("leading eigenvector:\n")
    # print(community_leading_eigenvector_plot(g))


if __name__ == '__main__':
    main()
