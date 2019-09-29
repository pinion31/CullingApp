from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Question, Quiz
# Create your views here.
class QuizListView(ListView):
    model = Quiz
    #template_name = 'quiz/list_quiz.html'
    #context_object_name = 'quiz_all'
    #ordering = ['-date_posted']
    context = {
        'quiz_all': None,
    }

    def get(self, request, context=context):
        context['quiz_all'] = Quiz.objects.filter(owner_id=request.user.id)
        return render(request, 'quiz/list_quiz.html', context)


class QuestionListView(ListView):
    model = Question
    template_name = 'quiz/list_question.html'
    context_object_name = 'question_all'
    #ordering = ['-date_posted']

class QuestionCreateView(CreateView):
    model = Quiz
    template_name = 'quiz/create_question.html'

    context = {
        'question': '',
        'quiz': None,
        'ques_pk': None,
        'answers': [],
        'ques_created': False,
        'answers_created': False,
        'correct_answer':'',
        'choose_answer_mode': False,
    }

    def post(self, request, pk, context=context):
        context['ques_pk'] = pk
        if context['quiz'] == None:
            context['quiz'] = Quiz.objects.get(pk=pk)
            
        if request.POST.get('question_text'):
            context['question'] = request.POST.get('question_text')
            context['ques_created'] = True
        elif request.POST.get('answer_text'):
            context['answers'].append(request.POST.get('answer_text'))
            context['answers_created'] = True
        else:
            #submit quiz and answers
            if context['choose_answer_mode'] == False:
                context['choose_answer_mode'] = True
                return render(request, 'quiz/create_question.html', context)
            if request.POST.get('correct_answer'):
                context['correct_answer'] = request.POST.get('correct_answer') 
                Question.objects.create(
                    quiz_parent=context['quiz'],
                    question=context['question'],
                    answers=context['answers'],
                    correct_answer= context['correct_answer'],
                )
                self.resetContext(context)
                return redirect('create-quiz', pk=pk)
        return render(request, 'quiz/create_question.html', context)

    def resetContext(self, context=context):
        context = {
            'question': '',
            'quiz': None,
            'ques_pk': None,
            'answers': [],
            'ques_created': False,
            'answers_created': False,
            'correct_answer':'',
            'choose_answer_mode': False,
        }
        print(context)

    def get(self, request, pk, context=context):
        context['ques_pk'] = pk
        quiz = Quiz.objects.get(pk=pk)
        context['quiz'] = quiz
        return render(request, 'quiz/create_question.html', context)

class QuizCreateView(CreateView):
    model = Question 
    template_name = 'quiz/create_quiz.html'

    context = {
        'questions': False,
        'quiz': None,
        'ques_pk': None,
        'answers': [],
    }

    def get(self, request, pk, context=context):
        created_questions = Question.objects.filter(quiz_parent_id=pk)
        print(created_questions)
        context['ques_pk'] = pk
        context['questions'] = created_questions
        if context['quiz'] == None:
            context['quiz'] = Quiz.objects.get(pk=pk)
            # throw error here if quiz is blank

        
        return render(request, 'quiz/create_quiz.html', context)

    # def post(self, request, pk, context=context):
    #     context['ques_pk'] = pk
    #     if context['quiz'] == None:
    #         context['quiz'] = Quiz.objects.get(pk=pk)
    #         # throw error here if quiz is blank

    #     if request.POST.get('question_text'):
    #         context['questions'].append(request.POST.get('question_text'))
    #         return render(request, 'quiz/create_question.html', context)
    #     elif request.POST.get('answer_text'):
    #         question_index = int(request.path.split('/')[3])
    #         context["answers"].append((question_index, request.POST.get('answer_text')))
    #         return render(request, 'quiz/create_question.html', context)
    #     else:
    #         #submit quiz and answers
    #         for index, question in enumerate(context['questions']):
    #             answer_set_to_add = []
    #             for answer in context['answers']:
    #                 if answer[0] == index:
    #                     answer_set_to_add.append(answer)
    #             Question.objects.create(
    #                 quiz_parent=context['quiz'],
    #                 question=question,
    #                 answers=answer_set_to_add,
    #                 correct_answer='temp answer',
    #             )
    #         self.resetContext(context)
    #         return render(request, 'quiz/create_quiz.html')

class QuizNameView(CreateView):
    model = Quiz
    template_name = 'quiz/name_quiz.html'
    fields = ['name']

    def post(self, request):
        created_quiz = Quiz.objects.create(name=request.POST.get('quiz_name'),owner=request.user)
        print(created_quiz.id)
        return redirect(f"create-quiz/{created_quiz.id}")


