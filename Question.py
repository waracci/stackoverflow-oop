# Question model
class Question(object):
    # Empty List to hold the questions asked
    questions_list = []
    # constructor
    def __init__(self, title, description, owner):
        self.title = title
        self.description = description
        self.owner = owner

    # class method to save a question
    def save_question(self, question):
        Question.questions_list.append(question)
        return dict(
            title=Question.questions_list[0].title,
            description=Question.questions_list[0].description,
            owner=Question.questions_list[0].owner
        )
    
     # class method to update questions details
    def update_question(self, question):
        # get the question data from database
        # make the necessary edits
        # save the data back to db
        pass