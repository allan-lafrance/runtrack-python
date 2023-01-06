def arrondir_notes(notes):
  notes_arrondies = []
  
  for note in notes:
    if note < 40:
      notes_arrondies.append(note)
    else:
      if note % 5 < 3:
        note_arrondie = (note // 5) * 5 + 5
      else:
        note_arrondie = note
      notes_arrondies.append(note_arrondie)
      
  return notes_arrondies

# On teste la fonction avec quelques exemples
print(arrondir_notes([82, 83, 95, 36, 73, 37, 42]))