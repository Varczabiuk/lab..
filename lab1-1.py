from abc import ABC, abstractmethod

# 1. Базовий абстрактний клас (Наслідування + Інкапсуляція)
class Camera(ABC):
    def __init__(self, location):
        self._location = location  # Інкапсуляція — захищене поле

    @abstractmethod
    def record(self):
        pass

    def get_location(self):
        return self._location


# 2. Похідні класи
class IPCamera(Camera):
    def __init__(self, location, ip_address):
        super().__init__(location)
        self.__ip_address = ip_address  # Інкапсуляція — приватне поле

    def record(self):
        return f"IP Camera at {self._location} is recording via {self.__ip_address}"

    def get_ip(self):
        return self.__ip_address


class AnalogCamera(Camera):
    def __init__(self, location, channel):
        super().__init__(location)
        self.__channel = channel  # Інкапсуляція — приватне поле

    def record(self):
        return f"Analog Camera at {self._location} is recording on channel {self.__channel}"

    def get_channel(self):
        return self.__channel


# 3. Поліморфізм — колекція камер
cameras = [
    IPCamera("Main Gate", "192.168.1.10"),
    AnalogCamera("Parking Lot", 5)
]

# Проходимо по всіх об'єктах і викликаємо record()
for cam in cameras:
    print(f"Location: {cam.get_location()}")
    print(cam.record())