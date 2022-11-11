در ابتدا بر روی برنچ main فایل main.py را با استفاده از دستور touch می سازیم و کامیت می کنیم و سپس بر روی گیت هاب قرار می دهیم.
<p align="center">
<img src="https://github.com/yasmansh/SE_LAB2/blob/alimohammadiamirhossein-patch-1/gozaresh/pic1.png" height="600">
</p>

<p align="center">
<img src="https://github.com/yasmansh/SE_LAB2/blob/alimohammadiamirhossein-patch-1/gozaresh/pic2.png" height="600">
</p>

سپس فایل مربوط به merge_sort را ایجاد می کنیم و آن را پوش می کنیم. سپس نوبت به این می رسد که یک برنچ جدید به اسم dev بسازیم و حال در
این برنچ تغییراتی بر روی merge_sort می دهیم تا با برنچ main امان کانفلیکت داشته باشد. 

<p align="center">
<img src="https://github.com/yasmansh/SE_LAB2/blob/alimohammadiamirhossein-patch-1/gozaresh/pic4.png" height="600">
</p>

حال وقتی روی برنچ dev هستیم یک pul request به برنچ main می زنیم و به دلیل وجود conflict پروسه ی pull ما fail می شود. حال از دستور $git mergetool$ استفاده می کنیم.
پس از وارد کردن دستور با صفحه زیر مواجه می شویم که هر دو کد را پشت سر هم آورده است.

<p align="center">
<img src="https://github.com/yasmansh/SE_LAB2/blob/alimohammadiamirhossein-patch-1/gozaresh/pic5.png" height="600">
</p>

بخش هایی از دو کد که می خواهیم در ورژن نهایی باشد را انتخاب می کنیم و سپس دکمه Esc را فشار می دهیم و :wq را وارد می کنیم تا تغییرات ذخیره شود.

<p align="center">
<img src="https://github.com/yasmansh/SE_LAB2/blob/alimohammadiamirhossein-patch-1/gozaresh/pic5.png" height="600">
</p>

و سپس می توان دید که pull با موفقیت انجام شد.

<p align="center">
<img src="https://github.com/yasmansh/SE_LAB2/blob/alimohammadiamirhossein-patch-1/gozaresh/pic7.png" height="600">
</p>

کد ها را تکمیل تر می کنیم که پروسه ی تکمیل شدنشان در کامیت ها موجود است. سپس یک باگ در کد اصلی بر روی برنچ اصلی را در برنچ hotfix حل می کنیم و مشابه روند بالا 
مشکل کانفلیکت را با mergetool بر طرف می کنیم.

<p align="center">
<img src="https://github.com/yasmansh/SE_LAB2/blob/alimohammadiamirhossein-patch-1/gozaresh/pic8.png" height="600">
</p>

<p align="center">
<img src="https://github.com/yasmansh/SE_LAB2/blob/alimohammadiamirhossein-patch-1/gozaresh/pic9.png" height="600">
</p>

