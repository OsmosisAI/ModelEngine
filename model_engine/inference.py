from contextlib import contextmanager
from dataclasses import dataclass
from typing import List


@dataclass
class Result(object):
    pass


@dataclass
class Box(object):
    __slots__ = ['x_min', 'y_min', 'x_max', 'y_max']
    x_min: int
    y_min: int
    x_max: int
    y_max: int


@dataclass
class BoundingBoxResult(object):
    __slots__ = ['label', 'confidence', 'coordinates']
    label: str
    confidence: float
    coordinates: Box


class BaseModelInference(object):
    def inference(self, image) -> List[Result]:
        pass

    @contextmanager
    def inference_session(self, labels_path, weights_path) -> 'BaseModelInference':
        try:
            return self
        finally:
            pass
