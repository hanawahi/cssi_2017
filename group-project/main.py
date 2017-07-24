
import webapp2
import jinja2

env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


#Welcome Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('welcome.html')
        self.response.out.write(template.render())

#VentBot
class VentHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('ventbot.html')
        self.response.out.write(template.render())

class QuizHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('quizzes.html')
        self.response.out.write(template.render())

class RoomHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('chillroom.html')
        self.response.out.write(template.render())

class ResourceHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('info.html')
        self.response.out.write(template.render())

class MatchHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('listener.html')
        self.response.out.write(template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/ventbot', VentHandler),
    ('/quiz', QuizHandler),
    ('/chillroom', RoomHandler),
    ('/resources', ResourceHandler),
    ('/match', MatchHandler)
    ], debug=True)
