<h1>NotSpookyDataflow: 1. Pipeline parts.</h1>
The code in this folder will focus mainly on the basic parts that a Beam Pipeline has. 
The main point of this simple codes is to make Apache Beam and the Dataflow environment more friendly to someone that needs to work with and has never build his first one without using a Quickstart prebuild code. 
<br>
The reading starts at the python file main.py and from the comments you should be able to follow the execution thread. 
<br>
Please, first read the code and try to understand it and once you completed this task move to the following execution steps:<br>

1. Clone the repo:
```sh
git clone https://github.com/PinyaMan/NotSpookyDataflow.git
```
2. Locate your terminal inside the folder 1_pipeline_parts:
```sh
cd NotSpookyDataflow/Python/src/1_pipeline_parts/
```
3. Create an environent and install the python packages:
```sh
python3 -m venv env
source env/bin/activate
pip3 install -r ./requirements.txt
```
4. Let's execute this pipeline locally... How do I run this lovely pipeline? Check the help to see which parameters you should run:
```sh
python -m main --help
```
5. Now that you know what this pipeline need to be executed, set the parameters:
```sh
python -m main --output <PATH TO THE OUTPUT FOLDER>/result-
```
6. CONGRATS!!
7. Wait... You want to deploy it on Dataflow? Sure? Okay.
⋅⋅* You will need to create a GCP project and Google Cloud Storage bucket to run this on Dataflow.
⋅⋅* We should set two environment variables to run it on [Google Cloud Dataflow][1]
```sh
PROJECT=<Your PROJECTID>
BUCKET=<BUCKET NAME AND PATH THAT YOU WANT TO USE, ex: gs://my-bucket/blabla/ >
```
8. And now run it with:
```sh
python -m main \
  --output gs://$BUCKET/1_pipeline_parts/outputs \
  --temp_location gs://$BUCKET/1_pipeline_parts/tmp/ \
  --runner DataflowRunner \
  --project $PROJECT \
  --setup_file setup.py
```

[1]: https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python#run-wordcount-locally
