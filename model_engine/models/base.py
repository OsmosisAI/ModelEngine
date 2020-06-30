registered_models = {}


class RegisterModel(object):
    def __init__(self, model_name, model_identifier):
        self.model_name = model_name
        self.model_identifier = model_identifier

    def __call__(self, cls):
        registered_models[self.model_identifier] = cls
        return cls
