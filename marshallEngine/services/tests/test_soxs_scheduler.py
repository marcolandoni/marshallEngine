from __future__ import print_function
from builtins import str
import os
import shutil
import unittest
import yaml
from marshallEngine.utKit import utKit
from fundamentals import tools
from os.path import expanduser
home = expanduser("~")

packageDirectory = utKit("").get_project_root()
# settingsFile = packageDirectory + "/test_settings.yaml"
settingsFile = home + "/git_repos/_misc_/settings/marshall/test_settings.yaml"
su = tools(
    arguments={"settingsFile": settingsFile},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName=None,
    defaultSettingsFile=False
)
arguments, settings, log, dbConn = su.setup()

# SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
moduleDirectory = os.path.dirname(__file__)
pathToInputDir = moduleDirectory + "/input/"
pathToOutputDir = moduleDirectory + "/output/"

try:
    shutil.rmtree(pathToOutputDir)
except:
    pass
# COPY INPUT TO OUTPUT DIR
shutil.copytree(pathToInputDir, pathToOutputDir)

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)


# xt-setup-unit-testing-files-and-folders


class test_soxs_scheduler(unittest.TestCase):

    def test_soxs_scheduler_createAutoOB_function(self):

        from marshallEngine.services import soxs_scheduler
        schd = soxs_scheduler(
            log=log,
            settings=settings
        )
        schd.createAutoOB(transientBucketId=1)

    def test_soxs_scheduler_updateMagnitude_function(self):

        from marshallEngine.services import soxs_scheduler
        schd = soxs_scheduler(
            log=log,
            settings=settings
        )
        schd.updateMagnitude(transientBucketId=1)

    def test_soxs_scheduler_createFollowupOB_function(self):

        from marshallEngine.services import soxs_scheduler
        schd = soxs_scheduler(
            log=log,
            settings=settings
        )
        schd.createFollowupOB(transientBucketId=1)

    def test_soxs_scheduler_deleteOB_function(self):

        from marshallEngine.services import soxs_scheduler
        schd = soxs_scheduler(
            log=log,
            settings=settings
        )
        schd.deleteOB(OB_ID=1)

    def test_soxs_scheduler_function_exception(self):

        from marshallEngine.services import soxs_scheduler
        try:
            schd = soxs_scheduler(
                log=log,
                settings=settings,
                fakeKey="break the code"
            )
            schd.createAutoOB()
            assert False
        except Exception as e:
            assert True
            print(str(e))

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
