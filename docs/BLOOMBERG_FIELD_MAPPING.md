# Bloomberg Field Mapping

Ce document décrit comment le fournisseur Bloomberg de MarketPulse (`src/providers/bloomberg_provider.py`, TD10) transforme les données Bloomberg au format canonique commun à tous les fournisseurs. Il doit suffire pour implémenter le mapping sans ambiguïté.

## 1. Objectif et modes autorisés

MarketPulse compare un instrument à son indice de référence. Les calculs (`src/analytics.py`) ne dépendent pas de la source : chaque fournisseur (Yahoo, Bloomberg) doit renvoyer une liste d'**observations canoniques** avec exactement les mêmes clés et les mêmes types.

```text
Yahoo Finance     -> yahoo_provider.py     \
                                             -> observations canoniques -> analytics.py
Bloomberg         -> bloomberg_provider.py /
```

Deux modes d'accès sont prévus :

| Mode | Source des données | Disponibilité | Statut dans le projet |
|---|---|---|---|
| `APPROVED_SAMPLE` (par défaut) | `data/sample/bloomberg_reference_sample.json`, échantillon approuvé par l'enseignant | Partout, sans Terminal Bloomberg | Mode utilisé par l'équipe |
| `LIVE` | Terminal Bloomberg autorisé (salle de marché) | Uniquement dans un environnement autorisé | Point d'extension non implémenté : lève `NotImplementedError` |

Les valeurs de l'échantillon approuvé sont des valeurs pédagogiques (`"is_live_bloomberg_output": false`). Ce ne sont pas des données historiques Bloomberg certifiées.

## 2. Identifiants AAPL / SP500

Chaque source a son propre système d'identifiants. Le dictionnaire `BLOOMBERG_IDENTIFIERS` relie le ticker interne MarketPulse à l'identifiant Bloomberg.

| Ticker MarketPulse | Identifiant Bloomberg (`provider_identifier`) | Instrument | Rôle |
|---|---|---|---|
| `AAPL` | `AAPL US Equity` | Apple Inc. (action) | instrument |
| `SP500` | `SPX Index` | S&P 500 (indice) | benchmark |

Règle : l'identifiant Bloomberg sert uniquement à **trouver la série** dans le JSON. Les observations canoniques contiennent toujours le ticker interne (`AAPL`, `SP500`), jamais `AAPL US Equity` ni `SPX Index`.

## 3. Correspondance des champs et types

Structure d'une série dans le JSON source :

```json
{
  "role": "instrument",
  "canonical_ticker": "AAPL",
  "provider_identifier": "AAPL US Equity",
  "observations": [
    {"observation_date": "...", "open_value": ..., "high_value": ..., "low_value": ...,
     "close_value": ..., "volume_value": ...}
  ]
}
```

La série est sélectionnée par sa clé `provider_identifier`. Chaque observation est ensuite convertie ainsi :

| Champ source Bloomberg | Niveau dans le JSON | Champ MarketPulse | Type cible | Conversion |
|---|---|---|---|---|
| `observation_date` | observation | `date` | `str` (AAAA-MM-JJ) | recopié tel quel |
| `canonical_ticker` | série | `ticker` | `str` | recopié depuis la série |
| `open_value` | observation | `open` | `float` | `float(...)` |
| `high_value` | observation | `high` | `float` | `float(...)` |
| `low_value` | observation | `low` | `float` | `float(...)` |
| `close_value` | observation | `close` | `float` | `float(...)` |
| `volume_value` | observation | `volume` | `int` | `int(...)` |

Une observation canonique contient **exactement ces 7 clés** : `date`, `ticker`, `open`, `high`, `low`, `close`, `volume`.

Remarque : les noms `*_value` sont des clés pédagogiques de l'échantillon, pas des mnémoniques officiels Bloomberg.

## 4. Exemple fictif : brut → canonique

**Données fictives** : cet exemple illustre le contrat, ce n'est pas une extraction Bloomberg.

Observation brute (les nombres arrivent sous forme de chaînes) :

```python
raw = {
    "observation_date": "2026-11-18",
    "open_value": "100.0",
    "high_value": "112.0",
    "low_value": "99.0",
    "close_value": "110.0",
    "volume_value": "1500",
}
```

Observation canonique (série `AAPL US Equity`, donc ticker `AAPL`) :

```python
canonical = {
    "date": "2026-11-18",
    "ticker": "AAPL",
    "open": 100.0,
    "high": 112.0,
    "low": 99.0,
    "close": 110.0,
    "volume": 1500,
}
```

Pourquoi convertir ? Avec des chaînes, les calculs d'`analytics.py` échoueraient ou seraient faux (`"110.0" / "100.0"` provoque une erreur, et `"9" > "10"` est vrai en comparaison de texte).

## 5. Vérifications et limites du mode LIVE

Vérifications à faire sur chaque observation canonique :

```python
assert set(canonical) == {"date", "ticker", "open", "high", "low", "close", "volume"}
assert canonical["ticker"] in {"AAPL", "SP500"}
assert isinstance(canonical["date"], str)
assert isinstance(canonical["close"], float)
assert isinstance(canonical["volume"], int)
```

Anomalies à refuser avant la conversion, avec une `ValueError` explicite (fonction `validate_reference_series`, TD10) :

- série sans `canonical_ticker` ou liste `observations` absente ou vide ;
- observation à laquelle il manque un des 6 champs `observation_date`, `open_value`, `high_value`, `low_value`, `close_value`, `volume_value` ;
- deux observations avec la même date ;
- identifiant Bloomberg absent du JSON, ou ticker absent de `BLOOMBERG_IDENTIFIERS`.

Points d'attention sur l'échantillon approuvé :

- l'indice `SPX Index` a un volume à `0` : c'est normal, un indice ne s'échange pas directement ;
- certaines valeurs sont des entiers dans le JSON (par exemple `248`) : la conversion `float()` reste obligatoire pour respecter le contrat ;
- la présence du fichier `bloomberg_reference_expected.json` ne prouve rien : il faut comparer les valeurs ligne par ligne avant d'affirmer que le résultat est conforme.

Limites du mode LIVE :

- aucune connexion Bloomberg n'est disponible pour l'équipe : le mode `LIVE` lève `NotImplementedError` ;
- aucune connexion réussie ne doit être simulée, et toute capture d'écran doit indiquer le mode réellement utilisé (`APPROVED_SAMPLE`).
