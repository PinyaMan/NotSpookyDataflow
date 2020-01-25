from apache_beam.options.pipeline_options import PipelineOptions


class CustomOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        # Inside this function you will define all the parameters that you need
        parser.add_argument('--output_folder',
                            help='Output for the pipeline, Example: /home/usr/ouputFolder/',
                            default=' <PATH TO THE OUTPUT FOLDER>/result-')
