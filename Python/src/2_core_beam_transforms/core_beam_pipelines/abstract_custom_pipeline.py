from abc import ABC, abstractmethod


class CoreBeamTransformAbstractPipeline:
    options = None
    pipeline = None

    def __init__(self, options, pipeline) -> None:
        super().__init__()
        self.options = options
        self.pipeline = pipeline

    @abstractmethod
    def pipeline_builder(self):
        pass
