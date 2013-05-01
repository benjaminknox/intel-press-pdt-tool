from django.contrib.auth.decorators import login_required, user_passes_test


def not_in_student_group(user):
    if user:
        return user.groups.filter(name='Student').count() == 0
    return False