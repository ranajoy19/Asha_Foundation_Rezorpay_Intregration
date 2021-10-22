from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings


from .models import *
import razorpay
import requests


# Create your views here.

def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        amount =request.POST.get("amount")
        client = razorpay.Client(auth=("rzp_test_oSIBkN6Dsp7SoM", "ct4MP8vajSouvKYlCivQqdxu"))

        payment = client.order.create({"amount":int(amount)*100,"currency": "INR","payment_capture":'1'})
        print(payment)
        donation= Donation(name=name,email=email,amount=amount,payment_id= payment['id'])
        donation.save()
        content={"payment":payment,"donation":donation}
        return render(request, 'Payment_index.html', content)
    return render(request,'Payment_index.html',)


def base(request):

    return render(request,'base.html')


@csrf_exempt
def payment(request):
    if request.method == "POST":
        a=request.POST
        print(a)
        order_id=''
        for key,val in a.items():
            if key=='razorpay_order_id':
                order_id=val
                break
        user=Donation.objects.filter(payment_id=order_id).first()
        user.paid= True
        user.save()

        msg_plain = render_to_string('email.txt')

        msg_html= render_to_string('email.html')

        send_mail("your donation has been received", msg_plain, settings.EMAIL_HOST_USER,
                  [user.email], html_message=msg_html
                  )

    return render(request,'success_payment.html')


def DonerList(request):
    donation=Donation.objects.filter(paid=True)
    context={'donation':donation}
    return render(request,'list.html',context)
