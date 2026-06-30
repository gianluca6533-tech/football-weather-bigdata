from pathlib import Path
import os
import sys


def project_root() -> Path:
    """Return the project root for local runs and the Docker/Jupyter environment."""
    env_root = os.getenv('PROJECT_ROOT')
    candidates = []
    if env_root:
        candidates.append(Path(env_root).expanduser())

    cwd = Path.cwd()
    module_root = Path(__file__).resolve().parent
    candidates.extend([
        module_root,
        cwd,
        cwd / 'football-weather-bigdata',
        *cwd.parents,
        Path('/home/jovyan/work'),
    ])

    for candidate in candidates:
        if (candidate / 'notebooks').exists() and (candidate / 'docs').exists():
            return candidate

    raise FileNotFoundError('Could not locate project root. Set PROJECT_ROOT if needed.')


def ensure_pyspark_path() -> None:
    """Make PySpark importable in lightweight notebook images that only set SPARK_HOME."""
    spark_home = Path(os.getenv('SPARK_HOME', '/usr/local/spark'))
    candidates = [
        spark_home / 'python',
        spark_home / 'python' / 'lib' / 'pyspark.zip',
        spark_home / 'python' / 'lib' / 'py4j-0.10.9.7-src.zip',
    ]
    for candidate in candidates:
        if candidate.exists():
            path = str(candidate)
            if path not in sys.path:
                sys.path.insert(0, path)
