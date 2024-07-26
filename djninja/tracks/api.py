from ninja import NinjaAPI

api = NinjaAPI()

#create normal Python functions using api.get()
# similar to Fast-API 
@api.get("/test")
def test(request):
    # django-ninja automatically serializes to JSON
    return {'test': 'success'}