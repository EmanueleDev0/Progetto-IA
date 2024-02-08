from Ricerca_Uniforme import uniform_cost_search
from Visualizzazione_Percorso import visualizza_percorso
from Grafo_Romania import romania_map

# Esempio di utilizzo:
start_city = "Arad"
goal_city = "Bucarest"
result_cost, result_path = uniform_cost_search(romania_map, start_city, goal_city)

if result_cost is not None and result_path is not None:
    print(f"Il percorso piu' breve da {start_city} a {goal_city} e':")
    for city, cost in result_path:
        print(f"Citta': {city}, Costo: {cost}")
    print(f"La distanza totale e': {result_cost}")

    # Visualizza il percorso sulla mappa
    visualizza_percorso(romania_map, result_path)
else:
    print(f"Percorso non trovato da {start_city} a {goal_city}")
