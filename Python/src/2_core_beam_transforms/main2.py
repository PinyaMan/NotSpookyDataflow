from core_beam_pipelines.abstract_custom_pipeline import CoreBeamTransformAbstractPipeline
import apache_beam as beam
from pipeline_options.custom_pipeline_options import CustomPipelineOptions
from core_beam_pipelines.pardo import ParDoTransformPipeline


def pipeline_applier_factory(pipeline, pipeline_options):
    print(pipeline_options.transform)
    factory_dict = {
        "PARDO": ParDoTransformPipeline,  # TODO: Complete with all the classes
        "GROUPBYKEY": None,
        "COMBINE": None,
        "COGROUPBYKEY": None,
        "FLATTEN": None,
        "PARTITION": None
    }
    return factory_dict[pipeline_options.transform](pipeline, pipeline_options)


if __name__ == '__main__':
    pipeline_options = CustomPipelineOptions()
    with beam.Pipeline(options=pipeline_options) as pipeline:
        pipeline_applier = pipeline_applier_factory(pipeline, pipeline_options)
        pipeline_applier.pipeline_builder()
        pipeline.run()
