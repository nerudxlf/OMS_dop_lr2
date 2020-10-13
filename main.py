import cairocffi
import igraph as ig
import time


def community_walktrap_plot(g: object):
    start_time = time.monotonic()
    wtrap = g.community_walktrap(steps=8)
    print(f'Прошло {time.monotonic() - start_time}')
    clust = wtrap.as_clustering()
    max_size = max(clust.sizes())
    len_clust = len(clust.sizes())
    modularity = clust.recalculate_modularity()
    ig.plot(clust, mark_groups = True)


def community_label_propagation_plot(g: object):
    start_time = time.monotonic()
    label_prop = g.community_label_propagation()
    print(f'Прошло {time.monotonic() - start_time}')
    max_size = max(label_prop.sizes())
    len_clust = len(label_prop.sizes())
    modularity = label_prop.recalculate_modularity()
    ig.plot(label_prop, mark_groups = True)


def community_spinglass_plot(g: object):
    #!!!long counts
    spinglass = g.community_spinglass()
    print(type(spinglass))



def community_edge_betweenness_plot(g: object):
    #!!!long counts
    edge_bet = g.community_edge_betweenness()
    print(type(edge_bet))


def community_fastgreedy_plot(g: object):
    start_time = time.monotonic()
    fastgreedy = g.community_fastgreedy()
    print(f'Прошло {time.monotonic() - start_time}')
    clust = fastgreedy.as_clustering()
    max_size = max(clust.sizes())
    len_clust = len(clust.sizes())
    modularity = clust.recalculate_modularity()
    ig.plot(clust, mark_groups = True)


def community_leading_eigenvector_plot(g: object):
    start_time = time.monotonic()
    leading_eigenvector = g.community_leading_eigenvector()
    print(f'Прошло {time.monotonic() - start_time}')
    max_size = max(leading_eigenvector.sizes())
    len_clust = len(leading_eigenvector.sizes())
    modularity = leading_eigenvector.recalculate_modularity()
    ig.plot(leading_eigenvector, mark_groups = True)



def main():
    g = ig.Graph.Read_Ncol("facebook_combined.txt",  directed=True).as_undirected()
    community_walktrap_plot(g)
    community_label_propagation_plot(g)
    community_edge_betweenness_plot(g)
    community_spinglass_plot(g)
    community_fastgreedy_plot(g)
    #ommunity_leading_eigenvector_plot(g)

    
if __name__ == '__main__':
    main()