#!/usr/bin/env python
# encoding: utf-8
"""
*Allow the marshall to communicate with the SOXS Scheduler via API calls*

:Author:
    Marco Landoni & David Young

:Date Created:
    July  8, 2020
"""
################# GLOBAL IMPORTS ####################
from builtins import object
import sys
import os
os.environ['TERM'] = 'vt100'
from fundamentals import tools


class soxs_scheduler(object):
    """
    *Allow the marshall to communicate with the SOXS Scheduler via API calls*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary

    **Usage:**

    To setup your logger, settings and database connections, please use the ``fundamentals`` package (`see tutorial here <http://fundamentals.readthedocs.io/en/latest/#tutorial>`_). 

    To initiate a soxs_scheduler object, use the following:

    ```eval_rst
    .. todo::
        - add usage info
        - add a tutorial about ``soxs_scheduler`` to documentation
    ```

    ```python
    usage code 
    ```

    """

    def __init__(
            self,
            log,
            settings=False,

    ):
        self.log = log
        log.debug("instansiating a new 'soxs_scheduler' object")
        self.settings = settings

        return None

    def createAutoOB(
            self,
            transientBucketId):
        """*Create OB in the scheduler for the first time*

        **Key Arguments:**
            - ``transientBucketId`` -- the unique ID of the transient in the marshall

        **Return:**
            - ``OB_ID`` -- the unique ID of the OB from the SOXS scheduler

        **Usage:**

        ```python
        usage code 
        ```

        ---

        ```eval_rst
        .. todo::
            - add usage info
        ```
        """
        self.log.debug('starting the ``createAutoOB`` method')

        self.log.debug('completed the ``createAutoOB`` method')
        return None

    def updateMagnitude(
            self,
            transientBucketId):
        """*Update the magnitude of the transient in the scheduler whenever new photometry has been added to the marshall lightcurve*

        **Key Arguments:**
            - ``transientBucketId`` -- the unique ID of the transient in the marshall

        **Usage:**

        ```python
        usage code 
        ```

        ---

        ```eval_rst
        .. todo::
            - add usage info
        ```
        """
        self.log.debug('starting the ``updateMagnitude`` method')

        self.log.debug('completed the ``updateMagnitude`` method')
        return None

    def createFollowupOB(
            self,
            transientBucketId):
        """*Specify the instrument setup and exptime when requesting followup data from SOXS for a given transient. This is for the OB button on the Marhsall UI.*

        **Key Arguments:**
            - ``transientBucketId`` -- the unique ID of the transient in the marshall

        **Return:**
            - ``OB_ID`` -- the unique ID of the OB from the SOXS scheduler

        **Usage:**

        ```python
        usage code 
        ```

        ---

        ```eval_rst
        .. todo::
            - add usage info
        ```
        """
        self.log.debug('starting the ``createFollowupOB`` method')

        self.log.debug('completed the ``createFollowupOB`` method')
        return None

    def deleteOB(
            self,
            OB_ID):
        """*Remove an OB from the SOXS Scheduler*

        **Key Arguments:**
            - ``OB_ID`` -- the unique ID of the OB in the SOXS scheduler

        **Usage:**

        ```python
        usage code 
        ```

        ---

        ```eval_rst
        .. todo::
            - add usage info
        ```
        """
        self.log.debug('starting the ``deleteOB`` method')

        self.log.debug('completed the ``deleteOB`` method')
        return None
