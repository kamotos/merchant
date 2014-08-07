from billing import Gateway
from billing.gateway import GatewayNotConfigured
from django.conf import settings
from payzone import PayZoneClient


class PayzoneGateway(Gateway):
    display_name = "Payzone"
    homepage_url = "http://www.payzone.ma"

    def __init__(self, *args, **kwargs):
        merchant_settings = getattr(settings, "MERCHANT_SETTINGS", {})
        payzone_settings = merchant_settings.get("payzone", None)
        if not merchant_settings or not payzone_settings:
            raise GatewayNotConfigured("The '%s' gateway is not correctly "
                                       "configured." % self.display_name)

        self.payzone = PayZoneClient(**payzone_settings)

    def purchase(self, money, credit_card=None, options=None):
        response = self.payzone.transaction.create(**options)


