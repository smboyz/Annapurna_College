from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from adminpanel.models import GlobalSettings, Navigation, ContactUS, Forms
from django.contrib import messages
from django.core.paginator import Paginator


def base(request):
    pop = True
    glob = GlobalSettings.objects.all()
    pop = Navigation.objects.filter(status='Publish', page_type='Popup')
    sli = Navigation.objects.filter(status='Publish', page_type='Slider').order_by('position')
    abo = Navigation.objects.filter(status='Publish', page_type='Home/About').order_by('position')
    pro = Navigation.objects.filter(status='Publish', page_type='Program').order_by('position')
    pro_1 = Navigation.objects.filter(status='Publish', page_type='Program_1').order_by('position')
    why = Navigation.objects.filter(status='Publish', page_type='Why').order_by('position')
    why_1 = Navigation.objects.filter(status='Publish', page_type='Why_1').order_by('position')
    why_2 = Navigation.objects.filter(status='Publish', page_type='Why_2').order_by('position')
    why_3 = Navigation.objects.filter(status='Publish', page_type='Why_3').order_by('position')
    why_4 = Navigation.objects.filter(status='Publish', page_type='Why_4').order_by('position')
    why_5 = Navigation.objects.filter(status='Publish', page_type='Why_5').order_by('position')
    why_6 = Navigation.objects.filter(status='Publish', page_type='Why_6').order_by('position')
    why_7 = Navigation.objects.filter(status='Publish', page_type='Why_7').order_by('position')
    why_8 = Navigation.objects.filter(status='Publish', page_type='Why_8').order_by('position')
    why_9 = Navigation.objects.filter(status='Publish', page_type='Why_9').order_by('position')
    tes = Navigation.objects.filter(status='Publish', page_type='Testimonials').order_by('position')
    tes_1 = Navigation.objects.filter(status='Publish', page_type='Testimonials_1').order_by('position')
    gall = Navigation.objects.filter(status='Publish', page_type='Home/Gallery').order_by('position')
    gall_1 = Navigation.objects.filter(status='Publish', page_type='Gallery_3').order_by('position')

    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "national/home.html", {'pop':pop,'sli':sli,'glob':glob,'abo':abo,'pro':pro,'gall':gall,
                                                  'pro_1':pro_1,'why':why,'why_1':why_1,'why_2':why_2,
                                                  'why_3':why_3,'why_4':why_4,'why_5':why_5,'tes':tes,'tes_1':tes_1,
                                                  'why_6':why_6,'why_7':why_7,'why_8':why_8,'why_9':why_9,
                                                  'main':main,"gall_1":gall_1,'pop':pop}) 

def redirect_to_url(request, name):
    if name == '94':
       return redirect('about')
    elif name == '142':
        return redirect('contact')
    elif name == '149':
        return redirect('admission')
    elif name == '149':
        return redirect('newsevents')
    elif name == '100':
        return redirect('plus2Program')
    elif name == '101':
        return redirect('bachelor')
    elif name == '136':
        return redirect('photogallery')
    elif name == '137':
        return redirect('videoGallery')
    
    
    else:
        return HttpResponse("Id not Matched")
    
def about(request):
    glob = GlobalSettings.objects.all()
    abo = Navigation.objects.filter(status='Publish', page_type='About').order_by('position')
    abo_1 = Navigation.objects.filter(status='Publish', page_type='About_1').order_by('position')
    abo_2 = Navigation.objects.filter(status='Publish', page_type='About_2').order_by('position')
    abo_3 = Navigation.objects.filter(status='Publish', page_type='About_3').order_by('position')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "national/about.html",{'glob':glob,'abo':abo,'abo_1':abo_1,'abo_2':abo_2,
                                                  'abo_3':abo_3,'main':main})

def plus2Program(request):
    glob = GlobalSettings.objects.all()
    plus2 = Navigation.objects.filter(status='Publish', page_type='+2 Program').order_by('position')
    sub = Navigation.objects.filter(status='Publish', page_type='SubjectTitle').order_by('position')
    sci = Navigation.objects.filter(status='Publish', page_type='Science').order_by('position')
    sci_1 = Navigation.objects.filter(status='Publish', page_type='Science_1').order_by('position')
    man = Navigation.objects.filter(status='Publish', page_type='Management').order_by('position')
    man_1 = Navigation.objects.filter(status='Publish', page_type='Management_1').order_by('position')
    hum = Navigation.objects.filter(status='Publish', page_type='Humanities').order_by('position')
    hum_1 = Navigation.objects.filter(status='Publish', page_type='Humanities_1').order_by('position')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "national/plus2Program.html",{'glob':glob,'plus2':plus2,'sub':sub,'sci':sci,
                                                        'sci_1':sci_1,'man':man,'man_1':man_1,'hum':hum,
                                                        'hum_1':hum_1,'main':main})

def bachelor(request):
    glob = GlobalSettings.objects.all()
    bac = Navigation.objects.filter(status='Publish', page_type='Bachelors Program').order_by('position')
    sub = Navigation.objects.filter(status='Publish', page_type='SubjectTitle_1').order_by('position')
    bbs = Navigation.objects.filter(status='Publish', page_type='BBS').order_by('position')
    bbs_1 = Navigation.objects.filter(status='Publish', page_type='BBS_1').order_by('position')
    bba = Navigation.objects.filter(status='Publish', page_type='BBA').order_by('position')
    bba_1 = Navigation.objects.filter(status='Publish', page_type='BBA_1').order_by('position')
    bsc = Navigation.objects.filter(status='Publish', page_type='Bsc.CSIT').order_by('position')
    bsc_1 = Navigation.objects.filter(status='Publish', page_type='Bsc.CSIT_1').order_by('position')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "national/bachelorprogram.html",{'glob':glob,'bac':bac,'sub':sub,'bbs':bbs,
                                                        'bbs_1':bbs_1,'bba':bba,'bba_1':bba_1,'bsc':bsc,
                                                        'bsc_1':bsc_1,'main':main})

def photogallery(request):
    glob = GlobalSettings.objects.all()
    gall = Navigation.objects.filter(status='Publish', page_type='Gallery').order_by('position')
    gall_1 = Navigation.objects.filter(status='Publish', page_type='Gallery_3').order_by('position')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    gallery = Navigation.objects.filter(status='Publish', page_type='Gallery_3')
    gallery = gallery.order_by('-id')
    paginator = Paginator(gallery, 12)  # Show 6 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "national/photoGallery.html",{'glob':glob,'gall':gall,'main':main,'gall_1':gall_1,
                                                    'page_obj':page_obj})

# def photogallery1(request, id):
#     glob = GlobalSettings.objects.all()
#     gall = Navigation.objects.filter(status='Publish', page_type='Gallery').order_by('position')
#     gallery = Navigation.objects.filter(status='Publish', id=id)
#     main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

#     return render(request, "national/photoGallery1.html",{'glob':glob,'gall':gall,'main':main,'gallery ':gallery})

def videoGallery(request):
    glob = GlobalSettings.objects.all()
    vid = Navigation.objects.filter(status='Publish', page_type='Video').order_by('position')
    vid_1 = Navigation.objects.filter(status='Publish', page_type='Video_1').order_by('position')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    video = Navigation.objects.filter(status='Publish', page_type='Video_1')
    video = video.order_by('-id')
    paginator = Paginator(video, 6)  # Show 6 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, "national/videoGallery.html",{'glob':glob,'main':main,'vid':vid,'vid_1':vid_1,
                                                    'page_obj':page_obj})

def admission(request):
    glob = GlobalSettings.objects.all()
    adm = Navigation.objects.filter(status='Publish', page_type='Admission').order_by('position')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        dateofbirth=request.POST.get('dateofbirth')        
        mobile=request.POST.get('mobile')
        province=request.POST.get('province')
        district=request.POST.get('district')
        municipality=request.POST.get('municipality')
        ward_no=request.POST.get('ward_no')
        tole=request.POST.get('tole')
        province_1=request.POST.get('province_1')
        district_1=request.POST.get('district_1')
        municipality_1=request.POST.get('municipality_1')
        ward_no_1=request.POST.get('ward_no_1')
        tole_1=request.POST.get('tole_1')
        father_name=request.POST.get('father_name')
        father_no=request.POST.get('father_no')
        mother_name=request.POST.get('mother_name')
        mother_no=request.POST.get('mother_no')
        school_name=request.POST.get('school_name')
        pass_year=request.POST.get('pass_year')
        score=request.POST.get('score')
        shift=request.POST.get('shift')
        science=request.POST.get('science')
        management=request.POST.get('management')
        humanities=request.POST.get('humanities')
        transport=request.POST.get('transport')
        hostel=request.POST.get('hostel')
        destination=request.POST.get('destination')
        passport_image=request.FILES.get('passport_image')
        certificate=request.FILES.get('certificate')
        businesss=request.POST.get('businesss')
        computerscis=request.POST.get('computerscis')
        hotelmanagements=request.POST.get('hotelmanagements')
        t_ms=request.POST.get('t_ms')
        socialmath=request.POST.get('socialmath')
        masscomms=request.POST.get('masscomms')
        sociologys=request.POST.get('sociologys')
        t_mhs=request.POST.get('t_mhs')
        populations=request.POST.get('populations')
        rurals=request.POST.get('rurals')
        biologys=request.POST.get('biologys')
        computers=request.POST.get('computers')
        ways=request.POST.get('ways')


        if (name and len(name) >= 2) and (email and len(email) >= 3) and (gender and len(gender) >= 3) and (dateofbirth and len(dateofbirth) >= 4) and (mobile and len(mobile) >= 2) and (province and len(province) >= 2) and (district and len(district) >= 3) and (municipality and len(municipality) >= 4) and (ward_no and len(ward_no) >= 2) and (tole and len(tole) >= 2) and (province_1 and len(province_1) >= 3) and (district_1 and len(district_1) >= 4) and (municipality_1 and len(municipality_1) >= 2) and (ward_no_1 and len(ward_no_1) >= 2) and (tole_1 and len(tole_1) >= 3) and (father_name and len(father_name) >= 4) and (father_no and len(father_no) >= 2) and (mother_name and len(mother_name) >= 2) and (mother_no and len(mother_no) >= 3) and (school_name and len(school_name) >= 4) and (pass_year and len(pass_year) >= 2) and (score and len(score) >= 2) and (shift and len(shift) >= 4) and (science and len(science) >= 2) and (management and len(management) >= 2) and (humanities and len(humanities) >= 2) and (transport and len(transport) >= 2) and (hostel and len(hostel) >= 2) and (destination and len(destination) >= 2) and (passport_image and len(passport_image) >= 2) and (certificate and len(certificate) >= 2) and (businesss and len(businesss) >= 2) and (computerscis and len(computerscis) >= 2) and (hotelmanagements and len(hotelmanagements) >= 2) and (t_ms and len(t_ms) >= 2) and (socialmath and len(socialmath) >= 2) and (masscomms and len(masscomms) >= 2) and (sociologys and len(sociologys) >= 2) and (t_mhs and len(t_mhs) >= 2) and (populations and len(populations) >= 2) and (rurals and len(rurals) >= 2) and (biologys and len(biologys) >= 2) and (computers and len(computers) >= 2) and (ways and len(ways) >= 2):
            messages.error(request,"Cannot submit your form. Something went wrong.",)

        else:
            admi=Forms(name=name,email=email,gender=gender,dateofbirth=dateofbirth,mobile=mobile,province=province,
                        district=district,municipality=municipality,ward_no=ward_no,tole=tole,province_1=province_1,
                        district_1=district_1,municipality_1=municipality_1,ward_no_1=ward_no_1,tole_1=tole_1,
                        father_name=father_name,father_no=father_no,mother_name=mother_name,mother_no=mother_no,
                        school_name=school_name,pass_year=pass_year,score=score,shift=shift,science=science,
                        management=management,humanities=humanities,transport=transport,hostel=hostel,
                        destination=destination,businesss=businesss,computerscis=computerscis,hotelmanagements=hotelmanagements,
                        t_ms=t_ms,socialmath=socialmath,masscomms=masscomms,sociologys=sociologys,t_mhs=t_mhs,populations=populations,
                        rurals=rurals,biologys=biologys,computers=computers,ways=ways)
            if passport_image:
                admi.passport_image = passport_image
    
            if certificate:
                admi.certificate = certificate

            admi.save()
            messages.success(request,"Successfully submitted your Forms. We will contact you soon...",)
            
    return render(request, "national/admission.html",{'glob':glob,'adm':adm,'main':main})

def newsevents(request):
    glob = GlobalSettings.objects.all()
    new = Navigation.objects.filter(status='Publish', page_type='New/Event').order_by('position')
    new_1 = Navigation.objects.filter(status='Publish', page_type='New/Event_1').order_by('position')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    news = Navigation.objects.filter(status='Publish', page_type='New/Event_1')
    news = news.order_by('-id')
    paginator = Paginator(news, 6)  # Show 6 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "national/news&events.html",{'glob':glob,'new':new,'new_1':new_1,'main':main,
                                                  'page_obj':page_obj})

def event(request,id):
    glob = GlobalSettings.objects.all()
    new_1 = Navigation.objects.filter(status='Publish', id=id).order_by('position')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "national/event.html",{'glob':glob,'new_1':new_1,'main':main})

def contact(request):
    glob = GlobalSettings.objects.all()
    conn = Navigation.objects.filter(status='Publish', page_type='Contact').order_by('position')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        if len(name)<2 or len(email)<3 or len(subject)<4 or len(message)<2:
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            con=ContactUS(name=name,email=email,subject=subject,message=message)
            con.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request, "national/contact.html",{'glob':glob,'conn':conn,'main':main})

def why(request):
    glob = GlobalSettings.objects.all()
    why = Navigation.objects.filter(status='Publish', page_type='Why').order_by('position')
    why_1 = Navigation.objects.filter(status='Publish', page_type='Why_1').order_by('position')
    why_2 = Navigation.objects.filter(status='Publish', page_type='Why_2').order_by('position')
    why_3 = Navigation.objects.filter(status='Publish', page_type='Why_3').order_by('position')
    why_4 = Navigation.objects.filter(status='Publish', page_type='Why_4').order_by('position')
    why_5 = Navigation.objects.filter(status='Publish', page_type='Why_5').order_by('position')
    why_6 = Navigation.objects.filter(status='Publish', page_type='Why_6').order_by('position')
    why_7 = Navigation.objects.filter(status='Publish', page_type='Why_7').order_by('position')
    why_8 = Navigation.objects.filter(status='Publish', page_type='Why_8').order_by('position')
    why_9 = Navigation.objects.filter(status='Publish', page_type='Why_9').order_by('position')
    why_10= Navigation.objects.filter(status='Publish', page_type='Why_10').order_by('position')
    why_11 = Navigation.objects.filter(status='Publish', page_type='Why_11').order_by('position')
    why_12 = Navigation.objects.filter(status='Publish', page_type='Why_12').order_by('position')
    why_13 = Navigation.objects.filter(status='Publish', page_type='Why_13').order_by('position')
    why_14 = Navigation.objects.filter(status='Publish', page_type='Why_14').order_by('position')
    why_15= Navigation.objects.filter(status='Publish', page_type='Why_15').order_by('position')
    why_16 = Navigation.objects.filter(status='Publish', page_type='Why_16').order_by('position')
    why_17 = Navigation.objects.filter(status='Publish', page_type='Why_17').order_by('position')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')


    return render(request, "national/whytochooseus.html",{'glob':glob,'why':why,'why_1':why_1,'why_2':why_2,
                                                          'why_3':why_3,'why_4':why_4,'why_5':why_5,'why_6':why_6,
                                                          'why_7':why_7,'why_8':why_8,'why_9':why_9,'why_10':why_10,
                                                          'why_11':why_11,'why_12':why_12,'why_13':why_13,'why_14':why_14,
                                                          'why_15':why_15,'why_16':why_16,'why_17':why_17,'main':main})