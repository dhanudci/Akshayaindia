from django.contrib import admin

# Register your models here.
from .models import (
	CorporateEnquiry,
	CorporateHeading,
	CorporateIncentives,
	CorporateEvent,

	FlightEnquiry,
	CarEnquiry,
	HotelEnquiry,
	VisaEnquiry,
	VacationEnquiry,
	Testimonial,
	Vacation,
	ItinerarySectionModel,
    GallaryModel,
	FAQ,
	AskQuestionEnquiry,
    Visa,
    VisaFAQ,
    TypesOfVisa,
    Blog,
    BlogGallary,
    ContactUs,
    VacationCategory,
    FAQCategory,
	)

admin.site.register(CorporateHeading)
admin.site.register(CorporateIncentives)
admin.site.register(CorporateEvent)


class VacationEnquiryModelAdmin(admin.ModelAdmin):
	list_display = ["name", "email","phone_number","timestamp"]
	list_filter = ["name", "email","phone_number","timestamp"]
	search_fields = ["name", "email","phone_number"]

	class Meta:
		model = VacationEnquiry
admin.site.register(VacationEnquiry, VacationEnquiryModelAdmin)


class BlogModelAdmin(admin.ModelAdmin):
	list_display = ["title", "hero_blog","home_visible","meta_title","meta_keywords","updated","timestamp"]
	list_filter = ["hero_blog","home_visible","meta_title",'meta_keywords']
	search_fields = ["title", "meta_title","meta_keywords"]

	class Meta:
		model = Blog
admin.site.register(Blog, BlogModelAdmin)



class VacationModelAdmin(admin.ModelAdmin):
	list_display = ["id","title","position","tour_type","home_visible","vacation_label","hero_tour","updated","timestamp"]
	
	class Meta:
		model = Vacation
admin.site.register(Vacation, VacationModelAdmin)

class ItinerarySectionModeladmin(admin.ModelAdmin):
	list_display = ["vacation","heading","breakfast","lunch","dinner","stay_in_hotel","updated","timestamp"]
	list_filter = ["vacation", "heading","breakfast","lunch","dinner","stay_in_hotel"]
	search_fields = ["vacation", "heading"]

	class Meta:
		model = ItinerarySectionModel
admin.site.register(ItinerarySectionModel, ItinerarySectionModeladmin)

class GallaryModeladmin(admin.ModelAdmin):
	list_display = ["vacation","gallary_image","updated","timestamp"]
	class Meta:
		model = GallaryModel
admin.site.register(GallaryModel, GallaryModeladmin)

class VacationCategoryModelAdmin(admin.ModelAdmin):
	list_display = ["category_name","short_desc","icon","updated","timestamp"]
	list_filter = ["category_name",]
	search_fields = ["category_name","short_desc"]
	
	class Meta:
		model = VacationCategory
admin.site.register(VacationCategory, VacationCategoryModelAdmin)

class ContactUsModelAdmin(admin.ModelAdmin):
	list_display = ["name", "email","timestamp"]
	list_filter = ["name", "email","timestamp"]
	search_fields = ["name", "email"]

	class Meta:
		model = ContactUs
admin.site.register(ContactUs, ContactUsModelAdmin)	


class FlightEnquiryModelAdmin(admin.ModelAdmin):
	list_display = ["travel_from","name", "email","phone_number","timestamp"]
	list_filter = ["name", "email","phone_number","timestamp"]
	search_fields = ["name", "email","phone_number","timestamp"]

	class Meta:
		model = FlightEnquiry
admin.site.register(FlightEnquiry, FlightEnquiryModelAdmin)

class CarEnquiryModelAdmin(admin.ModelAdmin):
	list_display = ["name", "email","phone_number","date_of_journey","timestamp"]
	list_filter = ["name", "email","phone_number","timestamp"]
	search_fields = ["name", "email","phone_number","timestamp"]

	class Meta:
		model = CarEnquiry
admin.site.register(CarEnquiry, CarEnquiryModelAdmin)

class HotelEnquiryModelAdmin(admin.ModelAdmin):
	list_display = ["name", "email","phone_number","timestamp"]
	list_filter = ["name", "email","phone_number","timestamp"]
	search_fields = ["name", "email","phone_number","timestamp"]

	class Meta:
		model = HotelEnquiry
admin.site.register(HotelEnquiry, HotelEnquiryModelAdmin)

class CorporateEnquiryModelAdmin(admin.ModelAdmin):
	list_display = ["name", "email","phone_number","timestamp"]
	list_filter = ["name", "email","phone_number","timestamp"]
	search_fields = ["name", "email","phone_number","timestamp"]

	class Meta:
		model = CorporateEnquiry
admin.site.register(CorporateEnquiry, CorporateEnquiryModelAdmin)

class VisaEnquiryModelAdmin(admin.ModelAdmin):
	list_display = ["name", "email","phone_number","timestamp"]
	list_filter = ["name", "email","phone_number","timestamp"]
	search_fields = ["name", "email","phone_number","timestamp"]

	class Meta:
		model = VisaEnquiry
admin.site.register(VisaEnquiry, VisaEnquiryModelAdmin)

class TypesOfVisaModelAdmin(admin.ModelAdmin):
	list_display = ["country","visa_name","updated","timestamp"]
	list_filter = ["country","visa_name","timestamp"]
	search_fields = ["country","visa_name","timestamp"]
	class Meta:
		model = TypesOfVisa

admin.site.register(TypesOfVisa, TypesOfVisaModelAdmin)

class AskQuestionEnquiryModelAdmin(admin.ModelAdmin):
	list_display = ["name", "email","question_type","timestamp"]
	list_filter = ["name", "email","question_type","timestamp"]
	search_fields = ["name", "email","question_type","timestamp"]

	class Meta:
		model = AskQuestionEnquiry
admin.site.register(AskQuestionEnquiry, AskQuestionEnquiryModelAdmin)

class FAQModelAdmin(admin.ModelAdmin):
	list_display = ["tag", "question","helpful","updated","timestamp"]
	list_filter = ["tag", "question","helpful","timestamp"]
	search_fields = ["tag", "question","helpful","timestamp"]

	class Meta:
		model = FAQ
admin.site.register(FAQ, FAQModelAdmin)

class FAQCategoryModelAdmin(admin.ModelAdmin):
	list_display = ["category_name","updated","timestamp"]
	list_filter = ["category_name","timestamp"]
	search_fields = ["category_name"]

	class Meta:
		model = FAQCategory
admin.site.register(FAQCategory, FAQCategoryModelAdmin)

class TestimonialModelAdmin(admin.ModelAdmin):
	list_display = ["name",'city',"updated","timestamp"]
	list_filter = ["name", 'city',"timestamp"]
	search_fields = ["name", 'city',"timestamp"]

	class Meta:
		model = Testimonial
admin.site.register(Testimonial, TestimonialModelAdmin)

class VisaModelAdmin(admin.ModelAdmin):
	list_display = ["country","updated","timestamp"]
	search_fields = ["country"]

	class Meta:
		model = Visa
admin.site.register(Visa, VisaModelAdmin)

class VisaFAQModelAdmin(admin.ModelAdmin):
	list_display = ["country", "question","updated","timestamp"]
	search_fields = ["country", "question","timestamp"]

	class Meta:
		model = VisaFAQ
admin.site.register(VisaFAQ, VisaFAQModelAdmin)
