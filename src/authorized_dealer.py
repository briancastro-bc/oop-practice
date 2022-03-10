from operator import le
from shutil import ExecError
from typing import List
from .vehicle import Vehicle

class AuthorizedDealer:

    @property
    def vehicles(self) -> List[Vehicle]:
        return self.__vehicles

    def __init__(self, vehicles: List[Vehicle]) -> None:
        """if type(vehicles) is not List[Vehicle]:
            raise ValueError('El parametro no es una lista de vehiculos')"""
        self.__vehicles: List[Vehicle] = vehicles
        self.__limit = 5
    
    def add_vehicle(self, vehicle: Vehicle):
        if len(self.vehicles) > self.__limit:
            raise Exception('El limite fue alcanzado')
        self.vehicles.append(vehicle)
    
    def remove_vehicles(self):
        self.vehicles.clear()
    
    def remove_vehicule(self, vehicle: Vehicle):
        self.vehicles.remove(vehicle)