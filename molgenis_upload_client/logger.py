import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
log = logging.getLogger("molgenis_upload_client")
