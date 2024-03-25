# THIS PAGE INSERT ALL DETAILS OF OUR APPINFO MODEL ON ALL THE PAGES OF THE WEBSITE
# AFTER THIS PAGE, GO TO SETTINGS.PY TO ADD IT TO TEMPLATES

# watch context_processor video under pagination video in the django car app by emmanuel eseigbe

from .models import AppInfo, Category


def horbital(request):
    info = AppInfo.objects.get(pk=2)
    cat = Category.objects.all()

    context = {
        'info': info,
        'cat':cat,
    }

    return context