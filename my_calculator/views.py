from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


from .calculator.notation import notation_calculator
from .calculator.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from .calculator.percent import total_to_value, total_to_proportion, standard_to_value, standard_to_proportion
from .calculator.area import area_calculator
from .calculator.mass import mass_calculator

# main
class IndexView(View):
    def get(self, request):
        context = {}
        context["type"] = ""
        context["title"] = "온라인 계산기"
        context["content"] = "다양한 종류의 계산기를 온라인으로 사용할 수 있습니다."
        return render(request, 'my_calculator/index.html', context)

# math 수학
class MathView(View):
    def get(self, request):
        context = {}
        context["type"] = "math"
        context["title"] = "수학 계산기"
        context["content"] = "진수 계산기, 수열 등 다양한 계산기들이 있습니다."
        return render(request, 'my_calculator/math.html', context)

class NotationView(View):
    def get(self, request):
        context = {}
        context["type"] = "math"
        context["title"] = "진수 계산기"
        context["content"] = "2진수 · 8진수 · 10진수 · 16진수를 상호변환할 수 있습니다."
        return render(request, 'my_calculator/notation.html', context)

    def post(self, request):
        befor_type = request.POST["befor_type"]
        befor_num = request.POST["befor_num"]
        after_type = request.POST["after_type"]
        after_num = notation_calculator(befor_type, befor_num, after_type)
        if after_type == "binary":
            after_num = str(after_num) + "(2)"
        elif after_type == "octal":
            after_num = str(after_num) + "(8)"
        elif after_type == "decimal":
            after_num = str(after_num) + "(10)"
        elif after_type == "hexadecimal":
            after_num = str(after_num) + "(16)"
        context = {"after_num": after_num,}
        return JsonResponse(context)

class PercentView(View):
    def get(self, request):
        context = {}
        context["type"] = "math"
        context["title"] = "퍼센트 계산기"
        context["content"] = "퍼센트 · 백분율 · 할인가를 계산할 수 있습니다."
        return render(request, 'my_calculator/percent.html', context)

    def post(self, request):
        context = {}
        first = request.POST["first"]
        second = request.POST["second"]
        if request.POST["type"] == "total_to_value":
            ans = total_to_value(first, second)
            context["answer"] = ans
        elif request.POST["type"] == "total_to_proportion":
            ans = total_to_proportion(first, second)
            context["answer"] = ans
        elif request.POST["type"] == "standard_to_value":
            inc_dec = request.POST["inc_dec"]
            ans = standard_to_value(first, second, inc_dec)
            context["answer"] = ans
        elif request.POST["type"] == "standard_to_proportion":
            ans = standard_to_proportion(first, second)
            context["answer"] = ans
        return JsonResponse(context)

# unit 단위 변환
class UnitView(View):
    def get(self, request):
        context = {}
        context["type"] = "unit"
        context["title"] = "단위 변환기"
        context["content"] = "화씨·섭씨 변환기 등 다양한 변환기들이 있습니다."
        return render(request, 'my_calculator/unit.html', context)

class TemperatureView(View):
    def get(self, request):
        context = {}
        context["type"] = "unit"
        context["title"] = "섭씨 · 화씨 온도 변환기"
        context["content"] = "섭씨(℃) · 화씨(℉) 온도를 변환할 수 있습니다."
        return render(request, 'my_calculator/temperature.html', context)

    def post(self, request):
        context = {}
        if request.POST["celsius"]:
            celsius = request.POST["celsius"]
            ansCelsius = celsius_to_fahrenheit(celsius)
            context["ansCelsius"] = str(ansCelsius) + " (℉)"
        elif request.POST["fahrenheit"]:
            fahrenheit = request.POST["fahrenheit"]
            ansFahrenheit = fahrenheit_to_celsius(fahrenheit)
            context["ansFahrenheit"] = str(ansFahrenheit) + " (℃)"
        return JsonResponse(context)

class AreaView(View):
    def get(self, request):
        context = {}
        context["type"] = "unit"
        context["title"] = "넓이 면적 변환기"
        context["content"] = "제곱미터(m²) · 평(坪) · 스퀘어피트(ft²)를 상호 변환할 수 있습니다."
        return render(request, 'my_calculator/area.html', context)

    def post(self, request):
        befor_type = request.POST["befor_type"]
        befor_num = request.POST["befor_num"]
        after_type = request.POST["after_type"]
        after_num = area_calculator(befor_type, befor_num, after_type)
        if after_type == "square_meter":
            after_num = str(after_num) + "(m²)"
        elif after_type == "pyeong":
            after_num = str(after_num) + "(평)"
        elif after_type == "square_feet":
            after_num = str(after_num) + "(ft²)"
        context = {"after_num": after_num,}
        return JsonResponse(context)


class MassView(View):
    def get(self, request):
        context = {}
        context["type"] = "unit"
        context["title"] = "질량 무게 변환기"
        context["content"] = "그램(g) · 킬로그램(kg) · 온스(oz) · 파운드(lb)를 상호 변환할 수 있습니다."
        return render(request, 'my_calculator/mass.html', context)

    def post(self, request):
        befor_type = request.POST["befor_type"]
        befor_num = request.POST["befor_num"]
        after_type = request.POST["after_type"]
        after_num = mass_calculator(befor_type, befor_num, after_type)
        print(after_num)
        if after_type == "gram":
            after_num = str(after_num) + "(g)"
        elif after_type == "kilogram":
            after_num = str(after_num) + "(kg)"
        elif after_type == "ounce":
            after_num = str(after_num) + "(oz)"
        elif after_type == "pound":
            after_num = str(after_num) + "(lb)"
        context = {"after_num": after_num,}
        return JsonResponse(context)