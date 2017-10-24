words=['Cat','Window','Defenestrate']
for w in words:
    if len(w)>6:
        words.insert(0, w)
for w in words[:]: # Loop over a slice copy of the entire list.
... if len(w) > 6:
... words.insert(0, w)
