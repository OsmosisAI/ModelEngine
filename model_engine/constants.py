import enum


class TensorflowStrategy(enum.Enum):
    MIRRORED_STRATEGY = 'MirroredStrategy'
    TPU_STRATEGY = 'TPUStrategy'
    MULTI_WORKER_STRATEGY = 'MultiWorkerMirroredStrategy'
    CENTRAL_STORAGE_STRATEGY = 'CentralStorageStrategy'
    PARAMETER_SERVER_STRATEGY = 'ParameterServerStrategy'
    ONE_DEVICE_STRATEGY = 'OneDeviceStrategy'
