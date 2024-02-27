from models.gemini import Gemini
from models.gpt4turbo import Gpt4Turbo

MODELS_DIC = {'gemini': Gemini(), 'gpt4turbo': Gpt4Turbo()}

class Models():
    def __init__(self, model_nane=''):
        if not model_nane:
            model_nane = 'gemini'
        self.model_name = model_nane
        self.m = MODELS_DIC[model_nane]

    def text(self, question):
        return self.m.text(question)

    def vision(self, question, imgs):
        return self.m.vision(question, imgs)
