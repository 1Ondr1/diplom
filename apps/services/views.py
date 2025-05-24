from django.shortcuts import render, redirect, get_object_or_404
from .models import Advertisement, AdImage
from .forms import AdForm
from django.contrib.auth.decorators import login_required

def services(request):
    ads = Advertisement.objects.all().order_by('-created_at')
    search_type = request.GET.get('search_type', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    min_area = request.GET.get('min_area', '')
    max_area = request.GET.get('max_area', '')

    filters_applied = False

    if search_type:
        ads = ads.filter(type=search_type)
        filters_applied = True

    if min_price:
        ads = ads.filter(price__gte=min_price)
        filters_applied = True
    
    if max_price:
        ads = ads.filter(price__lte=max_price)
        filters_applied = True

    if min_area:
        ads = ads.filter(area__gte=min_area)
        filters_applied = True

    if max_area:
        ads = ads.filter(area__lte=max_area)
        filters_applied = True

    сontext = {
        'ads': ads,
        'search_type': search_type,
        'min_price': min_price,
        'max_price': max_price,
        'min_area': min_area,
        'max_area': max_area,
        'filters_applied': filters_applied
    }

    return render(request, 'services.html', сontext)

@login_required
def create_ad(request):
    if request.method == 'POST':
        ad_form = AdForm(request.POST, request.FILES)
        if ad_form.is_valid():
            ad = ad_form.save(commit=False)
            ad.owner = request.user
            ad.save()
            if 'images' in request.FILES:
                for image in request.FILES.getlist('images'):
                    ad_image = AdImage(image=image)
                    ad_image.advertisement = Advertisement.objects.get(id=ad.id)
                    ad_image.save()
                    ad.images.add(ad_image)
            return redirect('services')
    else:
        ad_form = AdForm()
    return render(request, 'new_listing.html', {'ad_form': ad_form})

def ad_detail(request, ad_id):
    ad = Advertisement.objects.get(id=ad_id)
    images = ad.images.all()
    return render(request, 'advertisement.html', {'ad': ad, 'images': images})

@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Advertisement, id=ad_id, owner=request.user)
    images = ad.images.all()
    if request.method == 'POST':
        if 'save' in request.POST:
            ad_form = AdForm(request.POST, request.FILES, instance=ad)
            images_to_delete = request.POST.getlist('delete_images')
            if ad_form.is_valid():
                ad_form.save()
                for image_id in images_to_delete:
                    image = AdImage(id=image_id)
                    ad.images.remove(image)
                    image.delete()
                if 'images' in request.FILES:
                    for image in request.FILES.getlist('images'):
                        ad_image = AdImage.objects.create(image=image, advertisement=ad)
                        ad.images.add(ad_image)
                return redirect('ad_detail', ad_id=ad.id)
        elif 'delete' in request.POST:
            ad.delete()
            return redirect('services')
    else:
        ad_form = AdForm(instance=ad)
    return render(request, 'edit_ad.html', {'ad_form': ad_form, 'ad': ad, 'images': images})