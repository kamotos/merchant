from billing import Integration, get_gateway, IntegrationNotConfigured
from django.conf import settings
from django.conf.urls import patterns, url
#from billing.forms.payzone_forms import StripeForm


class StripeIntegration(Integration):
    display_name = "Stripe"
    template = "billing/payzone.html"

    def __init__(self):
        super(StripeIntegration, self).__init__()
        merchant_settings = getattr(settings, "MERCHANT_SETTINGS")
        if not merchant_settings or not merchant_settings.get("payzone"):
            raise IntegrationNotConfigured("The '%s' integration is not correctly "
                                       "configured." % self.display_name)
        payzone_settings = merchant_settings["payzone"]
        self.gateway = get_gateway("payzone")
        self.publishable_key = payzone_settings['PUBLISHABLE_KEY']

    def transaction(self, request):
        # Subclasses must override this
        raise NotImplementedError
