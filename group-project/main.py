
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

class SubmitHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = { 'name_of_game': self.request.get('game') }
        template = env.get_template('submit.html')
        self.response.out.write(template.render(template_vars))
    def post(self):
        results_template = env.get_template('submit.html')
        template_variables = {
            'q1':self.request.get("q1"),
            }
        self.response.out.write(results_template.render(template_variables))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', MainHandler),
    ('/ventbot', VentHandler),
    ('/quiz', QuizHandler),
    ('/chillroom', RoomHandler),
    ('/resources', ResourceHandler),
    ('/submit', SubmitHandler)
    ], debug=True)
