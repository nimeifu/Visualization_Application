import base64
import io

from django.shortcuts import render
from django.db import connection
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import seaborn as sns
from .models import Restaurant


# Create your views here.
def index(request):
    context = {
        'title': 'Home Page',
        'heading': 'Welcome to Home page!',
        'content': 'This is some content for Home page.',
    }
    return render(request, 'index.html', context)


def home(request):
    return render(request, 'home.html')


def karaoke_data(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM karaoke")
        karaokes = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(karaokes, columns=columns)
    plt.figure(figsize=(12, 8))
    sns.barplot(data=df, x="NumberPeople", y="Hours", color="pink")

    plt.title("Karaoke Hours by Number of People", fontsize=14)
    plt.xlabel("Number of People", fontsize=10)
    plt.ylabel("Hours", fontsize=10)
    plt.ylim(0, 10)

    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    karaoke_room_data = base64.b64encode(buf.getvalue()).decode()

    context = {
        'karaokes': karaokes,
        'room_data': karaoke_room_data
    }

    return render(request, 'karaoke.html', context)


def orders_data(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(orders, columns=columns)

    df['TimePlaced'] = pd.to_datetime(df['TimePlaced'])

    plt.figure(figsize=(12, 8))
    plt.hist(df['TimePlaced'].dt.hour, bins=range(0, 25), color='skyblue', width=0.9)

    plt.xticks(range(25))
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Orders')
    plt.title('Number of Orders Placed by Hour')
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    order_time_data = base64.b64encode(buf.getvalue()).decode()

    plt.figure(figsize=(12, 8))
    plt.boxplot(x=df['Cost'], vert=False, patch_artist=True,
                boxprops=dict(facecolor="skyblue"))
    plt.xlabel('Cost($)')
    plt.title('Range of Order Costs')
    plt.tight_layout()

    plt.savefig(buf, format='png')
    buf.seek(0)
    order_cost_data = base64.b64encode(buf.getvalue()).decode()

    context = {
        'orders': orders,
        'time_data': order_time_data,
        'cost_data': order_cost_data
    }

    return render(request, 'order.html', context)


def restaurant_data(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM restaurant")
        restaurants = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

    # restaurants = Restaurant.objects.all()
  

    context = {
        'restaurants': restaurants,
        'columns': columns
    }

    return render(request, 'restaurant.html', context)
