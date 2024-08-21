from restaurant import Restaurant
from car import Car

def main():
    pizza_planet = Restaurant("Pizza Planet", "Pizzaria")
    fusca = Car("Fusca Itamar", "Black", 1994)
    
    print(pizza_planet.__str__())
    print(fusca.__str__())
    

if __name__ == '__main__':
    main()