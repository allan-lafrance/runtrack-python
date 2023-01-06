def distance_parcourue(marches, hauteur_marche):
  distance_par_jour = (marches * hauteur_marche * 2 * 5) / 100
  distance_par_semaine = distance_par_jour * 7
  
  print(f'Pour {marches} marches de {hauteur_marche} cm, le gardien parcours {distance_par_semaine:.2f} m par semaine.')

distance_parcourue(345, 10)