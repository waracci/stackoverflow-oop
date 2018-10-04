# comment model
class Comment(object):
    # Empty List to hold the comments asked
    comments_list = []
    # constructor
    def __init__(self, title, description, answer_id, contributor):
        self.title = title
        self.description = description
        self.answer_id = answer_id
        self.contributor = contributor

    # class method to save a comment
    def save_comment(self, comment):
        Comment.comments_list.append(comment)
        return dict(
            title=Comment.comments_list[0].title,
            description=Comment.comments_list[0].description,
            answer_id=Comment.comments_list[0].answer_id,
            contributor=Comment.comments_list[0].contributor
        )
    
     # class method to update comments details
    def update_comment(self, comment):
        # get the comment data from database
        # make the necessary edits
        # save the data back to db
        pass