from django.db import models
# from django.utils import timezone

class GlobalSettings(models.Model):
    SiteName = models.CharField(max_length=100)
    SiteContact = models.CharField(max_length=100)
    SiteEmail = models.EmailField()
    SiteAddress = models.CharField(max_length=500)
    Sitedescription = models.CharField(max_length=500)
    Sitelicence = models.CharField(max_length=300)
    Sitetwitterlink = models.CharField(max_length=300)
    Sitefacebooklink = models.CharField(max_length=300)
    Sitelinkdinlink = models.CharField(max_length=300)
    Siteinstagramlink = models.CharField(max_length=300, null=True)
    Sitewhatsapplink = models.CharField(max_length=300)
    Sitefax = models.CharField(max_length=300,null=True)
    logo = models.ImageField(upload_to="Global/",max_length=200, null=True, default=None)
    back_image = models.ImageField(upload_to="Global/",null=True)
    brochure = models.FileField(upload_to="brochure/",null=True)
    brochure_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.SiteName

class ContactUS(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=1500,null=True)
    
    def __str__(self):
        return self.name
    
    

class Navigation(models.Model):
    PAGE_TYPE = (
        ('Home', 'Home'),('Slider','Slider'),('Home/About', 'Home/About'),('Normal','Normal'),
        ('Home/Gallery','Home/Gallery'),('Program', 'Program'),('Program_1', 'Program_1'),('About', 'About'),
        ('Why','Why'),('Why_1','Why_1'),('Why_2','Why_2'),('Why_3','Why_3'),('Why_4','Why_4'),('Why_5','Why_5'),
        ('Why_6','Why_6'),('Why_7','Why_7'),('Testimonials','Testimonials'),('Testimonials_1','Testimonials_1'),
        ('Why_8','Why_8'),('Why_9','Why_9'),('Why_10','Why_10'),('Why_11','Why_11'),('Why_12','Why_12'),('Why_13','Why_13'),
        ('Why_14','Why_14'),('Why_15','Why_15'),('Why_16','Why_16'),('Why_17','Why_17'),('About_1', 'About_1'),
        ('About_2', 'About_2'),('About_3', 'About_3'),('Science', 'Science'),('Management', 'Management'),('Humanities', 'Humanities'),
        ('BBS', 'BBS'),('BBA', 'BBA'),('Bsc.CSIT', 'Bsc.CSIT'),('+2 Program', '+2 Program'),('Bachelors Program', 'Bachelors Program'),
        ('SubjectTitle', 'SubjectTitle'),('SubjectTitle_1', 'SubjectTitle_1'),('Science_1', 'Science_1'),('Management_1', 'Management_1'),
        ('Humanities_1', 'Humanities_1'),('BBS_1', 'BBS_1'),('BBA_1', 'BBA_1'),('Bsc.CSIT_1', 'Bsc.CSIT_1'),('Gallery', 'Gallery'),
        ('Gallery_1', 'Gallery_1'),('Video', 'Video'),('Video_1', 'Video_1'),('Contact', 'Contact'),('New/Event', 'New/Event'),
        ('New/Event_1', 'New/Event_1'),('Admission', 'Admission'),('Popup', 'Popup'),('Gallery_2', 'Gallery_2'),
        ('Gallery_3', 'Gallery_3'),('Gallery_4', 'Gallery_4'),('Gallery_5', 'Gallery_5'),('Gallery_6', 'Gallery_6'),
    )

    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft')
    )
    name = models.CharField(max_length=100, null=False)
    caption = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS, max_length=50)
    position = models.IntegerField()
    page_type = models.CharField(choices=PAGE_TYPE, null=True, blank=True, max_length=50)
    title = models.CharField(max_length=200)
    short_desc = models.TextField(null=True)
    desc = models.TextField(null=True)
    bannerimage = models.ImageField(upload_to="abnner/",null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)
    icon_image = models.TextField(null=True)
    image = models.ImageField(upload_to="image/", null=True)
    video = models.FileField(upload_to="video/%y", null=True)
    slider_image = models.ImageField(upload_to="slider/", null=True)
    Parent = models.ForeignKey('self', related_name="childs", on_delete=models.CASCADE, null=True, blank=True)
    brochure = models.FileField(upload_to="brochure/",null=True)

    def __str__(self):
        return self.name


class Forms(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    passport_image = models.ImageField(upload_to="passport/",null=True)
    dateofbirth = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    ward_no = models.CharField(max_length=100)
    tole = models.CharField(max_length=100)
    province_1 = models.CharField(max_length=100)
    district_1 = models.CharField(max_length=100)
    municipality_1 = models.CharField(max_length=100)
    ward_no_1 = models.CharField(max_length=100)
    tole_1 = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    father_no = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_no = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    pass_year = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    certificate = models.FileField(upload_to="certificate/",null=True)
    shift = models.CharField(max_length=100)
    science = models.CharField(max_length=100, null=True)
    management  = models.CharField(max_length=100, null=True)
    humanities = models.CharField(max_length=100, null=True)
    transport = models.CharField(max_length=100, null=True)
    hostel = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=100, null=True)
    businesss = models.CharField(max_length=100, null=True)
    computerscis = models.CharField(max_length=100, null=True)
    hotelmanagements = models.CharField(max_length=100, null=True)
    t_ms = models.CharField(max_length=100, null=True)
    socialmath = models.CharField(max_length=100, null=True)
    masscomms = models.CharField(max_length=100, null=True)
    sociologys = models.CharField(max_length=100, null=True)
    t_mhs = models.CharField(max_length=100, null=True)
    populations =  models.CharField(max_length=100, null=True)
    rurals = models.CharField(max_length=100, null=True)
    biologys = models.CharField(max_length=100, null=True)
    computers = models.CharField(max_length=100, null=True)
    ways = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
    
class Gallery(models.Model):
    name = models.CharField(max_length=100)
    images = models.FileField(upload_to="gallery/", null=True, blank=True)

    def __str__(self):
        return self.name
    
# class Admin_Forms(models.Model):
#     name = models.CharField(max_length=100)
#     gender = models.CharField(max_length=100)
#     passport_image = models.ImageField(upload_to="passport/",null=True)
#     dateofbirth = models.CharField(max_length=100)
#     email = models.EmailField()
#     mobile = models.CharField(max_length=100)
#     province = models.CharField(max_length=100)
#     district = models.CharField(max_length=100)
#     municipality = models.CharField(max_length=100)
#     ward_no = models.CharField(max_length=100)
#     tole = models.CharField(max_length=100)
#     province_1 = models.CharField(max_length=100)
#     district_1 = models.CharField(max_length=100)
#     municipality_1 = models.CharField(max_length=100)
#     ward_no_1 = models.CharField(max_length=100)
#     tole_1 = models.CharField(max_length=100)
#     father_name = models.CharField(max_length=100)
#     father_no = models.CharField(max_length=100)
#     mother_name = models.CharField(max_length=100)
#     mother_no = models.CharField(max_length=100)
#     school_name = models.CharField(max_length=100)
#     pass_year = models.CharField(max_length=100)
#     score = models.CharField(max_length=100)
#     certificate = models.FileField(upload_to="certificate/",null=True)
#     shift = models.CharField(max_length=100)
#     science = models.CharField(max_length=100, null=True)
#     management  = models.CharField(max_length=100, null=True)
#     humanities = models.CharField(max_length=100, null=True)
#     transport = models.CharField(max_length=100, null=True)
#     hostel = models.CharField(max_length=100, null=True)
#     destination = models.CharField(max_length=100, null=True)
#     business = models.CharField(max_length=100, null=True)
#     computerscis = models.CharField(max_length=100, null=True)
#     hotelmanagements = models.CharField(max_length=100, null=True)
#     t_ms = models.CharField(max_length=100, null=True)
#     socialmath = models.CharField(max_length=100, null=True)
#     masscomms = models.CharField(max_length=100, null=True)
#     sociologys = models.CharField(max_length=100, null=True)
#     t_mhs = models.CharField(max_length=100, null=True)
#     populations =  models.CharField(max_length=100, null=True)
#     rurals = models.CharField(max_length=100, null=True)
#     biologys = models.CharField(max_length=100, null=True)
#     computers = models.CharField(max_length=100, null=True)
#     ways = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.name

