def generer_rapport(format: str, donnees: dict) -> str:
    if format == "txt":
        return f"Rapport\n-------\n" + "\n".join(f"{k}: {v}" for k, v in donnees.items())
    elif format == "html":
        lignes = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in donnees.items())
        return f"<table>{lignes}</table>"
    elif format == "csv":
        return "\n".join(f"{k},{v}" for k, v in donnees.items())
    else:
        raise ValueError(f"Format inconnu : {format}")





donnees_txt = {"nom": "Alice", "age": 30}
rapport_txt = generer_rapport("txt", donnees_txt)
print(rapport_txt)

donnees_html = {"nom": "Alice", "age": 30}
rapport_html = generer_rapport("html", donnees_html)
print(rapport_html)

donnees_csv = {"nom": "Alice", "age": 30}
rapport_csv = generer_rapport("csv", donnees_csv)
print(rapport_csv)