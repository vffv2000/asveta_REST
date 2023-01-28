from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='прозвішча, імя')
    amount_courses = models.IntegerField(default=0, verbose_name='колькасць наведвальных курсаў')
    courses = models.ManyToManyField("Course",verbose_name="урок")
    mail=models.CharField(max_length=30, verbose_name="email адрес")# значчение email адрес уже подтягивается из формы
    phone=models.CharField(max_length=30, verbose_name="номер телефона")# Так же было бы хорошо если подтягивали номер телефона
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вучань'
        verbose_name_plural = 'Вучнi'


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='прозвішча, імя')
    specialization = models.CharField(max_length=30, verbose_name='спецыялізацыя', blank=True)
    education = models.CharField(max_length=20, blank=True,verbose_name='адукацыя')
    work_experience = models.IntegerField(blank=True, verbose_name='стаж')
    amount_courses = models.IntegerField(default=0, verbose_name='колькасць курсаў')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Настаўнік'
        verbose_name_plural = 'Настаўнікі'


class Course(models.Model):
    subject = models.CharField(max_length=20, verbose_name='прадмет' )
    grade = models.IntegerField(default=0, verbose_name='клас')
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, verbose_name='настаўнік')
    time_lesson = models.TimeField(verbose_name='час правядзення')
    amount_studens = models.IntegerField(default=0, verbose_name='колькасць вучаняў зараз')
    is_full=models.BooleanField(default=False, verbose_name="Группа укомплектована")#С помощью этой строки будет легче выбирать группы в которые ещё требуются ученики по сравнению со стокой ниже. 
    # Или если если потребуется уменьшить группы или наооборот
    #amount_places = models.IntegerField(default=5, verbose_name='ўсяго месц')


    def __str__(self):
        return f"{self.subject} {self.grade} клас"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
