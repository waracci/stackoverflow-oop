# answer model
class Answer(object):
    # Empty List to hold the answers asked
    answers_list = []
    # constructor
    def __init__(self, title, description, question_id, contributor):
        self.title = title
        self.description = description
        self.question_id = question_id
        self.contributor = contributor

    # class method to save a answer
    def save_answer(self, answer):
        Answer.answers_list.append(answer)
        return dict(
            title=Answer.answers_list[0].title,
            description=Answer.answers_list[0].description,
            question_id=Answer.answers_list[0].question_id,
            contributor=Answer.answers_list[0].contributor
        )
    
     # class method to update answers details
    def update_answer(self, answer):
        # get the answer data from database
        # make the necessary edits
        # save the data back to db
        pass