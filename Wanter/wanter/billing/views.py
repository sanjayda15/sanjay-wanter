from django.shortcuts import render, redirect
import stripe
from django.http import JsonResponse, HttpResponse
from .models import BillingProfile,Card

from django.utils.http import is_safe_url

stripe.api_key = "sk_test_51HKHvFEL1aolqJrtCtFXgyp1KxFAWYxo7SgKA7mOsgPlaxPIRv4E1Kl3uIAcOrLdEkCJg7pSmXra5curIYaalRr700SjecnYt0"


STRIPE_PUB_KEY = 'pk_test_51HKHvFEL1aolqJrts4JePzE9jyZpPm9X59Bb5tMkwnj6IBSdtApnL287iBBSRmdRn6HFPYlhpyw8pcpUFX88Dw9u00QbnQLdVI'


def payment_method_view(request):
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect("/cart")
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url": next_url})

def payment_method_createview(request):
    if request.method == "POST" and request.is_ajax():
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message": "Cannot find this user"}, status_code=401)
        token = request.POST.get("token")
        if token is not None:
            new_card_obj = Card.objects.add_new(billing_profile, token)
        return JsonResponse({"message": " Success! Your card was added."})
    return HttpResponse("error", status_code=401)


# Create your views here.
