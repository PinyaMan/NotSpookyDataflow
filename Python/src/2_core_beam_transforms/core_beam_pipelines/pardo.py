from core_beam_pipelines.abstract_custom_pipeline import CoreBeamTransformAbstractPipeline


class ParDoTransformPipeline(CoreBeamTransformAbstractPipeline):

    def pipeline_builder(self):
        print(self.pipeline, self.options)
        pass
