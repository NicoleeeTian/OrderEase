from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from.models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    # @receiver(post_save, sender=User): this function should be called after the save() method of a User model instant is executed
    # sender: the model calss that sends the signal. User is the sender here
    # instace: the actual instance of the sender that is being saved
    # created: a boolean flag that indicates whether this is a new instance or an update
    # **kwargs: a dictionary containing any additional keyword arguments
    if created:
        # So when the user is created, the User Profile is also created
        UserProfile.objects.create(user=instance)
        print('User profile is created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # When you first create User, then update to have a UserProfile. 
            # Then if you delete UserProfile without delete the User, it will reach this line
            UserProfile.objects.create(user=instance)
            print('Profile was not exist, but I created one')
        print('User is updated')

@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender,instance,**kwargs):
    # print(instance.username,'this user is being saved')
    pass