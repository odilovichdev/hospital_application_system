
def application_list(request):
    if request.user.is_authenticated:
        applications = request.user.applications.all()
    else:
        applications = []
    return {"applications": applications}
