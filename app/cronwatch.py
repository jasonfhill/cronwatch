import cherrypy
from utils import secure_filename

cherrypy.config.update(
    {'server.socket_host': '0.0.0.0',
     'server.socket_port': 57655})


class Main(object):
    usage = "Nothing to see here."

    @cherrypy.expose
    def index(self):
        return self.usage

    @cherrypy.expose
    def cron(self, crontab=None, user=None):
        file = None

        if crontab:
            crontab = secure_filename(crontab)
            file = '/'.join(['/etc/cron.d', crontab])
        if user:
            user = secure_filename(user)
            file = '/'.join(['/var/spool/cron/crontabs', user])

        if file:
            try:
                with open(file, 'r') as f:
                    read_data = '<html><body><pre>' + f.read() + \
                                '</pre></body></html>'
                    output = read_data
                    output.replace(' ', '&nbsp;').replace('\n', '<br>')

            except (OSError, IOError):
                output = '<html><body>File not found: %s </body></html>' % file

            return output

        else:
            return self.usage

cherrypy.quickstart(Main())