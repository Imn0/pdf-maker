import random
from datetime import datetime

from Events.ExtraordinaryEvent import ExtraordinaryEvent
from Events.ArUcoEvent import ArUcoEvent
from Events.InfrastructureEvent import InfrastructureEvent
from Events.WorkerEvent import WorkerEvent

kategorie = ["Rurociag", "Linia wysokiego napiecia", "ogrodzenie", "Pozostawiony sprzet"]
zdarzenia = ["Intruz", "Ogien", "Rdza"]


def aruco(count: int):
    events = []
    for _ in range(count):
        events.append(ArUcoEvent(random.randint(1, 100), (random.uniform(50, 55), random.uniform(15, 20)), "img/image2.jpg", random.choice([True, False]), random.choice([True, False])))
    return events

def worker(count: int):
    events = []
    for _ in range(count):
        events.append(WorkerEvent(random.choice([True, False]), random.choice([True, False]), random.choice([True, False]), "img/image2.jpg", (random.uniform(50, 55), random.uniform(15, 20))))
    return events

def infrastructure(count: int):
    events = []
    for _ in range(count):
        events.append(InfrastructureEvent(random.choice(kategorie), datetime.now(), (random.uniform(50, 55), random.uniform(15, 20)), "img/image2.jpg" ))
    return events

def extraordinary(count: int):
    events = []
    for _ in range(count):
        events.append(ExtraordinaryEvent(random.choice(zdarzenia), datetime.now(), (random.uniform(50, 55), random.uniform(15, 20)), "img/image2.jpg", random.choice([True, False])))
    return events