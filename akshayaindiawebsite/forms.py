from django import forms
from .models import (
    FlightEnquiry, 
    VacationEnquiry,
    VisaEnquiry,
    CarEnquiry,
    HotelEnquiry,
    CorporateEnquiry,
    ContactUs,
    AskQuestionEnquiry,
    )


class FlightEnquiryForm(forms.ModelForm):
    ADULTS_CHOICES = (
        ("Adult", "No. of Adult"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    )
    CHILDS_CHOICES = (
        ("0", "Children"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    )
    INFANTS_CHOICES = (
        ("0", "Infant"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    )
    CLASS_CHOICES = (
        ("Class","Class"),
        ("First Class","First Class"),
        ("Business","Business"),
        ("Premium Economy","Premium Economy"),
        ("Economy","Economy"),
        )
    number_of_adult = forms.ChoiceField(choices=ADULTS_CHOICES)
    number_of_children = forms.ChoiceField(choices=CHILDS_CHOICES)
    number_of_infant = forms.ChoiceField(choices=INFANTS_CHOICES)
    Class = forms.ChoiceField(choices=CLASS_CHOICES)
    email = forms.EmailField()

    class Meta:
        model = FlightEnquiry
        fields = [
            "travel_from",
            "travel_to",
            "departure_date",
            "arrival_date",
            "number_of_adult",
            "number_of_children",
            "number_of_infant",
            "Class",
            "name",
            "email",
            "phone_number",
        ]

class VacationEnquiryForm(forms.ModelForm):
    ADULTS_CHOICES = (
        ("Adult", "No. of Adult"),# donot remove this is form validation
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    )
    CHILDS_CHOICES = (
        ("0", "Children"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    )
    INFANTS_CHOICES = (
        ("0", "Infant"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    )

    CLASS_CHOICES = (
        ("Class","Class"),
        ("Premium","Premium"),
        ("Premium Economy","Premium Economy"),
        ("Economy","Economy"),
        )
    MODE_CHOICES = (
        ("Travel Mode","Travel Mode"),
        ("Flight","Flight"),
        ("Train","Train"),
        ("Road","Road"),
        )
    number_of_adult = forms.ChoiceField(choices=ADULTS_CHOICES)
    number_of_children = forms.ChoiceField(choices=CHILDS_CHOICES)
    number_of_infant = forms.ChoiceField(choices=INFANTS_CHOICES)
    Class = forms.ChoiceField(choices=CLASS_CHOICES)
    travel_mode = forms.ChoiceField(choices=MODE_CHOICES)
    email = forms.EmailField()

    class Meta:
        model = VacationEnquiry
        fields = [
            "travel_from",
            # "travel_to",
            "travel_mode",
            "departure_date",
            # "arrival_date",
            "number_of_adult",
            "number_of_children",
            "number_of_infant",
            "Class",
            "name",
            "email",
            "phone_number",
        ]

class VisaEnquiryForm(forms.ModelForm):
    # general_visa_name = forms.CharField(max_length=120)
    city_of_residence = forms.CharField(max_length=120)
    additional_request = forms.CharField(max_length=255)
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=120)

    class Meta:
        model = VisaEnquiry
        fields = [
            "general_visa_name",    
            "type_of_visa",
            "city_of_residence",
            "date_of_travel",
            "additional_request",
            "name",
            "email",
            "phone_number",
        ]

class CarEnquiryForm(forms.ModelForm):
    ADULTS_CHOICES = (
        ("0", "No. of Adult"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    )
    CHILDS_CHOICES = (
        ("0", "Children"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    ) 
    
    REQ_CHOICES = (
        ("Rental Type", "Rental Type"),
        ("Airport Pickup/Drop", "Airport Pickup/Drop"),
        ("One Day City Tour", "One Day City Tour"),
        ("Outstation Tour", "Outstation Tour"),
        ("Other", "Other"),

    )
    VEHICLE_CHOICES = (
        ("Vehicle Type", "Vehicle Type"),
        ("4-Seater", "4-Seater"),
        ("7-Seater", "7-Seater"),
        ("Coach", "Coach"),
    )
    number_of_adult = forms.ChoiceField(choices=ADULTS_CHOICES)
    number_of_children = forms.ChoiceField(choices=CHILDS_CHOICES)
    email = forms.EmailField()
    type_of_requirement = forms.ChoiceField(choices=REQ_CHOICES)
    vehical_type = forms.ChoiceField(choices=VEHICLE_CHOICES)
     

    class Meta:
        model = CarEnquiry
        fields = [
            "type_of_requirement",
            "pick_up_from",
            "date_of_journey",
            "vehical_type",
            "number_of_adult",
            "number_of_children",
            "additional_request",
            "name",
            "email",
            "phone_number",
        ]



class HotelEnquiryForm(forms.ModelForm):
    ADULTS_CHOICES = (
        ("Adult", "No. of Adult"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    )
    CHILDS_CHOICES = (
        ("0", "Children"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    )
    ROOM_CHOICES = (
        ("room", "No. of Rooms"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    )
    number_of_adult = forms.ChoiceField(choices=ADULTS_CHOICES)
    number_of_children = forms.ChoiceField(choices=CHILDS_CHOICES)
    email = forms.EmailField()
    number_of_room = forms.ChoiceField(choices=ROOM_CHOICES)
     

    class Meta:
        model = HotelEnquiry
        fields = [
            "destination",
            "number_of_room",
            "number_of_adult",
            "number_of_children",
            "additional_request",
            "name",
            "email",
            "phone_number",
        ]

class CorporateEnquiryForm(forms.ModelForm):
    WORK_CHOICES = (
        ("Cor_Act","Corporate Activity"),
        ("Meetings","Meetings"),
        ("Incentives","Incentives"),
        ("Conferences","Conferences"),
        ("Events","Events"),
        )
    type_of_work = forms.ChoiceField(choices=WORK_CHOICES)
    email = forms.EmailField()

    class Meta:
        model = CorporateEnquiry
        fields = [
            "type_of_work",
            "company_name",
            "name",
            "email",
            "phone_number",
            "additional_request",
        ]

class ContactUsForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    # message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = ContactUs
        fields = [
            "name",
            "email",
            "message",
        ]


class AskQuestionEnquiryForm(forms.ModelForm):
    QUE_CHOICES = (
        ("General", "General"),
        ("Tours", "Tours"),
        ("Visa", "Visa"),
        ("Hotels", "Hotels"),
        ("Cars", "Cars"),
        ("Couple", "Couple"),
        ("Packages", "Packages")
        )
    question_type = forms.ChoiceField(choices=QUE_CHOICES)
    name = forms.CharField(max_length=120)

    class Meta:
        model = AskQuestionEnquiry
        fields = [
            "name",
            "email",
            "question_type",
            "your_question",
        ]