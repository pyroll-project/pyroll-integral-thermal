import logging
from importlib import reload
from pathlib import Path

from pyroll.core import solve, RollPass
from pyroll.ui import Reporter


def test_solve(tmp_path: Path, caplog):
    caplog.set_level(logging.DEBUG, logger="pyroll")

    import pyroll.integral_thermal

    import pyroll.ui.cli.res.input_min as input_py
    reload(input_py)

    in_profile = input_py.in_profile
    sequence = input_py.sequence

    in_profile.temperature = 1273
    in_profile.density = 7e3
    in_profile.thermal_capacity = 630

    solve(sequence, in_profile)

    report = Reporter()

    rendered = report.render(sequence)
    print()

    report_file = tmp_path / "report.html"
    report_file.write_text(rendered)
    print(report_file)

    print("\nLog:")
    print(caplog.text)
