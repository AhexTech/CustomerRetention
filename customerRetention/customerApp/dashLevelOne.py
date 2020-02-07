class levelOne:
    def calculate(self,*args):
        self.a=args

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
        AsianVegiesPricesell=0
        AsianVegiesUnit=0
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
            for i in range(0, len(self.a)):

                if self.a[i][0] == "Pumpkins":
                    PumpkinsPricesell += self.a[i][1]
                    PumpkinsUnit += self.a[i][2]
                context['Pumpkins'] = ['Pumpkins', PumpkinsPricesell, PumpkinsUnit]

                if self.a[i][0] == "Citrus":
                    CitrusPricesell += self.a[i][1]
                    CitrusUnit += self.a[i][2]
                context['Citrus'] = ['Citrus', CitrusPricesell, CitrusUnit]

                if self.a[i][0] == "Bunch Vegies":
                    BunchVegiesPricesell += self.a[i][1]
                    BunchVegiesUnit += self.a[i][2]
                context['Bunch Vegies'] = ['Bunch Vegies', BunchVegiesPricesell, BunchVegiesUnit]

                if self.a[i][0] == "Other Vegies":
                    OtherVegiesPricesell += self.a[i][1]
                    OtherVegiesUnit += self.a[i][2]
                context['Other Vegies'] = ['Other Vegies', OtherVegiesPricesell, OtherVegiesUnit]

                if self.a[i][0] == "Cabbages":
                    CabbagesPricesell += self.a[i][1]
                    CabbagesUnit += self.a[i][2]
                context['Cabbages'] = ['Cabbages', CabbagesPricesell, CabbagesUnit]

                if self.a[i][0] == "Asian Vegies":
                    AsianVegiesPricesell += self.a[i][1]
                    AsianVegiesUnit += self.a[i][2]
                context['Asian Vegies'] = ['Asian Vegies', AsianVegiesPricesell, AsianVegiesUnit]

                if self.a[i][0] == "Stonefruits":
                    StonefruitsPricesell += self.a[i][1]
                    StonefruitsUnit += self.a[i][2]
                context['Stonefruits'] = ['Stonefruits', StonefruitsPricesell, StonefruitsUnit]

                if self.a[i][0] == "Onions":
                    OnionsPricesell += self.a[i][1]
                    OnionsUnit += self.a[i][2]
                context['Onions'] = ['Onions', OnionsPricesell, OnionsUnit]

                if self.a[i][0] == "carrots":
                    carrotsPricesell += self.a[i][1]
                    carrotsUnit += self.a[i][2]
                context['carrots'] = ['carrots', carrotsPricesell, carrotsUnit]

                if self.a[i][0] == "Tropical Fruits":
                    TropicalFruitsPricesell += self.a[i][1]
                    TropicalFruitsUnit += self.a[i][2]
                context['Tropical Fruits'] = ['Tropical Fruits', TropicalFruitsPricesell, TropicalFruitsUnit]

                if self.a[i][0] == "Melons":
                    MelonsPricesell += self.a[i][1]
                    MelonsUnit += self.a[i][2]
                context['Melons'] = ['Melons', MelonsPricesell, MelonsUnit]

                if self.a[i][0] == "Grapes":
                    GrapesPricesell += self.a[i][1]
                    GrapesUnit += self.a[i][2]
                context['Grapes'] = ['Grapes', GrapesPricesell, GrapesUnit]

                if self.a[i][0] == "Potatoes":
                    PotatoesPricesell += self.a[i][1]
                    PotatoesUnit += self.a[i][2]
                context['Potatoes'] = ['Potatoes', PotatoesPricesell, PotatoesUnit]

                if self.a[i][0] == "Tomatoes":
                    TomatoesPricesell += self.a[i][1]
                    TomatoesUnit += self.a[i][2]
                context['Tomatoes'] = ['Tomatoes', TomatoesPricesell, TomatoesUnit]

                if self.a[i][0] == "Cucumbers":
                    CucumbersPricesell += self.a[i][1]
                    CucumbersUnit += self.a[i][2]
                context['Cucumbers'] = ['Cucumbers', CucumbersPricesell, CucumbersUnit]

                if self.a[i][0] == "Bananas":
                    BananasPricesell += self.a[i][1]
                    BananasUnit += self.a[i][2]
                context['Bananas'] = ['Bananas', BananasPricesell, BananasUnit]

                if self.a[i][0] == "Apples":
                    ApplesPricesell += self.a[i][1]
                    ApplesUnit += self.a[i][2]
                context['Apples'] = ['Apples', ApplesPricesell, ApplesUnit]

                if self.a[i][0] == "Pears":
                    PearsPricesell += self.a[i][1]
                    PearsUnit += self.a[i][2]
                context['Pears'] = ['Pears', PearsPricesell, PearsUnit]

                if self.a[i][0] == "Chillies":
                    ChilliesPricesell += self.a[i][1]
                    ChilliesUnit += self.a[i][2]
                context['Chillies'] = ['Chillies', ChilliesPricesell, ChilliesUnit]

                if self.a[i][0] == "Other Fruits":
                    OtherFruitsPricesell += self.a[i][1]
                    OtherFruitsUnit += self.a[i][2]
                context['Other Fruits'] = ['Other Fruits', OtherFruitsPricesell, OtherFruitsUnit]

                if self.a[i][0] == "Herbs":
                    HerbsPricesell += self.a[i][1]
                    HerbsUnit += self.a[i][2]
                context['Herbs'] = ['Herbs', HerbsPricesell, HerbsUnit]

                if self.a[i][0] == "Mushrooms":
                    MushroomsPricesell += self.a[i][1]
                    MushroomsUnit += self.a[i][2]
                context['Mushrooms'] = ['Mushrooms', MushroomsPricesell, MushroomsUnit]

                if self.a[i][0] == "Lettuces":
                    LettucesPricesell += self.a[i][1]
                    LettucesUnit += self.a[i][2]
                context['Lettuces'] = ['Lettuces', LettucesPricesell, LettucesUnit]

                if self.a[i][0] == "capsicum":
                    capsicumPricesell += self.a[i][1]
                    capsicumUnit += self.a[i][2]
                context['capsicum'] = ['capsicum', capsicumPricesell, capsicumUnit]

                if self.a[i][0] == "Veggies":
                    VeggiesPricesell += self.a[i][1]
                    VeggiesUnit += self.a[i][2]
                context['Veggies'] = ['Veggies', VeggiesPricesell, VeggiesUnit]

                if self.a[i][0] == "Root Vegies":
                    RootVegiesPricesell += self.a[i][1]
                    RootVegiesUnit += self.a[i][2]
                context['Root Vegies'] = ['Root Vegies', RootVegiesPricesell, RootVegiesUnit]

                if self.a[i][0] == "Avocadoes":
                    AvocadoesPricesell += self.a[i][1]
                    AvocadoesUnit += self.a[i][2]
                context['Avocadoes'] = ['Avocadoes', AvocadoesPricesell, AvocadoesUnit]

                if self.a[i][0] == "Berries":
                    BerriesPricesell += self.a[i][1]
                    BerriesUnit += self.a[i][2]
                context['Berries'] = ['Berries', BerriesPricesell, BerriesUnit]

                if self.a[i][0] == "Cut Veggies":
                    CutVeggiesPricesell += self.a[i][1]
                    CutVeggiesUnit += self.a[i][2]
                context['Cut Veggies'] = ['Cut Veggies', CutVeggiesPricesell, CutVeggiesUnit]

                if self.a[i][0] == "Flowers":
                    FlowersPricesell += self.a[i][1]
                    FlowersUnit += self.a[i][2]
                context['Flowers'] = ['Flowers', FlowersPricesell, FlowersUnit]

                if self.a[i][0] == "Multi buy":
                    MultibuyPricesell += self.a[i][1]
                    MultibuyUnit += self.a[i][2]
                context['Multi buy'] = ['Multi buy', MultibuyPricesell, MultibuyUnit]

                if self.a[i][0] == "Sri Lankan Groceries":
                    SriLankanGroceriesPricesell += self.a[i][1]
                    SriLankanGroceriesUnit += self.a[i][2]
                context['Sri Lankan Groceries'] = ['Sri Lankan Groceries', SriLankanGroceriesPricesell, SriLankanGroceriesUnit]

                if self.a[i][0] == "Olympian Products":
                    OlympianProductsPricesell += self.a[i][1]
                    OlympianProductsUnit += self.a[i][2]
                context['Olympian Products'] = ['Olympian Products', OlympianProductsPricesell, OlympianProductsUnit]

                if self.a[i][0] == "Nuts":
                    NutsPricesell += self.a[i][1]
                    NutsUnit += self.a[i][2]
                context['Nuts'] = ['Nuts', NutsPricesell, NutsUnit]

                if self.a[i][0] == "Groceries-Dry Goods":
                    GroceriesDryGoodsPricesell += self.a[i][1]
                    GroceriesDryGoodsUnit += self.a[i][2]
                context['Groceries-Dry Goods'] = ['Groceries-Dry Goods', GroceriesDryGoodsPricesell, GroceriesDryGoodsUnit]

                if self.a[i][0] == "Cut Fruits":
                    CutFruitsPricesell += self.a[i][1]
                    CutFruitsUnit += self.a[i][2]
                context['Cut Fruits'] = ['Cut Fruits', CutFruitsPricesell, CutFruitsUnit]

                if self.a[i][0] == "coconut Products":
                    coconutProductsPricesell += self.a[i][1]
                    coconutProductsUnit += self.a[i][2]
                context['Coconut Products'] = ['Coconut Products', coconutProductsPricesell, coconutProductsUnit]

                if self.a[i][0] == "Fruits":
                    FruitsPricesell += self.a[i][1]
                    FruitsUnit += self.a[i][2]
                context['Fruits'] = ['Fruits', FruitsPricesell, FruitsUnit]

                if self.a[i][0] == "Kalamata olives":
                    KalamataolivesPricesell += self.a[i][1]
                    KalamataolivesUnit += self.a[i][2]
                context['Kalamata olives'] = ['Kalamata olives', KalamataolivesPricesell, KalamataolivesUnit]

                if self.a[i][0] == "markdown bag":
                    markdownbagPricesell += self.a[i][1]
                    markdownbagUnit += self.a[i][2]
                context['Markdown bag'] = ['Markdown bag', markdownbagPricesell, markdownbagUnit]

                if self.a[i][0] == "Eggs":
                    EggsPricesell += self.a[i][1]
                    EggsUnit += self.a[i][2]
                context['Eggs'] = ['Eggs', EggsPricesell, EggsUnit]

        except:
            pass

        return context