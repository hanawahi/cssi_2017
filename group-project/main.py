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

#Resources

class ResourceHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('info.html')
        self.response.out.write(template.render())

class DrugsHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('drugs.html')
        self.response.out.write(template.render())

class DepressionHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('depression.html')
        self.response.out.write(template.render())

class AnxiousHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('anxious.html')
        self.response.out.write(template.render())

class EatingHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('eating_disorder.html')
        self.response.out.write(template.render())
#####

def second(pair):
    return pair[1]



class SubmitHandler(webapp2.RequestHandler):
    def post(self):
        results_template = env.get_template('submit.html')

        quiz_results_dict = {}

        for i in range(1,10):
            value = self.request.get("q"+str(i))
            if value in quiz_results_dict:
                quiz_results_dict[value] +=1
            else:
                quiz_results_dict[value] = 1

        maximum = max(quiz_results_dict, key=quiz_results_dict.get)
        sorted_quiz_results_list = sorted(quiz_results_dict.items(), key=second, reverse=True)




        template_variables = {
            'common_answer':maximum,
            'quiz_results':sorted_quiz_results_list
        }

        self.response.out.write(results_template.render(template_variables))







app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', MainHandler),
    ('/ventbot', VentHandler),
    ('/quiz', QuizHandler),
    ('/chillroom', RoomHandler),
    ('/info', ResourceHandler),
    ('/submit', SubmitHandler),
    ('/drug_abuse', DrugsHandler),
    ('/depression', DepressionHandler),
    ('/anxious', AnxiousHandler),
    ('/eating_disorder', EatingHandler),

    ], debug=True)
