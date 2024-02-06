from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Teacher
from .forms import TeacherForm
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'home.html')

def show_all_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'show_all_teachers.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_all_teachers')
    else:
        form = TeacherForm() 
    return render(request, 'add_teacher.html', {'form': form})

def filter_teachers(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        number_of_classes = request.POST.get('numberofclass')

        filtered_teachers = Teacher.objects.filter(
            age__icontains=age,
            Numberofclasses__icontains=number_of_classes
        )
        return render(request, 'filtered_teachers.html', {'teachers': filtered_teachers})

    return render(request, 'filtered_teachers.html')


def update_teacher(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        teacher = get_object_or_404(Teacher, employee_id=employee_id)

        if 'name' in request.POST and request.POST['name']:
            teacher.name = request.POST['name']
        if 'dob' in request.POST and request.POST['dob']:
            teacher.date_of_birth = request.POST['dob']
        if 'age' in request.POST and request.POST['age']:
            teacher.age = int(request.POST['age'])
        if 'noofclasses' in request.POST and request.POST['noofclasses']:
            teacher.Numberofclasses = int(request.POST['noofclasses'])
        if 'designation' in request.POST and request.POST['designation']:
            teacher.designation = request.POST['designation']
        if 'salary' in request.POST and request.POST['salary']:
            teacher.salary = request.POST['salary']
        if 'experience' in request.POST and request.POST['experience']:
            teacher.experience = int(request.POST['experience'])
        if 'work' in request.POST and request.POST['work']:
            teacher.work = request.POST['work']
        if 'classtaking' in request.POST and request.POST['classtaking']:
            teacher.classtaking = request.POST['classtaking']
        if 'major' in request.POST and request.POST['major']:
            teacher.major = request.POST['major']

        try:
            teacher.full_clean() 
            teacher.save()
            return HttpResponse('<p>Teacher details updated successfully</p>')
        except ValidationError as e:
            error_message = ", ".join([f"{field}: {error[0]}" for field, error in e.message_dict.items()])
            return HttpResponse(f'<p>Error updating teacher details: {error_message}</p>')
    return render(request, 'update_teacher.html')

def search_teacher(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee_id')
        name = request.POST.get('name')
        if employee_id and name:
            try:
                teacher = Teacher.objects.get(employee_id=employee_id, name=name)
                return render(request, 'teacher_details.html', {'teacher': teacher})
            except Teacher.DoesNotExist:
                error = "Teacher with the provided ID and name does not exist."
                return render(request, 'search_teacher.html', {'error': error})
        else:
            error = "Please provide both the employee ID and name."
            return render(request, 'search_teacher.html', {'error': error})
    else:
        return render(request, 'search_teacher.html')

def delete_record(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        name = request.POST.get('name')
        dob = request.POST.get('dateofbirth')

        if employee_id and name and dob:
            try:
                teacher = Teacher.objects.get(employee_id=employee_id, name=name, date_of_birth=dob)
                teacher.delete()
                return HttpResponse('<p>Record deleted successfully</p>')
            except Teacher.DoesNotExist:
                return HttpResponse('<p>Teacher not found</p>')
        else:
            return HttpResponse('<p>Please provide employee_id, name, and date of birth</p>')
    else:
        return render(request, 'delete_user.html')
    
def Bonustask(request):
    teachers = Teacher.objects.all()
    total_classes = sum(teacher.Numberofclasses for teacher in teachers)
    total_teachers = teachers.count()
    average_classes = total_classes / total_teachers if total_teachers > 0 else 0

    context = {
        'teachers': teachers,
        'average_classes': average_classes
    }
    return render(request, 'teacher_list.html', context)
