// Locate your terminal inside the folder 1_pipeline_parts
// Install the python beam packages
$ pip3 install -r ./requirements.txt
//How to run this lovely pipeline, check the help to see which parameters you should run:
$ python -m main --help

//Now set the parameters
$ python -m main --output <PATH TO THE OUTPUT FOLDER>/result-

// You want to deploy it on Dataflow :O? You ready? Sure? Okay.
// We will set two environment variables
// https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python#run-wordcount-locally
$ PROJECT=<Your PROJECTID>
$ BUCKET=<BUCKET NAME AND PATH THAT YOU WANT TO USE, ex: gs://my-bucket/blabla/ >

// And now run it with...
// nervous? joking.
python -m main \
  --output gs://$BUCKET/1_pipeline_parts/outputs \
  --temp_location gs://$BUCKET/1_pipeline_parts/tmp/ \
  --runner DataflowRunner \
  --project $PROJECT \
  --setup_file setup.py
