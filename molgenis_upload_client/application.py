import molgenis.client


class App(object):

    def __init__(self):
        pass

    def test(self):
        session = molgenis.client.Session("https://molgenis07.gcc.rug.nl/api/")
        session.login("","")
        my_table = session.get("testentityid")
        print(my_table)
