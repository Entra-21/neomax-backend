from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(
        help_text="Insira a sua data de nascimento.", null=True, blank=True
    )
    profile_picture = models.CharField(
        help_text="Insira a URL da imagem de perfil.",
        max_length=200,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}"


class Exercise(models.Model):
    name = models.CharField(
        help_text="Insira o nome do exercício.",
        max_length=100,
        null=True,
        blank=True,
    )
    gif = models.CharField(
        help_text="Insira a URL do gif de demonstração do exercício.",
        max_length=100,
        null=True,
        blank=True,
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


class Workout(models.Model):
    name = models.CharField(
        help_text="Insira o nome do treino.",
        max_length=50,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        help_text="Informe o usuário de criação do treino.",
        related_name="workouts",
        default=1,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Routine(models.Model):
    title = models.CharField(
        help_text="Insira o título da rotina.",
        max_length=50,
        null=True,
        blank=True,
    )
    exercises = models.ManyToManyField(Exercise)
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="routines"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"


class Diet(models.Model):
    name = models.CharField(
        help_text="Insira o nome da dieta.",
        max_length=50,
        null=True,
        blank=True,
    )
    active = models.BooleanField(help_text="Informe se esta é a dieta ativa.")
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        help_text="Informe o usuário de criação da dieta.",
        related_name="diets",
        default=1,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Day(models.Model):
    name = models.CharField(
        help_text="Insira o nome do dia.",
        max_length=50,
        null=True,
        blank=True,
    )
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, related_name="days")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Meal(models.Model):
    name = models.CharField(
        help_text="Insira o nome da refeição.",
        max_length=100,
        null=True,
        blank=True,
    )
    time = models.TimeField(
        help_text="Insira o horário da refeição.",
        null=True,
        blank=True,
    )
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="meals")

    class Meta:
        ordering = ["time"]

    def __str__(self):
        return f"{self.time}"
