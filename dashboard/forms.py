from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import  CKEditorUploadingWidget
from akshayaindiawebsite.models import (
    Blog,
    Testimonial,
    FAQ,
    Visa,
    TypesOfVisa,

    Vacation,
    ItinerarySectionModel,
    GallaryModel,

    CorporateHeading,
    CorporateIncentives,
    CorporateEvent,
    )


class BlogAddForm(forms.ModelForm):
    blog_content = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control'}))
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Blog
        fields = [
            "title",
            "hero_blog",
            "home_visible",
            "banner_image",
            "card_image",
            "blog_content",

            "meta_title",
            "meta_description",
            "meta_keywords",

            'x',
            'y',
            'width',
            'height',
            'x1',
            'y1',
            'width1',
            'height1',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Heading'}),
            'banner_image': forms.FileInput(attrs={'id':'banner_image'}),
            'card_image': forms.FileInput(attrs={'id':'card_image'}),
            'hero_blog': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'home_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'meta_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Description'}),
            'meta_keywords': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Example keyword1, keyword 2'}),
        }

class BlogEditForm(forms.ModelForm):
    blog_content = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control'}))
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    banner_image = forms.FileField(widget=forms.FileInput(attrs={'id':'banner_image'}), required=False)
    card_image = forms.FileField(widget=forms.FileInput(attrs={'id':'card_image'}), required=False)
    class Meta:
        model = Blog
        fields = [
            "title",
            "short_desc",
            "hero_blog",
            "home_visible",
            "banner_image",
            "card_image",
            "blog_content",

            "meta_title",
            "meta_description",
            "meta_keywords",

            'x',
            'y',
            'width',
            'height',
            'x1',
            'y1',
            'width1',
            'height1',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Heading'}),
            'short_desc': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Short Description'}),
            'hero_blog': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'home_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'meta_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Description'}),
            'meta_keywords': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Example keyword1, keyword 2'}),
        }

class TestimonialAddForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = [
            "name",
            "city",
            "photo",
            "words",
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'City'}),
            'photo': forms.FileInput(attrs={}),
            'words': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5}),
        }

class TestimonialEditForm(forms.ModelForm):
    photo = forms.FileField(widget=forms.FileInput(attrs={}), required=False)
    class Meta:
        model = Testimonial
        fields = [
            "name",
            "city",
            "photo",
            "words",
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'City'}),
            # 'photo': forms.FileInput(attrs={'class': 'dropify', 'required':'false'}),
            'words': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5}),
        }

class FAQAddForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = [
            "question",
            "answere",
            "category",
        ]
        widgets = {
            'question': forms.Textarea(attrs={'class': 'form-control txtArea', 'placeholder':'Question', 'rows': 5}),
            'answere': forms.Textarea(attrs={'class': 'form-control txtArea', 'placeholder':'Answer', 'rows': 5}),
            # 'category': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category' : forms.CheckboxSelectMultiple(),
        }

class VisaAddForm(forms.ModelForm):
    # country= forms.CharField(widget=forms.Select(choices=COUNTRY_CHOICES, attrs={'class': 'form-control'}))
    description = forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control'}))
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Visa
        fields = [
            "country",
            # "price",
            "banner_image",
            "card_image",
            "document",
            "description",

            "meta_title",
            "meta_description",
            "meta_keywords",

            'x',
            'y',
            'width',
            'height',
            'x1',
            'y1',
            'width1',
            'height1',
        ]
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            # 'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Price'}),
            'banner_image': forms.FileInput(attrs={ 'id':'banner_image'}),
            'card_image': forms.FileInput(attrs={'id':'card_image'}),

            'meta_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Description'}),
            'meta_keywords': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Example keyword1, keyword 2'}),
        }

class VisaEditForm(forms.ModelForm):
    banner_image = forms.FileField(widget=forms.FileInput(attrs={'id':'banner_image'}), required=False)
    card_image = forms.FileField(widget=forms.FileInput(attrs={'id':'card_image'}), required=False)
    document = forms.FileField(widget=forms.FileInput(attrs={}), required=False)
    

    description = forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control'}))
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Visa
        fields = [
            "country",
            # "price",
            "banner_image",
            "card_image",
            "document",
            "description",

            "meta_title",
            "meta_description",
            "meta_keywords",

            'x',
            'y',
            'width',
            'height',
            'x1',
            'y1',
            'width1',
            'height1',
        ]
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            # 'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Price'}),
            # 'banner_image': forms.FileInput(attrs={'class': 'dropify', 'id':'banner_image'}, required=False),
            # 'card_image': forms.FileInput(attrs={'class': 'dropify', 'id':'card_image'}, required=False),
            # 'document': forms.FileInput(attrs={'class': 'form-control file-upload-default'}, required=False),
            'meta_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Description'}),
            'meta_keywords': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Example keyword1, keyword 2'}),
        }

class TypesOfVisaForm(forms.ModelForm):
    class Meta:
        model = TypesOfVisa
        fields = [
            "id",
            "visa_name",
            "processing_time",
            "stay_period",
            "validity",
            "entry",
            "fees",
        ]
        widgets = {
            # 'id': forms.HiddenInput(attrs={'class': 'formset-field'}),
            'visa_name': forms.TextInput(attrs={'class': 'formset-field form-control', 'placeholder': 'Max 30 characters'}),
            'processing_time': forms.TextInput(attrs={'class': 'formset-field form-control', 'placeholder': 'Max 30 characters'}),
            'stay_period': forms.TextInput(attrs={'class': 'formset-field form-control', 'placeholder': 'Max 30 characters'}),
            'validity': forms.TextInput(attrs={'class': 'formset-field form-control', 'placeholder': 'Max 30 characters'}),
            'entry': forms.TextInput(attrs={'class': 'formset-field form-control', 'placeholder': 'Max 30 characters'}),
            'fees': forms.TextInput(attrs={'class': 'formset-field form-control', 'placeholder': 'Max 30 characters'}),
        }

class VacationAddForm(forms.ModelForm):
    overview_content = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control'}))
    experience_content = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control'}))
    information_content = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control'}))

    # banner_image = forms.FileField(widget=forms.FileInput(attrs={'class': 'file-upload-default', 'id':'banner_image'}))
    # card_image = forms.FileField(widget=forms.FileInput(attrs={'class': 'file-upload-default', 'id':'card_image'}))

    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    
    x1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height1 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    x2 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y2 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width2 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height2 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    # For Gallary
    # x3 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # y3 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # width3 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # height3 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    # x4 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # y4 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # width4 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # height4 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # x5 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # y5 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # width5 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # height5 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    # x6 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # y6 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # width6 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # height6 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # x7 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # y7 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # width7 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # height7 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    # x8 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # y8 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # width8 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # height8 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # x9 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # y9 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # width9 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # height9 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    # x10 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # y10 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # width10 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # height10 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    # x11 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # y11 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # width11 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # height11 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    
    class Meta:
        model = Vacation
        fields = [
            "title",
            "category",
            "home_visible",
            "vacation_label",
            "hero_tour",
            "tour_price",
            "tour_discounted_price",
            "day_in_tour",
            "night_in_tour",
            "banner_image",
            "card_image",
            "poster_image",
            "services",
            "overview_content",
            "experience_content",
            "information_content",

            "meta_title",
            "meta_description",
            "meta_keywords",

            'x',
            'y',
            'width',
            'height',

            'x1',
            'y1',
            'width1',
            'height1',
            
            'x2',
            'y2',
            'width2',
            'height2',
        ]
        widgets = {
            'category' : forms.CheckboxSelectMultiple(),
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Name of the Tour (Max 64 characters)'}),
            'home_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'vacation_label': forms.Select(),
            'hero_tour': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tour_price': forms.TextInput(attrs={'class': 'form-control'}),
            'tour_discounted_price': forms.TextInput(attrs={'class': 'form-control'}),
            'day_in_tour': forms.NumberInput(attrs={'class': 'form-control'}),
            'night_in_tour': forms.NumberInput(attrs={'class': 'form-control'}),
            'services': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Example: Food, Luxury Rooms, Gala Dinner'}),
            'banner_image': forms.FileInput(attrs={ 'id':'banner_image'}),
            'card_image': forms.FileInput(attrs={'id':'card_image'}),
            'poster_image': forms.FileInput(attrs={'id':'poster_image'}),

            'meta_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Description'}),
            'meta_keywords': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Example keyword1, keyword 2'}),
        }
        def split_tags(self):
            return self.tags.split(',')


class VacationEditForm(forms.ModelForm):
    overview_content = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control'}))
    experience_content = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control'}))
    information_content = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control'}))

    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)

    x1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height1 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    x2 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y2 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width2 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height2 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    card_image = forms.FileField(widget=forms.FileInput(attrs={'id':'card_image'}), required=False)
    banner_image = forms.FileField(widget=forms.FileInput(attrs={'id':'banner_image'}), required=False)
    poster_image = forms.FileField(widget=forms.FileInput(attrs={'id':'poster_image'}), required=False)

    class Meta:
        model = Vacation
        fields = [
            "title",
            "category",
            "home_visible",
            "vacation_label",
            "hero_tour",
            "tour_price",
            "tour_discounted_price",
            "day_in_tour",
            "night_in_tour",
            "card_image",
            "banner_image",
            "poster_image",
            "services",
            "overview_content",
            "experience_content",
            "information_content",

            "meta_title",
            "meta_description",
            "meta_keywords",

            'x',
            'y',
            'width',
            'height',
            
            'x1',
            'y1',
            'width1',
            'height1',

            'x2',
            'y2',
            'width2',
            'height2',
        ]
        widgets = {
            'category' : forms.CheckboxSelectMultiple(),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'home_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'vacation_label': forms.Select(),
            'hero_tour': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tour_price': forms.TextInput(attrs={'class': 'form-control'}),
            'tour_discounted_price': forms.TextInput(attrs={'class': 'form-control'}),
            'day_in_tour': forms.NumberInput(attrs={'class': 'form-control'}),
            'night_in_tour': forms.NumberInput(attrs={'class': 'form-control'}),
            'services': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Example: Food, Luxury Rooms, Gala Dinner'}),
            # 'banner_image': forms.FileInput(attrs={'id':'banner_image'}),
            # 'card_image': forms.FileInput(attrs={'id':'card_image'}),
            # 'poster_image': forms.FileInput(attrs={'id':'poster_image'}),

            'meta_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Description'}),
            'meta_keywords': forms.Textarea(attrs={'class': 'form-control txtArea', 'rows': 5, 'placeholder':'Example keyword1, keyword 2'}),
        }
        def split_tags(self):
            return self.tags.split(',')
        

class ItinerarySectionModelForm(forms.ModelForm):
    # description = forms.CharField(widget=CKEditorWidget(attrs={'class':'formset-field'}))
    class Meta:
        model = ItinerarySectionModel
        fields = [
        "heading",
        "description",
        "breakfast",
        "lunch",
        "dinner",
        "stay_in_hotel",
        ]
        widgets = {
            'heading': forms.TextInput(attrs={'class': 'formset-field form-control','placeholder':'Heading (Max 64 characters)'}),
            'description': forms.Textarea(attrs={'class': 'formset-field form-control txtArea','placeholder':'Description', 'rows': 5}),
            'breakfast': forms.CheckboxInput(attrs={'class': 'formset-field'}),
            'lunch': forms.CheckboxInput(attrs={'class': 'formset-field'}),
            'dinner': forms.CheckboxInput(attrs={'class': 'formset-field'}),
            'stay_in_hotel': forms.CheckboxInput(attrs={'class': 'formset-field'}),
        }

class GallaryModelForm(forms.ModelForm):  
    # gallary_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'formset-field gallary_image'}), required=False)    
    class Meta:
        model = GallaryModel
        fields = ['gallary_image', ]
        widgets = {
            'gallary_image': forms.FileInput(attrs={'class': 'formset-field '}),
        }


class CorporateHeadingForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width1 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height1 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    x2 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y2 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width2 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height2 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x3 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y3 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width3 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height3 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    x4 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y4 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width4 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height4 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x5 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y5 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width5 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height5 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    x6 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y6 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width6 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height6 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x7 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y7 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width7 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height7 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    x8 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y8 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width8 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height8 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x9 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y9 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width9 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height9 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    x10 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y10 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width10 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height10 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    x11 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y11 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width11 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height11 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x12 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y12 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width12 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height12 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    x13 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y13 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width13 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height13 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x14 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y14 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width14 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height14 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    x14 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y14 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width14 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height14 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    x15 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y15 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width15 = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height15 = forms.FloatField(widget=forms.HiddenInput(), required=False)

    meetings_content = forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control '}))
    conferences_content = forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control'}))
    class Meta:
        model = CorporateHeading
        fields = [
            "meetings_content",
            "conferences_content",
            'x',
            'y',
            'width',
            'height',
            'x1',
            'y1',
            'width1',
            'height1',
            'x2',
            'y2',
            'width2',
            'height2',
            'x3',
            'y3',
            'width3',
            'height3',
            'x4',
            'y4',
            'width4',
            'height4',
            'x5',
            'y5',
            'width5',
            'height5',
            'x6',
            'y6',
            'width6',
            'height6',
            'x7',
            'y7',
            'width7',
            'height7',
            'x8',
            'y8',
            'width8',
            'height8',
            'x9',
            'y9',
            'width9',
            'height9',
            'x10',
            'y10',
            'width10',
            'height10',
            'x11',
            'y11',
            'width11',
            'height11',
            'x12',
            'y12',
            'width12',
            'height12',
            'x13',
            'y13',
            'width13',
            'height13',
            'x14',
            'y14',
            'width14',
            'height14',
            'x15',
            'y15',
            'width15',
            'height15',
        ]

class CorporateIncentivesForm(forms.ModelForm):
    class Meta:
        model = CorporateIncentives
        fields = [
            "heading",
            "heading_image",

        ]
        widgets = {
            'heading': forms.TextInput(attrs={'class': 'formset-field form-control', 'placeholder':'Heading'}),
            'heading_image': forms.FileInput(attrs={'class': 'formset-field'}),
        }

class CorporateEventForm(forms.ModelForm):
    class Meta:
        model = CorporateEvent
        fields = [
            "heading",
            "heading_image",
            
        ]
        widgets = {
            'heading': forms.TextInput(attrs={'class': 'formset-field form-control', 'placeholder':'Heading'}),
            'heading_image': forms.FileInput(attrs={'class': 'formset-field '}),
        }
