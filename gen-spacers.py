from pathlib import Path
import subprocess
import shutil

OPENSCAD_EXE=r"C:\Users\jordan\Downloads\OpenSCAD-2025.10.17-x86-64\OpenSCAD-2025.10.17-x86-64\openscad.exe"
SCRIPT_DIR = Path(__file__).parent

class Spacer:
    def __init__(self, type: str, id: float, od: float, length: float, subsystem: str, count: int, label: str):
        self.type = type
        self.id = id
        self.od = od
        self.length = length
        self.subsystem = subsystem
        self.count = count
        self.label = label

spacers = [
    Spacer("hex", 0.5, 0.75, 0.1, "IT", 6, "A"),
    Spacer("hex", 0.5, 0.75, 0.12, "IT", 2, "B"),
    Spacer("hex", 0.5, 0.75, 0.661, "IT", 2, "C"),
    Spacer("hex", 0.5, 0.75, 1.393, "IT", 2, "D"),
    Spacer("hex", 0.5, 0.75, 0.058, "IT", 2, "E"),
    Spacer("hex", 0.5, 0.75, 0.25, "IN", 2, "F"),
    Spacer("hex", 0.5, 0.75, 0.188, "IN", 2, "G"),
    Spacer("hex", 0.5, 0.75, 0.0625, "IN", 2, "H"),
    Spacer("hex", 0.5, 0.75, 0.125, "IN", 32, "I"),
    Spacer("hex", 0.5, 0.75, 0.437, "IN", 2, "J"),
    Spacer("hex", 0.5, 0.75, 1.75, "KI", 1, "K"),
    Spacer("hex", 0.5, 0.75, 2.5, "KI", 1, "L"),
    Spacer("hex", 0.5, 0.75, 0.69, "KI", 1, "M"),
    Spacer("hex", 0.5, 0.75, 0.0625, "KI", 2, "N"),
    Spacer("round", 1.250, 1.5, 0.062, "KI", 1, "O"),
    Spacer("hex", 0.5, 0.75, 0.5, "TU", 4, "P"),
    Spacer("hex", 0.5, 0.75, 0.221, "TU", 1, "Q"),
    Spacer("hex", 0.5, 0.75, 0.281, "TU", 1, "R"),
    Spacer("hex", 0.5, 0.75, 0.189, "TU", 1, "S"),
    Spacer("hex", 0.5, 0.75, 0.281, "TU", 2, "T"),
    Spacer("hex", 0.5, 0.75, 0.25, "TU", 1, "U"),
    Spacer("hex", 0.5, 0.75, 0.125, "SH", 3, "V"),
    Spacer("hex", 0.5, 0.75, 0.377, "SH", 1, "W"),
    Spacer("hex", 0.5, 0.75, 0.625, "SH", 2, "X"),
    Spacer("hex", 0.5, 0.75, 0.062, "SH", 2, "Y"),
    Spacer("hex", 0.5, 0.75, 0.187, "SH", 2, "Z"),
    Spacer("hex", 0.5, 0.75, 0.75, "SH", 2, "0"),
    Spacer("hex", 0.5, 0.75, 2.5, "SH", 2, "1")
]

out_dir = SCRIPT_DIR / "out"
if out_dir.is_dir():
    shutil.rmtree(out_dir)
out_dir.mkdir()

for spacer in spacers:
    out_file = out_dir / f"{spacer.subsystem}-{spacer.label}.stl"
    subprocess.run([
        OPENSCAD_EXE,
        "--enable", "textmetrics",
        "-o", str(out_file.resolve().as_posix()),
        "-D", f'TYPE="{spacer.type}"',
        "-D", f'ID={spacer.id}',
        "-D", f'OD={spacer.od}',
        "-D", f'LENGTH={spacer.length}',
        "-D", f'SUBSYSTEM="{spacer.subsystem}"',
        "-D", f'LABEL="{spacer.label}"',
        "gen-spacers.scad"
    ], cwd=SCRIPT_DIR).check_returncode()
