from pathlib import Path
import json
import re
import unicodedata

import pandas as pd

from project_paths import project_root


STATSBOMB_BASE_URL = 'https://raw.githubusercontent.com/statsbomb/open-data/master/data'
STATSBOMB_COMPETITION_ALIASES = {
    'Africa Cup of Nations': 'African Cup of Nations',
}

LONG_BALL_MIN_LENGTH = 30.0

SOURCE_ELO_BASE_URL = 'https://www.eloratings.net'
ELO_FAVORITE_THRESHOLD = 75
STATSBOMB_TO_ELO_ALIASES = {
    'Cape Verde Islands': 'Cape Verde',
    'Congo DR': 'DR Congo',
    'Czech Republic': 'Czechia',
    "Cote d'Ivoire": 'Ivory Coast',
    "Côte d'Ivoire": 'Ivory Coast',
}

OPEN_METEO_GEOCODING_ENDPOINT = 'https://geocoding-api.open-meteo.com/v1/search'
OPEN_METEO_ARCHIVE_URL = 'https://archive-api.open-meteo.com/v1/archive'
OPEN_METEO_HOURLY_VARIABLES = ['temperature_2m', 'apparent_temperature', 'precipitation', 'rain']
REQUEST_HEADERS = {'User-Agent': 'football-weather-bigdata-student-project/1.0'}

COUNTRY_CODES = {
    'Azerbaijan': 'AZ',
    "Côte d'Ivoire": 'CI',
    'Denmark': 'DK',
    'England': 'GB',
    'Germany': 'DE',
    'Hungary': 'HU',
    'Italy': 'IT',
    'Netherlands': 'NL',
    'Qatar': 'QA',
    'Romania': 'RO',
    'Russia': 'RU',
    'Scotland': 'GB',
    'Spain': 'ES',
    'United States of America': 'US',
}

EXPECTED_COUNTRY_NAMES = {
    "Côte d'Ivoire": {"Côte d'Ivoire", 'Ivory Coast'},
    'England': {'United Kingdom', 'England'},
    'Scotland': {'United Kingdom', 'Scotland'},
    'United States of America': {'United States'},
}

GEOCODING_QUERY_OVERRIDES = {
    ('San Pedro', "Côte d'Ivoire"): 'San-Pedro',
}

TEMPERATURE_COLD_MAX = 10.0
TEMPERATURE_MILD_MAX = 20.0
TEMPERATURE_WARM_MAX = 28.0
TEMPERATURE_GROUP_LABELS = ['cold', 'mild', 'warm', 'hot']
TEMPERATURE_GROUP_BINS = [
    -float('inf'),
    TEMPERATURE_COLD_MAX,
    TEMPERATURE_MILD_MAX,
    TEMPERATURE_WARM_MAX,
    float('inf'),
]

WEATHER_SCHEMA_VERSION = 'weather_observation.v1'
DEFAULT_KAFKA_WEATHER_TOPIC = 'weather.observations'
DEFAULT_SPARK_MASTER = 'spark://172.29.16.102:7077'
DEFAULT_KAFKA_BOOTSTRAP_SERVERS = '172.29.16.101:9092'


SPECIAL_ASCII_REPLACEMENTS = str.maketrans({
    'ı': 'i',
    'İ': 'I',
    'ł': 'l',
    'Ł': 'L',
})


def load_tournament_scope(root: Path | None = None) -> dict:
    base_path = root or project_root()
    with (base_path / 'data' / 'reference' / 'tournament_scope.json').open('r', encoding='utf-8') as file:
        return json.load(file)


def expected_match_count(root: Path | None = None) -> int:
    return int(load_tournament_scope(root)['expected_totals']['matches'])


def expected_team_match_rows(root: Path | None = None) -> int:
    return int(load_tournament_scope(root)['expected_totals']['team_match_rows'])


def classify_elo_group(elo_diff):
    if pd.isna(elo_diff):
        return pd.NA
    if elo_diff > ELO_FAVORITE_THRESHOLD:
        return 'favorite'
    if elo_diff < -ELO_FAVORITE_THRESHOLD:
        return 'underdog'
    return 'balanced'


def strip_accents(value: str) -> str:
    normalized = unicodedata.normalize('NFKD', value.translate(SPECIAL_ASCII_REPLACEMENTS))
    return ''.join(character for character in normalized if not unicodedata.combining(character))


def normalize_for_match(value):
    if pd.isna(value):
        return ''
    return re.sub(r'[^a-z0-9]+', ' ', strip_accents(str(value)).lower()).strip()


def assign_temperature_group(series: pd.Series) -> pd.Series:
    groups = pd.cut(
        series,
        bins=TEMPERATURE_GROUP_BINS,
        labels=TEMPERATURE_GROUP_LABELS,
        right=False,
    )
    groups = groups.astype('string')
    groups.loc[series == 28.0] = 'warm'
    return groups
