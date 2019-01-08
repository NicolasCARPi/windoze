# Upload the most recent .nd file to elabftw
# Run it in a journal on MM at end of acquisition
# put config file in same folder as script: config.yml with endpoint and token
import os
import sys
import elabapy
import datetime
import operator
import yaml

print("Uploading the .nd file to elabftw. Stay put.")

# add double \ to avoid unicode decode error
workdir = "D:\\Users"
today = datetime.date.today()
kdate = today.strftime('%Y%m%d')
# read config
config = yaml.safe_load(open("config.yml"))
# init manager from elabapy
manager = elabapy.Manager(token=config["token"], endpoint=config["endpoint"])

def getLastNdFile():
	""""
	    Get the path of the latest .nd file saved in Users folder
	"""
	ndFiles = {}
	for dirpath, dirnames, filenames in os.walk(workdir):
		for file in filenames:
			curpath = os.path.join(dirpath, file)
			fileModified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
			if curpath.endswith('.nd'):
				ndFiles[curpath] = fileModified
	# now we have a dict full of nd files paths
        # sort it by value
	sortedNd = sorted(ndFiles.items(), key=lambda kv: kv[1])
        # and return the path of the last one (most recent)
	return sortedNd[-1][0]

ndFile = getLastNdFile()
# user is the second folder of the path
user = ndFile.split("\\")[2]

# create experiment, update it and upload file
exp = manager.create_experiment()
params = {"title": "mVideoPiel acquisition by " + user, "body": "Experiment created automatically through API", "date": kdate}
manager.post_experiment(exp["id"], params)
files = {'file': open(ndFile, 'rb')}
manager.upload_to_experiment(exp["id"], files)
