from src.vehicle import Vehicle
from src.authorized_dealer import AuthorizedDealer

def main() -> None:
    vehicle = Vehicle(id="A-1", brand="Ford", model="Fiesta", mileage=150)
    vehicle2 = Vehicle(id="A-2", brand="Chevrolet", model="GT", mileage=200, price=45000)
    print(vehicle.information())
    authorized_dealer = AuthorizedDealer([vehicle, vehicle2, vehicle, vehicle2, vehicle2, vehicle])
    print(authorized_dealer.vehicles)

if __name__ == '__main__':
    main()