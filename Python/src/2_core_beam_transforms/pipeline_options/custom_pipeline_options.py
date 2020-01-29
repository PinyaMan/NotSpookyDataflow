from apache_beam.options.pipeline_options import PipelineOptions


class CustomPipelineOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument('--output_folder',
                            help='Output for the pipeline, Example: /home/usr/ouputFolder/',
                            default=' <PATH TO THE OUTPUT FOLDER>/result-')
        parser.add_argument('--transform',
                            help='Beam transform that you want to run, values: PARDO, GROUPBYKEY,COMBINE,COGROUPBYKEY,'
                                 'FLATTEN,PARTITION',
                            default='PARDO')
