from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHROMEDRIVER_CONFIG_FILE = PROJECT_ROOT / "chromedriver_path.txt"
DEFAULT_CHROMEDRIVER_PATH = r"C:\Program Files\Chromedriver\chromedriver.exe"


def get_chromedriver_path():
    env_path = os.getenv("CHROMEDRIVER_PATH", "").strip()
    if env_path:
        return env_path

    if CHROMEDRIVER_CONFIG_FILE.exists():
        configured_path = CHROMEDRIVER_CONFIG_FILE.read_text(encoding="utf-8").strip()
        if configured_path:
            return configured_path

    return DEFAULT_CHROMEDRIVER_PATH


def save_chromedriver_path(path):
    CHROMEDRIVER_CONFIG_FILE.write_text(path.strip(), encoding="utf-8")
