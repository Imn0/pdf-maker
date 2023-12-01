from typing import Tuple
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer


class ArUcoEvent:
    contents: int
    position: Tuple[float, float]
    photo_path: str
    position_change: bool
    contents_change: bool

    def __init__(self, contents: int,
                 position: Tuple[float, float],
                 photo_path: str,
                 position_change: bool,
                 contents_change: bool) -> None:
        self.contents = contents
        self.position = position
        self.photo_path = photo_path
        self.position_change = position_change
        self.contents_change = contents_change


    """
    ArUco
    """
    def get_aruco_event(self):
        return [self.contents, f"lat: {self.position[0]:.4f} \nlon: {self.position[1]:.4f}", "Tak" if self.position_change else "Nie", "Tak" if self.contents_change else "Nie", Image(self.photo_path, width=50, height=50)]
