# coding=utf-8

# 1 - imports
from datetime import date, datetime
import pandas as pd
import numpy as np

from models.additive import Additive
from models.allergen import Allergen
from models.brand import Brand
from models.category import Category
from models.country import Country
from models.emb import Emb
from models.label import Label
from models.package import Package
from models.product import Product
from models.trace import Trace
from models.store import Store
from base import Session, engine, Base
from sqlalchemy.exc import IntegrityError

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()
products = []
# 4 - create products
df = pd.read_csv("en.openfoodfacts.org.products.csv", sep='\t', dtype={'code':str})
df = df.replace({np.nan: None})
df = df.drop_duplicates(subset=['code'], keep='last')
length = len(df.index)
additive_inserted = {}
allergen_inserted = {}
brand_inserted    = {}
category_inserted = {}
country_inserted = {}
emb_inserted = {}
label_inserted = {}
packaging_inserted = {}
trace_inserted = {}
store_inserted = {}
for index, row in df.iterrows():
    dt_started = datetime.utcnow()
    # Additives
    if row["additives_en"] == None:
        additive_list = ["Unknown"]
    else:
        additive_list = row["additives_en"].split(',')
    additive_append = []
    for additive_ in additive_list:
        additive_ = additive_.strip()
        if additive_ in additive_inserted:
            c_id = additive_inserted[additive_]
        else:
            c_id = Additive(
                name=additive_
            )
            additive_inserted[additive_] = c_id
        additive_append.append(c_id)
    # Allergen
    if row["allergens"] == None:
        allergen_list = ["Unknown"]
    else:
        allergen_list = row["allergens"].split(',')
    allergen_append = []
    for allergen_ in allergen_list:
        allergen_ = allergen_.strip()
        if allergen_ in allergen_inserted:
            c_id = allergen_inserted[allergen_]
        else:
            c_id = Allergen(
                name=allergen_
            )
            allergen_inserted[allergen_] = c_id
        allergen_append.append(c_id)
    # Brands
    if row["brands"] == None:
        brand_list = ["Unknown"]
    else:
        brand_list = row["brands"].split(',')
    brand_append = []
    for brand_ in brand_list:
        brand_ = brand_.strip()
        if brand_ in brand_inserted:
            c_id = brand_inserted[brand_]
        else:
            c_id = Brand(
                name=brand_
            )
            brand_inserted[brand_] = c_id
        brand_append.append(c_id)
    # Countries
    if row["countries_en"] == None:
        country_list = ["Unknown"]
    else:
        country_list = row["countries_en"].split(',')
    country_append = []
    for country_ in country_list:
        country_ = country_.strip()
        if country_ in country_inserted:
            c_id = country_inserted[country_]
        else:
            c_id = Country(
                name_en=country_
            )
            country_inserted[country_] = c_id
        country_append.append(c_id)

    # Categories
    if row["categories"] == None:
        category_list = ["Unknown"]
    else:
        category_list = row["categories"].split(',')
    category_append = []
    for category_ in category_list:
        category_ = category_.strip()
        if category_ in category_inserted:
            c_id = category_inserted[category_]
        else:
            c_id = Category(
                name=category_
            )
            category_inserted[category_] = c_id
        category_append.append(c_id)

    # Origin
    if row["origins"] == None:
        country_list = ["Unknown"]
    else:
        country_list = row["origins"].split(',')
    origin_append = []
    for country_ in country_list:
        country_ = country_.strip()
        if country_ in country_inserted:
            c_id = country_inserted[country_]
        else:
            c_id = Country(
                name_en=country_
            )
            country_inserted[country_] = c_id
        origin_append.append(c_id)
    # Emb
    if row["emb_codes"] == None:
        emb_list = ["Unknown"]
    else:
        emb_list = row["emb_codes"].split(',')
    emb_append = []
    for emb_ in emb_list:
        emb_ = emb_.strip()
        if emb_ in emb_inserted:
            c_id = emb_inserted[emb_]
        else:
            c_id = Emb(
                name=emb_
            )
            emb_inserted[emb_] = c_id
        emb_append.append(c_id)   
    # Labels
    if row["labels"] == None:
        label_list = ["Unknown"]
    else:
        label_list = row["labels"].split(',')
    label_append = []
    for label_ in label_list:
        label_ = label_.strip()
        if label_ in label_inserted:
            c_id = label_inserted[label_]
        else:
            c_id = Label(
                name=label_
            )
            label_inserted[label_] = c_id
        label_append.append(c_id)
    # Package
    if row["packaging"] == None:
        packaging_list = ["Unknown"]
    else:
        packaging_list = row["packaging"].split(',')
    packaging_append = []
    for packaging_ in packaging_list:
        packaging_ = packaging_.strip()
        if packaging_ in packaging_inserted:
            c_id = packaging_inserted[packaging_]
        else:
            c_id = Package(
                name=packaging_
            )
            packaging_inserted[packaging_] = c_id
        packaging_append.append(c_id)
    # Traces
    if row["traces_en"] == None:
        trace_list = ["Unknown"]
    else:
        trace_list = row["traces_en"].split(',')
    trace_append = []
    for trace_ in trace_list:
        trace_ = trace_.strip()
        if trace_ in trace_inserted:
            c_id = trace_inserted[trace_]
        else:
            c_id = Trace(
                name=trace_
            )
            trace_inserted[trace_] = c_id
        trace_append.append(c_id)
    # Stores
    if row["stores"] == None:
        store_list = ["Unknown"]
    else:
        store_list = row["stores"].split(',')
    store_append = []
    for store_ in store_list:
        store_ = store_.strip()
        if store_ in store_inserted:
            c_id = store_inserted[store_]
        else:
            c_id = Store(
                name=store_
            )
            store_inserted[store_] = c_id
        store_append.append(c_id)
    dt_ended = datetime.utcnow()
    # print((dt_ended - dt_started).total_seconds())
    # Products
    product = Product(
        code=row["code"],
        url=row["url"],
        creator=row["creator"],
        created_at=date.fromtimestamp(row["created_t"]),
        updated_at=date.fromtimestamp(row["last_modified_t"]),
        product_name=row["product_name"],
        abbreviated_product_name=row["abbreviated_product_name"],
        generic_name=row["generic_name"],
        quantity=row["quantity"],
        manufacturing_places = row["manufacturing_places"],
        manufacturing_places_tags = row["manufacturing_places_tags"],
        first_packaging_code_geo = row["first_packaging_code_geo"],
        cities = row["cities"],
        cities_tags = row["cities_tags"],
        purchase_places = row["purchase_places"],
        stores = row["stores"],
        ingredients_text = row["ingredients_text"],
        serving_size = row["serving_size"],
        serving_quantity = row["serving_quantity"],
        no_nutriments = row["no_nutriments"],
        ingredients_from_palm_oil_n = row["ingredients_from_palm_oil_n"],
        ingredients_from_palm_oil = row["ingredients_from_palm_oil"],
        ingredients_from_palm_oil_tags = row["ingredients_from_palm_oil_tags"],
        ingredients_that_may_be_from_palm_oil_n = row["ingredients_that_may_be_from_palm_oil_n"],
        ingredients_that_may_be_from_palm_oil = row["ingredients_that_may_be_from_palm_oil"],
        ingredients_that_may_be_from_palm_oil_tags = row["ingredients_that_may_be_from_palm_oil_tags"],
        nutriscore_score = row["nutriscore_score"],
        nutriscore_grade = row["nutriscore_grade"],
        nova_group = row["nova_group"],
        pnns_groups_1 = row["pnns_groups_1"],
        pnns_groups_2 = row["pnns_groups_2"],
        # states = row["states"],
        # states_tags = row["states_tags"],
        # states_en = row["states_en"],
        brand_owner = row["brand_owner"],
        main_category = row["main_category"],
        main_category_en = row["main_category_en"],
        ecoscore_score_fr = row["ecoscore_score_fr"],
        ecoscore_grade_fr = row["ecoscore_grade_fr"],
        image_url = row["image_url"],
        image_small_url = row["image_small_url"],
        image_ingredients_url = row["image_ingredients_url"],
        image_ingredients_small_url = row["image_ingredients_small_url"],
        image_nutrition_url = row["image_nutrition_url"],
        image_nutrition_small_url = row["image_nutrition_small_url"],
        energy_kj_100g = row["energy-kj_100g"],
        energy_kcal_100g = row["energy-kcal_100g"],
        energy_100g = row["energy_100g"],
        energy_from_fat_100g = row["energy-from-fat_100g"],
        fat_100g = row["fat_100g"],
        saturated_fat_100g = row["saturated-fat_100g"],
        butyric_acid_100g = row["-butyric-acid_100g"],
        caproic_acid_100g = row["-caproic-acid_100g"],
        caprylic_acid_100g = row["-caprylic-acid_100g"],
        capric_acid_100g = row["-capric-acid_100g"],
        lauric_acid_100g = row["-lauric-acid_100g"],
        myristic_acid_100g = row["-myristic-acid_100g"],
        palmitic_acid_100g = row["-palmitic-acid_100g"],
        stearic_acid_100g = row["-stearic-acid_100g"],
        arachidic_acid_100g = row["-arachidic-acid_100g"],
        behenic_acid_100g = row["-behenic-acid_100g"],
        lignoceric_acid_100g = row["-lignoceric-acid_100g"],
        cerotic_acid_100g = row["-cerotic-acid_100g"],
        montanic_acid_100g = row["-montanic-acid_100g"],
        melissic_acid_100g = row["-melissic-acid_100g"],
        monounsaturated_fat_100g = row["monounsaturated-fat_100g"],
        polyunsaturated_fat_100g = row["polyunsaturated-fat_100g"],
        omega_3_fat_100g = row["omega-3-fat_100g"],
        alpha_linolenic_acid_100g = row["-alpha-linolenic-acid_100g"],
        eicosapentaenoic_acid_100g = row["-eicosapentaenoic-acid_100g"],
        docosahexaenoic_acid_100g = row["-docosahexaenoic-acid_100g"],
        omega_6_fat_100g = row["omega-6-fat_100g"],
        linoleic_acid_100g = row["-linoleic-acid_100g"],
        arachidonic_acid_100g = row["-arachidonic-acid_100g"],
        gamma_linolenic_acid_100g = row["-gamma-linolenic-acid_100g"],
        dihomo_gamma_linolenic_acid_100g = row["-dihomo-gamma-linolenic-acid_100g"],
        omega_9_fat_100g = row["omega-9-fat_100g"],
        oleic_acid_100g = row["-oleic-acid_100g"],
        elaidic_acid_100g = row["-elaidic-acid_100g"],
        gondoic_acid_100g = row["-gondoic-acid_100g"],
        mead_acid_100g = row["-mead-acid_100g"],
        erucic_acid_100g = row["-erucic-acid_100g"],
        nervonic_acid_100g = row["-nervonic-acid_100g"],
        trans_fat_100g = row["trans-fat_100g"],
        cholesterol_100g = row["cholesterol_100g"],
        carbohydrates_100g = row["carbohydrates_100g"],
        sugars_100g = row["sugars_100g"],
        sucrose_100g = row["-sucrose_100g"],
        glucose_100g = row["-glucose_100g"],
        fructose_100g = row["-fructose_100g"],
        lactose_100g = row["-lactose_100g"],
        maltose_100g = row["-maltose_100g"],
        maltodextrins_100g = row["-maltodextrins_100g"],
        starch_100g = row["starch_100g"],
        polyols_100g = row["polyols_100g"],
        fiber_100g = row["fiber_100g"],
        soluble_fiber_100g = row["-soluble-fiber_100g"],
        insoluble_fiber_100g = row["-insoluble-fiber_100g"],
        proteins_100g = row["proteins_100g"],
        casein_100g = row["casein_100g"],
        serum_proteins_100g = row["serum-proteins_100g"],
        nucleotides_100g = row["nucleotides_100g"],
        salt_100g = row["salt_100g"],
        sodium_100g = row["sodium_100g"],
        alcohol_100g = row["alcohol_100g"],
        vitamin_a_100g = row["vitamin-a_100g"],
        beta_carotene_100g = row["beta-carotene_100g"],
        vitamin_d_100g = row["vitamin-d_100g"],
        vitamin_e_100g = row["vitamin-e_100g"],
        vitamin_k_100g = row["vitamin-k_100g"],
        vitamin_c_100g = row["vitamin-c_100g"],
        vitamin_b1_100g = row["vitamin-b1_100g"],
        vitamin_b2_100g = row["vitamin-b2_100g"],
        vitamin_pp_100g = row["vitamin-pp_100g"],
        vitamin_b6_100g = row["vitamin-b6_100g"],
        vitamin_b9_100g = row["vitamin-b9_100g"],
        folates_100g = row["folates_100g"],
        vitamin_b12_100g = row["vitamin-b12_100g"],
        biotin_100g = row["biotin_100g"],
        pantothenic_acid_100g = row["pantothenic-acid_100g"],
        silica_100g = row["silica_100g"],
        bicarbonate_100g = row["bicarbonate_100g"],
        potassium_100g = row["potassium_100g"],
        chloride_100g = row["chloride_100g"],
        calcium_100g = row["calcium_100g"],
        phosphorus_100g = row["phosphorus_100g"],
        iron_100g = row["iron_100g"],
        magnesium_100g = row["magnesium_100g"],
        zinc_100g = row["zinc_100g"],
        copper_100g = row["copper_100g"],
        manganese_100g = row["manganese_100g"],
        fluoride_100g = row["fluoride_100g"],
        selenium_100g = row["selenium_100g"],
        chromium_100g = row["chromium_100g"],
        molybdenum_100g = row["molybdenum_100g"],
        iodine_100g = row["iodine_100g"],
        caffeine_100g = row["caffeine_100g"],
        taurine_100g = row["taurine_100g"],
        ph_100g = row["ph_100g"],
        fruits_vegetables_nuts_100g = row["fruits-vegetables-nuts_100g"],
        fruits_vegetables_nuts_dried_100g = row["fruits-vegetables-nuts-dried_100g"],
        fruits_vegetables_nuts_estimate_100g = row["fruits-vegetables-nuts-estimate_100g"],
        fruits_vegetables_nuts_estimate_from_ingredients_100g = row["fruits-vegetables-nuts-estimate-from-ingredients_100g"],
        collagen_meat_protein_ratio_100g = row["collagen-meat-protein-ratio_100g"],
        cocoa_100g = row["cocoa_100g"],
        chlorophyl_100g = row["chlorophyl_100g"],
        carbon_footprint_100g = row["carbon-footprint_100g"],
        carbon_footprint_from_meat_or_fish_100g = row["carbon-footprint-from-meat-or-fish_100g"],
        nutrition_score_fr_100g = row["nutrition-score-fr_100g"],
        nutrition_score_uk_100g = row["nutrition-score-uk_100g"],
        glycemic_index_100g = row["glycemic-index_100g"],
        water_hardness_100g = row["water-hardness_100g"],
        choline_100g = row["choline_100g"],
        phylloquinone_100g = row["phylloquinone_100g"],
        beta_glucan_100g = row["beta-glucan_100g"],
        inositol_100g = row["inositol_100g"],
        carnitine_100g = row["carnitine_100g"],
    )
    for a in additive_append:
        product.additives.append(a)
    for a in allergen_append:
        product.allergens.append(a)
    for b in brand_append:
        product.brands.append(b)
    for c in category_append:
        product.categories.append(c)
    for c in country_append:
        product.countries.append(c)
    for e in emb_append:
        product.emb_codes.append(e)
    for l in label_append:
        product.labels.append(l)
    for o in origin_append:
        product.origins.append(o)
    for p in packaging_append:
        product.packages.append(p)
    for t in trace_append:
        product.traces.append(t)
    for s in store_append:
        product.stores.append(s)
    try:
        products.append(product)
        if index % 2000 == 0:
            session.add_all(products)
            session.commit()
            products = []
            print(f"{datetime.utcnow()} {index}/{length} {index/length}")
    except IntegrityError as e :
        error = e.orig.pgerror
        if "duplicate key value" in error:
            code_err = error.split('Key (code)=(')[1].split(') already exists.')[0]
            print(f"Duplicate code found : {code_err}")
        else:
            print("x")
            pass
        # if ""
        session.rollback()
        pass
session.add_all(products)
session.commit()
session.close()