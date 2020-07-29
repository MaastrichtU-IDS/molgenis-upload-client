import os
from typing import Dict

import molgenis.client
import yaml
from logger.logger import log
from package_creator import packager

class App(object):
    config = Dict

    def __init__(self):
        log.debug("Loading configuration.")
        with open("application.yml", 'r') as stream:
            try:
                self.config = yaml.safe_load(stream)
                log.debug(self.config)
            except yaml.YAMLError as exc:
                log.error("Error parsing configuration.", exc)

    def upload_emx_file(self):
        filename = os.path.basename(self.config['data']['csv-folder-location']) + ".zip"
        packager.create_package(self.config['data']['csv-folder-location'], filename)
        session = molgenis.client.Session(self.config['molgenis']['url'])
        session.login(self.config['molgenis']['credentials']['username'],
                      self.config['molgenis']['credentials']['password'])
        response = session.upload_zip(filename)
        print(response)

        # my_table = session.get("rd3_disease")
        # print(my_table)
        # result = session.add('aaaac4zs4cruh6qwhzgo3eqaae',id=3, label='uploaded entity 2')
        # print(result)
