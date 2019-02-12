from django.contrib import admin
from django import forms
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model


from nomadgram.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()

# model 컬럼 추가시 여기서도 추가 해줘야 함 
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", 
                    {"fields": 
                        ("name","followers","following","profile_image","bio","website", "gender", 'push_token')
                    }
                ),
    ) + auth_admin.UserAdmin.fieldsets
    
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])