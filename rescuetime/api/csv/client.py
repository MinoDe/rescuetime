import mechanize

CSV_URL = 'https://www.rescuetime.com/browse/productivity/by/hour/for/the/day/of/%s.csv'
LOGIN_URL = 'https://rescuetime.com/login'

def get_day(br, date):
    url = CSV_URL % date.strftime('%Y-%m-%d')
    resp = br.open(url)
    return resp

class RescueTime(object):
    def __init__(self):
        self.logged_in = False
        self.br = mechanize.Browser()
        self.cj = mechanize.CookieJar()
        self.br.set_cookiejar(self.cj)
        self.br.set_handle_refresh(False)

        self.br.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64; \
                               rv:13.0) Gecko/20100101 Firefox/13.0.1')]

    def login(self, email, password):
        self.br.open(LOGIN_URL)
        self.br.select_form(nr=0)
        self.br['email'] = email
        self.br['password'] = password
        self.br.submit()
        self.logged_in = True

    def get_day(self, date):
        url = CSV_URL % date.strftime('%Y-%m-%d')
        resp = self.br.open(url)
        return resp
