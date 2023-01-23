def describe(row):
    name, mass, recclass, date = row['name'], row['mass'], row['recclass'], row['year']
    if recclass == "Stone-uncl":
        recclass += " (stone meteorite that has not yet been classified)"
    return f'Name: {name}<br>Mass: {mass} kg<br>Recommended classification: {recclass}<br>Year of fall: {date}'
