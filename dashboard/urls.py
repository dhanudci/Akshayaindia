from django.urls import path

from . import views

app_name = "Dashboard"

urlpatterns = [

	path('login/', views.user_login, name="login"),
	path('logout/', views.user_logout, name="logout"),


	path("", views.home, name="home"),
	# CMS
	path("vacation/india/", views.india, name="india"),
	path("vacation/india/add/", views.vacation_india_add, name="vacation_india_add"),
	path("vacation/india/edit/<str:slug>", views.vacation_india_edit, name="vacation_india_edit"),

	path("vacation/international/", views.international, name="international"),
	path("vacation/international/add/", views.vacation_international_add, name="vacation_international_add"),
	path("vacation/international/edit/<str:slug>", views.vacation_international_edit, name="vacation_international_edit"),

	path("vacation/cruise/", views.cruise, name="cruise"),
	path("vacation/cruise/add/", views.vacation_cruise_add, name="vacation_cruise_add"),
	path("vacation/cruise/edit/<str:slug>", views.vacation_cruise_edit, name="vacation_cruise_edit"),
	path("vacation/delete/<str:slug>/", views.vacation_delete, name="vacation_delete"),
	
	path("corporate/", views.corporate, name="corporate"),
	path("corporate/edit/", views.corporate_edit, name="corporate_edit"),

	path("visa/", views.visa_list, name="visa_list"),
	path("visa/add/", views.visa_add, name="visa_add"),
	path("visa/edit/<str:slug>/", views.visa_edit, name="visa_edit"),
	path("visa/delete/<str:slug>/", views.visa_delete, name="visa_delete"),
	path("visa/edit/", views.visa_type_delete, name="visa_type_delete"),
	path("visa_type_delete/", views.visa_type_delete, name="visa_type_delete"),

	path("blog/", views.blog_list, name="blog_list"),
	path("blog/add/", views.blog_add, name="blog_add"),
	path("blog/edit/<str:slug>/", views.blog_edit, name="blog_edit"),
	path("blog/delete/<str:slug>/", views.blog_delete, name="blog_delete"), 

	path("testimonial/", views.testimonial_list, name="testimonial_list"),
	path("testimonial/add/", views.testimonial_add, name="testimonial_add"),
	path("testimonial/edit/<int:id>/", views.testimonial_edit, name="testimonial_edit"),
	path("testimonial/delete/<int:id>/", views.testimonial_delete, name="testimonial_delete"), 

	path("faq/", views.faq_list, name="faq_list"),
	path("faq/add/", views.faq_add, name="faq_add"),
	path("faq/edit/<int:id>", views.faq_edit, name="faq_edit"),
	path("faq/delete/<int:id>/", views.faq_delete, name="faq_delete"),  

	# Inquiries
	# Vacations Inquiries
	path("india_inquiry/", views.india_inquiry_list, name="india_inquiry_list"),
	path("international_inquiry/", views.international_inquiry_list, name="international_inquiry_list"),
	path("cruise_inquiry/", views.cruise_inquiry_list, name="cruise_inquiry_list"),
	# Others Inquiries
	path("flight_inquiry/", views.flight_inquiry_list, name="flight_inquiry_list"),
	path("hotel_inquiry/", views.hotel_inquiry_list, name="hotel_inquiry_list"),
	path("car_inquiry/", views.car_inquiry_list, name="car_inquiry_list"),
	path("corporate_inquiry/", views.corporate_inquiry_list, name="corporate_inquiry_list"),
	path("visa_inquiry/", views.visa_inquiry_list, name="visa_inquiry_list"),
	path("faqs_inquiry/", views.faqs_inquiry_list, name="faqs_inquiry_list"),
	path("contact_inquiry/", views.contact_inquiry_list, name="contact_inquiry_list"),

	path('export/contact_enquiry/csv/',views.export_contact_enquiry_csv, name='export_contact_enquiry_csv'),
	path('export/faq_enquiry/csv/',views.export_faq_enquiry_csv, name='export_faq_enquiry_csv'),
	path('export/visa_enquiry/csv/',views.export_visa_enquiry_csv, name='export_visa_enquiry_csv'),
	path('export/corporate_enquiry/csv/',views.export_corporate_enquiry_csv, name='export_corporate_enquiry_csv'),
	path('export/car_enquiry/csv/',views.export_car_enquiry_csv, name='export_car_enquiry_csv'),
	path('export/hotel_enquiry/csv/',views.export_hotel_enquiry_csv, name='export_hotel_enquiry_csv'),
	path('export/flight_enquiry/csv/',views.export_flight_enquiry_csv, name='export_flight_enquiry_csv'),

	path('export/vacation_india_enquiry/csv/',views.export_vacation_india_enquiry_csv, name='export_vacation_india_enquiry_csv'),
	path('export/vacation_international_enquiry/csv/',views.export_vacation_international_enquiry_csv, name='export_vacation_international_enquiry_csv'),
	path('export/vacation_cruise_enquiry/csv/',views.export_vacation_cruise_enquiry_csv, name='export_vacation_cruise_enquiry_csv'),
	
	path('tour_move_up/', views.tour_move_up, name='vacation_move_up'),
	path('tour_move_down/', views.tour_move_down, name='vacation_move_down'),	
]
