from sqlalchemy import Column, String, Integer, TIMESTAMP, BigInteger, Float
from sqlalchemy.orm import relationship

from base import Base
from models.additive_product import AdditiveProduct
from models.allergen_product import AllergenProduct
from models.brand_product import BrandProduct
from models.category_product import CategoryProduct
from models.country_product import CountryProduct
from models.emb_product import EmbProduct
from models.label_product import LabelProduct
from models.origin_product import OriginProduct
from models.package_product import PackageProduct
from models.product_trace import ProductTrace
from models.product_store import ProductStore
class Product(Base):
    __tablename__ = 'Product'

    code = Column(String, primary_key=True)
    url = Column(String, nullable=False)
    creator = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    product_name = Column(String, nullable=False)
    abbreviated_product_name = Column(String, nullable=True)
    generic_name = Column(String, nullable=True)
    quantity = Column(String, nullable=True)
    packages = relationship('Package', secondary='PackageProduct', back_populates='products')
    brands = relationship('Brand', secondary='BrandProduct', back_populates='products')
    categories = relationship('Category', secondary='CategoryProduct', back_populates='products')
    origins = relationship('Country', secondary='OriginProduct', back_populates='products_origins')
    # origins = Column(String, nullable=True)
    # origins_tags = Column(String, nullable=True)
    # origins_en = Column(String, nullable=True)
    manufacturing_places = Column(String, nullable=True)
    manufacturing_places_tags = Column(String, nullable=True)
    labels = relationship('Label', secondary='LabelProduct', back_populates='products')
    emb_codes = relationship('Emb', secondary='EmbProduct', back_populates='products')
    # emb_codes = Column(String, nullable=True)
    # emb_codes_tags = Column(String, nullable=True)
    first_packaging_code_geo = Column(String, nullable=True)
    cities = Column(String, nullable=True)
    cities_tags = Column(String, nullable=True)
    purchase_places = Column(String, nullable=True)
    # stores = Column(String, nullable=True)
    stores = relationship('Store', secondary='ProductStore', back_populates='products')
    countries = relationship('Country', secondary='CountryProduct', back_populates='products')
    ingredients_text = Column(String, nullable=True)
    allergens = relationship('Allergen', secondary='AllergenProduct', back_populates='products')
    traces = relationship('Trace', secondary='ProductTrace', back_populates='products')
    # traces = Column(String, nullable=True)
    # traces_tags = Column(String, nullable=True)
    # traces_en = Column(String, nullable=True)
    serving_size = Column(String, nullable=True)
    serving_quantity = Column(String, nullable=True)
    no_nutriments = Column(String, nullable=True)
    additives = relationship('Additive', secondary='AdditiveProduct', back_populates='products')
    ingredients_from_palm_oil_n = Column(String, nullable=True)
    ingredients_from_palm_oil = Column(String, nullable=True)
    ingredients_from_palm_oil_tags = Column(String, nullable=True)
    ingredients_that_may_be_from_palm_oil_n = Column(String, nullable=True)
    ingredients_that_may_be_from_palm_oil = Column(String, nullable=True)
    ingredients_that_may_be_from_palm_oil_tags = Column(String, nullable=True)
    nutriscore_score = Column(String, nullable=True)
    nutriscore_grade = Column(String, nullable=True)
    nova_group = Column(String, nullable=True)
    pnns_groups_1 = Column(String, nullable=True)
    pnns_groups_2 = Column(String, nullable=True)
    states = Column(String, nullable=True)
    states_tags = Column(String, nullable=True)
    states_en = Column(String, nullable=True)
    brand_owner = Column(String, nullable=True)
    ecoscore_score_fr = Column(String, nullable=True)
    ecoscore_grade_fr = Column(String, nullable=True)
    main_category = Column(String, nullable=True)
    main_category_en = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    image_small_url = Column(String, nullable=True)
    image_ingredients_url = Column(String, nullable=True)
    image_ingredients_small_url = Column(String, nullable=True)
    image_nutrition_url = Column(String, nullable=True)
    image_nutrition_small_url = Column(String, nullable=True)
    energy_kj_100g = Column(Float, nullable=True)
    energy_kcal_100g = Column(Float, nullable=True)
    energy_100g = Column(Float, nullable=True)
    energy_from_fat_100g = Column(Float, nullable=True)
    fat_100g = Column(Float, nullable=True)
    saturated_fat_100g = Column(Float, nullable=True)
    butyric_acid_100g = Column(Float, nullable=True)
    caproic_acid_100g = Column(Float, nullable=True)
    caprylic_acid_100g = Column(Float, nullable=True)
    capric_acid_100g = Column(Float, nullable=True)
    lauric_acid_100g = Column(Float, nullable=True)
    myristic_acid_100g = Column(Float, nullable=True)
    palmitic_acid_100g = Column(Float, nullable=True)
    stearic_acid_100g = Column(Float, nullable=True)
    arachidic_acid_100g = Column(Float, nullable=True)
    behenic_acid_100g = Column(Float, nullable=True)
    lignoceric_acid_100g = Column(Float, nullable=True)
    cerotic_acid_100g = Column(Float, nullable=True)
    montanic_acid_100g = Column(Float, nullable=True)
    melissic_acid_100g = Column(Float, nullable=True)
    monounsaturated_fat_100g = Column(Float, nullable=True)
    polyunsaturated_fat_100g = Column(Float, nullable=True)
    omega_3_fat_100g = Column(Float, nullable=True)
    alpha_linolenic_acid_100g = Column(Float, nullable=True)
    eicosapentaenoic_acid_100g = Column(Float, nullable=True)
    docosahexaenoic_acid_100g = Column(Float, nullable=True)
    omega_6_fat_100g = Column(Float, nullable=True)
    linoleic_acid_100g = Column(Float, nullable=True)
    arachidonic_acid_100g = Column(Float, nullable=True)
    gamma_linolenic_acid_100g = Column(Float, nullable=True)
    dihomo_gamma_linolenic_acid_100g = Column(Float, nullable=True)
    omega_9_fat_100g = Column(Float, nullable=True)
    oleic_acid_100g = Column(Float, nullable=True)
    elaidic_acid_100g = Column(Float, nullable=True)
    gondoic_acid_100g = Column(Float, nullable=True)
    mead_acid_100g = Column(Float, nullable=True)
    erucic_acid_100g = Column(Float, nullable=True)
    nervonic_acid_100g = Column(Float, nullable=True)
    trans_fat_100g = Column(Float, nullable=True)
    cholesterol_100g = Column(Float, nullable=True)
    carbohydrates_100g = Column(Float, nullable=True)
    sugars_100g = Column(Float, nullable=True)
    sucrose_100g = Column(Float, nullable=True)
    glucose_100g = Column(Float, nullable=True)
    fructose_100g = Column(Float, nullable=True)
    lactose_100g = Column(Float, nullable=True)
    maltose_100g = Column(Float, nullable=True)
    maltodextrins_100g = Column(Float, nullable=True)
    starch_100g = Column(Float, nullable=True)
    polyols_100g = Column(Float, nullable=True)
    fiber_100g = Column(Float, nullable=True)
    soluble_fiber_100g = Column(Float, nullable=True)
    insoluble_fiber_100g = Column(Float, nullable=True)
    proteins_100g = Column(Float, nullable=True)
    casein_100g = Column(Float, nullable=True)
    serum_proteins_100g = Column(Float, nullable=True)
    nucleotides_100g = Column(Float, nullable=True)
    salt_100g = Column(Float, nullable=True)
    sodium_100g = Column(Float, nullable=True)
    alcohol_100g = Column(Float, nullable=True)
    vitamin_a_100g = Column(Float, nullable=True)
    beta_carotene_100g = Column(Float, nullable=True)
    vitamin_d_100g = Column(Float, nullable=True)
    vitamin_e_100g = Column(Float, nullable=True)
    vitamin_k_100g = Column(Float, nullable=True)
    vitamin_c_100g = Column(Float, nullable=True)
    vitamin_b1_100g = Column(Float, nullable=True)
    vitamin_b2_100g = Column(Float, nullable=True)
    vitamin_pp_100g = Column(Float, nullable=True)
    vitamin_b6_100g = Column(Float, nullable=True)
    vitamin_b9_100g = Column(Float, nullable=True)
    folates_100g = Column(Float, nullable=True)
    vitamin_b12_100g = Column(Float, nullable=True)
    biotin_100g = Column(Float, nullable=True)
    pantothenic_acid_100g = Column(Float, nullable=True)
    silica_100g = Column(Float, nullable=True)
    bicarbonate_100g = Column(Float, nullable=True)
    potassium_100g = Column(Float, nullable=True)
    chloride_100g = Column(Float, nullable=True)
    calcium_100g = Column(Float, nullable=True)
    phosphorus_100g = Column(Float, nullable=True)
    iron_100g = Column(Float, nullable=True)
    magnesium_100g = Column(Float, nullable=True)
    zinc_100g = Column(Float, nullable=True)
    copper_100g = Column(Float, nullable=True)
    manganese_100g = Column(Float, nullable=True)
    fluoride_100g = Column(Float, nullable=True)
    selenium_100g = Column(Float, nullable=True)
    chromium_100g = Column(Float, nullable=True)
    molybdenum_100g = Column(Float, nullable=True)
    iodine_100g = Column(Float, nullable=True)
    caffeine_100g = Column(Float, nullable=True)
    taurine_100g = Column(Float, nullable=True)
    ph_100g = Column(Float, nullable=True)
    fruits_vegetables_nuts_100g = Column(Float, nullable=True)
    fruits_vegetables_nuts_dried_100g = Column(Float, nullable=True)
    fruits_vegetables_nuts_estimate_100g = Column(Float, nullable=True)
    fruits_vegetables_nuts_estimate_from_ingredients_100g = Column(Float, nullable=True)
    collagen_meat_protein_ratio_100g = Column(Float, nullable=True)
    cocoa_100g = Column(Float, nullable=True)
    chlorophyl_100g = Column(Float, nullable=True)
    carbon_footprint_100g = Column(Float, nullable=True)
    carbon_footprint_from_meat_or_fish_100g = Column(Float, nullable=True)
    nutrition_score_fr_100g = Column(Float, nullable=True)
    nutrition_score_uk_100g = Column(Float, nullable=True)
    glycemic_index_100g = Column(Float, nullable=True)
    water_hardness_100g = Column(Float, nullable=True)
    choline_100g = Column(Float, nullable=True)
    phylloquinone_100g = Column(Float, nullable=True)
    beta_glucan_100g = Column(Float, nullable=True)
    inositol_100g = Column(Float, nullable=True)
    carnitine_100g = Column(Float, nullable=True)
    def __init__(
        self, code, url, creator, created_at, updated_at, product_name, 
        abbreviated_product_name=None, generic_name=None, quantity=None, 
        packaging=None, packaging_text=None, packaging_tags=None, 
        brands=None, brands_tags=None, categories = None, categories_tags=None,
        categories_en=None, origins=None, origins_tags=None, origins_en=None,
        manufacturing_places=None, manufacturing_places_tags=None,labels=None,
        labels_tags=None,labels_en=None,emb_codes=None,emb_codes_tags=None,
        first_packaging_code_geo=None,cities=None,cities_tags=None,purchase_places=None,
        stores=None,countries=None,countries_tags=None,countries_en=None,
        ingredients_text=None,allergens=None,allergens_en=None,traces=None,traces_tags=None,
        traces_en=None,serving_size=None,serving_quantity=None,no_nutriments=None,
        additives_n=None,additives=None,additives_tags=None,additives_en=None,
        ingredients_from_palm_oil_n=None,ingredients_from_palm_oil=None,
        ingredients_from_palm_oil_tags=None,ingredients_that_may_be_from_palm_oil_n=None,
        ingredients_that_may_be_from_palm_oil=None,ingredients_that_may_be_from_palm_oil_tags=None,
        nutriscore_score=None,nutriscore_grade=None,nova_group=None,pnns_groups_1=None,
        pnns_groups_2=None,states=None,states_tags=None,states_en=None,brand_owner=None,
        ecoscore_score_fr=None,ecoscore_grade_fr=None,main_category=None,main_category_en=None,
        image_url=None,image_small_url=None,image_ingredients_url=None,image_ingredients_small_url=None,
        image_nutrition_url=None,image_nutrition_small_url=None,
        energy_kj_100g=None,energy_kcal_100g=None,energy_100g=None,
        energy_from_fat_100g=None,fat_100g=None,saturated_fat_100g=None,butyric_acid_100g=None,
        caproic_acid_100g=None,caprylic_acid_100g=None,capric_acid_100g=None,lauric_acid_100g=None,
        myristic_acid_100g=None,palmitic_acid_100g=None,stearic_acid_100g=None,arachidic_acid_100g=None,
        behenic_acid_100g=None,lignoceric_acid_100g=None,cerotic_acid_100g=None,montanic_acid_100g=None,
        melissic_acid_100g=None,monounsaturated_fat_100g=None,polyunsaturated_fat_100g=None,omega_3_fat_100g=None,
        alpha_linolenic_acid_100g=None,eicosapentaenoic_acid_100g=None,docosahexaenoic_acid_100g=None,
        omega_6_fat_100g=None,linoleic_acid_100g=None,arachidonic_acid_100g=None,gamma_linolenic_acid_100g=None,
        dihomo_gamma_linolenic_acid_100g=None,omega_9_fat_100g=None,oleic_acid_100g=None,elaidic_acid_100g=None,
        gondoic_acid_100g=None,mead_acid_100g=None,erucic_acid_100g=None,nervonic_acid_100g=None,trans_fat_100g=None,
        cholesterol_100g=None,carbohydrates_100g=None,sugars_100g=None,sucrose_100g=None,glucose_100g=None,
        fructose_100g=None,lactose_100g=None,maltose_100g=None,maltodextrins_100g=None,starch_100g=None,polyols_100g=None,
        fiber_100g=None,soluble_fiber_100g=None,insoluble_fiber_100g=None,proteins_100g=None,casein_100g=None,serum_proteins_100g=None,
        nucleotides_100g=None,salt_100g=None,sodium_100g=None,alcohol_100g=None,vitamin_a_100g=None,beta_carotene_100g=None,
        vitamin_d_100g=None,vitamin_e_100g=None,vitamin_k_100g=None,vitamin_c_100g=None,vitamin_b1_100g=None,vitamin_b2_100g=None,
        vitamin_pp_100g=None,vitamin_b6_100g=None,vitamin_b9_100g=None,folates_100g=None,vitamin_b12_100g=None,biotin_100g=None,
        pantothenic_acid_100g=None,silica_100g=None,bicarbonate_100g=None,potassium_100g=None,chloride_100g=None,calcium_100g=None,
        phosphorus_100g=None,iron_100g=None,magnesium_100g=None,zinc_100g=None,copper_100g=None,manganese_100g=None,fluoride_100g=None,
        selenium_100g=None,chromium_100g=None,molybdenum_100g=None,iodine_100g=None,caffeine_100g=None,taurine_100g=None,ph_100g=None,
        fruits_vegetables_nuts_100g=None,fruits_vegetables_nuts_dried_100g=None,fruits_vegetables_nuts_estimate_100g=None,
        fruits_vegetables_nuts_estimate_from_ingredients_100g=None,collagen_meat_protein_ratio_100g=None,cocoa_100g=None,
        chlorophyl_100g=None,carbon_footprint_100g=None,carbon_footprint_from_meat_or_fish_100g=None,nutrition_score_fr_100g=None,
        nutrition_score_uk_100g=None,glycemic_index_100g=None,water_hardness_100g=None,choline_100g=None,phylloquinone_100g=None,
        beta_glucan_100g=None,inositol_100g=None,carnitine_100g=None
    ):
        self.code = code
        self.url = url
        self.creator = creator
        self.created_at = created_at
        self.updated_at = updated_at
        self.product_name = product_name
        self.abbreviated_product_name = abbreviated_product_name
        self.generic_name = generic_name
        self.quantity = quantity
        self.packaging = packaging
        self.packaging_text = packaging_text
        self.packaging_tags = packaging_tags
        # self.brands = brands
        # self.brands_tags = brands_tags
        # self.categories = categories
        # self.categories_tags = categories_tags
        # self.categories_en = categories_en
        # self.origins = origins
        # self.origins_tags = origins_tags
        # self.origins_en = origins_en
        self.manufacturing_places = manufacturing_places
        self.manufacturing_places_tags = manufacturing_places_tags
        # self.labels = labels
        # self.labels_tags = labels_tags
        # self.labels_en = labels_en
        # self.emb_codes = emb_codes
        # self.emb_codes_tags = emb_codes_tags
        self.first_packaging_code_geo = first_packaging_code_geo
        self.cities = cities
        self.cities_tags = cities_tags
        self.purchase_places = purchase_places
        # self.stores = stores
        # self.countries = countries
        # self.countries_tags = countries_tags
        # self.countries_en = countries_en
        self.ingredients_text = ingredients_text
        # self.allergens = allergens
        # self.allergens_en = allergens_en
        # self.traces = traces
        # self.traces_tags = traces_tags
        # self.traces_en = traces_en
        self.serving_size = serving_size
        self.serving_quantity = serving_quantity
        self.no_nutriments = no_nutriments
        # self.additives_n = additives_n
        # self.additives = additives
        # self.additives_tags = additives_tags
        # self.additives_en = additives_en
        self.ingredients_from_palm_oil_n = ingredients_from_palm_oil_n
        self.ingredients_from_palm_oil = ingredients_from_palm_oil
        self.ingredients_from_palm_oil_tags = ingredients_from_palm_oil_tags
        self.ingredients_that_may_be_from_palm_oil_n = ingredients_that_may_be_from_palm_oil_n
        self.ingredients_that_may_be_from_palm_oil = ingredients_that_may_be_from_palm_oil
        self.ingredients_that_may_be_from_palm_oil_tags = ingredients_that_may_be_from_palm_oil_tags
        self.nutriscore_score = nutriscore_score
        self.nutriscore_grade = nutriscore_grade
        self.nova_group = nova_group
        self.pnns_groups_1 = pnns_groups_1
        self.pnns_groups_2 = pnns_groups_2
        self.states = states
        self.states_tags = states_tags
        self.states_en = states_en
        self.brand_owner = brand_owner
        self.ecoscore_score_fr = ecoscore_score_fr
        self.ecoscore_grade_fr = ecoscore_grade_fr
        self.main_category = main_category
        self.main_category_en = main_category_en
        self.image_url = image_url
        self.image_small_url = image_small_url
        self.image_ingredients_url = image_ingredients_url
        self.image_ingredients_small_url = image_ingredients_small_url
        self.image_nutrition_url = image_nutrition_url
        self.image_nutrition_small_url = image_nutrition_small_url
        self.energy_kj_100g = energy_kj_100g
        self.energy_kcal_100g = energy_kcal_100g
        self.energy_100g = energy_100g
        self.energy_from_fat_100g = energy_from_fat_100g
        self.fat_100g = fat_100g
        self.saturated_fat_100g = saturated_fat_100g
        self.butyric_acid_100g = butyric_acid_100g
        self.caproic_acid_100g = caproic_acid_100g
        self.caprylic_acid_100g = caprylic_acid_100g
        self.capric_acid_100g = capric_acid_100g
        self.lauric_acid_100g = lauric_acid_100g
        self.myristic_acid_100g = myristic_acid_100g
        self.palmitic_acid_100g = palmitic_acid_100g
        self.stearic_acid_100g = stearic_acid_100g
        self.arachidic_acid_100g = arachidic_acid_100g
        self.behenic_acid_100g = behenic_acid_100g
        self.lignoceric_acid_100g = lignoceric_acid_100g
        self.cerotic_acid_100g = cerotic_acid_100g
        self.montanic_acid_100g = montanic_acid_100g
        self.melissic_acid_100g = melissic_acid_100g
        self.monounsaturated_fat_100g = monounsaturated_fat_100g
        self.polyunsaturated_fat_100g = polyunsaturated_fat_100g
        self.omega_3_fat_100g = omega_3_fat_100g
        self.alpha_linolenic_acid_100g = alpha_linolenic_acid_100g
        self.eicosapentaenoic_acid_100g = eicosapentaenoic_acid_100g
        self.docosahexaenoic_acid_100g = docosahexaenoic_acid_100g
        self.omega_6_fat_100g = omega_6_fat_100g
        self.linoleic_acid_100g = linoleic_acid_100g
        self.arachidonic_acid_100g = arachidonic_acid_100g
        self.gamma_linolenic_acid_100g = gamma_linolenic_acid_100g
        self.dihomo_gamma_linolenic_acid_100g = dihomo_gamma_linolenic_acid_100g
        self.omega_9_fat_100g = omega_9_fat_100g
        self.oleic_acid_100g = oleic_acid_100g
        self.elaidic_acid_100g = elaidic_acid_100g
        self.gondoic_acid_100g = gondoic_acid_100g
        self.mead_acid_100g = mead_acid_100g
        self.erucic_acid_100g = erucic_acid_100g
        self.nervonic_acid_100g = nervonic_acid_100g
        self.trans_fat_100g = trans_fat_100g
        self.cholesterol_100g = cholesterol_100g
        self.carbohydrates_100g = carbohydrates_100g
        self.sugars_100g = sugars_100g
        self.sucrose_100g = sucrose_100g
        self.glucose_100g = glucose_100g
        self.fructose_100g = fructose_100g
        self.lactose_100g = lactose_100g
        self.maltose_100g = maltose_100g
        self.maltodextrins_100g = maltodextrins_100g
        self.starch_100g = starch_100g
        self.polyols_100g = polyols_100g
        self.fiber_100g = fiber_100g
        self.soluble_fiber_100g = soluble_fiber_100g
        self.insoluble_fiber_100g = insoluble_fiber_100g
        self.proteins_100g = proteins_100g
        self.casein_100g = casein_100g
        self.serum_proteins_100g = serum_proteins_100g
        self.nucleotides_100g = nucleotides_100g
        self.salt_100g = salt_100g
        self.sodium_100g = sodium_100g
        self.alcohol_100g = alcohol_100g
        self.vitamin_a_100g = vitamin_a_100g
        self.beta_carotene_100g = beta_carotene_100g
        self.vitamin_d_100g = vitamin_d_100g
        self.vitamin_e_100g = vitamin_e_100g
        self.vitamin_k_100g = vitamin_k_100g
        self.vitamin_c_100g = vitamin_c_100g
        self.vitamin_b1_100g = vitamin_b1_100g
        self.vitamin_b2_100g = vitamin_b2_100g
        self.vitamin_pp_100g = vitamin_pp_100g
        self.vitamin_b6_100g = vitamin_b6_100g
        self.vitamin_b9_100g = vitamin_b9_100g
        self.folates_100g = folates_100g
        self.vitamin_b12_100g = vitamin_b12_100g
        self.biotin_100g = biotin_100g
        self.pantothenic_acid_100g = pantothenic_acid_100g
        self.silica_100g = silica_100g
        self.bicarbonate_100g = bicarbonate_100g
        self.potassium_100g = potassium_100g
        self.chloride_100g = chloride_100g
        self.calcium_100g = calcium_100g
        self.phosphorus_100g = phosphorus_100g
        self.iron_100g = iron_100g
        self.magnesium_100g = magnesium_100g
        self.zinc_100g = zinc_100g
        self.copper_100g = copper_100g
        self.manganese_100g = manganese_100g
        self.fluoride_100g = fluoride_100g
        self.selenium_100g = selenium_100g
        self.chromium_100g = chromium_100g
        self.molybdenum_100g = molybdenum_100g
        self.iodine_100g = iodine_100g
        self.caffeine_100g = caffeine_100g
        self.taurine_100g = taurine_100g
        self.ph_100g = ph_100g
        self.fruits_vegetables_nuts_100g = fruits_vegetables_nuts_100g
        self.fruits_vegetables_nuts_dried_100g = fruits_vegetables_nuts_dried_100g
        self.fruits_vegetables_nuts_estimate_100g = fruits_vegetables_nuts_estimate_100g
        self.fruits_vegetables_nuts_estimate_from_ingredients_100g = fruits_vegetables_nuts_estimate_from_ingredients_100g
        self.collagen_meat_protein_ratio_100g = collagen_meat_protein_ratio_100g
        self.cocoa_100g = cocoa_100g
        self.chlorophyl_100g = chlorophyl_100g
        self.carbon_footprint_100g = carbon_footprint_100g
        self.carbon_footprint_from_meat_or_fish_100g = carbon_footprint_from_meat_or_fish_100g
        self.nutrition_score_fr_100g = nutrition_score_fr_100g
        self.nutrition_score_uk_100g = nutrition_score_uk_100g
        self.glycemic_index_100g = glycemic_index_100g
        self.water_hardness_100g = water_hardness_100g
        self.choline_100g = choline_100g
        self.phylloquinone_100g = phylloquinone_100g
        self.beta_glucan_100g = beta_glucan_100g
        self.inositol_100g = inositol_100g
        self.carnitine_100g = carnitine_100g