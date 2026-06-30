from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


_CANONICAL_PATH = Path(__file__).resolve().parents[1] / 'project_paths.py'
_SPEC = spec_from_file_location('_football_weather_project_paths', _CANONICAL_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f'Could not load canonical project_paths module from {_CANONICAL_PATH}')

_MODULE = module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

project_root = _MODULE.project_root
ensure_pyspark_path = _MODULE.ensure_pyspark_path
