import subprocess
import sys
from pathlib import Path


def test_cli_filter_sku():
    data_path = Path(__file__).resolve().parent.parent / "sample_data.json"
    result = subprocess.run([
        sys.executable,
        "-m",
        "pantopia.cli",
        str(data_path),
        "--sku",
        "a1b2c3d4-e5f6-7890-1234-567890abcdef",
    ], capture_output=True, text=True)
    assert "a1b2c3d4-e5f6-7890-1234-567890abcdef" in result.stdout
    assert "Apple iPhone 15 Pro" in result.stdout
    assert "$1119.78" in result.stdout
    assert result.returncode == 0


def test_cli_search():
    data_path = Path(__file__).resolve().parent.parent / "sample_data.json"
    result = subprocess.run([
        sys.executable,
        "-m",
        "pantopia.cli",
        str(data_path),
        "--search",
        "apple",
    ], capture_output=True, text=True)
    assert "Apple iPhone 15 Pro" in result.stdout
    assert result.returncode == 0
