import sys
from unittest import TestCase

from rescuetime.tests.data import url, key 

from rescuetime.api.service.Service import Service
from rescuetime.api.access.AnalyticApiKey import AnalyticApiKey

class TestApiKey(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

    def runTest(self):
        pass

    def setUp(self):
        pass

    def test1(self):
        s = Service(url)
        s.debug(s.server_loc)
        k = AnalyticApiKey(key, s)
        s.debug('exists: ' + unicode(k.exists()))


    def test2(self):
        s = Service(url)
        s.debug(s.server_loc)
        k = AnalyticApiKey(key, s)
        k.exists()
        s.debug('exists: ' + unicode(k.exists()))


if __name__ == '__main__':                                                                                          
    import nose                                                                      
    nose.runmodule(argv=[__file__,'-vvs','-x','--pdb', '--pdb-failure'],exit=False)   
