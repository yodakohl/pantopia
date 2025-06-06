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
        "11111111-1111-1111-1111-111111111111",
    ], capture_output=True, text=True)
    assert "11111111-1111-1111-1111-111111111111" in result.stdout
    assert "Widget" in result.stdout
    assert "$12.00" in result.stdout
    assert result.returncode == 0
