from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_view(request):
    return render(request, 'attends/main.html', {})

def result(request):
    print()
    print(request.POST)
    print(request.POST['name'])
    print()
    user_name = request.POST['name']

    return render(request, 'attends/result.html', {'name':user_name})

# def contact_upload(request):
#     # template = 'contact_upload.html'
#
#     prompt = {
#
#     }
#
#     if request.method == 'GET':
#         return render(request, template, prompt)
#
#     csv_file = request.FILES['file']
#     if not csv_file.name.endswith('.csv'):
#         messages.error(request, 'This is not a csv.file')
#
#     data_set = csv_file.read().decode('UTF-8')
#     io_string = io.StringIO(data_set)
#     next(io_string)
#     for column in csv.reader(io_string, delimiter=',', quotechar='|'):
#         _, created = Contact.objects.update_or_create(
#
#         )
