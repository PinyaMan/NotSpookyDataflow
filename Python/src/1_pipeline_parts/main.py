import apache_beam as beam
from things_the_pipeline_will_use.pipeline_options import CustomOptions
from things_the_pipeline_will_use.pipeline_pardo import WordSplitCustomPardo, DataPrinterCustomPardo


def pipeline_builder():
    # The pipeline will use the custom options that we designed for it, so, we have to specify the pipeline Options on
    # builder of the beam.Pipeline.
    # https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
    pipeline_options = CustomOptions()
    # WHY are we using the with statement? https://stackoverflow.com/a/52282001/11293189
    with beam.Pipeline(options=pipeline_options) as pipeline:
        # We will be building the pipeline using the variable 'pipeline', you will see some other codes using 'p'
        # instead of 'pipeline' referring to this variable.

        # For example, we will build a simple batch pipeline that reads from a generated PCollection and writes
        # the words separately into a text file. In order to do that we will ahve to create a PCollection and make it
        # as source from our pipeline.
        # https://beam.apache.org/documentation/programming-guide/#creating-a-pcollection
        input_read_transform = beam.Create([
            'To be, or not to be: that is the question: ',
            "Whether 'tis nobler in the mind to suffer ",
            'The slings and arrows of outrageous fortune, ',
            'Or to take arms against a sea of troubles, '])

        # Now that we have the input PCollection we have to apply it as source four our pipeline, in order to do that
        # we will use the following syntax:
        # ------------------------------------------------------------------------------------------------------------
        # [Output PCollection] = [Input PCollection] | [Transform]
        # ------------------------------------------------------------------------------------------------------------

        # https://beam.apache.org/documentation/programming-guide/#applying-transforms
        read_transform_pcollection = pipeline | input_read_transform

        # Now we want to apply separate each phrase into individual words, to do so we will be using a Pardo transform
        # https://beam.apache.org/documentation/programming-guide/#core-beam-transforms
        word_split_transform = beam.ParDo(WordSplitCustomPardo())
        pardo_transform_pcollection = read_transform_pcollection | word_split_transform

        # If you don't trust anyone and think that returning a list won't separate this phrase into different words
        # putting them on a PCollection each, uncomment the following line and apply the print ParDo
        data_printer_transform = beam.ParDo(DataPrinterCustomPardo())
        pardo_print_transform_pcollection = pardo_transform_pcollection | data_printer_transform

        # Lastly, we have to set a sink/output for all the processed data, in this case we will write to a txt document.
        # https://beam.apache.org/documentation/programming-guide/#pipeline-io-writing-data

        sink_transform = beam.io.WriteToText(
            pipeline_options.output_folder,
            file_name_suffix=".txt")
        last_transform = pardo_transform_pcollection | sink_transform

        # The following code is the equivalent to all the single steps that we did above, following the syntax:
        # ------------------------------------------------------------------------------------------------------------
        # [Final Output PCollection] = ([Initial Input PCollection] | [First Transform]
        #               | [Second Transform]
        #               | [Third Transform])
        # ------------------------------------------------------------------------------------------------------------
        # last_transform = (pipeline
        #                  | "replicated" >> word_split_transform
        #                  | "replicate2d" >> data_printer_transform
        #                  | "replicated3" >> sink_transform)


if __name__ == '__main__':
    print("YOU ARE RUNNING A BEAUTIFUL PIPELINE, ENJOY ;)")
    pipeline_builder()
