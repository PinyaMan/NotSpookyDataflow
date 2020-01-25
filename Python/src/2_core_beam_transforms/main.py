import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def pipeline_builder():
    pipeline_options = PipelineOptions()
    with beam.Pipeline(options=pipeline_options) as pipeline:
        pass


if __name__ == '__main__':
    print("YOU ARE RUNNING A BEAUTIFUL PIPELINE, ENJOY ;)")
    pipeline_builder()
