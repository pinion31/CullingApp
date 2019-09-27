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
    template_name = 'quiz/list_quiz.html'
    context_object_name = 'quiz_all'
    #ordering = ['-date_posted']

class QuestionListView(ListView):
    model = Question
    template_name = 'quiz/list_question.html'
    context_object_name = 'question_all'
    #ordering = ['-date_posted']

class QuestionCreateView(CreateView):
    model = Question 
    template_name = 'quiz/create_question.html'
    questions = []

    context = {
        'questions': questions,
        'quiz': None,
        'ques_pk': None,
        'answers': [],
    }

    def post(self, request, pk, context=context):
        context['ques_pk'] = pk
        print(f"quiz is {context['quiz']}")
        if context['quiz'] == None:
            context['quiz'] = Quiz.objects.get(pk=pk)
            print("context['quiz']")
            print(context['quiz'])
            # throw error here if quiz is blank

        if request.POST.get('question_text'):
            print('path1')
            context['questions'].append(request.POST.get('question_text'))
            return render(request, 'quiz/create_question.html', context)
        elif request.POST.get('answer_text'):
            print('path2')
            question_index = int(request.path.split('/')[3])
            context["answers"].append((question_index, request.POST.get('answer_text')))
            return render(request, 'quiz/create_question.html', context)
        else:
            print('quiz created')
            print(context['questions'])
            #create quiz
            for index, question in enumerate(context['questions']):
                answer_set_to_add = []
                for answer in context['answers']:
                    if answer[0] == index:
                        answer_set_to_add.append(answer)
                Question.objects.create(
                    quiz_parent=context['quiz'],
                    question=question,
                    answers=answer_set_to_add,
                    correct_answer='temp answer',
                )
            return render(request, 'quiz/create_quiz.html')
            # quiz_parent = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
            # question = models.TextField(null=False)
            # correct_answer = models.TextField(null=False)
            # answers= ArrayField(models.TextField(null=False), default=[])
            #create question and add answers
            # add link from question and quiz
            return render(request, 'quiz/create_quiz.html', context)

    def get(self, request, pk, context=context):
        quiz = Quiz.objects.get(pk=pk)
        context['quiz'] = quiz
        print('path3')
        return render(request, 'quiz/create_question.html', context)

class QuizCreateView(CreateView):
    model = Quiz
    template_name = 'quiz/create_quiz.html'
    fields = ['name']

    def post(self, request):
        created_quiz = Quiz.objects.create(name=request.POST.get('quiz_name'),owner=None)
        return redirect(f"create-question/{created_quiz.id}")

    # def get(request):
    #     quiz_all = Quiz.objects.all()
    #     return render(request, 'quiz/list_quiz.html', {'quiz_all': quiz_all})
    


# class QuizCreateView(CreateView):
#     model = Quiz
#     template_name = 'quiz/create_quiz.html'
#     fields = ['name']
#     questions = []

#     # def get(request):
#     #     quiz_all = Quiz.objects.all()
#     #     return render(request, 'quiz/list_quiz.html', {'quiz_all': quiz_all})
    
#     def post(self, request, questions = questions):
#         print(request)
#         #quiz_name = ''

#         context = {
#             'questions': questions,
#         }

#         if (request.POST.get('question_name')):
#             questions.append(request.POST.get('question_name'))
#             print(questions)
#             # print(request.GET.get('index'))
#             return render(request, 'quiz/create_quiz.html', context)
#         # if request.POST['quiz_name']:
#         #     Quiz.objects.create(name=request.POST['quiz_name'],owner=None)
#         #     return redirect("view-quiz")
#         # elif request.POST['question_name']:
#         #     pass
#         # Quiz.objects.create(name=request.POST['quiz_name'],owner=None)
#         return redirect("view-quiz")

