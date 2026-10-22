"""Ranking content-based deterministico: nessun addestramento statistico."""
from collections.abc import Mapping
from numbers import Integral
import numpy as np

FEATURE_NAMES = ('programmazione', 'sistemi', 'dati', 'pratica')
COURSES = {
    'python': (1, 0, 0, 1), 'java': (1, 1, 0, 0), 'sql': (0, 0, 1, 1),
    'ml': (1, 0, 1, 1), 'reti': (0, 1, 0, 1),
}


def _unit_vector(values, name):
    a = np.asarray(values, dtype=float)
    if (a.shape != (len(FEATURE_NAMES),)
            or not np.isfinite(a).all() or (a < 0).any()):
        raise ValueError(f'{name}: 4 pesi finiti non negativi')
    maximum = float(a.max())
    if maximum == 0:
        raise ValueError(f'{name}: almeno un peso deve essere positivo')
    # Riscalare prima della norma evita overflow con pesi enormi.
    scaled = a / maximum
    return scaled / np.linalg.norm(scaled)


def recommend(profile, k=3, courses=None, exclude=()):
    """Parità: nome alfabetico; k oltre il catalogo restituisce tutti i candidati."""
    if isinstance(k, (bool, np.bool_)) or not isinstance(k, Integral) or k < 0:
        raise ValueError('k deve essere un intero non negativo')
    unit_profile = _unit_vector(profile, 'profile')
    catalog = COURSES if courses is None else courses
    if not isinstance(catalog, Mapping):
        raise ValueError('courses deve essere una mappa nome -> vettore')
    if isinstance(exclude, str):
        raise ValueError('exclude deve essere una collezione di nomi, non una stringa')
    try:
        omitted = set(exclude)
    except TypeError as error:
        raise ValueError('exclude deve essere una collezione di nomi') from error
    if not all(isinstance(name, str) for name in omitted):
        raise ValueError('exclude contiene un nome non testuale')
    ranked = []
    for name, vector in catalog.items():
        if not isinstance(name, str) or not name:
            raise ValueError('ogni corso deve avere un nome testuale non vuoto')
        unit_course = _unit_vector(vector, f'corso {name}')
        if name not in omitted:
            score = float(np.clip(np.dot(unit_profile, unit_course), 0.0, 1.0))
            ranked.append((name, score))
    ranked.sort(key=lambda item: (-item[1], item[0]))
    return ranked[:int(k)]


def run_example():
    profile = [1, 0, 1, 1]
    return {'profile': profile, 'feature_names': list(FEATURE_NAMES),
            'catalog': {name: list(values) for name, values in COURSES.items()},
            'ranking': [{'course': name, 'score': score} for name, score in recommend(profile, k=5)],
            'excluding_ml': [{'course': name, 'score': score} for name, score in recommend(profile, exclude=['ml'])]}


def main():
    print('P076 — profilo [1, 0, 1, 1]; ranking completo')
    for item in run_example()['ranking']:
        print(f"{item['course']}: {item['score']:.6f}")
    print('Escludendo ml:', ', '.join(name for name, _ in recommend([1, 0, 1, 1], exclude=['ml'])))


if __name__ == '__main__':
    main()
