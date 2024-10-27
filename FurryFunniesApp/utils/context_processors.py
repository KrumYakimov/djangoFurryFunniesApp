from FurryFunniesApp.utils.profile_helpers import get_profile


def profile_exists(request):
    profile = get_profile()
    return {
        'profile_exists': profile is not None
    }
