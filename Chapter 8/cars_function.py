def make_car(make, model, **car_info):
    """Build a dictionary with info on a car"""
    car_info['manufacturer'] = make
    car_info['model'] = model
    return car_info