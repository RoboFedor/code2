class Planet:
    def __init__(self, description, forward, back):
        self.description = description
        self.forward = forward
        self.back = back


Mecury = Planet(
    "Планета Меркурий. Температура: от -170 С до +430 С. Самая маленькая планета Солнечной системы. Самая близкая к Солнцу планета.",
    None, "Сосед от Солнца Венера.")
Venus = Planet(
    "Планета Венера. Температура: до +470 С. Шестая по размеру в Солнечной системе. Давление в 95 раз больше земного.",
    "Сосед к Солнцу Меркурий.", "Сосед от Солнца Земля.")
Earth = Planet(
    "Планета Земля. Температура: пригодная для жизни человека. Пятая по размеру в Солнечной системе. Условия пригодные для жизни.",
    "Сосед к Солнцу Венера.", "Сосед от Солнца Марс.")
Mars = Planet(
    "Планета Марс. Температура: от -100 С до +20 С. Седьмая по размеру планета Солнечной системы. Граничит с поясом астероидов.",
    'Cосед к Солнцу Земля.', "Сосед от Солнца Юпитер.")
Jupiter = Planet(
    "Планета Юпитер. Средняя температура: -108 С. Самая большая планета Солнечной системы. Имеет более 60 спутников.",
    "Сосед к Солнцу Марс.", "Сосед от Солнца Сатурн.")

Saturn = Planet(
    "Планета Сатурн. Средняя температура: -139 С. Вторая по размеру планета Солнечной системы.Имеет большую систему колец из комет и космической пыли. ",
    "Сосед к Солнцу Юпитер.", "Сосед от Солнца Уран.")
Uranium = Planet(
    "Планета Уран. Средняя температура: -197 С. Третья по размеру планета Солнечной системы. Единственная планета, названная в честь греческого бога,а не римского, как все остальные планеты.",
    "Сосед к Солнцу Сатурн.", "Сосед от Солнца Нептун.")
Neptune = Planet(
    "Планета Нептун. Средняя температура: -201 С. Четвёртая по размеру планета Солнечной системы. Самая отдалённая от Солнца планета.",
    "Сосед к Солнцу Уран.", "Нептун последняя планета Солнечной системы.")
planets = [Mecury, Venus, Earth, Mars, Jupiter, Saturn, Uranium, Neptune]
current = 2
user_chose = None
while user_chose != 'Q':
    user_chose = input()
    if user_chose == "H":
        current = 2
        print(
            "Планета Земля. Температура пригодная для жизни человека. Пятая по размеру в Солнечной системе. Условия пригодные для жизни.",
            "Сосед к солнцу Венера", "Сосед от солнца Марс.")
    elif user_chose == "B":
        current += 1
    elif user_chose == "F":
        current -= 1
    print(planets[current].description)
    print(planets[current].back)
    print(planets[current].forward)
