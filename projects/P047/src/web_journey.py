from urllib.parse import urlparse

def journey(url: str):
    u = urlparse(url)
    if u.scheme not in {"http","https"} or not u.hostname:
        raise ValueError("URL non valido")
    try:
        port = u.port
    except ValueError as exc:
        raise ValueError("porta non valida") from exc
    if u.username is not None or u.password is not None or port == 0:
        raise ValueError("credenziali o porta non ammesse")
    target = (u.path or "/") + ("?" + u.query if u.query else "")
    steps = [
        ("URL", f"analisi di {u.scheme}://{u.hostname}"),
        ("DNS", f"risoluzione del nome {u.hostname}"),
        ("IP", "scelta dell'indirizzo destinazione"),
        ("TCP", "apertura della connessione affidabile"),
    ]
    if u.scheme == "https":
        steps.append(("TLS", "negoziazione cifratura e verifica certificato"))
    steps += [
        ("HTTP", f"richiesta della risorsa {target}"),
        ("RESPONSE", "status, header e body"),
        ("CACHE", "eventuale riuso secondo le direttive HTTP"),
    ]
    return steps
