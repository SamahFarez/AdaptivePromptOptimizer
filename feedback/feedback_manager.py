# feedback/feedback_manager.py
class FeedbackManager:
    def __init__(self):
        self.feedback_scores = {"positive": 0, "negative": 0}
        
    def record_feedback(self, is_positive):
        if is_positive:
            self.feedback_scores["positive"] += 1
        else:
            self.feedback_scores["negative"] += 1
            
    def get_feedback_scores(self):
        return self.feedback_scores
