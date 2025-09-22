from django.shortcuts import render, HttpResponse
from .forms import AccountForm, StudentForm, OwnerForm, CarForm, BookForm, AuthorForm, BorrowForm
from .models import Student, Account, Owner, Car, Author, Book, Borrow

# def studentAccount(request):
#     accountform=AccountForm()
#     studentform=StudentForm()
#     if request.method=='POST':
#         accountform=AccountForm(request.POST)
#         studentform=StudentForm(request.POST)
#         idSave=studentform.save()
#         # accountform.student_id=idSave.id
#         # delete=Student.objects.all().delete()
#         accountform.save()

#         # accountform.save(commit=False)
#         if accountform.is_valid and studentform.is_valid:
#             id_acc=accountform.cleaned_data['id']
#             password=accountform.cleaned_data['password']
#             email=accountform.cleaned_data['email']
#             studenName=studentform.cleaned_data['name']
#             return HttpResponse(f'name: {studenName}, id: {id_acc}, password: {password}, email: {email}')
#     else:
#         return render(request, 'index.html', {'accountform':accountform, 'studentform':studentform})

def ownerCar(request):
    ownerForm=OwnerForm()
    carForm=CarForm()
    if request.method=='POST':
        ownerForm=OwnerForm(request.POST)
        carForm=CarForm(request.POST)
        idSave=ownerForm.save()
        carForm.owner_id=idSave.name

        carForm.owner_id=idSave!!!

        # delete=Owner.objects.all().delete()
        carForm.save()

        if ownerForm.is_valid and carForm.is_valid:
            brand=carForm.cleaned_data['brand']
            color=carForm.cleaned_data['color']
            speed=carForm.cleaned_data['speed']
            ownerName=ownerForm.cleaned_data['name']
            return HttpResponse(f'name: {ownerName}, brand car: {brand}, color: {color}, speed: {speed}')
    else:
        return render(request, 'index.html', {'accountform':ownerForm, 'studentform':carForm})


# def authorBook(request):
#     bookForm=BookForm()
#     authorForm=StudentForm()
#     borrowForm=BorrowForm()
#     if request.method=='POST':
#         bookForm=BookForm(request.POST)
#         authorForm=AuthorForm(request.POST)
#         borrowForm=BorrowForm(request.POST)
#         idSaveBook=bookForm.save()
#         idSaveAuthor=authorForm.save()
#         borrowForm.author_id=idSaveAuthor.id
#         borrowForm.book_id=idSaveBook.id
#         # delete=Student.objects.all().delete()
#         borrowForm.save()
#         if bookForm.is_valid and authorForm.is_valid and borrowForm.is_valid:
#             borrow_date=borrowForm.cleaned_data['borrow_date']
#             published_year=bookForm.cleaned_data['published_year']
#             return_date=borrowForm.cleaned_data['return_date']
#             authorName=authorForm.cleaned_data['name']
#             bookName=bookForm.cleaned_data['name']
#             return HttpResponse(f'name: {authorName}, bookName: {bookName}, published_year: {published_year}, borrow_date: {borrow_date},  return_date: {return_date}')
#     else:
#         return render(request, 'authorBook.html', {'bookForm':bookForm, 'authorForm':authorForm, 'borrowForm':borrowForm})
    
 

    # Вопросы:
    # inlineformset_factory
    # instance in save()
    # betterforms
    # return super().execute