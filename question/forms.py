from django import forms
from question.models import Choice, Question, Question5, Choice5, Question4, Choice4, Choice3, Question3, Question2, \
    Choice2, Question6, Choice6


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'answer', 'question_category')


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('fault', 'choice_to')


class QuestionForm2(forms.ModelForm):
    class Meta:
        model = Question2
        fields = ('question', 'answer', 'question_category')


class ChoiceForm2(forms.ModelForm):
    class Meta:
        model = Choice2
        fields = ('fault', 'choice_to')


class QuestionForm3(forms.ModelForm):
    class Meta:
        model = Question3
        fields = ('question', 'answer', 'question_category')


class ChoiceForm3(forms.ModelForm):
    class Meta:
        model = Choice3
        fields = ('fault', 'choice_to')


class QuestionForm4(forms.ModelForm):
    class Meta:
        model = Question4
        fields = ('question', 'answer', 'question_category')


class ChoiceForm4(forms.ModelForm):
    class Meta:
        model = Choice4
        fields = ('fault', 'choice_to')


class QuestionForm5(forms.ModelForm):
    class Meta:
        model = Question5
        fields = ('question', 'answer', 'question_category')


class ChoiceForm5(forms.ModelForm):
    class Meta:
        model = Choice5
        fields = ('fault', 'choice_to')


class QuestionForm6(forms.ModelForm):
    class Meta:
        model = Question6
        fields = ('question', 'answer', 'question_category')


class ChoiceForm6(forms.ModelForm):
    class Meta:
        model = Choice6
        fields = ('fault', 'choice_to')
