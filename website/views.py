from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
	return render(request, 'home.html', {})


def about(request):
	return render(request, 'about.html', {})



def patient(request):
	return render(request, 'patients.html', {})



def news(request):
	return render(request, 'news.html', {})


def service(request):
	return render(request, 'services.html', {})



def appoinment(request):
	if request.method == "POST":
		first_name = request.POST['first-name']	
		last_name = request.POST['last-name']
		date = request.POST['date']
		email = request.POST['email']
		treatment = request.POST['treatment']
		print(treatment)
		note = request.POST['note']

		subject =  'Name: ' + first_name+ ' '+ last_name +' ; ' + 'treatment: '+ treatment 
		message =note + ' ; ' + 'Date: ' + str(date) + '; Email ' + email
		context = {
			'first_name':first_name,
			'last_name': last_name,
			'date':date,
			'email':email,
			'treatment':treatment,
			'note':note,
		}

		send_mail(
			subject, # subject
			message,
			email,
			['arifuldesigner2014@gmail.com'],

			)
		return render(request, 'contact.html', context)

			

	else:
		return render(request, 'contact.html', {})		

def contact(request):
	if request.method == "POST":
		fullname = request.POST['fullname']	
		
		email = request.POST['email']
		message= request.POST['message']


		send_mail(
			fullname, # subject
			message,
			email,
			['arifuldesigner2014@gmail.com'],

			)
		return render(request, 'contact.html', {})
	else:
		return render(request, 'contact.html', {})		




