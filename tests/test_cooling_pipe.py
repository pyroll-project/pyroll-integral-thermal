import logging
import webbrowser
from pathlib import Path

from pyroll.core import Profile, PassSequence, CoolingPipe


def test_solve(tmp_path: Path, caplog):
    caplog.set_level(logging.DEBUG, logger="pyroll")

    import pyroll.integral_thermal

    in_profile = Profile.round(
        diameter=8e-3,
        temperature=1100 + 273.15,
        strain=0,
        material=["StT-IV", "steel"],
        flow_stress=100e6,
        density=7.5e3,
        specific_heat_capacity=690,
        velocity=32.8
    )

    sequence = PassSequence(
        [
            CoolingPipe(
                length=1720e-3,
                inner_diameter=20e-3,
                cooling_water_volume_flux=0.0101194,
            )
        ]
    )

    try:
        sequence.solve(in_profile)
    finally:
        print("\nLog:")
        print(caplog.text)

    try:
        from pyroll.report import report
        report = report(sequence)
        f = tmp_path / "report.html"
        f.write_text(report)
        webbrowser.open(f.as_uri())
    except ImportError:
        pass
