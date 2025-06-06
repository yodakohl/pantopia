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
        "WID-001",
    ], capture_output=True, text=True)
    assert "WID-001" in result.stdout
    assert "Widget" in result.stdout
    assert "$12.00" in result.stdout
    assert result.returncode == 0
