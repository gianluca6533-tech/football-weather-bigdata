from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


_CANONICAL_PATH = Path(__file__).resolve().parents[1] / 'pipeline_config.py'
_SPEC = spec_from_file_location('_football_weather_pipeline_config', _CANONICAL_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f'Could not load canonical pipeline_config module from {_CANONICAL_PATH}')

_MODULE = module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

for _name in dir(_MODULE):
    if not _name.startswith('_'):
        globals()[_name] = getattr(_MODULE, _name)
