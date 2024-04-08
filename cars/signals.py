import os
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from cars.models import Cars


def delete_cover(instace):
    try:
        os.remove(instace.cover.path) 
    except (ValueError, FileNotFoundError):
        ...


@receiver(pre_delete, sender=Cars)
def car_cover_delete(sender, instance, *args, **kwargs):
    old_instance = Cars.objects.filter(pk=instance.pk).first()
    
    if old_instance:
        delete_cover(old_instance)


@receiver(pre_save, sender=Cars)
def car_cover_save(sender, instance, *args, **kwargs):
    old_instance = Cars.objects.filter(pk = instance.pk).first()

    new_instance = old_instance.cover != instance.cover

    if not old_instance:
        return

    if new_instance:
        delete_cover(old_instance)