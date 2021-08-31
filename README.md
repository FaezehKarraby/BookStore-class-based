# BookStore

CMD:
python manage.py runserver

BROWSER:
صفحه اصلی :
127.0.0.1:8000/
    ورود :
    127.0.0.1:8000/account/login/
        خروج :
        127.0.0.1:8000/account/logout/
        پروفایل :
        127.0.0.1:8000/account/profile/new/
            ویرایش :
            127.0.0.1:8000/account/profile/<int:pk>/edit/
    ثبتنام :
    127.0.0.1:8000/account/signup/
    محصولات :
    127.0.0.1:8000/product/
        ثبت دسته بندی جدید :
        127.0.0.1:8000/product/create/
        کتاب :
        127.0.0.1:8000/product/books/
            انتخاب کتاب :
            127.0.0.1:8000/product/books/<int:pk>
            ثبت کتاب جدید :
            127.0.0.1:8000/product/books/create/
            
