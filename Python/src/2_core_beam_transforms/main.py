from apache_beam.options.pipeline_options import PipelineOptions
from custom_core_beam_transforms.pardo_transforms import *
from apache_beam.options.pipeline_options import PipelineOptions

from custom_core_beam_transforms.pardo_transforms import *


def pipeline_builder():
    pipeline_options = PipelineOptions()
    # ParDos
    unique_words_pardo_transform = "Unique words ParDo transform." >> beam.ParDo(UniqueWordsParDo())
    simple_map_pardo_transform = "Simple map ParDo transform" >> beam.ParDo(SimpleMapPardo())
    element_printer_pardo_transform = beam.ParDo(PrinterParDo())

    # GroupByKey
    # noinspection PyUnresolvedReferences
    fixed_window_transform = beam.WindowInto(beam.window.FixedWindows(60))
    group_by_transform = beam.GroupByKey()

    # Example source
    input_read_transform = beam.Create([
        'To be, or not to be: that is the question: ',
        "Whether 'tis nobler in the mind to suffer ",
        'The slings and arrows of outrageous fortune, ',
        'Or to take arms against a sea of troubles, '])

    with beam.Pipeline(options=pipeline_options) as pipeline:
        output_before_window = (pipeline | input_read_transform
                                | unique_words_pardo_transform
                                | simple_map_pardo_transform)
        without_window = (output_before_window | "Without window" >> element_printer_pardo_transform)
        applying_window = (output_before_window | fixed_window_transform
                           | group_by_transform)
        (applying_window | "Applying window" >> element_printer_pardo_transform)

        def summer(x, y):
            return x, sum(y)

        # Map has exactly a correlation of 1:1 1 Input will always give 1 output
        result = (applying_window
                  | beam.MapTuple(summer)
                  | "After Reduce " >> beam.Map(print))


if __name__ == '__main__':
    print("YOU ARE RUNNING A BEAUTIFUL PIPELINE, ENJOY ;)")
    # The objective on this pipeline will be to perform all the Core Beam transforms to explain them
    # https://beam.apache.org/documentation/programming-guide/#core-beam-transforms
    pipeline_builder()
