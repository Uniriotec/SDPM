# -*- coding: utf-8 -*-
"""
    finances.models
    ~~~~~~~~~~~~~~

    Has the content related to models for finances.
    
    :copyright: (c) 2012 by Arruda.
"""

import datetime
from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices

from utils.abs_models import Abs_Named_Model

        
class TransactionTypeAwareManager(models.Manager):
    """
    Manager for Transaction that knows how to deal with the credit and debit proxies
    """
    def __init__(self, type=None, *args, **kwargs):
        super(TransactionTypeAwareManager, self).__init__(*args, **kwargs)
        self.type = type
    
    def get_query_set(self):
        qq = super(TransactionTypeAwareManager, self).get_query_set()
        if self.type:
            qq = qq.filter(transaction_type=self.type)
            
        return qq
    
    
class FinancialTransaction(Abs_Named_Model):
    """Represents a financial transaction:
    
        name: the name of this transaction, something that explains where the money is comming or going to.
        project: the project that this transaction is related to.
        transaction_type: if its a debit or credit.        
        
        --
        start_date: The date of the first parcel.
        end_date: The date of the last parcel.
        total: The sum of all parcel's values
    """
    
    TRANSACTION_TYPE = Choices(
                            ('d', 'debit', _('Debit')),
                            ('c', 'credit', _('Credit')),
                            )
    
    project = models.ForeignKey('projects.Project')
    
    transaction_type = models.CharField(_('Transaction Type'), choices=TRANSACTION_TYPE, default=TRANSACTION_TYPE.debit, max_length=2)
  
    description = models.TextField(_('Description'))
  
    objects = TransactionTypeAwareManager()  
    class Meta:
        app_label = 'finances'
    
    
class DebitTransaction(FinancialTransaction):
    
    class Meta:
        app_label = 'finances'
        proxy = True
        
    objects = TransactionTypeAwareManager(type=FinancialTransaction.TRANSACTION_TYPE.debit)

    def save(self, *args, **kwargs):
        self.transaction_type = FinancialTransaction.TRANSACTION_TYPE.debit
        return super(CreditTransaction, self).save(*args, **kwargs)
    
class CreditTransaction(FinancialTransaction):
    
    class Meta:
        app_label = 'finances'
        proxy = True
        
    objects = TransactionTypeAwareManager(type=FinancialTransaction.TRANSACTION_TYPE.credit)

    def save(self, *args, **kwargs):
        self.transaction_type = FinancialTransaction.TRANSACTION_TYPE.credit
        return super(CreditTransaction, self).save(*args, **kwargs)
    
    
    
class TransactionParcel(models.Model):
    """
    It's a parcel from a transaction.
    """
    
    transaction = models.ForeignKey(FinancialTransaction,related_name='parcels')
    
    value = models.DecimalField(_("Value"),max_digits=12, decimal_places=2,default=Decimal("0"))
    
    date = models.DateField(_("Date"), default=datetime.date.today)
    
    class Meta:
        app_label = 'finances'
        ordering = ['date',]
    
    def __unicode__(self):
        return "% - %  - %s " % (self.transaction, self.date, self.value)
    