from django.contrib import admin

from finances.models import FinancialTransaction, TransactionParcel



class TransactionParcelInline(admin.TabularInline):
    model = TransactionParcel
    extra = 1
    min = 1


class FinancialTransactionAdmin(admin.ModelAdmin):
    inlines = [TransactionParcelInline]
    




admin.site.register(FinancialTransaction, FinancialTransactionAdmin)