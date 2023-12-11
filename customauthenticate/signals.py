from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import CustomUser,Code


@receiver(post_save,sender = CustomUser)
def create_code(sender, instance, created, **kwargs):
    if created:
        print(">>>>> working......")
        Code.objects.create(user=instance)
