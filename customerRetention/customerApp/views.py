from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.views.generic import TemplateView
from datetime import date
import datetime
import calendar
from django.views.generic import View
from .models import *
from django.http import JsonResponse
from .dashLevelOne import  *

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
import requests


# def Index(request):
#     my_date = date.today()
#     time = datetime.date.today()
#     day = calendar.day_name[my_date.weekday()]
#     context = {'time':time,'day':day}
#     return render(request,'index.html', context)



class Index(View):
    def get(self, request):
        my_date = date.today()
        time = datetime.date.today()
        day = calendar.day_name[my_date.weekday()]
        data = Fruithut.objects.all()[:50]

        # print(data.get())
        Sumadd=[]
        AllUnit=[]
        for d in data:
            Sumadd.append(d.__str__()['pricesell'])
            AllUnit.append(d.__str__()['units'])

        PricesellAdded = sum(Sumadd)
        Sumunit = sum(AllUnit)
        context = {'time':time,
                   'day':day,
                   'data':data,
                   'PricesellAdded': round(PricesellAdded,2),
                   'Sumunit':Sumunit}
        return render(request, 'index.html', context)

    # def post(self, request):
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    #     return render(request, 'index.html', {'form': form})


class CanvasTest(View):
    def get(self, request):
        a = Fruithut.objects.values_list('catergory', 'pricesell', 'units' ,flat=False)
        context = {}
        PumpkinsPricesell = 0
        PumpkinsUnit = 0
        CitrusPricesell = 0
        CitrusUnit = 0
        BunchVegiesPricesell = 0
        BunchVegiesUnit = 0
        OtherVegiesPricesell = 0
        OtherVegiesUnit = 0
        CabbagesPricesell = 0
        CabbagesUnit = 0
        AsianVegiesPricesell = 0
        AsianVegiesUnit = 0
        StonefruitsPricesell = 0
        StonefruitsUnit = 0
        OnionsPricesell = 0
        OnionsUnit = 0
        carrotsPricesell = 0
        carrotsUnit = 0
        TropicalFruitsPricesell = 0
        TropicalFruitsUnit = 0
        MelonsPricesell = 0
        MelonsUnit = 0
        GrapesPricesell = 0
        GrapesUnit = 0
        PotatoesPricesell = 0
        PotatoesUnit = 0
        TomatoesPricesell = 0
        TomatoesUnit = 0
        CucumbersPricesell = 0
        CucumbersUnit = 0
        BananasPricesell = 0
        BananasUnit = 0
        ApplesPricesell = 0
        ApplesUnit = 0
        PearsPricesell = 0
        PearsUnit = 0
        OtherFruitsPricesell = 0
        OtherFruitsUnit = 0
        HerbsPricesell = 0
        HerbsUnit = 0
        MushroomsPricesell = 0
        MushroomsUnit = 0
        LettucesPricesell = 0
        LettucesUnit = 0
        capsicumPricesell = 0
        capsicumUnit = 0
        VeggiesPricesell = 0
        VeggiesUnit = 0
        RootVegiesPricesell = 0
        RootVegiesUnit = 0
        AvocadoesPricesell = 0
        AvocadoesUnit = 0
        BerriesPricesell = 0
        BerriesUnit = 0
        CutVeggiesPricesell = 0
        CutVeggiesUnit = 0
        FlowersPricesell = 0
        FlowersUnit = 0
        MultibuyPricesell = 0
        MultibuyUnit = 0
        SriLankanGroceriesPricesell = 0
        SriLankanGroceriesUnit = 0
        OlympianProductsPricesell = 0
        OlympianProductsUnit = 0
        NutsPricesell = 0
        NutsUnit = 0
        GroceriesDryGoodsPricesell = 0
        GroceriesDryGoodsUnit = 0
        CutFruitsPricesell = 0
        CutFruitsUnit = 0
        coconutProductsPricesell = 0
        coconutProductsUnit = 0
        FruitsPricesell = 0
        FruitsUnit = 0
        KalamataolivesPricesell = 0
        KalamataolivesUnit = 0
        markdownbagPricesell = 0
        markdownbagUnit = 0
        EggsPricesell = 0
        EggsUnit = 0
        ChilliesPricesell = 0
        ChilliesUnit = 0

        try:
            for i in range(0, len(a)):

                if a[i][0] == "Pumpkins":
                    PumpkinsPricesell += a[i][1]
                    PumpkinsUnit += a[i][2]
                context['Pumpkins'] = ['Pumpkins', PumpkinsPricesell, PumpkinsUnit]

                if a[i][0] == "Citrus":
                    CitrusPricesell += a[i][1]
                    CitrusUnit += a[i][2]
                context['Citrus'] = ['Citrus', CitrusPricesell, CitrusUnit]

                if a[i][0] == "Bunch Vegies":
                    BunchVegiesPricesell += a[i][1]
                    BunchVegiesUnit += a[i][2]
                context['Bunch Vegies'] = ['Bunch Vegies', BunchVegiesPricesell, BunchVegiesUnit]

                if a[i][0] == "Other Vegies":
                    OtherVegiesPricesell += a[i][1]
                    OtherVegiesUnit += a[i][2]
                context['Other Vegies'] = ['Other Vegies', OtherVegiesPricesell, OtherVegiesUnit]

                if a[i][0] == "Cabbages":
                    CabbagesPricesell += a[i][1]
                    CabbagesUnit += a[i][2]
                context['Cabbages'] = ['Cabbages', CabbagesPricesell, CabbagesUnit]

                if a[i][0] == "Asian Vegies":
                    AsianVegiesPricesell += a[i][1]
                    AsianVegiesUnit += a[i][2]
                context['Asian Vegies'] = ['Asian Vegies', AsianVegiesPricesell, AsianVegiesUnit]

                if a[i][0] == "Stonefruits":
                    StonefruitsPricesell += a[i][1]
                    StonefruitsUnit += a[i][2]
                context['Stonefruits'] = ['Stonefruits', StonefruitsPricesell, StonefruitsUnit]

                if a[i][0] == "Onions":
                    OnionsPricesell += a[i][1]
                    OnionsUnit += a[i][2]
                context['Onions'] = ['Onions', OnionsPricesell, OnionsUnit]

                if a[i][0] == "carrots":
                    carrotsPricesell += a[i][1]
                    carrotsUnit += a[i][2]
                context['carrots'] = ['carrots', carrotsPricesell, carrotsUnit]

                if a[i][0] == "Tropical Fruits":
                    TropicalFruitsPricesell += a[i][1]
                    TropicalFruitsUnit += a[i][2]
                context['Tropical Fruits'] = ['Tropical Fruits', TropicalFruitsPricesell, TropicalFruitsUnit]

                if a[i][0] == "Melons":
                    MelonsPricesell += a[i][1]
                    MelonsUnit += a[i][2]
                context['Melons'] = ['Melons', MelonsPricesell, MelonsUnit]

                if a[i][0] == "Grapes":
                    GrapesPricesell += a[i][1]
                    GrapesUnit += a[i][2]
                context['Grapes'] = ['Grapes', GrapesPricesell, GrapesUnit]

                if a[i][0] == "Potatoes":
                    PotatoesPricesell += a[i][1]
                    PotatoesUnit += a[i][2]
                context['Potatoes'] = ['Potatoes', PotatoesPricesell, PotatoesUnit]

                if a[i][0] == "Tomatoes":
                    TomatoesPricesell += a[i][1]
                    TomatoesUnit += a[i][2]
                context['Tomatoes'] = ['Tomatoes', TomatoesPricesell, TomatoesUnit]

                if a[i][0] == "Cucumbers":
                    CucumbersPricesell += a[i][1]
                    CucumbersUnit += a[i][2]
                context['Cucumbers'] = ['Cucumbers', CucumbersPricesell, CucumbersUnit]

                if a[i][0] == "Bananas":
                    BananasPricesell += a[i][1]
                    BananasUnit += a[i][2]
                context['Bananas'] = ['Bananas', BananasPricesell, BananasUnit]

                if a[i][0] == "Apples":
                    ApplesPricesell += a[i][1]
                    ApplesUnit += a[i][2]
                context['Apples'] = ['Apples', ApplesPricesell, ApplesUnit]

                if a[i][0] == "Pears":
                    PearsPricesell += a[i][1]
                    PearsUnit += a[i][2]
                context['Pears'] = ['Pears', PearsPricesell, PearsUnit]

                if a[i][0] == "Chillies":
                    ChilliesPricesell += a[i][1]
                    ChilliesUnit += a[i][2]
                context['Chillies'] = ['Chillies', ChilliesPricesell, ChilliesUnit]

                if a[i][0] == "Other Fruits":
                    OtherFruitsPricesell += a[i][1]
                    OtherFruitsUnit += a[i][2]
                context['Other Fruits'] = ['Other Fruits', OtherFruitsPricesell, OtherFruitsUnit]

                if a[i][0] == "Herbs":
                    HerbsPricesell += a[i][1]
                    HerbsUnit += a[i][2]
                context['Herbs'] = ['Herbs', HerbsPricesell, HerbsUnit]

                if a[i][0] == "Mushrooms":
                    MushroomsPricesell += a[i][1]
                    MushroomsUnit += a[i][2]
                context['Mushrooms'] = ['Mushrooms', MushroomsPricesell, MushroomsUnit]

                if a[i][0] == "Lettuces":
                    LettucesPricesell += a[i][1]
                    LettucesUnit += a[i][2]
                context['Lettuces'] = ['Lettuces', LettucesPricesell, LettucesUnit]

                if a[i][0] == "capsicum":
                    capsicumPricesell += a[i][1]
                    capsicumUnit += a[i][2]
                context['capsicum'] = ['capsicum', capsicumPricesell, capsicumUnit]

                if a[i][0] == "Veggies":
                    VeggiesPricesell += a[i][1]
                    VeggiesUnit += a[i][2]
                context['Veggies'] = ['Veggies', VeggiesPricesell, VeggiesUnit]

                if a[i][0] == "Root Vegies":
                    RootVegiesPricesell += a[i][1]
                    RootVegiesUnit += a[i][2]
                context['Root Vegies'] = ['Root Vegies', RootVegiesPricesell, RootVegiesUnit]

                if a[i][0] == "Avocadoes":
                    AvocadoesPricesell += a[i][1]
                    AvocadoesUnit += a[i][2]
                context['Avocadoes'] = ['Avocadoes', AvocadoesPricesell, AvocadoesUnit]

                if a[i][0] == "Berries":
                    BerriesPricesell += a[i][1]
                    BerriesUnit += a[i][2]
                context['Berries'] = ['Berries', BerriesPricesell, BerriesUnit]

                if a[i][0] == "Cut Veggies":
                    CutVeggiesPricesell += a[i][1]
                    CutVeggiesUnit += a[i][2]
                context['Cut Veggies'] = ['Cut Veggies', CutVeggiesPricesell, CutVeggiesUnit]

                if a[i][0] == "Flowers":
                    FlowersPricesell += a[i][1]
                    FlowersUnit += a[i][2]
                context['Flowers'] = ['Flowers', FlowersPricesell, FlowersUnit]

                if a[i][0] == "Multi buy":
                    MultibuyPricesell += a[i][1]
                    MultibuyUnit += a[i][2]
                context['Multi buy'] = ['Multi buy', MultibuyPricesell, MultibuyUnit]

                if a[i][0] == "Sri Lankan Groceries":
                    SriLankanGroceriesPricesell += a[i][1]
                    SriLankanGroceriesUnit += a[i][2]
                context['Sri Lankan Groceries'] = ['Sri Lankan Groceries', SriLankanGroceriesPricesell,
                                                   SriLankanGroceriesUnit]

                if a[i][0] == "Olympian Products":
                    OlympianProductsPricesell += a[i][1]
                    OlympianProductsUnit += a[i][2]
                context['Olympian Products'] = ['Olympian Products', OlympianProductsPricesell, OlympianProductsUnit]

                if a[i][0] == "Nuts":
                    NutsPricesell += a[i][1]
                    NutsUnit += a[i][2]
                context['Nuts'] = ['Nuts', NutsPricesell, NutsUnit]

                if a[i][0] == "Groceries-Dry Goods":
                    GroceriesDryGoodsPricesell += a[i][1]
                    GroceriesDryGoodsUnit += a[i][2]
                context['Groceries-Dry Goods'] = ['Groceries-Dry Goods', GroceriesDryGoodsPricesell,
                                                  GroceriesDryGoodsUnit]

                if a[i][0] == "Cut Fruits":
                    CutFruitsPricesell += a[i][1]
                    CutFruitsUnit += a[i][2]
                context['Cut Fruits'] = ['Cut Fruits', CutFruitsPricesell, CutFruitsUnit]

                if a[i][0] == "coconut Products":
                    coconutProductsPricesell += a[i][1]
                    coconutProductsUnit += a[i][2]
                context['Coconut Products'] = ['Coconut Products', coconutProductsPricesell, coconutProductsUnit]

                if a[i][0] == "Fruits":
                    FruitsPricesell += a[i][1]
                    FruitsUnit += a[i][2]
                context['Fruits'] = ['Fruits', FruitsPricesell, FruitsUnit]

                if a[i][0] == "Kalamata olives":
                    KalamataolivesPricesell += a[i][1]
                    KalamataolivesUnit += a[i][2]
                context['Kalamata olives'] = ['Kalamata olives', KalamataolivesPricesell, KalamataolivesUnit]

                if a[i][0] == "markdown bag":
                    markdownbagPricesell += a[i][1]
                    markdownbagUnit += a[i][2]
                context['Markdown bag'] = ['Markdown bag', markdownbagPricesell, markdownbagUnit]

                if a[i][0] == "Eggs":
                    EggsPricesell += a[i][1]
                    EggsUnit += a[i][2]
                context['Eggs'] = ['Eggs', EggsPricesell, EggsUnit]

        except:
            pass
        contextNew={
            'PumpkinsPricesell' : PumpkinsPricesell,
            'PumpkinsUnit' : PumpkinsUnit,
            'CitrusPricesell' : CitrusPricesell,
            'CitrusUnit' : CitrusUnit,
            'BunchVegiesPricesell' : BunchVegiesPricesell,
            'BunchVegiesUnit' : BunchVegiesUnit,
            'OtherVegiesPricesell' : OtherVegiesPricesell,
            'OtherVegiesUnit' : OtherVegiesUnit,
            'CabbagesPricesell' : CabbagesPricesell,
            'CabbagesUnit' : CabbagesUnit,
            'AsianVegiesPricesell' : AsianVegiesPricesell,
            'AsianVegiesUnit' : AsianVegiesUnit,
            'StonefruitsPricesell' : StonefruitsPricesell,
            'StonefruitsUnit' : StonefruitsUnit,
            'OnionsPricesell' : OnionsPricesell,
            'OnionsUnit' : OnionsUnit,
            'carrotsPricesell' : carrotsPricesell,
            'carrotsUnit' : carrotsUnit,
            'TropicalFruitsPricesell' : TropicalFruitsPricesell,
            'TropicalFruitsUnit' : TropicalFruitsUnit,
            'MelonsPricesell' : MelonsPricesell,
            'MelonsUnit' : MelonsUnit,
            'GrapesPricesell' : GrapesPricesell,
            'GrapesUnit' : GrapesUnit,
            'PotatoesPricesell' : PotatoesPricesell,
            'PotatoesUnit' : PotatoesUnit,
            'TomatoesPricesell' : TomatoesPricesell,
            'TomatoesUnit' : TomatoesUnit,
            'CucumbersPricesell' : CucumbersPricesell,
            'CucumbersUnit' : CucumbersUnit,
            'BananasPricesell' : BananasPricesell,
            'BananasUnit' : BananasUnit,
            'ApplesPricesell' : ApplesPricesell,
            'ApplesUnit' : ApplesUnit,
            'PearsPricesell' : PearsPricesell,
            'PearsUnit' : PearsUnit,
            'OtherFruitsPricesell' : OtherFruitsPricesell,
            'OtherFruitsUnit' : OtherFruitsUnit,
            'HerbsPricesell' : HerbsPricesell,
            'HerbsUnit' : HerbsUnit,
            'MushroomsPricesell' : MushroomsPricesell,
            'MushroomsUnit' : MushroomsUnit,
            'LettucesPricesell' : LettucesPricesell,
            'LettucesUnit' : LettucesUnit,
            'capsicumPricesell' : capsicumPricesell,
            'capsicumUnit' : capsicumUnit,
            'VeggiesPricesell' : VeggiesPricesell,
            'VeggiesUnit' : VeggiesUnit,
            'RootVegiesPricesell' : RootVegiesPricesell,
            'RootVegiesUnit' : RootVegiesUnit,
            'AvocadoesPricesell' : AvocadoesPricesell,
            'AvocadoesUnit' : AvocadoesUnit,
            'BerriesPricesell' : BerriesPricesell,
            'BerriesUnit' : BerriesUnit,
            'CutVeggiesPricesell' : CutVeggiesPricesell,
            'CutVeggiesUnit' : CutVeggiesUnit,
            'FlowersPricesell' : FlowersPricesell,
            'FlowersUnit' : FlowersUnit,
            'MultibuyPricesell' : MultibuyPricesell,
            'MultibuyUnit' : MultibuyUnit,
            'SriLankanGroceriesPricesell' : SriLankanGroceriesPricesell,
            'SriLankanGroceriesUnit' : SriLankanGroceriesUnit,
            'OlympianProductsPricesell' : OlympianProductsPricesell,
            'OlympianProductsUnit' : OlympianProductsUnit,
            'NutsPricesell' : NutsPricesell,
            'NutsUnit' : NutsUnit,
            'GroceriesDryGoodsPricesell' : GroceriesDryGoodsPricesell,
            'GroceriesDryGoodsUnit' : GroceriesDryGoodsUnit,
            'CutFruitsPricesell' : CutFruitsPricesell,
            'CutFruitsUnit' : CutFruitsUnit,
            'coconutProductsPricesell' : coconutProductsPricesell,
            'coconutProductsUnit' : coconutProductsUnit,
            'FruitsPricesell' : FruitsPricesell,
            'FruitsUnit' : FruitsUnit,
            'KalamataolivesPricesell' : KalamataolivesPricesell,
            'KalamataolivesUnit' : KalamataolivesUnit,
            'markdownbagPricesell' : markdownbagPricesell,
            'markdownbagUnit' : markdownbagUnit,
            'EggsPricesell' : EggsPricesell,
            'EggsUnit' : EggsUnit,
            'ChilliesPricesell' : ChilliesPricesell,
            'ChilliesUnit' : ChilliesUnit,
        }

        print(context)
        return render(request, 'canvas.html', contextNew)


############to get all category name in JSON#####################
# class test(View):
#     def get(self,request):
#         data2 = Fruithut.objects.values_list('catergory', flat=True)
#         new=[]
#         for data in data2:
#             if data not in new:
#                 new.append(data)
#         return JsonResponse({"Data": list(new)}, safe=False)


###############to get all objects in JSON#########################
class test(View):
    def get(self,request):
        data2 = Fruithut.objects.all()[:5].values()
        return JsonResponse({"Data": list(data2)}, safe=False)



class testJson(View):

    def get(self, request):
        data2 = Fruithut.objects.all()[:5].values()

        return render(request, 'testJson.html', {'context': data2})


