# visualizzazione_percorso.py
import matplotlib.pyplot as plt
import networkx as nx

def visualizza_percorso(mappa, percorso):
    # Creazione del grafo diretto pesato
    G = nx.DiGraph()
    for città, archi in mappa.items():
        G.add_node(città)
        for arco, peso in archi:
            G.add_edge(città, arco, weight=peso)

    # Estrazione delle città dal percorso
    città_del_percorso = [città for città, _ in percorso]

    # Creazione del sottografo del percorso
    percorso_edges = [(città_del_percorso[i], città_del_percorso[i + 1]) for i in range(len(città_del_percorso) - 1)]
    percorso_graph = G.edge_subgraph(percorso_edges)

    # Posizionamento delle città nel grafo
    pos = nx.spring_layout(G)

    # Disegno del grafo completo
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=500, node_color='skyblue')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Disegno del percorso
    nx.draw(percorso_graph, pos, edge_color='red', width=2, arrowsize=30, connectionstyle='arc3,rad=0.2', arrowstyle='->,head_width=0.2,head_length=0.3')

    # Mostra il grafico
    plt.show()
