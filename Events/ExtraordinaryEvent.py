from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer
from datetime import datetime
from typing import Tuple


class ExtraordinaryEvent:
    event_type: str
    detection_time: datetime
    position: Tuple[float, float]
    photo_path: str
    notification: bool

    def __init__(self, event_type: str,
                 detection_time: datetime,
                 position: Tuple[float, float],
                 photo_path: str,
                 notification: bool) -> None:
        self.event_type = event_type
        self.detection_time = detection_time.strftime("%Y-%m-%d %H:%M:%S")
        self.position = position
        self.photo_path = photo_path
        self.notification = notification

    """
    sytuacje nadzwyczajne
    """

    def get_extraordinary_event(self):
        return [self.event_type, self.detection_time, f"lat: {self.position[0]:.4f} \nlon: {self.position[1]:.4f}", Image(self.photo_path, width=50, height=50), "Tak" if self.notification else "Nie"]
