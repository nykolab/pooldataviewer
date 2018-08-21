# chdir into given folder pool
# for every file in underlying folder (pool/10/10/10/10) unpickle file and save as json
import os
import glob
import logging
import sys

DATA_FOLDER = "C:\\Dev\\pooldataviewer\\testdata"
logger.info("Processing folder %s", DATA_FOLDER)

# setup logger (put in additional module ? TODO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


# check if folder exists
if not os.path.exists(DATA_FOLDER):
    sys.exit("Data folder %s is not exist" % DATA_FOLDER)


os.chdir(DATA_FOLDER)

for name in glob.glob("pool/[0-9]*/[0-9]*/[0-9]*/[0-9]*"):
    print "name: %s, type: %s" % (name, type(name))

    # Create appropriate output folders to store json files



# import os, errno
#
# try:
#     os.makedirs(directory)
# except OSError as e:
#     if e.errno != errno.EEXIST:
#         raise
