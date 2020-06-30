from typing import Union, Type

from model_engine.inference import BaseModelInference
from model_engine.models.base import registered_models
from model_engine.models import yolov3
from model_engine.train import BaseModelTrain


class NoSuchModel(Exception):
    pass


def get_model(model_identifier) -> Union[Type[BaseModelInference], Type[BaseModelTrain]]:
    try:
        model = registered_models[model_identifier]
        return model
    except KeyError:
        raise NoSuchModel(f'No model with identifier: {model_identifier}')
