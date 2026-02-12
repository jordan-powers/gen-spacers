
class Spacer:
    def __init__(self, type: str, id: float, od: float, length: float, note: str, count: int):
        self.type = type
        self.id = id
        self.od = od
        self.length = length
        self.note = note
        self.count = count

spacers = [
    Spacer("hex", 0.5, 0.75, 0.1, "IT", 6),
    Spacer("hex", 0.5, 0.75, 0.12, "IT", 2),
    Spacer("hex", 0.5, 0.75, 0.661, "IT", 2),
    Spacer("hex", 0.5, 0.75, 1.393, "IT", 2),
    Spacer("hex", 0.5, 0.75, 0.058, "IT", 2),
    Spacer("hex", 0.5, 0.75, 0.25, "IN", 2),
    Spacer("hex", 0.5, 0.75, 0.188, "IN", 2),
    Spacer("hex", 0.5, 0.75, 0.0625, "IN", 2),
    Spacer("hex", 0.5, 0.75, 0.125, "IN", 32),
    Spacer("hex", 0.5, 0.75, 0.437, "IN", 2),
    Spacer("hex", 0.5, 0.75, 1.75, "KI", 1),
    Spacer("hex", 0.5, 0.75, 2.5, "KI", 1),
    Spacer("hex", 0.5, 0.75, 0.69, "KI", 1),
    Spacer("hex", 0.5, 0.75, 0.0625, "KI", 2),
    Spacer("round", 1.250, 1.5, 0.062, "KI", 1),
    Spacer("hex", 0.5, 0.75, 0.5, "TU", 4),
    Spacer("hex", 0.5, 0.75, 0.221, "TU", 1),
    Spacer("hex", 0.5, 0.75, 0.281, "TU", 1),
    Spacer("hex", 0.5, 0.75, 0.189, "TU", 1),
    Spacer("hex", 0.5, 0.75, 0.281, "TU", 2),
    Spacer("hex", 0.5, 0.75, 0.25, "TU", 1),
    Spacer("hex", 0.5, 0.75, 0.125, "SH", 3),
    Spacer("hex", 0.5, 0.75, 0.377, "SH", 1),
    Spacer("hex", 0.5, 0.75, 0.625, "SH", 2),
    Spacer("hex", 0.5, 0.75, 0.062, "SH", 2),
    Spacer("hex", 0.5, 0.75, 0.187, "SH", 2),
    Spacer("hex", 0.5, 0.75, 0.75, "SH", 2),
    Spacer("hex", 0.5, 0.75, 2.5, "SH", 2)
]
