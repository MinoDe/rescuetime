import datetime

from rescuetime.api.service.Service import Service
from rescuetime.api.access.AnalyticApiKey import AnalyticApiKey
from rescuetime.api.model.ResponseData import ResponseData

url = 'https://www.rescuetime.com'

class Request(object):

    def __init__(self, key):
        self.service = Service(url)
        self.key = AnalyticApiKey(key, self.service)
        self.r = ResponseData(self.key)

    def params(self, **kwargs):
        for k,v in kwargs.items():
            if isinstance(v, datetime.datetime) or isinstance(v, datetime.date):
                v = v.strftime('%Y-%m-%d')
            self.r.params(**{k:v})
        return self

    def request(self, **kwargs):
        self.params(**kwargs)
        print 'Making request...\n'
        print self.r._parameters
        self.r.sync()
        return self.r.object



if __name__ == '__main__':
    today = datetime.date.today()

    r = Request('B63p8QeY8a2Qa1VFblAKkEXBsCezhNZAJU9oX0rI')
    r.params(operation='select', perspective='interval')
    r.params(version="0",
             restrict_begin=(today - datetime.timedelta(weeks = 1)),
             restrict_end=datetime.datetime(2012, 7, 12),
             restrict_kind='productivity')
    r.params(resolution_time='hour')
    data = r.request()
    print data
