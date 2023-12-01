from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer
from typing import Tuple


class WorkerEvent:
    ehs: bool
    is_worker: bool
    change: bool
    position: Tuple[float, float]
    photo_path: str

    def __init__(self, is_worker: bool,
                 ehs: bool, change: bool,
                 photo_path: str,
                 position: Tuple[float, float] | None = None) -> None:
        self.ehs = ehs
        self.is_worker = is_worker
        self.change = change
        self.position = position
        self.photo_path = photo_path

    """
    pracownik
    """
    def get_worker_event(self):
        return ["Jest" if self.is_worker else "Nie ma", "Tak" if self.ehs else "Nie", f"lat: {self.position[0]:.4f} \nlon: {self.position[1]:.4f}" if self.is_worker else " ", "Tak" if self.change else "Nie", Image(self.photo_path, width=50, height=50)]
