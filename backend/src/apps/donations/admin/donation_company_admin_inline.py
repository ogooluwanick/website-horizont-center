from django.contrib import admin

from apps.donations.models import DonationCompany


class DonationCompanyForm(admin.StackedInline):
    model = DonationCompany
    extra = 0
    min_num = 1
    max_num = 1
