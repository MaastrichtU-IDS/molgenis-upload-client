# Molgenis Upload  Client
Molgenis upload client for the BReIN project

### Run Molgenis Upload Client
In the *application.yml*, update the url of molgenis and the credentials according to your molgenis install (or run the Molgenis docker-compose and add user *user/password* to use the defaults). At the moment, only an *upload* function exists.

``` 
pip install -e .
```

``` 
molgenis_upload_client upload
```

*Upload* packages the BReIN datamodel as a ZIP file and offers them to the Molgenis API.
