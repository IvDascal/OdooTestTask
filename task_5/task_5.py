class Crossroad:
    """
    NS_direction - shows if direction Nord - South is open to drive or walk
    WE_direction - shows if direction West - East is open to drive or walk
    """
    is_night = 0
    is_manual = 0
    NS_direction = 0
    WE_direction = 0
    switch_time = 120

    car_tl_slots = {
        'NW': [],
        'NE': [],
        'SW': [],
        'SE': []
    }

    pedestriat_tl_slots = {
        'NW': [],
        'NE': [],
        'SW': [],
        'SE': []
    }

    def add_car_tl(self, slot, direction):
        car_tl = TrafficLightCar(crossroad=self, direction=direction, slot=slot)
        self.car_tl_slots[slot] = car_tl

    def add_pedestriat_tl(self):
        pass

    def remove_tl(self):
        pass

    def set_manual_mode(self):
        pass

    def set_auto_mode(self):
        pass

    def set_night_regime(self):
        pass

    def set_day_regime(self):
        pass

    def set_NS_direction_state(self):
        pass

    def set_WE_direction_state(self):
        pass


class TrafficLight:
    is_active = False
    state = None

    def __init__(self, crossroad, direction, slot):
        self.crossroad = crossroad
        self.direction = direction
        self.slot = slot
    
    def listen_crossroad(self):
        pass


class TrafficLightCar(TrafficLight):
    STATES = [
        (0, 'RED'),
        (1, 'GREEN'),
        (2, 'YELLOW')
    ]

    def __init__(self, crossroad, direction, slot):
        super(TrafficLightCar, self).__init__(crossroad, direction, slot)


class TrafficLightPedestrian(TrafficLight):
    STATES = [
        (0, 'RED'),
        (1, 'GREEN')
    ]


if __name__ == '__main__':
    main_crossroad = Crossroad()
    main_crossroad.add_car_tl(direction='N', slot='NW')
    
    print(main_crossroad.car_tl_slots)
