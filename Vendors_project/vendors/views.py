from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from django.contrib.auth.decorators  import login_required
from django.utils import timezone

def home(request):
    vendors = Vendors.objects.all()
    context = {'vendors':vendors}
    return render(request, 'vendors/dashboard.html', context)

def vendor_details(request):
    vendors = Vendors.objects.all()
    context = {'vendors':vendors}
    return render(request, 'vendors/vendor_detail.html', context)

def vendor_contacts(request):
    contacts = Contacts.objects.all()
    context = {'contacts':contacts}
    return render(request, 'vendors/vendor_contact.html', context)

def create(request):
    if request.method == 'POST':
        if request.POST['vendorname'] and request.POST['phone'] and request.POST['fax'] and request.POST['website'] and request.POST['addressline1']  and request.POST['city'] and request.POST['state'] and request.POST['zip'] and request.POST['country'] and request.POST['ein'] and request.POST['consultants'] and request.POST['preferredvendors'] and request.POST['dateofagreement'] and request.POST['agreementstatus']:
            vendor = Vendors()
            vendor.name = request.POST['vendorname']
            vendor.phone_number = request.POST['phone']
            vendor.fax = request.POST['fax']
            if request.POST['website'].startswith('http://') or request.POST['website'].startswith('https://'):
                vendor.website = request.POST['website']
            else:
                vendor.website = 'http://' + request.POST['website']
            vendor.address1 = request.POST['addressline1']
            vendor.address2 = request.POST['addressline2']
            vendor.city = request.POST['city']
            vendor.state = request.POST['state']
            vendor.zipp = request.POST['zip']
            vendor.country = request.POST['country']
            vendor.ein = request.POST['ein']
            vendor.no_of_consultants = request.POST['consultants']
            vendor.preferred_vendor = request.POST['preferredvendors']
            vendor.date = request.POST['dateofagreement']
            vendor.agreement_status = request.POST['agreementstatus']
            
            vendor.save()
            return redirect('/vendors/' + str(vendor.id))
        else:
            return render(request, 'vendors/vendor.html',{'error':'All fields are required.'})
    else:
        return render(request, 'vendors/vendor.html')

def detail(request, vendor_id):
    vendor = get_object_or_404(Vendors, pk=vendor_id)
    return render(request, 'vendors/detail.html',{'vendor':vendor})

def contact(request):
    print(request.POST)
    if request.method == 'POST':
        if request.POST['vname'] and request.POST['firstname'] and request.POST['lastname'] and request.POST['title'] and request.POST['deskphone'] and request.POST['email'] and request.POST['addressline1'] and request.POST['city'] and request.POST['state'] and request.POST['zip'] and request.POST['country'] and request.POST['speciality']: 
            contact = Contacts()
            contact.name = request.POST['vname']
            contact.first_name = request.POST['firstname']
            contact.last_name = request.POST['lastname']
            contact.title = request.POST['title']
            contact.desk_phone = request.POST['deskphone']
            contact.mobile = request.POST['mobile']
            contact.email = request.POST['email']
            contact.address1 = request.POST['addressline1']
            contact.address2 = request.POST['addressline2']
            contact.city = request.POST['city']
            contact.state = request.POST['state']
            contact.zipp = request.POST['zip']
            contact.country = request.POST['country']
            contact.speciality = request.POST['speciality']
            contact.save()
            return redirect('/vendors/contact_detail')
        else:
            return render(request,'vendors/contact.html',{'error':'All fields are required.'})
       
    else:
        contact = Contacts.objects.all()
        vendors = Vendors.objects.all().order_by('name')
        return render(request,'vendors/contact.html',{'vendors':vendors})
    
def contact_detail(request):
    return render(request, 'vendors/contact_detail.html')