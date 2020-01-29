import apache_beam as beam
from core_beam_pipelines.pardo import ParDoTransformPipeline
from pipeline_options.custom_pipeline_options import CustomPipelineOptions


def pipeline_applier_factory(pipeline: beam.pipeline, pipeline_options: CustomPipelineOptions):
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
