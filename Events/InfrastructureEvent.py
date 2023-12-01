from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer
from datetime import datetime
from typing import Tuple


class InfrastructureEvent:
    category: str
    detection_time: datetime
    position: Tuple[float, float]
    photo_path: str

    def __init__(self, category: str,
                 detection_time: datetime,
                 position: Tuple[float, float],
                 photo_path: str) -> None:
        self.category = category
        self.detection_time = detection_time.strftime("%Y-%m-%d %H:%M:%S")
        self.position = position
        self.photo_path = photo_path
        pass

    """
    zmiany w infrastrukturze
    """

    def get_infrastructure_event(self):
        return [self.category, self.detection_time, f"lat: {self.position[0]:.4f} \nlon: {self.position[1]:.4f}", Image(self.photo_path, width=50, height=50)]
