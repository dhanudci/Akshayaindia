import csv
import xlwt
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from PIL import Image
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from akshayaindiawebsite.models import (
    Vacation,
    ItinerarySectionModel,
    GallaryModel,
    VacationCategory,
    VacationService,
    Visa,
    TypesOfVisa,
    Blog,
    Testimonial,
    FAQ,

    VacationEnquiry,
    VisaEnquiry,
    CorporateEnquiry,
    CorporateHeading,
    CorporateIncentives,
    CorporateEvent,

    FlightEnquiry,
    CarEnquiry,
    HotelEnquiry,
    AskQuestionEnquiry,
    ContactUs,
    )

from .forms import (
    BlogAddForm, 
    BlogEditForm,
    TestimonialAddForm,
    TestimonialEditForm,
    FAQAddForm,

    VisaAddForm,
    VisaEditForm,
    TypesOfVisaForm,

    VacationAddForm,
    VacationEditForm,
    ItinerarySectionModelForm,
    GallaryModelForm,

    CorporateHeadingForm,
    CorporateIncentivesForm,
    CorporateEventForm,
)

from django.forms import modelformset_factory, inlineformset_factory
from django.db import transaction, IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def user_login(request):
    context = {}
    username = password = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('Dashboard:home'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "akshayaindia-dashboad/index.html", context)
    else:
        return render(request, "akshayaindia-dashboad/index.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Dashboard:login'))

@login_required(login_url="Dashboard:login")
def home(request):
	context = {}
	
	visa_enquiry_objects = VisaEnquiry.objects.all()
	vacation_enquiry_objects = VacationEnquiry.objects.all()
	corporate_enquiry_objects = CorporateEnquiry.objects.all()

	enquiry_models_list = [
		VacationEnquiry,
		VisaEnquiry,
		CorporateEnquiry,
		FlightEnquiry,
		CarEnquiry,
		HotelEnquiry,
		AskQuestionEnquiry,
		ContactUs,
	]

	pending_counts = 0
	process_counts = 0
	resolved_counts = 0
	for model in enquiry_models_list:
		pending_counts += model.objects.filter(status="Pending").count()
		process_counts += model.objects.filter(status="Process").count()
		resolved_counts += model.objects.filter(status="Resolved").count()

	total_enquiry = pending_counts + process_counts + resolved_counts

	if pending_counts == 0 and process_counts == 0 and resolved_counts == 0:
		pending_percentage = 0.0
		process_percentage = 0.0
		resolved_percentage = 0.0
	else:
		pending_percentage = pending_counts/total_enquiry*100;
		process_percentage = process_counts/total_enquiry*100;
		resolved_percentage = resolved_counts/total_enquiry*100;

	context['visas'] = visa_enquiry_objects
	context['vacations'] = vacation_enquiry_objects
	context['corporates'] = corporate_enquiry_objects
	context['pending_percentage'] = round(pending_percentage,2)
	context['process_percentage'] = round(process_percentage,2)
	context['resolved_percentage'] = round(resolved_percentage,2)
	return render(request, 'akshayaindia-dashboad/home.html', context)

@login_required(login_url="Dashboard:login")
def india(request):
	context = {}
	# india_hero_list = Vacation.objects.filter(tour_type='India', hero_tour=True).order_by('position')
	india_vacation_list = Vacation.objects.filter(tour_type='India').order_by('position')
	page = request.GET.get('page', 1)
	paginator = Paginator(india_vacation_list, 20)
	try:
		india_vacation_list = paginator.page(page)
	except PageNotAnInteger:
		india_vacation_list = paginator.page(1)
	except EmptyPage:
		india_vacation_list = paginator.page(paginator.num_pages)
	context['india_vacation_list'] = india_vacation_list
	# context['india_hero_list'] = india_hero_list
	return render(request, 'akshayaindia-dashboad/pages/CMS/Vacations/cmsIndia.html',context)


@login_required(login_url="Dashboard:login")
def vacation_india_add(request):
	context = {}
	ItinerarySectionModelFormset = modelformset_factory(ItinerarySectionModel, form=ItinerarySectionModelForm)
	GallaryModelFormset = modelformset_factory(GallaryModel, form=GallaryModelForm, max_num=8, min_num=8, extra=8)

	formset1 = ItinerarySectionModelFormset(request.POST or None, queryset=ItinerarySectionModel.objects.none(), prefix='vacation1')
	formset2 = GallaryModelFormset(request.POST or None, request.FILES or None, queryset=GallaryModel.objects.none(), prefix='vacation2')
	
	form = VacationAddForm(request.POST or None, request.FILES or None)
	
	context['form'] = form
	context['formset1'] = formset1
	context['formset2'] = formset2
	if request.method == "POST":
		if form.is_valid() and formset1.is_valid() and formset2.is_valid():
			try:
				with transaction.atomic():
					temp_vacation_position = find_last_position()
					instance = form.save()

					x = request.POST.get('x')
					y = request.POST.get('y')
					w = request.POST.get('width')
					h = request.POST.get('height')

					x1 = request.POST.get('x1')
					y1 = request.POST.get('y1')
					w1 = request.POST.get('width1')
					h1 = request.POST.get('height1')

					x2 = request.POST.get('x2')
					y2 = request.POST.get('y2')
					w2 = request.POST.get('width2')
					h2 = request.POST.get('height2')

					if x and y and w and h:
				
						card_image = Image.open(instance.card_image)
						
						cropped_image = card_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
						resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
						resized_image.save(instance.card_image.path)

					if x1 and y1 and w1 and h1:
						
						banner_image = Image.open(instance.banner_image)
						
						cropped_image = banner_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
						resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
						resized_image.save(instance.banner_image.path)

					if x2 and y2 and w2 and h2:
						
						poster_image = Image.open(instance.poster_image)
						
						cropped_image = poster_image.crop((float(x2), float(y2), float(w2)+float(x2), float(h2)+float(y2)))
						resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
						resized_image.save(instance.poster_image.path)
					

					instance.tour_type = 'India'
					day = instance.day_in_tour
					night = instance.night_in_tour

					instance.position = int(temp_vacation_position) + 1 


					if day == night:
						instance.tour_duration = day
						instance.save()
					elif day > night:
						instance.tour_duration = day
						instance.save()
					else:
						instance.tour_duration = night
						instance.save()
					# instance.save()
					for i in formset1:
						obj = i.save(commit=False)
						obj.vacation = instance
						obj.save()

					for j in formset2:
						data = j.save(commit=False)
						data.vacation = instance
						data.save()

			except IntegrityError:
				print("Error Encounter")
			messages.success(request, "Tour has been saved saccessfully!")
			context['messages'] = messages
			return HttpResponseRedirect(reverse('Dashboard:india'), context)
	return render(request, 'akshayaindia-dashboad/pages/CMS/Vacations/cmsAddNewIndiaTour.html',context)


# @login_required(login_url="Dashboard:login")
def find_last_position():
	all_tours = Vacation.objects.all().order_by('position')
	temp_vacation_position = 1
		
	# for set the position
	for tour in all_tours:
		temp_vacation_position = tour.position

	return temp_vacation_position


@login_required(login_url="Dashboard:login")
def vacation_india_edit(request, slug):
	context = {}
	vacation = Vacation.objects.get(slug=slug)
	ItinerarySectionModelFormset = inlineformset_factory(Vacation, ItinerarySectionModel, fields=('heading','description','breakfast','lunch','dinner','stay_in_hotel',), extra=1, can_delete=True)
	GallaryModelFormset = inlineformset_factory(Vacation, GallaryModel, fields=('gallary_image',), max_num=8, min_num=8,can_delete=True)
	if request.method == 'POST':
		form = VacationEditForm(request.POST or None, request.FILES or None, instance=vacation)
		formset1 = ItinerarySectionModelFormset(request.POST or None, instance=vacation)
		formset2 = GallaryModelFormset(request.POST or None, request.FILES or None, instance=vacation)

		if  form.is_valid() and formset1.is_valid() and formset2.is_valid():
			instance = form.save()
			x = request.POST.get('x')
			y = request.POST.get('y')
			w = request.POST.get('width')
			h = request.POST.get('height')

			x1 = request.POST.get('x1')
			y1 = request.POST.get('y1')
			w1 = request.POST.get('width1')
			h1 = request.POST.get('height1')

			x2 = request.POST.get('x2')
			y2 = request.POST.get('y2')
			w2 = request.POST.get('width2')
			h2 = request.POST.get('height2')

			if x and y and w and h:
			
				card_image = Image.open(instance.card_image)
				
				cropped_image = card_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
				resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
				resized_image.save(instance.card_image.path)

			if x1 and y1 and w1 and h1:

				banner_image = Image.open(instance.banner_image)
				
				cropped_image = banner_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
				resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
				resized_image.save(instance.banner_image.path)

			if x2 and y2 and w2 and h2:
						
				poster_image = Image.open(instance.poster_image)
				
				cropped_image = poster_image.crop((float(x2), float(y2), float(w2)+float(x2), float(h2)+float(y2)))
				resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
				resized_image.save(instance.poster_image.path)
			

			day = instance.day_in_tour
			night = instance.night_in_tour

			if day == night:
				instance.tour_duration = day
				instance.save()
			elif day > night:
				instance.tour_duration = day
				instance.save()
			else:
				instance.tour_duration = night
				instance.save()
			formset1.save()
			formset2.save()
			messages.success(request, "Tour has been saved saccessfully!")
			context['messages'] = messages
			return HttpResponseRedirect(reverse("Dashboard:india"), context)
	context['form'] = VacationEditForm(instance=vacation)
	context['formset1'] = ItinerarySectionModelFormset(instance=vacation)
	context['formset2'] = GallaryModelFormset(instance=vacation)
	return render(request, 'akshayaindia-dashboad/pages/CMS/Vacations/cmsEditIndiaTour.html',context)


@login_required(login_url="Dashboard:login")
def international(request):
	context = {}
	# international_hero_list = Vacation.objects.filter(tour_type='International', hero_tour=True).order_by('position')
	international_vacation_list = Vacation.objects.filter(tour_type='International').order_by('position')
	page = request.GET.get('page', 1)
	paginator = Paginator(international_vacation_list, 20)
	try:
		international_vacation_list = paginator.page(page)
	except PageNotAnInteger:
		international_vacation_list = paginator.page(1)
	except EmptyPage:
		international_vacation_list = paginator.page(paginator.num_pages)
	context['international_vacation_list'] = international_vacation_list
	# context['international_hero_list'] = international_hero_list
	return render(request, 'akshayaindia-dashboad/pages/CMS/Vacations/cmsInternational.html',context)

@login_required(login_url="Dashboard:login")
def vacation_international_add(request):
	context = {}
	ItinerarySectionModelFormset = modelformset_factory(ItinerarySectionModel, form=ItinerarySectionModelForm)
	GallaryModelFormset = modelformset_factory(GallaryModel, form=GallaryModelForm, max_num=8, min_num=8, extra=8)

	formset1 = ItinerarySectionModelFormset(request.POST or None, queryset=ItinerarySectionModel.objects.none(), prefix='vacation1')
	formset2 = GallaryModelFormset(request.POST or None, request.FILES or None, queryset=GallaryModel.objects.none(), prefix='vacation2')
	
	form = VacationAddForm(request.POST or None, request.FILES or None)
	
	context['form'] = form
	context['formset1'] = formset1
	context['formset2'] = formset2
	if request.method == "POST":
		if form.is_valid() and formset1.is_valid() and formset2.is_valid():
			try:
				with transaction.atomic():
					temp_vacation_position = find_last_position()
					instance = form.save()

					x = request.POST.get('x')
					y = request.POST.get('y')
					w = request.POST.get('width')
					h = request.POST.get('height')

					x1 = request.POST.get('x1')
					y1 = request.POST.get('y1')
					w1 = request.POST.get('width1')
					h1 = request.POST.get('height1')

					x2 = request.POST.get('x2')
					y2 = request.POST.get('y2')
					w2 = request.POST.get('width2')
					h2 = request.POST.get('height2')


					if x and y and w and h:
						
						card_image = Image.open(instance.card_image)
						
						cropped_image = card_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
						resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
						resized_image.save(instance.card_image.path)

					if x1 and y1 and w1 and h1:
						
						banner_image = Image.open(instance.banner_image)
						
						cropped_image = banner_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
						resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
						resized_image.save(instance.banner_image.path)

					if x2 and y2 and w2 and h2:
						
						poster_image = Image.open(instance.poster_image)
						
						cropped_image = poster_image.crop((float(x2), float(y2), float(w2)+float(x2), float(h2)+float(y2)))
						resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
						resized_image.save(instance.poster_image.path)
						
					instance.tour_type = 'International'
					day = instance.day_in_tour
					night = instance.night_in_tour

					instance.position = int(temp_vacation_position) + 1

					if day == night:
						instance.tour_duration = day
						instance.save()
					elif day > night:
						instance.tour_duration = day
						instance.save()
					else:
						instance.tour_duration = night
						instance.save()
					# instance.save()
					for i in formset1:
						obj = i.save(commit=False)
						obj.vacation = instance
						obj.save()

					for j in formset2:
						data = j.save(commit=False)
						data.vacation = instance
						data.save()
			except IntegrityError:
				print("Error Encounter")
			messages.success(request, "Tour has been saved saccessfully!")
			context['messages'] = messages
			return HttpResponseRedirect(reverse('Dashboard:international'), context)
	return render(request, 'akshayaindia-dashboad/pages/CMS/Vacations/cmsAddNewInternationalTour.html',context)

@login_required(login_url="Dashboard:login")
def vacation_international_edit(request, slug):
	context = {}
	vacation = Vacation.objects.get(slug=slug)
	ItinerarySectionModelFormset = inlineformset_factory(Vacation, ItinerarySectionModel, fields=('heading','description','breakfast','lunch','dinner','stay_in_hotel',), extra=1, can_delete=True)
	GallaryModelFormset = inlineformset_factory(Vacation, GallaryModel, fields=('gallary_image',), max_num=8, min_num=8,can_delete=True)
	if request.method == 'POST':
		form = VacationEditForm(request.POST or None, request.FILES or None, instance=vacation)
		formset1 = ItinerarySectionModelFormset(request.POST or None, instance=vacation)
		formset2 = GallaryModelFormset(request.POST or None, request.FILES or None, instance=vacation)

		if  form.is_valid() and formset1.is_valid() and formset2.is_valid():
			instance = form.save()
			x = request.POST.get('x')
			y = request.POST.get('y')
			w = request.POST.get('width')
			h = request.POST.get('height')

			x1 = request.POST.get('x1')
			y1 = request.POST.get('y1')
			w1 = request.POST.get('width1')
			h1 = request.POST.get('height1')

			x2 = request.POST.get('x2')
			y2 = request.POST.get('y2')
			w2 = request.POST.get('width2')
			h2 = request.POST.get('height2')

			if x and y and w and h:
			
				card_image = Image.open(instance.card_image)
				
				cropped_image = card_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
				resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
				resized_image.save(instance.card_image.path)

			if x1 and y1 and w1 and h1:

				banner_image = Image.open(instance.banner_image)
				
				cropped_image = banner_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
				resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
				resized_image.save(instance.banner_image.path)

			if x2 and y2 and w2 and h2:
						
				poster_image = Image.open(instance.poster_image)
				
				cropped_image = poster_image.crop((float(x2), float(y2), float(w2)+float(x2), float(h2)+float(y2)))
				resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
				resized_image.save(instance.poster_image.path)
			
			day = instance.day_in_tour
			night = instance.night_in_tour

			if day == night:
				instance.tour_duration = day
				instance.save()
			elif day > night:
				instance.tour_duration = day
				instance.save()
			else:
				instance.tour_duration = night
				instance.save()
			formset1.save()
			formset2.save()
			messages.success(request, "Tour has been saved saccessfully!")
			context['messages'] = messages
			return HttpResponseRedirect(reverse("Dashboard:international"), context)
	context['form'] = VacationEditForm(instance=vacation)
	context['formset1'] = ItinerarySectionModelFormset(instance=vacation)
	context['formset2'] = GallaryModelFormset(instance=vacation)
	return render(request, 'akshayaindia-dashboad/pages/CMS/Vacations/cmsEditInternationalTour.html',context)

@login_required(login_url="Dashboard:login")
def cruise(request):
	context = {}
	# cruise_hero_list = Vacation.objects.filter(tour_type='Cruise', hero_tour=True).order_by('position')
	cruise_vacation_list = Vacation.objects.filter(tour_type='Cruise').order_by('position')
	page = request.GET.get('page', 1)
	paginator = Paginator(cruise_vacation_list, 20)
	try:
		cruise_vacation_list = paginator.page(page)
	except PageNotAnInteger:
		cruise_vacation_list = paginator.page(1)
	except EmptyPage:
		cruise_vacation_list = paginator.page(paginator.num_pages)
	context['cruise_vacation_list'] = cruise_vacation_list
	# context['cruise_hero_list'] = cruise_hero_list
	return render(request, 'akshayaindia-dashboad/pages/CMS/Vacations/cmsCruise.html',context)

@login_required(login_url="Dashboard:login")
def vacation_cruise_add(request):
	context = {}
	ItinerarySectionModelFormset = modelformset_factory(ItinerarySectionModel, form=ItinerarySectionModelForm)
	GallaryModelFormset = modelformset_factory(GallaryModel, form=GallaryModelForm, max_num=8, min_num=8, extra=8)

	formset1 = ItinerarySectionModelFormset(request.POST or None, queryset=ItinerarySectionModel.objects.none(), prefix='vacation1')
	formset2 = GallaryModelFormset(request.POST or None, request.FILES or None, queryset=GallaryModel.objects.none(), prefix='vacation2')
	
	form = VacationAddForm(request.POST or None, request.FILES or None)
	
	context['form'] = form
	context['formset1'] = formset1
	context['formset2'] = formset2
	if request.method == "POST":
		if form.is_valid() and formset1.is_valid() and formset2.is_valid():
			try:
				with transaction.atomic():
					temp_vacation_position = find_last_position()
					instance = form.save()

					x = request.POST.get('x')
					y = request.POST.get('y')
					w = request.POST.get('width')
					h = request.POST.get('height')

					x1 = request.POST.get('x1')
					y1 = request.POST.get('y1')
					w1 = request.POST.get('width1')
					h1 = request.POST.get('height1')

					x2 = request.POST.get('x2')
					y2 = request.POST.get('y2')
					w2 = request.POST.get('width2')
					h2 = request.POST.get('height2')

					if x and y and w and h:
						
						card_image = Image.open(instance.card_image)
						
						cropped_image = card_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
						resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
						resized_image.save(instance.card_image.path)

					if x1 and y1 and w1 and h1:
						
						banner_image = Image.open(instance.banner_image)
						
						cropped_image = banner_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
						resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
						resized_image.save(instance.banner_image.path)

					if x2 and y2 and w2 and h2:
						
						poster_image = Image.open(instance.poster_image)
						
						cropped_image = poster_image.crop((float(x2), float(y2), float(w2)+float(x2), float(h2)+float(y2)))
						resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
						resized_image.save(instance.poster_image.path)


					instance.tour_type = 'Cruise'
					day = instance.day_in_tour
					night = instance.night_in_tour

					
					instance.position = int(temp_vacation_position) + 1

					if day == night:
						instance.tour_duration = day
						instance.save()
					elif day > night:
						instance.tour_duration = day
						instance.save()
					else:
						instance.tour_duration = night
						instance.save()
					# instance.save()
					for i in formset1:
						obj = i.save(commit=False)
						obj.vacation = instance
						obj.save()

					for j in formset2:
						data = j.save(commit=False)
						data.vacation = instance
						data.save()
			except IntegrityError:
				print("Error Encounter")
			messages.success(request, "Tour has been saved saccessfully!")
			context['messages'] = messages
			return HttpResponseRedirect(reverse('Dashboard:cruise'), context)
	return render(request, 'akshayaindia-dashboad/pages/CMS/Vacations/cmsAddNewCruiseTour.html',context)

@login_required(login_url="Dashboard:login")
def vacation_cruise_edit(request, slug):
	context = {}
	vacation = Vacation.objects.get(slug=slug)
	ItinerarySectionModelFormset = inlineformset_factory(Vacation, ItinerarySectionModel, fields=('heading','description','breakfast','lunch','dinner','stay_in_hotel',), extra=1, can_delete=True)
	GallaryModelFormset = inlineformset_factory(Vacation, GallaryModel, fields=('gallary_image',), max_num=8, min_num=8,can_delete=True)
	if request.method == 'POST':
		form = VacationEditForm(request.POST or None, request.FILES or None, instance=vacation)
		formset1 = ItinerarySectionModelFormset(request.POST or None, instance=vacation)
		formset2 = GallaryModelFormset(request.POST or None, request.FILES or None, instance=vacation)

		if  form.is_valid() and formset1.is_valid() and formset2.is_valid():
			instance = form.save()
			x = request.POST.get('x')
			y = request.POST.get('y')
			w = request.POST.get('width')
			h = request.POST.get('height')

			x1 = request.POST.get('x1')
			y1 = request.POST.get('y1')
			w1 = request.POST.get('width1')
			h1 = request.POST.get('height1')

			x2 = request.POST.get('x2')
			y2 = request.POST.get('y2')
			w2 = request.POST.get('width2')
			h2 = request.POST.get('height2')

			if x and y and w and h:
			
				card_image = Image.open(instance.card_image)
				
				cropped_image = card_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
				resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
				resized_image.save(instance.card_image.path)

			if x1 and y1 and w1 and h1:

				banner_image = Image.open(instance.banner_image)
				
				cropped_image = banner_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
				resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
				resized_image.save(instance.banner_image.path)


			if x2 and y2 and w2 and h2:
						
				poster_image = Image.open(instance.poster_image)
				
				cropped_image = poster_image.crop((float(x2), float(y2), float(w2)+float(x2), float(h2)+float(y2)))
				resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
				resized_image.save(instance.poster_image.path)
				
			
			day = instance.day_in_tour
			night = instance.night_in_tour

			if day == night:
				instance.tour_duration = day
				instance.save()
			elif day > night:
				instance.tour_duration = day
				instance.save()
			else:
				instance.tour_duration = night
				instance.save()
			formset1.save()
			formset2.save()
			messages.success(request, "Tour has been saved saccessfully!")
			context['messages'] = messages
			return HttpResponseRedirect(reverse("Dashboard:cruise"), context)
	context['form'] = VacationEditForm(instance=vacation)
	context['formset1'] = ItinerarySectionModelFormset(instance=vacation)
	context['formset2'] = GallaryModelFormset(instance=vacation)
	return render(request, 'akshayaindia-dashboad/pages/CMS/Vacations/cmsEditCruiseTour.html',context)

@login_required(login_url="Dashboard:login")
def vacation_delete(request, slug):
	vacation = get_object_or_404(Vacation, slug=slug)

	if vacation.tour_type == 'India':
		vacation.delete()
		return HttpResponseRedirect(reverse('Dashboard:india'))
	if vacation.tour_type == 'International':
		vacation.delete()
		return HttpResponseRedirect(reverse('Dashboard:international'))
	if vacation.tour_type == 'Cruise':
		vacation.delete()
		return HttpResponseRedirect(reverse('Dashboard:cruise'))
	# return render(request, 'Dashboard/CMS/delete.html')


@login_required(login_url="Dashboard:login")
def corporate(request):
	context = {}
	obj = CorporateHeading.objects.all()
	if obj:
		return HttpResponseRedirect(reverse("Dashboard:corporate_edit"))
	else:
		CorporateFormset1 = modelformset_factory(CorporateIncentives, form=CorporateIncentivesForm, max_num=8,min_num=8)
		CorporateFormset2 = modelformset_factory(CorporateEvent, form=CorporateEventForm,max_num=8,min_num=8,extra=8)
		form = CorporateHeadingForm(request.POST or None, request.FILES or None)
		formset1 = CorporateFormset1(request.POST or None, request.FILES or None, prefix='corporate1', )
		formset2 = CorporateFormset2(request.POST or None, request.FILES or None, prefix='corporate2', )
		if request.method == 'POST':
			if form.is_valid() and formset1.is_valid() and formset2.is_valid():
				try:
					with transaction.atomic():
						cor = form.save(commit=False)
						cor.save()

						for i in formset1:
							data1 = i.save(commit=False)
							data1.corporate = cor
							data1.save()

						for j in formset2:
							data2 = j.save(commit=False)
							data2.corporate = cor
							data2.save()

				except IntegrityError:
					print("Error Encountered");
				return HttpResponseRedirect(reverse('Dashboard:corporate_edit'))
		context['formset1'] = formset1
		context['formset2'] = formset2
		context['form'] = form
	return render(request, "akshayaindia-dashboad/pages/CMS/cmsCorporates.html",context)

@login_required(login_url="Dashboard:login")
def corporate_edit(request):
	context = {}
	obj = CorporateHeading.objects.all()
	if obj:
		CorporateFormset1 = inlineformset_factory(CorporateHeading, CorporateIncentives, fields=('heading','heading_image'), max_num=8,min_num=8, can_delete=True)
		CorporateFormset2 = inlineformset_factory(CorporateHeading, CorporateEvent, fields=('heading','heading_image'), max_num=8, min_num=8,can_delete=True)
		if request.method == "POST":
			form = CorporateHeadingForm(request.POST or None, instance=obj[0] or None)
			formset1 = CorporateFormset1(request.POST or None, request.FILES or None, instance=obj[0] or None)
			formset2 = CorporateFormset2(request.POST or None, request.FILES or None, instance=obj[0] or None)
			context['form'] = form
			context['formset1'] = formset1
			context['formset2'] = formset2
			if form.is_valid():
				form.save()
			if formset1.is_valid():

				instance = formset1.save()
				
				x = request.POST.get('x')
				y = request.POST.get('y')
				w = request.POST.get('width')
				h = request.POST.get('height')

				x1 = request.POST.get('x1')
				y1 = request.POST.get('y1')
				w1 = request.POST.get('width1')
				h1 = request.POST.get('height1')

				x2 = request.POST.get('x2')
				y2 = request.POST.get('y2')
				w2 = request.POST.get('width2')
				h2 = request.POST.get('height2')

				x3 = request.POST.get('x3')
				y3 = request.POST.get('y3')
				w3 = request.POST.get('width3')
				h3 = request.POST.get('height3')

				x4 = request.POST.get('x4')
				y4 = request.POST.get('y4')
				w4 = request.POST.get('width4')
				h4 = request.POST.get('height4')

				x5 = request.POST.get('x5')
				y5 = request.POST.get('y5')
				w5 = request.POST.get('width5')
				h5 = request.POST.get('height5')

				x6 = request.POST.get('x6')
				y6 = request.POST.get('y6')
				w6 = request.POST.get('width6')
				h6 = request.POST.get('height6')

				x7 = request.POST.get('x7')
				y7 = request.POST.get('y7')
				w7 = request.POST.get('width7')
				h7 = request.POST.get('height7')

				try:
					
					if instance[0]:

						if x and y and w and h:

							
							heading_image = Image.open(instance[0].heading_image)
							
							cropped_image = heading_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance[0].heading_image.path)
				except(IndexError):
					pass


				try:
					if instance[1]:
						if x1 and y1 and w1 and h1:

							heading_image = Image.open(instance[1].heading_image)
							
							cropped_image = heading_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance[1].heading_image.path)
				except(IndexError):
					pass

				try:
					
					if instance[2]:

						if x2 and y2 and w2 and h2:


							heading_image = Image.open(instance[2].heading_image)
							
							cropped_image = heading_image.crop((float(x2), float(y2), float(w2)+float(x2), float(h2)+float(y2)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance[2].heading_image.path)
				except(IndexError):
					pass
				try:
					if instance[3]:
						if x3 and y3 and w3 and h3:

							heading_image = Image.open(instance[3].heading_image)
							
							cropped_image = heading_image.crop((float(x3), float(y3), float(w3)+float(x3), float(h3)+float(y3)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance[3].heading_image.path)
				except(IndexError):
					pass

				try:
					
					if instance[4]:

						if x4 and y4 and w4 and h4:


							heading_image = Image.open(instance[4].heading_image)
							
							cropped_image = heading_image.crop((float(x4), float(y4), float(w4)+float(x4), float(h4)+float(y4)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance[4].heading_image.path)
				except(IndexError):
					pass
				try:
					if instance[5]:
						if x5 and y5 and w5 and h5:

							heading_image = Image.open(instance[5].heading_image)
							
							cropped_image = heading_image.crop((float(x5), float(y5), float(w5)+float(x5), float(h5)+float(y5)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance[5].heading_image.path)
				except(IndexError):
					pass

				try:
					
					if instance[6]:

						if x6 and y6 and w6 and h6:

							
							heading_image = Image.open(instance[6].heading_image)
							
							cropped_image = heading_image.crop((float(x6), float(y6), float(w6)+float(x6), float(h6)+float(y6)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance[6].heading_image.path)
				except(IndexError):
					pass
				try:
					if instance[7]:
						if x7 and y7 and w7 and h7:

							heading_image = Image.open(instance[7].heading_image)
							
							cropped_image = heading_image.crop((float(x7), float(y7), float(w7)+float(x7), float(h7)+float(y7)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance[7].heading_image.path)
				except(IndexError):
					pass

				for obj in instance:
					obj.save()

			if formset2.is_valid():
			
				instance1 = formset2.save()
			

				x = request.POST.get('x8')
				y = request.POST.get('y8')
				w = request.POST.get('width8')
				h = request.POST.get('height8')
				

				x1 = request.POST.get('x9')
				y1 = request.POST.get('y9')
				w1 = request.POST.get('width9')
				h1 = request.POST.get('height9')

				x2 = request.POST.get('x10')
				y2 = request.POST.get('y10')
				w2 = request.POST.get('width10')
				h2 = request.POST.get('height10')

				x3 = request.POST.get('x11')
				y3 = request.POST.get('y11')
				w3 = request.POST.get('width11')
				h3 = request.POST.get('height11')

				x4 = request.POST.get('x12')
				y4 = request.POST.get('y12')
				w4 = request.POST.get('width12')
				h4 = request.POST.get('height12')

				x5 = request.POST.get('x13')
				y5 = request.POST.get('y13')
				w5 = request.POST.get('width13')
				h5 = request.POST.get('height13')

				x6 = request.POST.get('x14')
				y6 = request.POST.get('y14')
				w6 = request.POST.get('width14')
				h6 = request.POST.get('height14')

				x7 = request.POST.get('x15')
				y7 = request.POST.get('y15')
				w7 = request.POST.get('width15')
				h7 = request.POST.get('height15')
				
				try:
					
					if instance1[0]:

						if x and y and w and h:

							
							heading_image = Image.open(instance1[0].heading_image)
							
							cropped_image = heading_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance1[0].heading_image.path)
				except(IndexError):
					pass


				try:
					if instance1[1]:
						if x1 and y1 and w1 and h1:

							heading_image = Image.open(instance1[1].heading_image)
							
							cropped_image = heading_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance1[1].heading_image.path)
				except(IndexError):
					pass

				try:
					
					if instance1[2]:

						if x2 and y2 and w2 and h2:


							heading_image = Image.open(instance1[2].heading_image)
							
							cropped_image = heading_image.crop((float(x2), float(y2), float(w2)+float(x2), float(h2)+float(y2)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance1[2].heading_image.path)
				except(IndexError):
					pass
				try:
					if instance1[3]:
						if x3 and y3 and w3 and h3:

							heading_image = Image.open(instance1[3].heading_image)
							
							cropped_image = heading_image.crop((float(x3), float(y3), float(w3)+float(x3), float(h3)+float(y3)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance1[3].heading_image.path)
				except(IndexError):
					pass

				try:
					
					if instance1[4]:

						if x4 and y4 and w4 and h4:


							heading_image = Image.open(instance1[4].heading_image)
							
							cropped_image = heading_image.crop((float(x4), float(y4), float(w4)+float(x4), float(h4)+float(y4)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance1[4].heading_image.path)
				except(IndexError):
					pass
				try:
					if instance1[5]:
						if x5 and y5 and w5 and h5:

							heading_image = Image.open(instance1[5].heading_image)
							
							cropped_image = heading_image.crop((float(x5), float(y5), float(w5)+float(x5), float(h5)+float(y5)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance1[5].heading_image.path)
				except(IndexError):
					pass

				try:
					
					if instance[6]:

						if x6 and y6 and w6 and h6:

							
							heading_image = Image.open(instance[6].heading_image)
							
							cropped_image = heading_image.crop((float(x6), float(y6), float(w6)+float(x6), float(h6)+float(y6)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance[6].heading_image.path)
				except(IndexError):
					pass
				try:
					if instance[7]:
						if x7 and y7 and w7 and h7:

							heading_image = Image.open(instance[7].heading_image)
							
							cropped_image = heading_image.crop((float(x7), float(y7), float(w7)+float(x7), float(h7)+float(y7)))
							resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
							resized_image.save(instance[7].heading_image.path)
				except(IndexError):
					pass

				for obj1 in instance1:

					obj1.save()
			return HttpResponseRedirect(reverse("Dashboard:corporate_edit"))	


		form = CorporateHeadingForm(instance=obj[0])
		formset1 = CorporateFormset1(instance=obj[0])
		formset2 = CorporateFormset2(instance=obj[0])
		context['form'] = form
		context['formset1'] = formset1
		context['formset2'] = formset2
	else:
		return HttpResponseRedirect(reverse('Dashboard:corporate'))
	return render(request, "akshayaindia-dashboad/pages/CMS/cmsEditCorporates.html",context)

@login_required(login_url="Dashboard:login")
def visa_list(request):
	context = {}
	visa_list = Visa.objects.all().order_by('-id')
	page = request.GET.get('page', 1)
	paginator = Paginator(visa_list, 10)
	try:
		visa_list = paginator.page(page)
	except PageNotAnInteger:
		visa_list = paginator.page(1)
	except EmptyPage:
		visa_list = paginator.page(paginator.num_pages)
	context['visa_list'] = visa_list
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsVisa.html',context)

@login_required(login_url="Dashboard:login")
def visa_add(request):
	context = {}
	VisaTypeFormset = modelformset_factory(TypesOfVisa, form=TypesOfVisaForm)
	formset = VisaTypeFormset(request.POST or None, queryset=TypesOfVisa.objects.none(), prefix='visa_type')
	form = VisaAddForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid() and formset.is_valid():
			try:
				with transaction.atomic():
					visa = form.save()

					x = request.POST.get('x')
					y = request.POST.get('y')
					w = request.POST.get('width')
					h = request.POST.get('height')

					x1 = request.POST.get('x1')
					y1 = request.POST.get('y1')
					w1 = request.POST.get('width1')
					h1 = request.POST.get('height1')

					if x and y and w and h:
						
						card_image = Image.open(visa.card_image)
						
						cropped_image = card_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
						resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
						resized_image.save(visa.card_image.path)

					if x1 and y1 and w1 and h1:
						
						banner_image = Image.open(visa.banner_image)
						
						cropped_image = banner_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
						resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
						resized_image.save(visa.banner_image.path)
					
					visa.save()
					for i in formset:
						data = i.save(commit=False)
						data.country = visa
						data.save()
			except IntegrityError:
				print("Error Encountered");
			messages.success(request, "Tour has been saved saccessfully!")
			context['messages'] = messages
			return HttpResponseRedirect(reverse('Dashboard:visa_list'), context)
	context['formset'] = formset
	context['form'] = form
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsAddNewVisa.html',context)

@login_required(login_url="Dashboard:login")
def visa_edit(request, slug):
	context = {}
	visa = Visa.objects.get(slug=slug)
	VisaTypeFormset = inlineformset_factory(Visa, TypesOfVisa, fields=('visa_name','processing_time','stay_period','validity','entry','fees'), extra=1, can_delete=True)
	if request.method == 'POST':
		form = VisaEditForm(request.POST or None, request.FILES or None, instance=visa)
		formset = VisaTypeFormset(request.POST or None, instance=visa)
		if formset.is_valid() and form.is_valid():
			visa = form.save()
			x = request.POST.get('x')
			y = request.POST.get('y')
			w = request.POST.get('width')
			h = request.POST.get('height')

			x1 = request.POST.get('x1')
			y1 = request.POST.get('y1')
			w1 = request.POST.get('width1')
			h1 = request.POST.get('height1')


			if x and y and w and h:
				
				card_image = Image.open(visa.card_image)
				
				cropped_image = card_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
				resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
				resized_image.save(visa.card_image.path)

			if x1 and y1 and w1 and h1:
			
				banner_image = Image.open(visa.banner_image)
				
				cropped_image = banner_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
				resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
				resized_image.save(visa.banner_image.path)
			
			visa.save()
			formset.save()
			messages.success(request, "Visa has been saved saccessfully!")
			context['messages'] = messages
			return HttpResponseRedirect(reverse("Dashboard:visa_list"), context)
	formset = VisaTypeFormset(instance=visa)
	form = VisaEditForm(instance=visa)
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsEditVisa.html',{'formset':formset, 'form':form})


@login_required(login_url="Dashboard:login")
def visa_type_delete(request):
	if request.method == "GET" and request.is_ajax():
		visa_type = request.GET.get('visa_type_id')
		visa_type_id = int(visa_type)
		if visa_type_id:
			visa_type = TypesOfVisa.objects.filter(id=visa_type_id).delete()
			if visa_type:
				return JsonResponse({'success':True})
			else:
				return JsonResponse({'error':"Can't Delete"})

@login_required(login_url="Dashboard:login")
def visa_delete(request, slug):
	visa = get_object_or_404(Visa, slug=slug)
	visa.delete()
	return HttpResponseRedirect(reverse('Dashboard:visa_list'))

@login_required(login_url="Dashboard:login")
def blog_list(request):
	context = {}
	blog_list = Blog.objects.all().order_by('-id')
	page = request.GET.get('page', 1)
	paginator = Paginator(blog_list, 6)
	try:
		blog_list = paginator.page(page)
	except PageNotAnInteger:
		blog_list = paginator.page(1)
	except EmptyPage:
		blog_list = paginator.page(paginator.num_pages)
	context['blog_list'] = blog_list
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsBlog.html',context)


@login_required(login_url="Dashboard:login")
def blog_add(request):
	context = {}
	if request.method == "POST":
		blog_form = BlogAddForm(request.POST or None, request.FILES or None)
		context['form'] = blog_form
		
		if blog_form.is_valid():
			Blog = blog_form.save()
			x = request.POST.get('x')
			y = request.POST.get('y')
			w = request.POST.get('width')
			h = request.POST.get('height')

			x1 = request.POST.get('x1')
			y1 = request.POST.get('y1')
			w1 = request.POST.get('width1')
			h1 = request.POST.get('height1')

			if x and y and w and h:
				
				card_image = Image.open(Blog.card_image)
				
				cropped_image = card_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
				resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
				resized_image.save(Blog.card_image.path)

			if x1 and y1 and w1 and h1:
				
				banner_image = Image.open(Blog.banner_image)
				
				cropped_image = banner_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
				resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
				resized_image.save(Blog.banner_image.path)			
			Blog.save()
	        # return photo
			messages.success(request, "Tour has been saved saccessfully!")
			context['messages'] = messages
			return HttpResponseRedirect(reverse('Dashboard:blog_list'), context)
		else:
			return render(request, 'akshayaindia-dashboad/pages/CMS/cmsAddNewBlog.html',context)
	else:
		blog_form = BlogAddForm()
		context['form'] = blog_form
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsAddNewBlog.html',context)

@login_required(login_url="Dashboard:login")
def blog_edit(request, slug=None):
	context = {}
	blog = get_object_or_404(Blog, slug=slug)
	context = {}
	if request.method == "POST":
		blog_form = BlogEditForm(request.POST or None, request.FILES or None, instance=blog)
		context['form'] = blog_form
		if blog_form.is_valid():
			Blog_obj = blog_form.save()

			x = request.POST.get('x')
			y = request.POST.get('y')
			w = request.POST.get('width')
			h = request.POST.get('height')

			x1 = request.POST.get('x1')
			y1 = request.POST.get('y1')
			w1 = request.POST.get('width1')
			h1 = request.POST.get('height1')

			if x and y and w and h:
				
				card_image = Image.open(Blog_obj.card_image)
				
				cropped_image = card_image.crop((float(x), float(y), float(w)+float(x), float(h)+float(y)))
				resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
				resized_image.save(Blog_obj.card_image.path)

			if x1 and y1 and w1 and h1:
			
				banner_image = Image.open(Blog_obj.banner_image)
				
				cropped_image = banner_image.crop((float(x1), float(y1), float(w1)+float(x1), float(h1)+float(y1)))
				resized_image = cropped_image.resize((1920, 560), Image.ANTIALIAS)
				resized_image.save(Blog_obj.banner_image.path)			
			Blog_obj.save()
			messages.success(request, "Blog has been saved saccessfully!")
			context['messages'] = messages
			return HttpResponseRedirect(reverse('Dashboard:blog_list'), context)
		else:
			return render(request, 'akshayaindia-dashboad/pages/CMS/cmsEditBlog.html',context)
	else:
		if blog:
			card_image = blog.card_image.path
			banner_image = blog.banner_image.path
		blog_form = BlogEditForm(instance=blog)
		context = {
			"card_image":card_image, 
			"banner_image":banner_image, 
			"form":blog_form
		}
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsEditBlog.html',context)


@login_required(login_url="Dashboard:login")
def blog_delete(request, slug=None):
	blog = get_object_or_404(Blog, slug=slug)
	blog.delete()
	return HttpResponseRedirect(reverse('Dashboard:blog_list'))


@login_required(login_url="Dashboard:login")
def testimonial_list(request):
	context = {}
	testimonial_list = Testimonial.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(testimonial_list, 6)
	try:
		testimonial_list = paginator.page(page)
	except PageNotAnInteger:
		testimonial_list = paginator.page(1)
	except EmptyPage:
		testimonial_list = paginator.page(paginator.num_pages)
	context['testimonial_list'] = testimonial_list
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsTestimonial.html',context)


@login_required(login_url="Dashboard:login")
def testimonial_add(request):
	context = {}
	if request.method == "POST" and request.is_ajax():
		testimonial_form = TestimonialAddForm(request.POST or None, request.FILES or None)
		context['form'] = testimonial_form
		if testimonial_form.is_valid():		
			Words = testimonial_form.save()

			Description = Words.words
			data = Description.split(" ",20)

			new_string1 = ''
			length = len(data)
			for i in data:
				new_string1 += i + ' '

			
			Words.save()

			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':testimonial_form.errors})
	else:
		testimonial_form = TestimonialAddForm()
		context['form'] = testimonial_form
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsAddNewTestimonial.html',context)


@login_required(login_url="Dashboard:login")
def testimonial_edit(request, id=None):
	context = {}
	testimonial = get_object_or_404(Testimonial, id=id)
	if request.method == "POST" and request.is_ajax():
		testimonial = TestimonialEditForm(request.POST or None, request.FILES or None, instance=testimonial)
		context['form'] = testimonial
		if testimonial.is_valid():
			testimonial.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':testimonial.errors})
	
	testimonial = TestimonialEditForm(instance=testimonial)
	context['form'] = testimonial
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsEditTestimonial.html',context)

@login_required(login_url="Dashboard:login")	
def testimonial_delete(request, id):
	testimonial = get_object_or_404(Testimonial, id=id)
	testimonial.delete()
	return HttpResponseRedirect(reverse('Dashboard:testimonial_list'))

@login_required(login_url="Dashboard:login")
def faq_list(request):
	context = {}
	faq_list = FAQ.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(faq_list, 6)
	try:
		faq_list = paginator.page(page)
	except PageNotAnInteger:
		faq_list = paginator.page(1)
	except EmptyPage:
		faq_list = paginator.page(paginator.num_pages)
	context['faq_list'] = faq_list
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsFAQ.html',context)


@login_required(login_url="Dashboard:login")
def faq_add(request):
	context = {}
	if request.method == "POST" and request.is_ajax():
		faq_form = FAQAddForm(request.POST or None)
		context['form'] = faq_form
		if faq_form.is_valid():
			faq_form.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':faq_form.errors})
	else:
		faq_form = FAQAddForm()
		context['form'] = faq_form
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsAddNewFAQ.html',context)


@login_required(login_url="Dashboard:login")
def faq_edit(request, id=None):
	faq = get_object_or_404(FAQ, id=id)
	if request.method == "POST" and request.is_ajax():
		faq_form = FAQAddForm(request.POST, instance=faq)
		if faq_form.is_valid():
			faq_form.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':faq_form.errors})
	else:
		faq_form = FAQAddForm(instance=faq)
	return render(request, 'akshayaindia-dashboad/pages/CMS/cmsEditFAQ.html',{'form':faq_form})

@login_required(login_url="Dashboard:login")
def faq_delete(request, id):
	faq = get_object_or_404(FAQ, id=id)
	faq.delete()
	return HttpResponseRedirect(reverse('Dashboard:faq_list'))


# Here all inquiry function reside
@login_required(login_url="Dashboard:login")
def india_inquiry_list(request):
	context = {}
	if request.is_ajax():
		inquiry = get_object_or_404(VacationEnquiry, id=request.GET.get('id'))
		if inquiry:
			inquiry.status = request.GET.get('status')
			inquiry.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':"Updation failed"})
	inquiry_list = VacationEnquiry.objects.filter(vacation__tour_type='India')
	page = request.GET.get('page', 1)
	paginator = Paginator(inquiry_list, 20)
	try:
		inquiry_list = paginator.page(page)
	except PageNotAnInteger:
		inquiry_list = paginator.page(1)
	except EmptyPage:
		inquiry_list = paginator.page(paginator.num_pages)
	context['inquiry_list'] = inquiry_list
	return render(request, 'akshayaindia-dashboad/pages/Inquiries/Vacations/inquiryVacIndia.html',context)


@login_required(login_url="Dashboard:login")
def international_inquiry_list(request):
	context = {}
	if request.is_ajax():
		inquiry = get_object_or_404(VacationEnquiry, id=request.GET.get('id'))
		if inquiry:
			inquiry.status = request.GET.get('status')
			inquiry.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':"Updation failed"})

	inquiry_list = VacationEnquiry.objects.filter(vacation__tour_type='International')
	page = request.GET.get('page', 1)
	paginator = Paginator(inquiry_list, 20)
	try:
		inquiry_list = paginator.page(page)
	except PageNotAnInteger:
		inquiry_list = paginator.page(1)
	except EmptyPage:
		inquiry_list = paginator.page(paginator.num_pages)
	context['inquiry_list'] = inquiry_list
	return render(request, 'akshayaindia-dashboad/pages/Inquiries/Vacations/inquiryVacInternational.html',context)


@login_required(login_url="Dashboard:login")
def cruise_inquiry_list(request):
	context = {}
	if request.is_ajax():
		inquiry = get_object_or_404(VacationEnquiry, id=request.GET.get('id'))
		if inquiry:
			inquiry.status = request.GET.get('status')
			inquiry.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':"Updation failed"})
	inquiry_list = VacationEnquiry.objects.filter(vacation__tour_type='Cruise')
	page = request.GET.get('page', 1)
	paginator = Paginator(inquiry_list, 20)
	try:
		inquiry_list = paginator.page(page)
	except PageNotAnInteger:
		inquiry_list = paginator.page(1)
	except EmptyPage:
		inquiry_list = paginator.page(paginator.num_pages)
	context['inquiry_list'] = inquiry_list
	return render(request, 'akshayaindia-dashboad/pages/Inquiries/Vacations/inquiryVacCruise.html',context)


@login_required(login_url="Dashboard:login")
def flight_inquiry_list(request):
	context = {}
	if request.is_ajax():
		inquiry = get_object_or_404(FlightEnquiry, id=request.GET.get('id'))
		if inquiry:
			inquiry.status = request.GET.get('status')
			inquiry.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':"Updation failed"})
	inquiry_list = FlightEnquiry.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(inquiry_list, 20)
	try:
		inquiry_list = paginator.page(page)
	except PageNotAnInteger:
		inquiry_list = paginator.page(1)
	except EmptyPage:
		inquiry_list = paginator.page(paginator.num_pages)
	context['inquiry_list'] = inquiry_list
	return render(request, 'akshayaindia-dashboad/pages/Inquiries/inquiryFlight.html',context)

	

@login_required(login_url="Dashboard:login")
def hotel_inquiry_list(request):
	context = {}
	if request.is_ajax():
		inquiry = get_object_or_404(HotelEnquiry, id=request.GET.get('id'))
		if inquiry:
			inquiry.status = request.GET.get('status')
			inquiry.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':"Updation failed"})
	inquiry_list = HotelEnquiry.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(inquiry_list, 20)
	try:
		inquiry_list = paginator.page(page)
	except PageNotAnInteger:
		inquiry_list = paginator.page(1)
	except EmptyPage:
		inquiry_list = paginator.page(paginator.num_pages)
	context['inquiry_list'] = inquiry_list
	return render(request, 'akshayaindia-dashboad/pages/Inquiries/inquiryHotel.html',context)


@login_required(login_url="Dashboard:login")
def car_inquiry_list(request):
	context = {}
	if request.is_ajax():
		inquiry = get_object_or_404(CarEnquiry, id=request.GET.get('id'))
		if inquiry:
			inquiry.status = request.GET.get('status')
			inquiry.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':"Updation failed"})

	inquiry_list = CarEnquiry.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(inquiry_list, 20)
	try:
		inquiry_list = paginator.page(page)
	except PageNotAnInteger:
		inquiry_list = paginator.page(1)
	except EmptyPage:
		inquiry_list = paginator.page(paginator.num_pages)
	context['inquiry_list'] = inquiry_list
	return render(request, 'akshayaindia-dashboad/pages/Inquiries/inquiryCars.html',context)


@login_required(login_url="Dashboard:login")
def corporate_inquiry_list(request):
	context = {}
	if request.is_ajax():
		inquiry = get_object_or_404(CorporateEnquiry, id=request.GET.get('id'))
		if inquiry:
			inquiry.status = request.GET.get('status')
			inquiry.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':"Updation failed"})
	inquiry_list = CorporateEnquiry.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(inquiry_list, 20)
	try:
		inquiry_list = paginator.page(page)
	except PageNotAnInteger:
		inquiry_list = paginator.page(1)
	except EmptyPage:
		inquiry_list = paginator.page(paginator.num_pages)
	context['inquiry_list'] = inquiry_list
	return render(request, 'akshayaindia-dashboad/pages/Inquiries/inquiryCorporate.html',context)


@login_required(login_url="Dashboard:login")
def visa_inquiry_list(request):
	context = {}
	if request.is_ajax():
		inquiry = get_object_or_404(VisaEnquiry, id=request.GET.get('id'))
		if inquiry:
			inquiry.status = request.GET.get('status')
			inquiry.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':"Updation failed"})
	inquiry_list = VisaEnquiry.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(inquiry_list, 20)
	try:
		inquiry_list = paginator.page(page)
	except PageNotAnInteger:
		inquiry_list = paginator.page(1)
	except EmptyPage:
		inquiry_list = paginator.page(paginator.num_pages)
	context['inquiry_list'] = inquiry_list
	return render(request, 'akshayaindia-dashboad/pages/Inquiries/inquiryVisa.html',context)


@login_required(login_url="Dashboard:login")
def faqs_inquiry_list(request):
	context = {}
	if request.is_ajax():
		inquiry = get_object_or_404(AskQuestionEnquiry, id=request.GET.get('id'))
		if inquiry:
			inquiry.status = request.GET.get('status')
			inquiry.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':"Updation failed"})

	inquiry_list = AskQuestionEnquiry.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(inquiry_list, 20)
	try:
		inquiry_list = paginator.page(page)
	except PageNotAnInteger:
		inquiry_list = paginator.page(1)
	except EmptyPage:
		inquiry_list = paginator.page(paginator.num_pages)
	context['inquiry_list'] = inquiry_list
	return render(request, 'akshayaindia-dashboad/pages/Inquiries/inquiryFaq.html',context)


@login_required(login_url="Dashboard:login")
def contact_inquiry_list(request):
	context = {}
	if request.is_ajax():
		inquiry = get_object_or_404(ContactUs, id=request.GET.get('id'))
		if inquiry:
			inquiry.status = request.GET.get('status')
			inquiry.save()
			return JsonResponse({'success':True})
		else:
			return JsonResponse({'error':"Updation failed"})

	inquiry_list = ContactUs.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(inquiry_list, 20)
	try:
		inquiry_list = paginator.page(page)
	except PageNotAnInteger:
		inquiry_list = paginator.page(1)
	except EmptyPage:
		inquiry_list = paginator.page(paginator.num_pages)
	context['inquiry_list'] = inquiry_list
	return render(request, 'akshayaindia-dashboad/pages/Inquiries/inquiryContact.html',context)


@login_required(login_url="Dashboard:login")
def export_contact_enquiry_csv(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-ContactUs.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('ContactUs')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name', 'Email Address', 'Message', 'Status', 'Timestamp', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = ContactUs.objects.all().values_list('name', 'email', 'message', 'status', 'timestamp')
    for row in rows:
        row_list = list(row)
        row_list[4] = str(row_list[4])
        row = tuple(row_list)
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

@login_required(login_url="Dashboard:login")
def export_faq_enquiry_csv(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-FAQEnquiry.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('AskQuestionEnquiry')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name', 'Email Address', 'Question Type','Question', 'Status','Timestamp', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = AskQuestionEnquiry.objects.all().values_list('name', 'email', 'question_type', 'your_question','status','timestamp')
    for row in rows:
        row_list = list(row)
        row_list[5] = str(row_list[5])
        row = tuple(row_list)
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


@login_required(login_url="Dashboard:login")
def export_visa_enquiry_csv(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-VisaEnquiry.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('VisaEnquiry')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Country Name','Generic Visa Name','Type of Visa','City of Residence','Date of Travel','Additional Request','Name', 'Email Address', 'Phone Number','Status','Timestamp', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = VisaEnquiry.objects.all().values_list('visa__country','general_visa_name', 'type_of_visa', 'city_of_residence', 'date_of_travel','additional_request','name','email','phone_number','status','timestamp')
    for row in rows:
        row_list = list(row)
        row_list[3] = str(row_list[3])
        row_list[9] = str(row_list[9])
        row = tuple(row_list)
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

@login_required(login_url="Dashboard:login")
def export_corporate_enquiry_csv(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-CorporateEnquiry.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('CorporateEnquiry')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Corporate Activate','Company Name','Additional Request','Name', 'Email Address', 'Phone Number','Status','Timestamp', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = CorporateEnquiry.objects.all().values_list('type_of_work', 'company_name', 'additional_request', 'name','email','phone_number','status','timestamp')
    for row in rows:
        row_list = list(row)
        row_list[7] = str(row_list[7])
        row = tuple(row_list)
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


@login_required(login_url="Dashboard:login")
def export_car_enquiry_csv(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-CarEnquiry.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('CarEnquiry')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Rental Type','Location','Travel Date','Vehicle Type','Adults','Childrens','Additional Request','Name', 'Email Address', 'Phone Number','Status','Timestamp', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = CarEnquiry.objects.all().values_list('type_of_requirement', 'pick_up_from', 'date_of_journey','vehical_type', 'number_of_adult', 'number_of_children', 'additional_request','name','email','phone_number','status','timestamp')
    for row in rows:
        row_list = list(row)
        row_list[2] = str(row_list[2])
        row_list[11] = str(row_list[11])
        row = tuple(row_list)
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

@login_required(login_url="Dashboard:login")
def export_hotel_enquiry_csv(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-HotelEnquiry.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('HotelEnquiry')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Destination','Number of Room','Adults','Childrens','Additional Request','Name', 'Email Address', 'Phone Number','Status','Timestamp', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = HotelEnquiry.objects.all().values_list('destination', 'number_of_room', 'number_of_adult', 'number_of_children', 'additional_request','name','email','phone_number','status','timestamp')
    for row in rows:
        row_list = list(row)
        row_list[9] = str(row_list[9])
        row = tuple(row_list)
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

@login_required(login_url="Dashboard:login")
def export_flight_enquiry_csv(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-FlightEnquiry.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('FlightEnquiry')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['From','To','Departure Date','Return Date','Adults','Childrens','Infants','Class','Name', 'Email Address', 'Phone Number','Status','Timestamp', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = FlightEnquiry.objects.all().values_list('travel_from', 'travel_to','departure_date','arrival_date', 'number_of_adult', 'number_of_children', 'number_of_infant','Class','name','email','phone_number','status','timestamp')
    for row in rows:
        row_list = list(row)
        row_list[2] = str(row_list[2])
        row_list[3] = str(row_list[3])
        row_list[12] = str(row_list[12])
        row = tuple(row_list)
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

@login_required(login_url="Dashboard:login")
def export_vacation_india_enquiry_csv(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-VacationIndiaEnquiry.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('VacationIndiaEnquiry')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Tour Name','Departure Location','Travel Mode','Departure Date','Adults','Childrens','Infants','Class','Name', 'Email Address', 'Phone Number','Status','Timestamp', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = VacationEnquiry.objects.filter(vacation__tour_type='India').values_list('vacation__title','travel_from', 'travel_mode','departure_date','number_of_adult', 'number_of_children', 'number_of_infant','Class','name','email','phone_number','status','timestamp')
    for row in rows:
        row_list = list(row)
        row_list[3] = str(row_list[3])
        row_list[12] = str(row_list[12])
        row = tuple(row_list)
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

@login_required(login_url="Dashboard:login")
def export_vacation_international_enquiry_csv(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-VacationInternationalEnquiry.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('VacationInternationalEnquiry')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Tour Name','Departure Location','Travel Mode','Departure Date','Adults','Childrens','Infants','Class','Name', 'Email Address', 'Phone Number','Status','Timestamp', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = VacationEnquiry.objects.filter(vacation__tour_type='International').values_list('vacation__title','travel_from', 'travel_mode','departure_date','number_of_adult', 'number_of_children', 'number_of_infant','Class','name','email','phone_number','status','timestamp')
    for row in rows:
        row_list = list(row)
        row_list[3] = str(row_list[3])
        row_list[12] = str(row_list[12])
        row = tuple(row_list)
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


@login_required(login_url="Dashboard:login")
def export_vacation_cruise_enquiry_csv(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-VacationCruiseEnquiry.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('VacationCruiseEnquiry')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Tour Name','Departure Location','Travel Mode','Departure Date','Adults','Childrens','Infants','Class','Name', 'Email Address', 'Phone Number','Status','Timestamp', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = VacationEnquiry.objects.filter(vacation__tour_type='Cruise').values_list('vacation__title','travel_from', 'travel_mode','departure_date','number_of_adult', 'number_of_children', 'number_of_infant','Class','name','email','phone_number','status','timestamp')
    for row in rows:
        row_list = list(row)
        row_list[3] = str(row_list[3])
        row_list[12] = str(row_list[12])
        row = tuple(row_list)
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

@login_required(login_url="Dashboard:login")
def tour_move_up(request):
	if request.method == 'POST':
		vacation_id = int(request.POST.get('vacation_id'))
		get_vacation = Vacation.objects.get(id=vacation_id)

		if get_vacation:

			current_vacation_position = get_vacation.position
			vacation_type = get_vacation.tour_type
			vacation_hero = get_vacation.hero_tour
			

			if vacation_type == 'India':
				all_india_tours = Vacation.objects.filter(tour_type='India').order_by('position')
				temp_vacation_position = 1
			
				for i in all_india_tours:
					if i.position < current_vacation_position:
						temp_vacation_position = int(i.position)
				temp_vacation = Vacation.objects.get(position=temp_vacation_position)		
				current_vacation = Vacation.objects.get(position=current_vacation_position)

				temp_vacation.position = current_vacation_position
				current_vacation.position = temp_vacation_position

				temp_vacation.save()
				current_vacation.save()
		
				if temp_vacation and current_vacation:		
					return JsonResponse({'success':True})
				else:
					return JsonResponse({'error':'Operation could not done.'})


			elif vacation_type == 'International':
				all_india_tours = Vacation.objects.filter(tour_type='International').order_by('position')
				temp_vacation_position = 1
			
				for i in all_india_tours:
					if i.position < current_vacation_position:
						temp_vacation_position = int(i.position)
				temp_vacation = Vacation.objects.get(position=temp_vacation_position)		
				current_vacation = Vacation.objects.get(position=current_vacation_position)

				temp_vacation.position = current_vacation_position
				current_vacation.position = temp_vacation_position

				temp_vacation.save()
				current_vacation.save()
		
				if temp_vacation and current_vacation:		
					return JsonResponse({'success':True})
				else:
					return JsonResponse({'error':'Operation could not done.'})

			elif vacation_type == 'Cruise':
				all_india_tours = Vacation.objects.filter(tour_type='Cruise').order_by('position')
				temp_vacation_position = 1
			
				for i in all_india_tours:
					if i.position < current_vacation_position:
						temp_vacation_position = int(i.position)
				temp_vacation = Vacation.objects.get(position=temp_vacation_position)		
				current_vacation = Vacation.objects.get(position=current_vacation_position)

				temp_vacation.position = current_vacation_position
				current_vacation.position = temp_vacation_position

				temp_vacation.save()
				current_vacation.save()
		
				if temp_vacation and current_vacation:		
					return JsonResponse({'success':True})
				else:
					return JsonResponse({'error':'Operation could not done.'})
			else:
				return JsonResponse({'error':'Tour is not found'})
		else:
			return JsonResponse({'error':'not found'})


@login_required(login_url="Dashboard:login")
def tour_move_down(request):
	if request.method == 'POST':
		vacation_id = int(request.POST.get('vacation_id'))
		get_vacation = Vacation.objects.get(id=vacation_id)

		if get_vacation:
			current_vacation_position = get_vacation.position
			vacation_type = get_vacation.tour_type
			vacation_hero = get_vacation.hero_tour

			# For India Tour
			if vacation_type == 'India':
				all_india_tours = Vacation.objects.filter(tour_type='India').order_by('-position')
				temp_vacation_position = 1
				
				for i in all_india_tours:
					if i.position > current_vacation_position:
						temp_vacation_position = int(i.position)
				temp_vacation = Vacation.objects.get(position=temp_vacation_position)		
				current_vacation = Vacation.objects.get(position=current_vacation_position)

				temp_vacation.position = current_vacation_position
				current_vacation.position = temp_vacation_position

				temp_vacation.save()
				current_vacation.save()
			
				if temp_vacation and current_vacation:		
					return JsonResponse({'success':True})
				else:
					return JsonResponse({'error':'Operation could not done.'})

			# For International Tour
			elif vacation_type == 'International':
				all_india_tours = Vacation.objects.filter(tour_type='International').order_by('-position')
				temp_vacation_position = 1
				
				for i in all_india_tours:
					if i.position > current_vacation_position:
						temp_vacation_position = int(i.position)
				temp_vacation = Vacation.objects.get(position=temp_vacation_position)		
				current_vacation = Vacation.objects.get(position=current_vacation_position)

				temp_vacation.position = current_vacation_position
				current_vacation.position = temp_vacation_position

				temp_vacation.save()
				current_vacation.save()
			
				if temp_vacation and current_vacation:		
					return JsonResponse({'success':True})
				else:
					return JsonResponse({'error':'Operation could not done.'})

			# For Cruise Tour
			elif vacation_type == 'Cruise':
				all_india_tours = Vacation.objects.filter(tour_type='Cruise').order_by('-position')
				temp_vacation_position = 1
				
				for i in all_india_tours:
					if i.position > current_vacation_position:
						temp_vacation_position = int(i.position)
				temp_vacation = Vacation.objects.get(position=temp_vacation_position)		
				current_vacation = Vacation.objects.get(position=current_vacation_position)

				temp_vacation.position = current_vacation_position
				current_vacation.position = temp_vacation_position

				temp_vacation.save()
				current_vacation.save()
			
				if temp_vacation and current_vacation:		
					return JsonResponse({'success':True})
				else:
					return JsonResponse({'error':'Operation could not done.'})
			else:
				return JsonResponse({'error':'Tour is not found'})
		else:
			return JsonResponse({'error':'not found'})

