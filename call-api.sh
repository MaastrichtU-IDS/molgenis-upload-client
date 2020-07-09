TOKEN=$(curl -H "Content-Type: application/json" -X POST -d '{"username"="", "password"=""}' https://molgenis07.gcc.rug.nl/api/v1/login)
TOKEN=$(echo $TOKEN | jq '.token' | tr -d '"')
echo $TOKEN
REPONSE=$(curl -H "x-molgenis-token:$TOKEN" -X POST -F"file=@RD3 data model_exported from Molgenis 2020-06-04.xlsx" -Faction=ADD_UPDATE -Fnotify=true https://molgenis07.gcc.rug.nl/plugin/importwizard/importFile)
echo $RESPONSE

curl --location --request POST 'https://molgenis07.gcc.rug.nl/plugin/importwizard/importFile' \
--header 'Authorization: Bearer $TOKEN' \
--form 'file=@RD3 data model_exported from Molgenis 2020-06-04.xlsx' \
--form 'action=ADD_UPDATE_EXISTING' \
--form 'notify=true'