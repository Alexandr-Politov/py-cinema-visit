from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    hall_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()
    cleaner_instance = Cleaner(cleaner)

    for customer in customer_instances:
        bar_instance.sell_product(customer.food, customer)

    hall_instance.movie_session(movie, customer_instances, cleaner_instance)
