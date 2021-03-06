# 1. 1.8 to 1.10 and 1.10+ to 2 template rendering

<https://stackoverflow.com/questions/43787700/django-1-11-typeerror-context-must-be-a-dict-rather-than-context>

In [Django 1.8+](https://docs.djangoproject.com/en/1.11/releases/1.8/#dictionary-and-context-instance-arguments-of-rendering-functions), the template's `render` method takes a dictionary for the `context` parameter. Support for passing a `Context` instance [is deprecated](https://docs.djangoproject.com/en/1.11/releases/1.10/#features-removed-in-1-10), and gives an error in Django 1.10+.

In your case, just use a regular `dict` instead of a `Context` instance:

```
message = get_template('email_forms/direct_donation_form_email.html').render(ctx)
```

You may prefer to use the [`render_to_string`](https://docs.djangoproject.com/en/1.11/topics/templates/#django.template.loader.render_to_string) shortcut:

```
from django.template.loader import render_to_string

message = render_to_string('email_forms/direct_donation_form_email.html', ctx)
```

# 2. django URL

`<int: hours>` would help us check the type of parameter

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('time/', views.current_datetime),
    # <int: hours> would help us check the type of parameter
    path('time/plus/<int:hours_offset>', views.hours_ahead),

]
```

# 3. Django.db 外键

2.0 需要声明 'on_delete'.

具体其他参数地址可参考：<https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.ForeignKey.on_delete>
