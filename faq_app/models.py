from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def get_translation(self, lang_code):
        if lang_code == 'hi':
            return self.question_hi or self.question
        elif lang_code == 'bn':
            return self.question_bn or self.question
        return self.question

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
