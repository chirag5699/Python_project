from tkinter import *
import random
import datetime as dt
root=Tk()
file=open("data.txt","a")
root.geometry("1280x700")
# root.maxsize(width=1280,height=700)
# root.minsize(width=1280,height=700)
root.title("Billing Shoftware")

#======================Variable========================

bg_color = "black"
fg_color = "white"
lbl_color = 'white'

cus_name = StringVar()
c_phone = StringVar()
#==For Generating Random Bill Numbers==
x = random.randint(1000,9999)
c_bill_no = StringVar()
#==Seting Value to variable==
c_bill_no.set(str(x))

Net_Total=IntVar()
total_all=IntVar()
total_Chainese_prices=IntVar()
total_MasurDhosa_prices=IntVar()

#===============Chezzcake=================

original_new_york=IntVar()
Blueberry_cherry=IntVar()
strawbeery=IntVar()
mixed_berry=IntVar()
nutella=IntVar()
biscoff=IntVar()
oreo=IntVar()
all_about=IntVar()
pistachio=IntVar()
white_cho_raspberry=IntVar()
lemon_raspberry=IntVar()
ferrero_rocher=IntVar()

#=================Classic===============

espresso=IntVar()
americano=IntVar()
cortado=IntVar()
cappuccino=IntVar()
cafe_latte=IntVar()
flat_white=IntVar()
cafe_mocha=IntVar()
affogatto=IntVar()

#==============Handbrewed===============

v60_pour_over=IntVar()
aeropress=IntVar()
cold_brew=IntVar()

#===============caffeine refreshers=============
espresso_tonic=IntVar()
cold_brew_tonic=IntVar()
whisky_barrel_aged=IntVar()
bitter_ground_espresso=IntVar()
lime_light=IntVar()
cafeeine_bomb=IntVar()
vietnamese=IntVar()
bombon=IntVar()

#==============hand crafted=====================
the_breeze_espresso=IntVar()
coffee_cran_tonic=IntVar()
yuzu_espresso_tonic=IntVar()
orange_espresso_tonic=IntVar()
flora=IntVar()
cold_fassioned=IntVar()
tiramisu_hot_chocolate=IntVar()

#==============creamy cold frappes==============
frappe_latte=IntVar()
caramel_frappe_latte=IntVar()
hazelnut_frappe_latte=IntVar()
frappe_mocha=IntVar()
frappe_mocha_crumble=IntVar()
biscoff_frappe_latte=IntVar()
the_raven_snow_frappe=IntVar()

#===============shakes===================
oreo_cookies_cream=IntVar()
nutella_hazelnutes_shake=IntVar()
berry_blast_shake=IntVar()
biscoff_shake=IntVar()
berry_biscoff_shake=IntVar()
pink_chocolate_shake=IntVar()

#==============coolers================
mint_mojito=IntVar()
blue_ale=IntVar()
watermelon_mojito=IntVar()
green_apple=IntVar()
blueberry_slush=IntVar()
cranberry_slush=IntVar()
the_breeze=IntVar()
pinacolda=IntVar()
peach_iced_tea=IntVar()
lemon_iced_tea=IntVar()

#===============croissant============
butter_crossant=IntVar()
almond_croissant=IntVar()
nutella_croissant=IntVar()
pain_au_chocolate=IntVar()
exotic_cruffin=IntVar()
pistachio_raspberry_danish=IntVar()

#=============sandwichs==============
parmesan_spinach_cheese_sandwich=IntVar()
pesto_basil_spinach_sandwich=IntVar()
cream_cheese_bagel=IntVar()
veggi_cheese_bagel=IntVar()
veggi_cheese_croissant=IntVar()

#============Brownies*and cake=============
nutella_brownie=IntVar()
walnut_brownie=IntVar()
toffee=IntVar()
red_velvet_brownie=IntVar()
ganache_cake=IntVar()
choco_chips_cookie=IntVar()



total_menu = StringVar()
# total_Chainese = StringVar()
# total_MasurDhosa = StringVar()
# tax_PavBhaji = StringVar()
# tax_Chainese = StringVar()
# tax_MasurDhosa = StringVar()

def total():
#=================Total All Item 

    global total_all,total_menu
    total_all=(
        (original_new_york.get() * 200)+
        (Blueberry_cherry.get() * 230)+
        (strawbeery.get() * 230)+
        (mixed_berry.get() * 240)+
        (nutella.get() * 250)+
        (biscoff.get() * 270)+
        (oreo.get() * 270)+
        (all_about.get() * 280)+
        (pistachio.get() * 280)+
        (white_cho_raspberry.get() * 280)+
        (lemon_raspberry.get() * 280)+
        (ferrero_rocher.get() * 320)+
        (espresso.get() * 140)+
        (americano.get() * 150)+
        (cortado.get() * 160)+
        (cappuccino.get() * 160)+
        (cafe_latte.get() * 160)+
        (flat_white.get() * 160)+
        (cafe_mocha.get() * 180)+
        (affogatto.get() * 180)+
        (v60_pour_over.get() * 200)+
        (aeropress.get() * 220)+
        (cold_brew.get() * 170)+
        (espresso_tonic.get() * 220)+
        (cold_brew_tonic.get() * 200)+
        (whisky_barrel_aged.get() * 230)+
        (bitter_ground_espresso.get() * 250)+
        (lime_light.get() * 220)+
        (cafeeine_bomb.get() * 270)+
        (vietnamese.get() * 180)+
        (bombon.get() * 160)+
        (the_breeze_espresso.get() * 300)+
        (coffee_cran_tonic.get() * 250)+
        (yuzu_espresso_tonic.get() * 260)+
        (orange_espresso_tonic.get() * 240)+
        (flora.get() * 240)+
        (cold_fassioned.get() * 220)+
        (tiramisu_hot_chocolate.get() * 220)+
        (frappe_latte.get() * 220)+
        (caramel_frappe_latte.get() * 240)+
        (hazelnut_frappe_latte.get() * 240)+
        (frappe_mocha.get() * 250)+
        (frappe_mocha_crumble.get() * 270)+
        (biscoff_frappe_latte.get() * 280)+
        (the_raven_snow_frappe.get() * 300)+
        (oreo_cookies_cream.get() * 240)+
        (nutella_hazelnutes_shake.get() * 250)+
        (berry_blast_shake.get() * 250)+
        (biscoff_shake.get() * 260)+
        (berry_biscoff_shake.get() * 270)+
        (pink_chocolate_shake.get() * 280)+
        (mint_mojito.get() * 170)+
        (blue_ale.get() * 170)+
        (watermelon_mojito.get() * 170)+
        (green_apple.get() * 170)+
        (blueberry_slush.get() * 200)+
        (cranberry_slush.get() * 200)+
        (the_breeze.get() * 230)+
        (pinacolda.get() * 200)+
        (peach_iced_tea.get() * 180)+
        (lemon_iced_tea.get() * 180)+
        (butter_crossant.get() * 180)+
        (almond_croissant.get() * 220)+
        (nutella_croissant.get() * 230)+
        (pain_au_chocolate.get() * 220)+
        (exotic_cruffin.get() * 200)+
        (pistachio_raspberry_danish.get() * 200)+
        (parmesan_spinach_cheese_sandwich.get() * 230)+
        (pesto_basil_spinach_sandwich.get() * 180)+
        (cream_cheese_bagel.get() * 180)+
        (veggi_cheese_bagel.get() * 230)+
        (veggi_cheese_croissant.get() * 240)+
        (nutella_brownie.get() * 140)+
        (walnut_brownie.get() * 140)+
        (toffee.get() * 140)+
        (red_velvet_brownie.get() * 180)+
        (ganache_cake.get() * 250)+
        (choco_chips_cookie.get() * 80)
    )
    total_menu.set("Rs ."+str(total_all))

#===================Function For Text Area====================
date = dt.datetime.now()
def welcome_soft():
    txt.delete('1.0',END)
    txt.insert(END,"           WELCOME TO JUNEBERRY \n")
    txt.insert(END,f"\nDate : {date:%A,%B %d,%Y}")
    txt.insert(END,f"\nBill No. : {str(c_bill_no.get())}")
    txt.insert(END,f"\nCustomer Name : {str(cus_name.get())}")
    txt.insert(END,f"\nPhone No. : {str(c_phone.get())}")
    txt.insert(END,"\n===========================================")
    txt.insert(END,"\nProduct             Qty             Price")
    txt.insert(END,"\n===========================================")
    file.write(f"""\n           WELCOME TO Billing \n
    \nDate : {date:%A,%B %d,%Y}
    \nBill No. : {str(c_bill_no.get())}
    \nCustomer Name : {str(cus_name.get())}
    \nPhone No. : {str(c_phone.get())}
    \n===========================================
    \nProduct             Qty             Price
    \n===========================================
    """)


#==========Add Product name , qty and price to bill area===============

def bill_area():
    welcome_soft()
    if original_new_york.get() != 0:
        txt.insert(END,f"\nOriginal NewYork C.   {original_new_york.get()}               {original_new_york.get() * 200}")
        file.write(f"\nOriginal NewYork C.   {original_new_york.get()}               {original_new_york.get() * 200}")
    if Blueberry_cherry.get() != 0:
        txt.insert(END,f"\nBluberry/Cherry C.    {Blueberry_cherry.get()}               {Blueberry_cherry.get() * 230}")
        file.write(f"\nBluberry/Cherry C.    {Blueberry_cherry.get()}               {Blueberry_cherry.get() * 230}")
    if strawbeery.get() != 0:
        txt.insert(END,f"\nStrawberry C.         {strawbeery.get()}               {strawbeery.get() * 230}")
        file.write(f"\nStrawberry C.         {strawbeery.get()}               {strawbeery.get() * 230}")
    if mixed_berry.get() != 0:
        txt.insert(END,f"\nMixed Berry C.        {mixed_berry.get()}               {mixed_berry.get() * 240}")
        file.write(f"\nMixed Berry C.        {mixed_berry.get()}               {mixed_berry.get() * 240}")
    if nutella.get() != 0:
        txt.insert(END,f"\nNutellla C.           {nutella.get()}               {nutella.get() * 250}")
        file.write(f"\nNutellla C.           {nutella.get()}               {nutella.get() * 250}")
    if biscoff.get() != 0:
        txt.insert(END,f"\nBiscoff C.            {biscoff.get()}               {biscoff.get() * 270}")
        file.write(f"\nBiscoff C.            {biscoff.get()}               {biscoff.get() * 270}")
    if oreo.get() != 0:
        txt.insert(END,f"\nOreo                  {oreo.get()}               {oreo.get() * 270}")
        file.write(f"\nOreo                  {oreo.get()}               {oreo.get() * 270}")
    if all_about.get() != 0:
        txt.insert(END,f"\nAll About C.          {all_about.get()}               {all_about.get() * 280}")
        file.write(f"\nAll About C.          {all_about.get()}               {all_about.get() * 280}")
    if pistachio.get() != 0:
        txt.insert(END,f"\nPistachio C.          {pistachio.get()}               {pistachio.get() * 280}")
        file.write(f"\nPistachio C.          {pistachio.get()}               {pistachio.get() * 280}")
    if white_cho_raspberry.get() != 0:
        txt.insert(END,f"\nWhite Cho. Raspberry  {white_cho_raspberry.get()}               {white_cho_raspberry.get() * 280}")
        file.write(f"\nWhite Cho. Raspberry  {white_cho_raspberry.get()}               {white_cho_raspberry.get() * 280}")
    if lemon_raspberry.get() != 0:
        txt.insert(END,f"\nLemon Raspberry       {lemon_raspberry.get()}               {lemon_raspberry.get() * 280}")
        file.write(f"\nLemon Raspberry       {lemon_raspberry.get()}               {lemon_raspberry.get() * 280}")
    if ferrero_rocher.get() != 0: 
        txt.insert(END,f"\nFerrero Rocher        {ferrero_rocher.get()}               {ferrero_rocher.get() * 320}")
        file.write(f"\nFerrero Rocher        {ferrero_rocher.get()}               {ferrero_rocher.get() * 320}")
    if espresso.get() != 0:
        txt.insert(END,f"\nEspresso              {espresso.get()}               {espresso.get() * 140}")
        file.write(f"\nEspresso              {espresso.get()}               {espresso.get() * 140}")
    if americano.get() != 0:
        txt.insert(END,f"\nAmericano             {americano.get()}               {americano.get() * 150}")
        file.write(f"\nAmericano             {americano.get()}               {americano.get() * 150}")
    if cortado.get() != 0:
        txt.insert(END,f"\nCortado               {cortado.get()}               {cortado.get() * 160}")
        file.write(f"\nCortado               {cortado.get()}               {cortado.get() * 160}")
    if cappuccino.get() != 0:
        txt.insert(END,f"\nCappuccino            {cappuccino.get()}               {cappuccino.get() * 160}")
        file.write(f"\nCappuccino            {cappuccino.get()}               {cappuccino.get() * 160}")
    if cafe_latte.get() != 0:
        txt.insert(END,f"\nCafe Latte            {cafe_latte.get()}               {cafe_latte.get() * 160}")
        file.write(f"\nCafe Latte            {cafe_latte.get()}               {cafe_latte.get() * 160}")
    if flat_white.get() != 0:
        txt.insert(END,f"\nFlat White            {flat_white.get()}               {flat_white.get() * 160}")
        file.write(f"\nFlat White            {flat_white.get()}               {flat_white.get() * 160}")
    if cafe_mocha.get() != 0:
        txt.insert(END,f"\nCafe Mocha            {cafe_mocha.get()}               {cafe_mocha.get() * 180}")
        file.write(f"\nCafe Mocha            {cafe_mocha.get()}               {cafe_mocha.get() * 180}")
    if affogatto.get() != 0:
        txt.insert(END,f"\nAffogatto             {affogatto.get()}               {affogatto.get() * 180}")
        file.write(f"\nAffogatto             {affogatto.get()}               {affogatto.get() * 180}")
    if v60_pour_over.get() != 0:
        txt.insert(END,f"\nV60 PourOver          {v60_pour_over.get()}               {v60_pour_over.get() * 200}")
        file.write(f"\nV60 PourOver          {v60_pour_over.get()}               {v60_pour_over.get() * 200}")
    if aeropress.get() != 0:
        txt.insert(END,f"\nAeropress             {aeropress.get()}               {aeropress.get() * 220}")
        file.write(f"\nAeropress             {aeropress.get()}               {aeropress.get() * 220}")
    if cold_brew.get() != 0:
        txt.insert(END,f"\nCold Brew             {cold_brew.get()}               {cold_brew.get() * 170}")
        file.write(f"\nCold Brew             {cold_brew.get()}               {cold_brew.get() * 170}")
    if espresso_tonic.get() != 0:
        txt.insert(END,f"\nEspresso Tonic        {espresso_tonic.get()}               {espresso_tonic.get() * 220}")
        file.write(f"\nEspresso Tonic        {espresso_tonic.get()}               {espresso_tonic.get() * 220}")
    if cold_brew_tonic.get() != 0:
        txt.insert(END,f"\nCold Brew Tonic       {cold_brew_tonic.get()}               {cold_brew_tonic.get() * 200}")
        file.write(f"\nCold Brew Tonic       {cold_brew_tonic.get()}               {cold_brew_tonic.get() * 200}")
    if whisky_barrel_aged.get() != 0:
        txt.insert(END,f"\nWhisky Barrel A.      {whisky_barrel_aged.get()}               {whisky_barrel_aged.get() * 230}")
        file.write(f"\nWhisky Barrel A.      {whisky_barrel_aged.get()}               {whisky_barrel_aged.get() * 230}")
    if bitter_ground_espresso.get() != 0:
        txt.insert(END,f"\nBitter Ground         {bitter_ground_espresso.get()}               {bitter_ground_espresso.get() * 250}")
        file.write(f"\nBitter Ground         {bitter_ground_espresso.get()}               {bitter_ground_espresso.get() * 250}")
    if lime_light.get() != 0:
        txt.insert(END,f"\nLime Light            {lime_light.get()}               {lime_light.get() * 220}")
        file.write(f"\nLime Light            {lime_light.get()}               {lime_light.get() * 220}")
    if cafeeine_bomb.get() != 0:
        txt.insert(END,f"\nCasseine Bomb         {cafeeine_bomb.get()}               {cafeeine_bomb.get() * 270}")
        file.write(f"\nCasseine Bomb         {cafeeine_bomb.get()}               {cafeeine_bomb.get() * 270}")
    if vietnamese.get() != 0:
        txt.insert(END,f"\nVietnamese            {vietnamese.get()}               {vietnamese.get() * 180}")
        file.write(f"\nVietnamese            {vietnamese.get()}               {vietnamese.get() * 180}")
    if bombon.get() != 0:
        txt.insert(END,f"\nBombon                {bombon.get()}               {bombon.get() * 160}")
        file.write(f"\nBombon                {bombon.get()}               {bombon.get() * 160}")
    if the_breeze_espresso.get() != 0:
        txt.insert(END,f"\nBreeze Espresso       {the_breeze_espresso.get()}               {the_breeze_espresso.get() * 300}")
        file.write(f"\nBreeze Espresso       {the_breeze_espresso.get()}               {the_breeze_espresso.get() * 300}")
    if coffee_cran_tonic.get() != 0:
        txt.insert(END,f"\nCoffee Cran           {coffee_cran_tonic.get()}               {coffee_cran_tonic.get() * 250}")
        file.write(f"\nCoffee Cran           {coffee_cran_tonic.get()}               {coffee_cran_tonic.get() * 250}")
    if yuzu_espresso_tonic.get() != 0:
        txt.insert(END,f"\nYuzu Espresso         {yuzu_espresso_tonic.get()}               {yuzu_espresso_tonic.get() * 260}")
        file.write(f"\nYuzu Espresso         {yuzu_espresso_tonic.get()}               {yuzu_espresso_tonic.get() * 260}")
    if orange_espresso_tonic.get() != 0:
        txt.insert(END,f"\nOrange Espresso       {orange_espresso_tonic.get()}               {orange_espresso_tonic.get() * 240}")
        file.write(f"\nOrange Espresso       {orange_espresso_tonic.get()}               {orange_espresso_tonic.get() * 240}")
    if flora.get() != 0:
        txt.insert(END,f"\nFlora                 {flora.get()}               {flora.get() * 240}")
        file.write(f"\nFlora                 {flora.get()}               {flora.get() * 240}")
    if cold_fassioned.get() != 0:
        txt.insert(END,f"\nCold Fassioned        {cold_fassioned.get()}               {cold_fassioned.get() * 220}")
        file.write(f"\nCold Fassioned        {cold_fassioned.get()}               {cold_fassioned.get() * 220}")
    if tiramisu_hot_chocolate.get() != 0:
        txt.insert(END,f"\nTiramisu Hot Cho.     {tiramisu_hot_chocolate.get()}               {tiramisu_hot_chocolate.get() * 220}")
        file.write(f"\nTiramisu Hot Cho.     {tiramisu_hot_chocolate.get()}               {tiramisu_hot_chocolate.get() * 220}")
    if frappe_latte.get() != 0:
        txt.insert(END,f"\nFrappe Latte          {frappe_latte.get()}               {frappe_latte.get() * 220}")
        file.write(f"\nFrappe Latte          {frappe_latte.get()}               {frappe_latte.get() * 220}")
    if caramel_frappe_latte.get() != 0:
        txt.insert(END,f"\nCaramel Frappe L.     {caramel_frappe_latte.get()}               {caramel_frappe_latte.get() * 240}")
        file.write(f"\nCaramel Frappe L.     {caramel_frappe_latte.get()}               {caramel_frappe_latte.get() * 240}")
    if hazelnut_frappe_latte.get() != 0:
        txt.insert(END,f"\nHazelnut Frappe L.    {hazelnut_frappe_latte.get()}               {hazelnut_frappe_latte.get() * 240}")
        file.write(f"\nHazelnut Frappe L.    {hazelnut_frappe_latte.get()}               {hazelnut_frappe_latte.get() * 240}")
    if frappe_mocha.get() != 0:
        txt.insert(END,f"\nFreappe Mocha         {frappe_mocha.get()}               {frappe_mocha.get() * 250}")
        file.write(f"\nFreappe Mocha         {frappe_mocha.get()}               {frappe_mocha.get() * 250}")
    if frappe_mocha_crumble.get() != 0:
        txt.insert(END,f"\nFrappe M. Cru.        {frappe_mocha_crumble.get()}               {frappe_mocha_crumble.get() * 270}")
        file.write(f"\nFrappe M. Cru.        {frappe_mocha_crumble.get()}               {frappe_mocha_crumble.get() * 270}")
    if biscoff_frappe_latte.get() != 0:
        txt.insert(END,f"\nBiscoff Fra. L.       {biscoff_frappe_latte.get()}               {biscoff_frappe_latte.get() * 280}")
        file.write(f"\nBiscoff Fra. L.       {biscoff_frappe_latte.get()}               {biscoff_frappe_latte.get() * 280}")
    if the_raven_snow_frappe.get() != 0:
        txt.insert(END,f"\nRaven Snow F.         {the_raven_snow_frappe.get()}               {the_raven_snow_frappe.get() * 300}")
        file.write(f"\nRaven Snow F.         {the_raven_snow_frappe.get()}               {the_raven_snow_frappe.get() * 300}")
    if oreo_cookies_cream.get() != 0:
        txt.insert(END,f"\nOreo Coo./cream       {oreo_cookies_cream.get()}               {oreo_cookies_cream.get() * 240}")
        file.write(f"\nOreo Coo./cream       {oreo_cookies_cream.get()}               {oreo_cookies_cream.get() * 240}")
    if berry_blast_shake.get() != 0:
        txt.insert(END,f"\nBerry Blast S.        {berry_blast_shake.get()}               {berry_blast_shake.get() * 250}")
        file.write(f"\nBerry Blast S.        {berry_blast_shake.get()}               {berry_blast_shake.get() * 250}")
    if biscoff_shake.get() != 0:
        txt.insert(END,f"\nBiscoff Shake         {biscoff_shake.get()}               {biscoff_shake.get() * 260}")
        file.write(f"\nBiscoff Shake         {biscoff_shake.get()}               {biscoff_shake.get() * 260}")
    if berry_biscoff_shake.get() != 0:
        txt.insert(END,f"\nBerry Biscoff S.      {berry_biscoff_shake.get()}               {berry_biscoff_shake.get() * 270}")
        file.write(f"\nBerry Biscoff S.      {berry_biscoff_shake.get()}               {berry_biscoff_shake.get() * 270}")
    if pink_chocolate_shake.get() != 0:
        txt.insert(END,f"\nPink Chocolate S.     {pink_chocolate_shake.get()}               {pink_chocolate_shake.get() * 280}")
        file.write(f"\nPink Chocolate S.     {pink_chocolate_shake.get()}               {pink_chocolate_shake.get() * 280}")
    if mint_mojito.get() != 0:
        txt.insert(END,f"\nMint Mojito           {mint_mojito.get()}               {mint_mojito.get() * 170}")
        file.write(f"\nMint Mojito           {mint_mojito.get()}               {mint_mojito.get() * 170}")
    if blue_ale.get() != 0:
        txt.insert(END,f"\nBlue Ale              {blue_ale.get()}               {blue_ale.get() * 170}")
        file.write(f"\nBlue Ale              {blue_ale.get()}               {blue_ale.get() * 170}")
    if watermelon_mojito.get() != 0:
        txt.insert(END,f"\nWatermelon Mojito     {watermelon_mojito.get()}               {watermelon_mojito.get() * 170}")
        file.write(f"\nWatermelon Mojito     {watermelon_mojito.get()}               {watermelon_mojito.get() * 170}")
    if green_apple.get() != 0:
        txt.insert(END,f"\nGreen Apple           {green_apple.get()}               {green_apple.get() * 170}")
        file.write(f"\nGreen Apple           {green_apple.get()}               {green_apple.get() * 170}")
    if blueberry_slush.get() != 0:
        txt.insert(END,f"\nBlueberry S.          {blueberry_slush.get()}               {blueberry_slush.get() * 200}")
        file.write(f"\nBlueberry S.          {blueberry_slush.get()}               {blueberry_slush.get() * 200}")
    if cranberry_slush.get() != 0:
        txt.insert(END,f"\nCranberry S.          {cranberry_slush.get()}               {cranberry_slush.get() * 200}")
        file.write(f"\nCranberry S.          {cranberry_slush.get()}               {cranberry_slush.get() * 200}")
    if the_breeze.get() != 0:
        txt.insert(END,f"\nThe Breeze            {the_breeze.get()}               {the_breeze.get() * 230}")
        file.write(f"\nThe Breeze            {the_breeze.get()}               {the_breeze.get() * 230}")
    if pinacolda.get() != 0:
        txt.insert(END,f"\nPinacolda             {pinacolda.get()}               {pinacolda.get() * 200}")
        file.write(f"\nPinacolda             {pinacolda.get()}               {pinacolda.get() * 200}")
    if peach_iced_tea.get() != 0:
        txt.insert(END,f"\nPeach Iced Tea        {peach_iced_tea.get()}               {peach_iced_tea.get() * 180}")
        file.write(f"\nPeach Iced Tea        {peach_iced_tea.get()}               {peach_iced_tea.get() * 180}")
    if lemon_iced_tea.get() != 0:
        txt.insert(END,f"\nLemon Iced Tea        {lemon_iced_tea.get()}               {lemon_iced_tea.get() * 180}")
        file.write(f"\nLemon Iced Tea        {lemon_iced_tea.get()}               {lemon_iced_tea.get() * 180}")
    if butter_crossant.get() != 0:
        txt.insert(END,f"\nButter Croissant      {butter_crossant.get()}               {butter_crossant.get() * 180}")
        file.write(f"\nButter Croissant      {butter_crossant.get()}               {butter_crossant.get() * 180}")
    if almond_croissant.get() != 0:
        txt.insert(END,f"\nAlmond Croissant      {almond_croissant.get()}               {almond_croissant.get() * 220}")
        file.write(f"\nAlmond Croissant      {almond_croissant.get()}               {almond_croissant.get() * 220}")
    if nutella_croissant.get() != 0:
        txt.insert(END,f"\nNuteela Croissant     {nutella_croissant.get()}               {nutella_croissant.get() * 230}")
        file.write(f"\nNuteela Croissant     {nutella_croissant.get()}               {nutella_croissant.get() * 230}")
    if pain_au_chocolate.get() != 0:
        txt.insert(END,f"\nPain Au Chocolate     {pain_au_chocolate.get()}               {pain_au_chocolate.get() * 220}")
        file.write(f"\nPain Au Chocolate     {pain_au_chocolate.get()}               {pain_au_chocolate.get() * 220}")
    if exotic_cruffin.get() != 0:
        txt.insert(END,f"\nExotic Cruffin        {exotic_cruffin.get()}               {exotic_cruffin.get() * 200}")
        file.write(f"\nExotic Cruffin        {exotic_cruffin.get()}               {exotic_cruffin.get() * 200}")
    if pistachio_raspberry_danish.get() != 0:
        txt.insert(END,f"\nPistachio Ras.D.      {pistachio_raspberry_danish.get()}               {pistachio_raspberry_danish.get() * 200}")
        file.write(f"\nPistachio Ras.D.      {pistachio_raspberry_danish.get()}               {pistachio_raspberry_danish.get() * 200}")
    if parmesan_spinach_cheese_sandwich.get() != 0:
        txt.insert(END,f"\nParmesan Spi. Che.    {parmesan_spinach_cheese_sandwich.get()}               {parmesan_spinach_cheese_sandwich.get() * 230}")
        file.write(f"\nParmesan Spi. Che.    {parmesan_spinach_cheese_sandwich.get()}               {parmesan_spinach_cheese_sandwich.get() * 230}")
    if pesto_basil_spinach_sandwich.get() != 0:
        txt.insert(END,f"\nPesto Basil Spi.      {pesto_basil_spinach_sandwich.get()}               {pesto_basil_spinach_sandwich.get() * 180}")
        file.write(f"\nPesto Basil Spi.      {pesto_basil_spinach_sandwich.get()}               {pesto_basil_spinach_sandwich.get() * 180}")
    if cream_cheese_bagel.get() != 0:
        txt.insert(END,f"\nCream Cheese Bagel    {cream_cheese_bagel.get()}               {cream_cheese_bagel.get() * 180}")
        file.write(f"\nCream Cheese Bagel    {cream_cheese_bagel.get()}               {cream_cheese_bagel.get() * 180}")
    if veggi_cheese_bagel.get() != 0:
        txt.insert(END,f"\nVeggi Cheese Bagel    {veggi_cheese_bagel.get()}               {veggi_cheese_bagel.get() * 230}")
        file.write(f"\nVeggi Cheese Bagel    {veggi_cheese_bagel.get()}               {veggi_cheese_bagel.get() * 230}")
    if veggi_cheese_croissant.get() != 0:
        txt.insert(END,f"\nVeggi Cheese Cro.     {veggi_cheese_croissant.get()}               {veggi_cheese_croissant.get() * 240}")
        file.write(f"\nVeggi Cheese Cro.     {veggi_cheese_croissant.get()}               {veggi_cheese_croissant.get() * 240}")
    if nutella_brownie.get() != 0:
        txt.insert(END,f"\nNutella Brownie       {nutella_brownie.get()}               {nutella_brownie.get() * 140}")
        file.write(f"\nNutella Brownie       {nutella_brownie.get()}               {nutella_brownie.get() * 140}")
    if walnut_brownie.get() != 0:
        txt.insert(END,f"\nWalnut Brownie        {walnut_brownie.get()}               {walnut_brownie.get() * 140}")
        file.write(f"\nWalnut Brownie        {walnut_brownie.get()}               {walnut_brownie.get() * 140}")
    if toffee.get() != 0:
        txt.insert(END,f"\nToffee Brownie        {toffee.get()}               {toffee.get() * 140}")
        file.write(f"\nToffee Brownie        {toffee.get()}               {toffee.get() * 140}")
    if red_velvet_brownie.get() != 0:
        txt.insert(END,f"\nRed Velvet B.         {red_velvet_brownie.get()}               {red_velvet_brownie.get() * 180}")
        file.write(f"\nRed Velvet B.         {red_velvet_brownie.get()}               {red_velvet_brownie.get() * 180}")
    if ganache_cake.get() != 0:
        txt.insert(END,f"\nGanache Cake          {ganache_cake.get()}               {ganache_cake.get() * 250}")
        file.write(f"\nGanache Cake          {ganache_cake.get()}               {ganache_cake.get() * 250}")
    if choco_chips_cookie.get() != 0:
        txt.insert(END,f"\nChoco Chips Coo.      {choco_chips_cookie.get()}               {choco_chips_cookie.get() * 80}")
        file.write(f"\nChoco Chips Coo.      {choco_chips_cookie.get()}               {choco_chips_cookie.get() * 80}")
    txt.insert(END,"\n===========================================")
    txt.insert(END,f"\n                          Total : {total_all}")
    file.write("\n===========================================")
    file.write(f"\n                          Total : {total_all}")
    file.close()



def clear():
    txt.delete('1.0',END)

def exit():
    root.destroy()



#============Title Fream===========
title=Label(root,text="Billing Software",bd=12,bg=bg_color,fg=fg_color,relief="groove",font=("time new romen",30,"bold"),pady=13)
title.pack(fill=X)

#===========Customer Fream==============
F1=LabelFrame(text="Customer Ditails",font=("time new roman",12,"bold"),fg="gold",bg=bg_color,relief="groove",bd=10)
F1.place(x = 0,y = 90,relwidth= 1 )

#===============Customer Name===========#
cname_lbl=Label(F1,text="Customer Name ",bg=bg_color,fg=fg_color,font=("time new roman",15,"bold")).grid(row=0,column=0,padx=30,pady=5)
cname_en=Entry(F1,bd=8,relief="groove",textvariable=cus_name)
cname_en.grid(row=0,column=1,ipadx=40,ipady=4,pady=5)

#==============Customer Phone===========
cphone_lbl=Label(F1,text="Phone No.",bg=bg_color,fg=fg_color,font=("time new roman",15,"bold")).grid(row=0,column=2,padx=30)
cphone_en=Entry(F1,bd=8,relief="groove",textvariable=c_phone)
cphone_en.grid(row=0,column=3,ipadx=40,ipady=4,pady=5)

#=============Bill No==============
cbill_lbl=Label(F1,text="Bill No.",bg=bg_color,fg=fg_color,font=("time new roman",15,"bold")).grid(row=0,column=4,padx=30)
cbill_en=Entry(F1,bd=8,relief="groove",textvariable=c_bill_no)
cbill_en.grid(row=0,column=5,ipadx=40,ipady=4,pady=5)

#============Enter Button=========
cEnter=Button(F1,text="Enter",bg=bg_color,fg=fg_color,font=("time new roman",15,"bold"))
cEnter.grid(row=0,column=6,ipadx=45,padx=100,ipady=5,pady=5,)

#==========Costmetic ===============
canvas = Canvas(root,bd=0,bg=bg_color,height=100)
canvas.pack(side=LEFT, fill=BOTH, expand=True,pady=82)
scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# F2 = LabelFrame(canvas, text="Costmitc Item", bd=10)

F2=LabelFrame(canvas,text="Menu Item",bg=bg_color,fg="gold",font=("time new roman",12,"bold"),relief="groove",bd=10)
canvas.create_window((0, 0), window=F2, anchor="nw")
# F2.place(x=0,y=180,width=1153,height=380)


#================Cheesecake==================

Pavbhaji_label=Label(F2,text="CHEESECAKE",bg=bg_color,fg="gold",font=("time new roman",15,"bold"))
Pavbhaji_label.grid(row=0,column=0)

oil_lbl=Label(F2,text="Original new york",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=1,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=original_new_york,width=10)
oil_en.grid(row=1,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Blueberry/Cherry",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=1,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=Blueberry_cherry,width=10)
oil_en.grid(row=1,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Strawberry",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=1,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=strawbeery,width=10)
oil_en.grid(row=1,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Mixed Berry",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=2,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=mixed_berry,width=10)
oil_en.grid(row=2,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Nutella",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=2,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=nutella,width=10)
oil_en.grid(row=2,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Biscoff",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=2,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=biscoff,width=10)
oil_en.grid(row=2,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Oreo",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=3,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=oreo,width=10)
oil_en.grid(row=3,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="All About Chocolate",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=3,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=all_about,width=10)
oil_en.grid(row=3,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Pistachio",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=3,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=pistachio,width=10)
oil_en.grid(row=3,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="White ",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=4,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=white_cho_raspberry,width=10)
oil_en.grid(row=4,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Lemon Raspberry",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=4,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=lemon_raspberry,width=10)
oil_en.grid(row=4,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Ferrero Rocher",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=4,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=ferrero_rocher,width=10)
oil_en.grid(row=4,column=5,ipadx=10,ipady=5,padx=20)

#================CLASSIC==================

Pavbhaji_label=Label(F2,text="CLASSIC",bg=bg_color,fg="gold",font=("time new roman",15,"bold"))
Pavbhaji_label.grid(row=5,column=0)

oil_lbl=Label(F2,text="Espresso(H/I)",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=6,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=espresso,width=10)
oil_en.grid(row=6,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Americano(H/I)",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=6,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=americano,width=10)
oil_en.grid(row=6,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Cortado",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=6,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=cortado,width=10)
oil_en.grid(row=6,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Cappuccino",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=7,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=cappuccino,width=10)
oil_en.grid(row=7,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Cafe Latte(H/I)",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=7,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=cafe_latte,width=10)
oil_en.grid(row=7,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Flat White",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=7,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=flat_white,width=10)
oil_en.grid(row=7,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Cafe Mocha",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=8,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=cafe_mocha,width=10)
oil_en.grid(row=8,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Affogatto",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=8,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=affogatto,width=10)
oil_en.grid(row=8,column=3,ipadx=10,ipady=5,padx=20)

# #===================HAND BREWED==============
Pavbhaji_label=Label(F2,text="HAND BREWED",bg=bg_color,fg="gold",font=("time new roman",15,"bold"))
Pavbhaji_label.grid(row=9,column=0)

oil_lbl=Label(F2,text="V60 P.Over(H/I)",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=10,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=affogatto,width=10)
oil_en.grid(row=10,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Aeropress(H/I)",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=10,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=affogatto,width=10)
oil_en.grid(row=10,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Cold Brew",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=10,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=cold_brew,width=10)
oil_en.grid(row=10,column=5,ipadx=10,ipady=5,padx=20)

# #===================CAFFEINE REFRESHERS==============
Pavbhaji_label=Label(F2,text="CAFFEINE REFRESHERS",bg=bg_color,fg="gold",font=("time new roman",15,"bold"))
Pavbhaji_label.grid(row=11,column=0)

oil_lbl=Label(F2,text="Espresso Tonic",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=12,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=espresso_tonic,width=10)
oil_en.grid(row=12,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Cold Brew T.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=12,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=cold_brew_tonic,width=10)
oil_en.grid(row=12,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Whisky Barrel Aged",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=12,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=whisky_barrel_aged,width=10)
oil_en.grid(row=12,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Bitter Ground E.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=13,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=bitter_ground_espresso,width=10)
oil_en.grid(row=13,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Lime Light",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=13,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=lime_light,width=10)
oil_en.grid(row=13,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Caffeine Bomb",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=13,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=cafeeine_bomb,width=10)
oil_en.grid(row=13,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Vietnamese",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=14,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=vietnamese,width=10)
oil_en.grid(row=14,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Bombon",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=14,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=bombon,width=10)
oil_en.grid(row=14,column=3,ipadx=10,ipady=5,padx=20)

# #===================HAND CRAFTED==============
Pavbhaji_label=Label(F2,text="HAND CRAFTED",bg=bg_color,fg="gold",font=("time new roman",15,"bold"))
Pavbhaji_label.grid(row=15,column=0)

oil_lbl=Label(F2,text="Breeze Espresso",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=16,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=the_breeze_espresso,width=10)
oil_en.grid(row=16,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Coffee Cran T.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=16,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=coffee_cran_tonic,width=10)
oil_en.grid(row=16,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Yuzu Espresso T.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=16,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=yuzu_espresso_tonic,width=10)
oil_en.grid(row=16,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Orange Espresso T.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=17,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=orange_espresso_tonic,width=10)
oil_en.grid(row=17,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Flora",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=17,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=flora,width=10)
oil_en.grid(row=17,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Cold fassioned",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=17,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=cold_fassioned,width=10)
oil_en.grid(row=17,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Tiramisu Hot Cho.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=18,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=tiramisu_hot_chocolate,width=10)
oil_en.grid(row=18,column=1,ipadx=10,ipady=5,padx=20)

# #================CREAMY COLD FRAPPES=================
Pavbhaji_label=Label(F2,text="CREAMY COLD FRA.",bg=bg_color,fg="gold",font=("time new roman",15,"bold"))
Pavbhaji_label.grid(row=19,column=0)

oil_lbl=Label(F2,text="Frappe Latte",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=20,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=frappe_latte,width=10)
oil_en.grid(row=20,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Caramel Frappe L.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=20,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=caramel_frappe_latte,width=10)
oil_en.grid(row=20,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Hazelnut Frappe L.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=20,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=hazelnut_frappe_latte,width=10)
oil_en.grid(row=20,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Frappe mocha",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=21,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=frappe_mocha,width=10)
oil_en.grid(row=21,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Frappe Mocha Cru.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=21,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=frappe_mocha_crumble,width=10)
oil_en.grid(row=21,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="biscoff Frappe L.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=21,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=biscoff_frappe_latte,width=10)
oil_en.grid(row=21,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="The Raven Snow F.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=22,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=the_raven_snow_frappe,width=10)
oil_en.grid(row=22,column=1,ipadx=10,ipady=5,padx=20)

# #================SHAKES=================
Pavbhaji_label=Label(F2,text="SHAKES",bg=bg_color,fg="gold",font=("time new roman",15,"bold"))
Pavbhaji_label.grid(row=23,column=0)

oil_lbl=Label(F2,text="Oreo Cookies/Cream",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=24,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=oreo_cookies_cream,width=10)
oil_en.grid(row=24,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Nutella Hazelnuts S.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=24,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=nutella_hazelnutes_shake,width=10)
oil_en.grid(row=24,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Berry Blast Shake",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=24,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=berry_blast_shake,width=10)
oil_en.grid(row=24,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Biscoff Shake",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=25,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=biscoff_shake,width=10)
oil_en.grid(row=25,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Berry Biscoff S.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=25,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=berry_biscoff_shake,width=10)
oil_en.grid(row=25,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Pink Chocolate S.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=25,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=pink_chocolate_shake,width=10)
oil_en.grid(row=25,column=5,ipadx=10,ipady=5,padx=20)

# #================COOLERS=================
Pavbhaji_label=Label(F2,text="COOLESR",bg=bg_color,fg="gold",font=("time new roman",15,"bold"))
Pavbhaji_label.grid(row=26,column=0)

oil_lbl=Label(F2,text="Mint Mojito",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=27,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=mint_mojito,width=10)
oil_en.grid(row=27,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Blue Ale",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=27,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=blue_ale,width=10)
oil_en.grid(row=27,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Watermelon Mojito",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=27,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=watermelon_mojito,width=10)
oil_en.grid(row=27,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="green Apple",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=28,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=green_apple,width=10)
oil_en.grid(row=28,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Blueberry Slush",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=28,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=blueberry_slush,width=10)
oil_en.grid(row=28,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Cranberry Slush",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=28,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=cranberry_slush,width=10)
oil_en.grid(row=28,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="The Breeze",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=29,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=the_breeze,width=10)
oil_en.grid(row=29,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Pinacolda",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=29,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=pinacolda,width=10)
oil_en.grid(row=29,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Peach Iced Tea",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=29,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=peach_iced_tea,width=10)
oil_en.grid(row=29,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Lemon Iced Tea",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=30,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=lemon_iced_tea,width=10)
oil_en.grid(row=30,column=1,ipadx=10,ipady=5,padx=20)

# #================SPECIALITY BAKERY=================
Pavbhaji_label=Label(F2,text="SPECIALITY BAKERY",bg=bg_color,fg="gold",font=("time new roman",12,"bold"))
Pavbhaji_label.grid(row=31,column=0)

Pavbhaji_label=Label(F2,text="CROISSANT",bg=bg_color,fg="gold",font=("time new roman",15,"bold"))
Pavbhaji_label.grid(row=32,column=0)

oil_lbl=Label(F2,text="Butter Croissant",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=33,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=butter_crossant,width=10)
oil_en.grid(row=33,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Almond Croissant",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=33,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=almond_croissant,width=10)
oil_en.grid(row=33,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Nutella Croissant",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=33,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=nutella_croissant,width=10)
oil_en.grid(row=33,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Pain Au Chocolate",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=34,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=pain_au_chocolate,width=10)
oil_en.grid(row=34,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Exotic Cruffin",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=34,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=exotic_cruffin,width=10)
oil_en.grid(row=34,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Pistachio R. Danish",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=34,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=pistachio_raspberry_danish,width=10)
oil_en.grid(row=34,column=5,ipadx=10,ipady=5,padx=20)

# #================SANDWICHS=================
Pavbhaji_label=Label(F2,text="SANDWICHS",bg=bg_color,fg="gold",font=("time new roman",15,"bold"))
Pavbhaji_label.grid(row=35,column=0)

oil_lbl=Label(F2,text="Parmesan Spinach Cheese",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=36,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=parmesan_spinach_cheese_sandwich,width=10)
oil_en.grid(row=36,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Pesto Basil Spinache",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=36,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=pesto_basil_spinach_sandwich,width=10)
oil_en.grid(row=36,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Cream Cheese Bagel",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=36,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=cream_cheese_bagel,width=10)
oil_en.grid(row=36,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Veggi Cheese Bagel",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=37,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=veggi_cheese_bagel,width=10)
oil_en.grid(row=37,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Veggi Cheese Croissant",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=37,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=veggi_cheese_croissant,width=10)
oil_en.grid(row=37,column=3,ipadx=10,ipady=5,padx=20)

# #================BROWNIES* AND CAKE=================
Pavbhaji_label=Label(F2,text="BROWNIES/CAKE",bg=bg_color,fg="gold",font=("time new roman",15,"bold"))
Pavbhaji_label.grid(row=38,column=0)

oil_lbl=Label(F2,text="Nutella Brownie",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=39,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=nutella_brownie,width=10)
oil_en.grid(row=39,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Walnut Brownie",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=39,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=walnut_brownie,width=10)
oil_en.grid(row=39,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Toffee Brownie",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=39,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=toffee,width=10)
oil_en.grid(row=39,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Red Velvet B.",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=40,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=red_velvet_brownie,width=10)
oil_en.grid(row=40,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Ganache Cake",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=40,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=ganache_cake,width=10)
oil_en.grid(row=40,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="Choco Chips Cookie",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=40,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",textvariable=choco_chips_cookie,width=10)
oil_en.grid(row=40,column=5,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=41,column=0,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",width=15)
oil_en.grid(row=41,column=1,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=41,column=2,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",width=14)
oil_en.grid(row=41,column=3,ipadx=10,ipady=5,padx=20)

oil_lbl=Label(F2,text="",font=("time new roman",13,"bold"),bg=bg_color,fg=fg_color)
oil_lbl.grid(row=41,column=4,padx=4,pady=20)
oil_en=Entry(F2,bd=8,relief="groove",width=14)
oil_en.grid(row=41,column=5,ipadx=10,ipady=5,padx=20)



# F2.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))


#===================bill Area=========================
F5=Frame(canvas,bd=8,relief="groove")
F5.place(x=1140,width=384,height=470)
bill_titel=Label(F5,text="Bill Area",font=("Lucida",15,"bold"),bd=7,relief="groove")
bill_titel.pack(fill=X)

#====================Scroll bar in bill area=================
scroll_y=Scrollbar(F5,orient="vertical")
txt=Text(F5,yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=txt.yview)
txt.pack(fill=BOTH,expand=1)

#====================bill manu========================
F6=LabelFrame(root,text="Bill Manu",bg=bg_color,fg="gold",relief="groove",bd=10,font=("time new roman",12,"bold"))
F6.place(x=0,y=645,relwidth=1,height=150)

#======================cosmatics====================
cosmatics_lbl=Label(F6,text="Total All",bg=bg_color,fg=lbl_color,font=("time new roman",15,"bold"))
cosmatics_lbl.grid(row=2,column=0,padx=20,pady=15)
cosmatics_en=Entry(F6,bd=8,relief="groove",textvariable=total_menu)
cosmatics_en.grid(row=2,column=1,ipadx=15,ipady=8)


#====================total button=====================
total_lbl=Button(F6,text="Total",bg=bg_color,fg=lbl_color,font=("lucida",12,"bold"),bd=3,relief="groove",command=total)
total_lbl.grid(row=2,column=4,ipadx=30,padx=50)

#=====================genrate bill======================
gen_lbl=Button(F6,text="Generate Bill",bg=bg_color,fg=lbl_color,font=("lucida",12,"bold"),bd=3,relief="groove",command=bill_area)
gen_lbl.grid(row=2,column=5,ipadx=30,padx=50)

#===========================clear========================
clear_lbl=Button(F6,text="Clear",bg=bg_color,fg=lbl_color,font=("lucida",12,"bold"),bd=3,relief="groove",command=clear)
clear_lbl.grid(row=2,column=6,ipadx=20,padx=50)

#===========================exit========================
exit_lbl=Button(F6,text="Exit",bg=bg_color,fg=lbl_color,font=("lucida",12,"bold"),bd=3,relief="groove",command=exit)
exit_lbl.grid(row=2,column=7,ipadx=20,padx=50,pady=50)


root.mainloop()