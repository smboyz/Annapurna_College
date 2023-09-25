from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import GlobalSettings, ContactUS, Navigation, Forms, Gallery
from django.contrib.auth.decorators import login_required
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate,Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from io import BytesIO
from django.core.paginator import Paginator


def admin_login(request):
    glob = GlobalSettings.objects.all()
    try:
        # messages.info(request, 'Account not found')
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")         
            user_obj = User.objects.filter(username = username)
            
            if not user_obj.exists():
                messages.info(request, "Account not found")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            print(username, password)
            user_obj = authenticate(username = username, password = password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect("dashboard")
          
            messages.info(request, "Invalid password")
            return redirect('/')
                    
        return render(request, "login.html", {'glob':glob})
       
    except Exception as e:
        print(e)
        # Add a proper response in case of an exception
        return HttpResponse("An error occurred")

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    glob = GlobalSettings.objects.all()

    return render(request, "dashboard.html", {'glob':glob})

def Logoutpage(request):
    logout(request)
    return redirect("admin_login")

@login_required(login_url=settings.LOGIN_URL)
def globalsetting(request):
    glob = GlobalSettings.objects.all()
    try:
        data = GlobalSettings.objects.first()
    except GlobalSettings.DoesNotExist:
        data = None

    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        email = request.POST.get('email')
        description = request.POST.get('description')
        licence = request.POST.get('licence')
        twitterlink = request.POST.get('twitterlink')
        facebooklink = request.POST.get('facebooklink')
        linkdinlink = request.POST.get('linkdinlink')
        instagramlink = request.POST.get('instagramlink')
        whatsapplink = request.POST.get('whatsapplink')
        logo = request.FILES.get('logo')
        back_image = request.FILES.get('back_image')
        brochure = request.FILES.get('brochure')
        fax = request.POST.get('fax')
        brochure_name = request.POST.get('brochure_name')

        if data is None:
            # Create a new GlobalSettings object
            data = GlobalSettings(SiteName=name, SiteContact=contact, SiteAddress=address, SiteEmail=email,
                                  Sitedescription=description,Sitelicence=licence,Sitetwitterlink=twitterlink,
                                  Sitefacebooklink=facebooklink,Sitelinkdinlink=linkdinlink,Siteinstagramlink=instagramlink,
                                  Sitewhatsapplink=whatsapplink,Sitefax=fax,brochure_name=brochure_name,)
        else:
            # Update existing GlobalSettings object
            data.SiteName = name
            data.SiteContact = contact
            data.SiteAddress = address
            data.SiteEmail = email
            data.Sitedescription = description
            data.Sitelicence = licence
            data.Sitetwitterlink = twitterlink
            data.Sitefacebooklink = facebooklink
            data.Sitelinkdinlink = linkdinlink
            data.Siteinstagramlink = instagramlink
            data.Sitewhatsapplink = whatsapplink
            data.Sitefax = fax
            data.brochure_name=brochure_name

        if logo:
            # Set the uploaded image to the 'logo' field
            data.logo = logo
        if brochure:
            # Set the uploaded image to the 'logo' field
            data.brochure = brochure
        if back_image:
            data.back_image = back_image
        
        data.save()

        return redirect('globalsetting')  # Redirect to the same view after saving the data

    return render(request, "globalsetting.html", {"data": data, 'glob' : glob})

@login_required(login_url=settings.LOGIN_URL)
def contactus(request):
    glob = GlobalSettings.objects.all()
    con=ContactUS.objects.all()
    

    dels = ContactUS.objects.all()
    dels = dels.order_by('-id')
    paginator = Paginator(dels, 10)  # Show 6 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
 
    return render(request, "contactus.html",{'con':con, 'glob' : glob, 'page_obj':page_obj})

@login_required(login_url=settings.LOGIN_URL)
def delete_contact(request):
    if request.method == "POST":
        # Check if "selected_items" is in the POST data
        selected_items = request.POST.getlist('selected_items[]')
        
        if selected_items:
            # Loop through the selected items and delete them
            for item_pk in selected_items:
                con = get_object_or_404(ContactUS, pk=item_pk)
                con.delete()

    return redirect('contactus')
    # con = get_object_or_404(ContactUS, pk=pk)

    # if request.method == "POST":
    #     con.delete()
    #     return redirect('contactus')

    # return redirect('contactus')

@login_required(login_url=settings.LOGIN_URL)
def main_navigation(request, parent_id=None):
    glob=GlobalSettings.objects.all()
        
    if parent_id:
        obj = Navigation.objects.filter(Parent=parent_id).order_by('position')
    else:
        obj = Navigation.objects.filter(Parent = None).order_by('position')
 
    return render(request, "main_navigation.html", {'obj':obj, 'parent_id':parent_id,'glob':glob})

@login_required(login_url=settings.LOGIN_URL)
def navigation_list(request, parent_id=None):
    glob = GlobalSettings.objects.all()
    obj = Navigation.objects.all()

    if request.method == "POST":
        # Retrieve form data
        # next = request.POST.get('next','/')
        name = request.POST.get('name')
        caption = request.POST.get('caption')
        status = request.POST.get('status')
        position = request.POST.get('position')
        page_type = request.POST.get('page_type')
        title = request.POST.get('title')
        short_desc = request.POST.get('short_desc')
        bannerimage = request.FILES.get('bannerimage')
        brochure = request.FILES.get('brochure')
        meta_title = request.POST.get('meta_title')
        meta_keyword = request.POST.get('meta_keyword')
        icon_image = request.POST.get('icon_image')
        slider_image = request.FILES.get('slider_image')
        parent_id = request.POST.get('Parent')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        if parent_id:
            parent_navigation = Navigation.objects.get(pk=parent_id)
        else:
            parent_navigation = None

        # Create a new Navigation objectj
        obj = Navigation.objects.create(
            name=name,
            caption=caption,
            status=status,
            position=position,
            page_type=page_type,
            title=title,
            short_desc=short_desc,
            meta_title=meta_title,
            meta_keyword=meta_keyword,
            desc=desc,
            image=image,
            icon_image=icon_image,
            Parent=parent_navigation,  # Assign parent navigation object
        )
        # obj.Parent = Navigation.objects.filter(id=parent_id)

        # Set uploaded images
        if bannerimage:
            obj.bannerimage = bannerimage
        if video:
            obj.video = video
        if image:
            obj.image = image
        if slider_image:
            obj.slider_image = slider_image
        if brochure:
            obj.brochure = brochure

        obj.save()  # Save the new Navigation object to the database

        obj = Navigation.objects.all()  # Update the navigation list with the new object

        if parent_id:
            return redirect('main_navigation', parent_id=parent_id )
        else:
            return redirect('main_navigation')
      

    return render(request, 'navigation.html',{'obj': obj, 'glob' : glob, 'parent_id':parent_id})

@login_required(login_url=settings.LOGIN_URL)
def update(request, pk):
    glob = GlobalSettings.objects.all()
    data = get_object_or_404(Navigation, pk=pk)

    if request.method == "POST":
        name=request.POST.get('name')
        caption=request.POST.get('caption')
        status=request.POST.get('status')
        position=request.POST.get('position')
        page_type=request.POST.get('page_type')
        title=request.POST.get('title')
        short_desc=request.POST.get('short_desc')
        desc=request.POST.get('desc')
        bannerimage=request.FILES.get('bannerimage')
        meta_title=request.POST.get('meta_title')
        meta_keyword=request.POST.get('meta_keyword')
        icon_image=request.POST.get('icon_image')
        slider_image=request.FILES.get('slider_image')
        brochure = request.FILES.get('brochure')
        parent_id = request.POST.get('Parent')
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        

        if parent_id:
            parent_navigation = Navigation.objects.get(pk=parent_id)
        else:
            parent_navigation = None

        
        # Update the object with the form data
        data.name = name
        data.caption = caption
        data.status = status
        data.position = position
        data.page_type = page_type
        data.title = title
        data.short_desc = short_desc
        data.meta_title = meta_title
        data.meta_keyword = meta_keyword
        data.desc = desc
        data.Parent=parent_navigation
        data.icon_image=icon_image
        
        
        if bannerimage:
            data.bannerimage = bannerimage

        if video:
            data.video=video
        
        if image:
            data.image = image

        if slider_image:
            data.slider_image = slider_image
        
        if brochure:
            data.brochure = brochure
        
        data.save()

        if parent_id:
            return redirect('main_navigation', parent_id=parent_id )
        else:
            return redirect('main_navigation')
        
    parent_id = data.Parent.id if data.Parent else None

    return render(request, 'update.html', {'data': data,'glob':glob,'parent_id':parent_id})

@login_required(login_url=settings.LOGIN_URL)
def delete_nav(request, pk):
    obj = get_object_or_404(Navigation, pk=pk)
    parent_id = None

    if request.method == "POST":
        parent_id = obj.Parent.id if obj.Parent else None
        obj.delete()

    if parent_id:
        return redirect('main_navigation', parent_id=parent_id)
    else:
        return redirect('main_navigation')
    
    # return render(request, 'delete.html', {'obj': obj})

@login_required(login_url=settings.LOGIN_URL)
def admission_1(request,pk):
    glob = GlobalSettings.objects.all()
    # conn=Forms.objects.all()
    con = get_object_or_404(Forms, pk=pk)
 
    return render(request, "admission_1.html",{'glob' : glob,'con':con})

@login_required(login_url=settings.LOGIN_URL)
def admissions(request):
    glob = GlobalSettings.objects.all()
    con=Forms.objects.all()

    admi = Forms.objects.all()
    admi = admi.order_by('-id')
    paginator = Paginator(admi, 10)  # Show 6 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, "admissions.html",{'glob':glob,'con':con,'page_obj':page_obj})

@login_required(login_url=settings.LOGIN_URL)
def delete_admissions(request):
    if request.method == "POST":
        # Check if "selected_items" is in the POST data
        selected_items = request.POST.getlist('selected_items')
        
        if selected_items:
            # Loop through the selected items and delete them
            for item_pk in selected_items:
                con = get_object_or_404(Forms, pk=item_pk)
                con.delete()

    return redirect('admissions')
    # con = get_object_or_404(Forms, pk=pk)

    # if request.method == "POST":
    #     con.delete()
    #     return redirect('admissions')

    # return redirect('admissions')

def generate_pdf(request, pk):
    # Retrieve the form data
    form = get_object_or_404(Forms, pk=pk)
    
    # Create a PDF file in memory (BytesIO)
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []

    # Define the desired table width (in inches)
    table_width = 4  # Adjust this value as needed

    # Create a list of fields and their values, excluding fields with None values
    form_fields = [
        ("Full Name", form.name),
        ("Gender", form.gender),
        ("Date of Birth", form.dateofbirth),
        ("Email", form.email),
        ("Mobile", form.mobile),
        ("Province", form.province),
        ("District", form.district),
        ("Municipality", form.municipality),
        ("Ward No", form.ward_no),
        ("Tole", form.tole),
        ("Province 1", form.province_1),
        ("District 1", form.district_1),
        ("Municipality 1", form.municipality_1),
        ("Ward No 1", form.ward_no_1),
        ("Tole 1", form.tole_1),
        ("Father Name", form.father_name),
        ("Father Number", form.father_no),
        ("Mother Name", form.mother_name),
        ("Mother Number", form.mother_no),
        ("School Name", form.school_name),
        ("Pass Year", form.pass_year),
        ("Score", form.score),
        ("Shift", form.shift),
        ("Science", form.science),
        ("Management", form.management),
        ("Humanities", form.humanities),
        ("Transport", form.transport),
        ("Hostel", form.hostel),
        ("Destination", form.destination),
        ("Business", form.businesss),
        ("Computerscience", form.computerscis),
        ("Hotelmanagement", form.hotelmanagements),
        ("TM", form.t_ms),
        ("Social Math", form.socialmath),
        ("Mass_Comm", form.masscomms),
        ("Socialgoy", form.sociologys),
        ("T_M", form.t_mhs),
        ("Population", form.populations),
        ("Rural", form.rurals),
        ("Biology", form.biologys),
        ("Com_Science", form.computers),
        ("Way", form.ways),
        # Add more fields as needed
    ]

    # Filter out fields with None values
    form_fields = [(field, value) for field, value in form_fields if value is not None]

    # Create the table and set its style
    table = Table(form_fields, colWidths=[table_width * inch, 3 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Add the table to the PDF
    story.append(table)
    
    # Build the PDF document
    doc.build(story)
    
    buffer.seek(0)
    
    # Create a response with the PDF file
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{pk}.pdf"'
    
    return response


@login_required(login_url=settings.LOGIN_URL)
def gallery(request):
    glob = GlobalSettings.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        images = request.FILES.getlist('images')

        for image in images:
            Gallery.objects.create(
                name=name,
                images=image,
            )

    images = Gallery.objects.all()

    print(images)
       
    return render(request, "gallery.html", {'glob': glob,'images':images})

@login_required(login_url=settings.LOGIN_URL)
def gallery_1(request):
    glob = GlobalSettings.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        images = request.FILES.getlist('images')

        new = Gallery.objects.create(
            name=name,
        )

        # Handle multiple image uploads
        for image in images:
            new.images.create(images=image)

    return render(request, "gallery_1.html", {'glob': glob})

@login_required(login_url=settings.LOGIN_URL)
def delete_gall(request, pk):
    images = get_object_or_404(Gallery, pk=pk)

    if request.method == "POST":
        images.delete()
        return redirect('gallery_1')

    return redirect('gallery_1')
