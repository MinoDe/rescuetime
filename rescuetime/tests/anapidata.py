import sys
import datetime
from unittest import TestCase

from rescuetime.tests.data import url, key
from rescuetime.api.service.Service import Service
from rescuetime.api.access.AnalyticApiKey import AnalyticApiKey
from rescuetime.api.model.ResponseData import ResponseData

class TestApiData(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

    def runTest(self):
        pass

    def setUp(self):
        pass

    def teddst1(self):
        s = Service(url)
        s.debug(s.server_loc)
        k = AnalyticApiKey(key, s)
        s.debug('exists: ' + unicode(k.exists()))
        r = ResponseData(k, {'op': 'select',
                             'vn': 0,
                             'pv': 'rank',
                             'rb': (datetime.date.today() - datetime.timedelta(weeks = 1)).strftime('%Y-%m-%d'),
                             're': datetime.date.today().strftime('%Y-%m-%d'),
                             'rk': 'overview'
                             })
        r.sync()
        s.debug('data object: ' + unicode(r.object))
        s.debug('=============')
        for k in r.object:
            s.debug("\n\tkey: %s\n\tvalue:%s\n-------\n" % (unicode(k), unicode(r.object[k])))
            if k == 'rows':
                for ro in r.object[k]:
                    s.debug("\n\t\trow(%d): %s\n-------\n" % (len(ro), unicode(ro)))

    def test2(self):
        s = Service(url)
        s.debug(s.server_loc)
        k = AnalyticApiKey(key, s)
        s.debug('exists: ' + unicode(k.exists()))
        r = ResponseData(k)
        today = datetime.date.today()
        r.params(operation = 'select').params(perspective = 'interval')
        r.params(version = 0,
                 restrict_begin = (today - datetime.timedelta(weeks = 1)).strftime('%Y-%m-%d'),
                 restrict_end = today.strftime('%Y-%m-%d'),
                 restrict_kind = 'productivity')
        r.params(resolution_time='hour')

        r.sync()
        s.debug('data object: ' + unicode(r.object))
        s.debug('=============')
        for k in r.object:
            s.debug("\n\tkey: %s\n\tvalue:%s\n-------\n" % (unicode(k), unicode(r.object[k])))
            if k == 'rows':
                for ro in r.object[k]:
                    s.debug("\n\t\trow(%d): %s\n-------\n" % (len(ro), unicode(ro)))

if __name__ == '__main__':
    import nose                                                                      
    nose.runmodule(argv=[__file__,'-vvs','-x','--pdb', '--pdb-failure'],exit=False)   
