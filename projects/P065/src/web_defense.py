"""Controlli locali: testo HTML, token CSRF di sessione, risposta con CSP.

Non avvia un server né collauda le policy in un browser.
"""
from dataclasses import dataclass
import html
import hmac
import math
import re
import secrets


def safe_html(text):
    """Solo contenuto testuale HTML; non rende sicuri URL, CSS o JavaScript."""
    if not isinstance(text, str):
        raise TypeError("testo richiesto")
    return html.escape(text, quote=True)


def new_csrf_token():
    return secrets.token_urlsafe(32)


def verify_csrf(expected, supplied):
    for value in (expected, supplied):
        if not isinstance(value, str) or re.fullmatch(r"[A-Za-z0-9_-]{43}", value) is None:
            return False
    return hmac.compare_digest(expected, supplied)


def content_security_policy():
    return "default-src 'none'; script-src 'none'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'"


def _time(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("tempo finito >= 0 richiesto")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError("tempo troppo grande") from exc
    if not math.isfinite(result) or result < 0:
        raise ValueError("tempo finito >= 0 richiesto")
    return result


@dataclass(frozen=True)
class Response:
    status: int
    body: str
    headers: dict


class LocalWebApp:
    """Modello invocato direttamente dai test; sessione creata dopo login fidato."""
    def __init__(self, session_ttl=300):
        self.ttl = _time(session_ttl)
        if self.ttl <= 0:
            raise ValueError("ttl positivo")
        self.sessions = {}

    def start_session(self, *, now):
        timestamp = _time(now)
        expiry = timestamp + self.ttl
        if not math.isfinite(expiry) or expiry <= timestamp:
            raise ValueError("scadenza non rappresentabile")
        self._purge(timestamp)
        session_id, csrf = secrets.token_urlsafe(32), new_csrf_token()
        self.sessions[session_id] = {"csrf": csrf, "expires": expiry, "message": ""}
        return session_id, csrf

    def _purge(self, now):
        for key in list(self.sessions):
            if now >= self.sessions[key]["expires"]:
                del self.sessions[key]

    def logout(self, session_id):
        if isinstance(session_id, str):
            self.sessions.pop(session_id, None)

    @staticmethod
    def _response(status, body):
        return Response(status, body, {"Content-Type": "text/html; charset=utf-8",
                                      "Content-Security-Policy": content_security_policy(),
                                      "X-Content-Type-Options": "nosniff"})

    def update_message(self, session_id, csrf, message, *, method="POST", now):
        timestamp = _time(now)
        self._purge(timestamp)
        if method != "POST":
            return self._response(405, "Metodo non consentito")
        session = self.sessions.get(session_id) if isinstance(session_id, str) else None
        if session is None or not verify_csrf(session["csrf"], csrf):
            return self._response(403, "Richiesta rifiutata")
        if not isinstance(message, str) or len(message) > 1000:
            return self._response(400, "Messaggio non valido")
        session["message"] = message
        return self._response(200, "<p>" + safe_html(message) + "</p>")


def demo():
    app = LocalWebApp(session_ttl=60)
    session, token = app.start_session(now=1000)
    valid = app.update_message(session, token, "<b>Ciao</b> & arrivederci", now=1001)
    print("Richiesta valida:", valid.status)
    print("HTML:", valid.body)
    print("Token mancante:", app.update_message(session, None, "cambio", now=1002).status)
    print("Sessione scaduta:", app.update_message(session, token, "cambio", now=1060).status)
    print("CSP:", valid.headers["Content-Security-Policy"])


if __name__ == "__main__":
    demo()
