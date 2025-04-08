from django.shortcuts import render , redirect
from .forms import OrderArtForm
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def place_order(request):

    if request.method == 'POST':
        form = OrderArtForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            if 'submit' in request.POST:
                # Send email to the chosen artist
                # subject = f"New Art Order from {request.user.username}"
                # message = f"Hello,\n\nYou have a new order for an artwork:\n\n"
                # message += f"Title: {order.art_name}\nStory: {order.story}\n"
                # message += f"\nPlease contact the client for further details."
                

                # send_mail(
                # subject,
                # message,
                # 'your_email@example.com',  # Replace with your email
                # [order.artist_email],
                # fail_silently=False,
                # )

                messages.success(request, "Your order has been placed and sent to the artist.")
                return redirect('home')
    
    else:
        form = OrderArtForm(initial={'user': request.user})
    
    return render(request, 'order/neworderart.html', {'form': form})

