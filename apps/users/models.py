"""
User models for authentication and user management
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    """Extended User model with additional fields"""
    
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'Regular User'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, default='India')
    
    # Account Details
    pan = models.CharField(max_length=20, unique=True, blank=True, null=True)
    aadhar = models.CharField(max_length=20, blank=True, null=True)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    
    # Account Status
    is_verified = models.BooleanField(default=False)
    is_active_trader = models.BooleanField(default=False)
    kyc_verified = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'users_customuser'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user_type']),
            models.Index(fields=['is_active_trader']),
        ]
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    @property
    def is_admin(self):
        return self.user_type == 'admin'
    
    def update_last_login(self):
        self.last_login_at = timezone.now()
        self.save(update_fields=['last_login_at'])


class UserProfile(models.Model):
    """Extended user profile for trading-specific information"""
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='trading_profile')
    account_number = models.CharField(max_length=50, unique=True)
    total_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    cash_available = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    margin_used = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    margin_available = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    
    # Trading Statistics
    total_trades = models.IntegerField(default=0)
    total_profit_loss = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    win_rate = models.FloatField(default=0.0)
    
    # Risk Settings
    daily_loss_limit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    max_position_size = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users_userprofile'
    
    def __str__(self):
        return f"{self.user.username} - {self.account_number}"


class CashCredit(models.Model):
    """Track cash credits and debits for users"""
    
    TRANSACTION_TYPE_CHOICES = (
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    )
    
    SOURCE_CHOICES = (
        ('settlement', 'Weekly Settlement'),
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('trade_profit', 'Trade Profit'),
        ('trade_loss', 'Trade Loss'),
        ('admin_adjustment', 'Admin Adjustment'),
    )
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cash_credits')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)
    reference_id = models.CharField(max_length=100, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users_cashcredit'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'created_at']),
            models.Index(fields=['source']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"
