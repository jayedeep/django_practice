from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from datetime import datetime

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'phone_number', 'username', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_of_birth','custom_age']
    search_fields = ('name', 'email')  # Add fields to be searchable
    list_filter = ('name', 'email')  # Add filters for the list view
    date_hierarchy = 'created_at'  # Add a date-based hierarchy navigation
    readonly_fields = ('custom_age',)

    fieldsets = (
        ('Main Information', {
            'fields': ('name', 'email'),
        }),
        ('Additional Information', {
            'fields': ('date_of_birth',),
        }),
    )

    def custom_age(self, obj):
        current_date = datetime.now()

        age = current_date.year - obj.date_of_birth.year - (
                    (current_date.month, current_date.day) < (obj.date_of_birth.month, obj.date_of_birth.day))

        return f'{age}'

    actions = ['custom_action']

    def custom_action(self, request, queryset):
        # Your custom logic goes here
        print(">>>queryse>>>\n\n\n",queryset)
        selected_count = queryset.count()
        self.message_user(request, f'{selected_count} objects processed successfully.')


admin.site.register(Student, StudentAdmin)



class BookInline(admin.StackedInline):  # or admin.StackedInline for a different display
    model = Book
    extra = 1  # Number of empty forms to display

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)