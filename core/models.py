from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    name = models.CharField(
        help_text="Insira o nome do exercício.",
        max_length=100,
        null=True,
        blank=True,
    )
    exercise_gif = models.CharField(
        help_text="Insira a URL do gif de demonstração do exercício.",
        max_length=100,
        null=True,
        blank=True,
    )
    creation_user = models.ForeignKey(
        User,
        help_text="Usuário de criação do exercício.",
        default=1,
    )
    SHOULDER = "Ombros"
    CHEST = "Peitoral"
    FRONT_ARM = "Bíceps"
    FOREARM = "Antebraço"
    SIDE = "Oblíquos"
    STOMACH = "Abdômen"
    FRONT_THIGH_1 = "Quadríceps"
    FRONT_THIGH_2 = "Abdutores"
    FRONT_THIGH_3 = "Adutores"
    UPPER_BACK = "Trapézio"
    MIDDLE_BACK = "Dorsais"
    LOW_BACK = "Lombar"
    BACK_ARM = "Tríceps"
    BUTTOCKS = "Glúteos"
    BACK_THIGH = "Posteriores"
    CALF = "Panturrilha"
    MUSCLE_GROUP_CHOICES = [
        (SHOULDER, "Ombros"),
        (CHEST, "Peitoral"),
        (FRONT_ARM, "Bíceps"),
        (FOREARM, "Antebraço"),
        (SIDE, "Oblíquos"),
        (STOMACH, "Abdômen"),
        (FRONT_THIGH_1, "Quadríceps"),
        (FRONT_THIGH_2, "Abdutores"),
        (FRONT_THIGH_3, "Adutores"),
        (UPPER_BACK, "Trapézio"),
        (MIDDLE_BACK, "Dorsais"),
        (LOW_BACK, "Lombar"),
        (BACK_ARM, "Tríceps"),
        (BUTTOCKS, "Glúteos"),
        (BACK_THIGH, "Posteriores"),
        (CALF, "Panturrilha"),
    ]
    muscle_group = models.CharField(
        help_text="Selecione o grupo muscular do exercício.",
        max_length=20,
        choices=MUSCLE_GROUP_CHOICES,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"
