from django.db import models
from django.contrib.auth.models import User


# class UserProfile(models.Model):
#     group_number = models.TextField()
#     user = models.ForeignKey(User, unique=True)
    # def __str__(self):
    #     return self.user
class Skills(models.Model):
    class Meta():
        db_table = 'skills'

    # GITAR = '1'
    # BARABAN = '2'
    # RUN = '3'
    # REBUS = '4'
    # SKILL_CHOICES = (
    #     (GITAR, 'Игра на гитаре'),
    #     (BARABAN, 'Игра на барабане'),
    #     (RUN, 'Умение бегать'),
    #     (REBUS, 'Решать ребусы'),
    # )
    SKILL_MEDIA_CHOICES = (
        ('Спорт', (
            ('plavaniya', 'Плавания'),
            ('boibilding', 'Бодибилдинг'),
            ('beg', 'Бег'),
            ('sheiping', 'Шейпинг'),
            ('fitnes', 'Фитнес'),
            ('gimnastika', 'Гимнастика'),
            ('aerobika', 'Аэробика'),
            ('badmenton', 'Бадментон'),
            ('tennis', 'Теннис'),
            ('boevie iskusstva', 'Боевые искусства'),
            ('strel`ba', 'Стрельба'),
            ('futbol', 'Футбол'),
        )
         ),
        ('Наука', (
            ('Shahmati', 'Шахматы'),
            ('Sudoku', 'Судоку'),
        )
         ),
        ('Волонтерство', (
            ('Pomoch` bomjam', 'Помощь бездомным'),
            ('Pomoch` veteranam', 'Помощь ветеранам'),
        )
         ),
        ('Танцы', (
            ('Val`s', 'Вальс'),
            ('Chechetka', 'Чечетка'),
            ('Lezginka', 'Лезгинка'),
        )
         ),
        ('Музыка', (
            ('Gitara', 'Гитара'),
            ('Barabani', 'Барабаны'),
            ('Scripka', 'Скрипка'),
        )
         ),
        ('Рукоделие', (
            ('Derevi', 'Дерево'),
            ('Glina', 'Глина'),
        )
         ),
        ('unknown', 'Что-то свое'),
    )
    user = models.OneToOneField(User)
    skills_number = models.CharField(max_length=100,choices=SKILL_MEDIA_CHOICES, default='unknown')
    skills_comment = models.TextField()
    # skills_user = models.ForeignKey(User, unique=True)