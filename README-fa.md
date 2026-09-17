# 🔍 تحلیل‌گر MAC Address

یک ابزار ساده و آموزشی با زبان **Python** برای اعتبارسنجی و تحلیل MAC Address.

هدف این پروژه، یادگیری بهتر ساختار MAC Address و مفاهیمی مانند اعداد Hexadecimal، Binary، OUI، NIC و عملیات Bitwise است.

## ✨ قابلیت‌ها

* اعتبارسنجی MAC Address بدون استفاده از Regex
* پشتیبانی از جداکننده‌های `:` و `-`
* بررسی تعداد گروه‌های MAC Address
* بررسی طول هر گروه
* بررسی معتبر بودن کاراکترهای Hexadecimal
* استخراج OUI
* استخراج NIC
* تبدیل MAC Address به Binary
* تبدیل MAC Address به Decimal
* نمایش طول MAC Address
* تشخیص Unicast / Multicast
* تشخیص Universally / Locally Administered

## 🧩 ساختار MAC Address

یک MAC Address استاندارد **48 بیت** طول دارد و از 6 گروه تشکیل می‌شود.

مثال:

```text
A4:5E:60:12:34:56
```

هر گروه شامل دو رقم Hexadecimal است.

هر رقم Hexadecimal برابر با 4 بیت است:

```text
A = 1010
4 = 0100
```

بنابراین:

```text
A4 = 10100100
```

هر گروه:

```text
2 × 4 = 8 bits
```

و کل MAC Address:

```text
6 × 8 = 48 bits
```

## 🏗️ OUI و NIC

به صورت ساده می‌توان MAC Address را به دو بخش تقسیم کرد:

```text
A4:5E:60:12:34:56
└───────┘ └───────┘
   OUI       NIC
  24 bits    24 bits
```

### OUI

OUI مخفف:

**Organizationally Unique Identifier**

است.

OUI شامل 24 بیت اول MAC Address است و یک محدوده آدرس اختصاص‌یافته به یک سازمان یا تولیدکننده را مشخص می‌کند.

مثال:

```text
A4:5E:60
```

### NIC

بخش باقی‌مانده:

```text
12:34:56
```

در فضای آدرس اختصاص‌یافته برای شناسایی رابط‌ها استفاده می‌شود.

## 🔢 تبدیل به Binary

برنامه هر گروه Hexadecimal را به دقیقاً 8 بیت تبدیل می‌کند.

مثال:

```text
A4 = 10100100
5E = 01011110
60 = 01100000
12 = 00010010
34 = 00110100
56 = 01010110
```

نتیجه:

```text
10100100:01011110:01100000:00010010:00110100:01010110
```

در Python از این روش استفاده شده است:

```python
f"{value:08b}"
```

`08b` باعث می‌شود هر گروه دقیقاً 8 رقم باینری داشته باشد و صفرهای ابتدایی نیز حفظ شوند.

## 🧮 تبدیل به Decimal

کل MAC Address را می‌توان به عنوان یک مقدار 48 بیتی Hexadecimal در نظر گرفت.

مثلاً:

```text
A4:5E:60:12:34:56
```

به شکل:

```text
A45E60123456
```

در نظر گرفته شده و سپس به Decimal تبدیل می‌شود.

## 📡 Unicast / Multicast

اولین Byte شامل یک بیت به نام **I/G Bit** است.

برنامه این بیت را با:

```python
FirstByte & 1
```

بررسی می‌کند.

نتیجه:

```text
0 → Unicast
1 → Multicast
```

## 🌐 Universal / Local

اولین Byte همچنین شامل **U/L Bit** است.

برنامه این بیت را با:

```python
FirstByte & 2
```

بررسی می‌کند.

نتیجه:

```text
0 → Universally Administered
1 → Locally Administered
```

## 🛡️ اعتبارسنجی MAC Address

این پروژه برای Validation از **Regex استفاده نمی‌کند**.

برنامه موارد زیر را بررسی می‌کند:

* تعداد گروه‌ها
* طول هر گروه
* معتبر بودن کاراکترهای Hexadecimal
* ساختار کلی MAC Address

نمونه‌های معتبر:

```text
A4:5E:60:12:34:56
A4-5E-60-12-34-56
a4:5e:60:12:34:56
```

نمونه‌های نامعتبر:

```text
A4:5E:60:12:34
A4:5E:60:12:34:567
A4:5E:60:12:34:GG
A4:5E:60:12:34:5
A4:5E:60:12:34:56:78
```

## 🧪 مثال

### ورودی

```text
A4:5E:60:12:34:56
```

### خروجی

```text
MAC Address    : A4:5E:60:12:34:56
OUI            : A4:5E:60
NIC            : 12:34:56
Binary         : 10100100:01011110:01100000:00010010:00110100:01010110
Decimal        : ...
Bits           : 48
Type           : Unicast
Administration : Universally Administered
```

## 🐍 مفاهیم Python استفاده‌شده

در این پروژه با مفاهیم زیر تمرین شده است:

* Functions
* Strings
* Lists
* Loops
* Conditional Statements
* String Manipulation
* Hexadecimal
* Binary
* Bitwise Operations
* Input Validation

## 🚀 قابلیت‌های آینده

در نسخه‌های بعدی می‌توان قابلیت‌های زیر را اضافه کرد:

* OUI → Vendor Lookup
* استفاده از دیتابیس OUI مربوط به IEEE
* نمایش Bit-by-Bit
* ساخت MAC Address تصادفی
* Command-Line Arguments
* خروجی JSON
* پشتیبانی از فرمت‌های بیشتر MAC Address

## 🎯 هدف پروژه

این پروژه با هدف **یادگیری Python و مفاهیم Networking** ساخته شده است.

هدف اصلی این است که MAC Address را فقط به صورت یک String نبینیم، بلکه آن را به عنوان یک **مقدار 48 بیتی** بررسی کنیم و بفهمیم بخش‌ها و بیت‌های مختلف آن چه اطلاعاتی دارند.

[🇬🇧 English Version](README.md)