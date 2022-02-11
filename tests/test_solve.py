import subprocess
from pathlib import Path

THIS_DIR = Path(__file__).parent
INPUT = THIS_DIR / "input.py"
CONFIG = THIS_DIR / "config.yaml"


def test_solve(tmp_path: Path):
    (tmp_path / "input.py").write_text(INPUT.read_text())
    (tmp_path / "config.yaml").write_text(CONFIG.read_text())

    subprocess.run(("pyroll", "input-py", "solve", "report"), cwd=tmp_path).check_returncode()
