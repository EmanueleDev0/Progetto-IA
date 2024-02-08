import heapq #libreria per implementare la coda con priorità

def uniform_cost_search(mappa, start_city, goal_city):

   frontiera = []
   heapq.heappush(frontiera, (0, [start_city], [0]))  # città iniziale con costo 0
   explored_city = set()  # Set per tenere traccia delle città esplorate

   while frontiera:
       costo, percorso, costo_attuale = heapq.heappop(frontiera) #viene estratta la tupla col costo minore
       current_city = percorso[-1]

       if current_city == goal_city:
           return costo, list(zip(percorso, costo_attuale))  # Restituisci costo e percorso con costi intermedi

       if current_city not in explored_city:
           explored_city.add(current_city)

           for vicino, distanza in mappa[current_city]:
               if vicino not in explored_city:
                   costo_vicino = costo + distanza
                   nuovo_percorso = percorso.copy()  # Creo una copia del percorso per evitare modifiche indesiderate
                   nuovo_percorso.append(vicino)
                   costo_attuale_temporaneo = costo_attuale.copy()
                   costo_attuale_temporaneo.append(costo_vicino)
                   heapq.heappush(frontiera, (costo_vicino, nuovo_percorso, costo_attuale_temporaneo))

   return None, None  # Se si arriva qui, il percorso non è stato trovato