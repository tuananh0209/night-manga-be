from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import User


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = False

    class Meta(UserChangeForm.Meta):
        model = User

    def save(self, commit=True):
        instance = super().save(commit)
        return instance


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)


# class CustomPasswordResetForm(PasswordResetForm):
#     def save(
#         self,
#         domain_override=None,
#         subject_template_name="registration/password_reset_subject.txt",
#         email_template_name="registration/password_reset_email.html",
#         use_https=False,
#         token_generator=None,
#         from_email=None,
#         request=None,
#         html_email_template_name=None,
#         extra_email_context=None,
#     ):
#         """
#         Generate a one-use only link for resetting password and send it to the
#         user.
#         """
#         email = self.cleaned_data["email"]
#         for user in self.get_users(email):
#             if not domain_override:
#                 current_site = get_current_site(request)
#                 site_name = current_site.name
#                 domain = current_site.domain
#             else:
#                 site_name = domain = domain_override
#
#             otp = random_with_n_digits(6)
#             ResetPasswordOTP.objects.filter(user=user).delete()
#             ResetPasswordOTP.objects.create(user=user, otp=otp)
#
#             context = {
#                 "email": email,
#                 "domain": domain,
#                 "site_name": site_name,
#                 "user": user,
#                 "otp": otp,
#                 "protocol": "https" if use_https else "http",
#                 **(extra_email_context or {}),
#             }
#             self.send_mail(
#                 subject_template_name,
#                 email_template_name,
#                 context,
#                 from_email,
#                 email,
#                 html_email_template_name=html_email_template_name,
#             )
