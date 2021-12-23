class ResponseParser:
    def __init__(self, initial_data):
        for key in initial_data:
            setattr(self, key, initial_data[key])
