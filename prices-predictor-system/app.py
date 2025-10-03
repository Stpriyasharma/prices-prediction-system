import streamlit as st
import requests
import json

# MLFlow prediction server URL
url = "http://127.0.0.1:8000/invocations"
st.set_page_config(page_title="🏡 House Price Prediction", layout="wide")
st.title("🏡 House Price Predictor")

st.markdown("Fill in the details of the house to predict its price")

# --- Input fields (you can improve with dropdowns/sliders where applicable) ---
with st.expander("🆔 Identification & Classification", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        Order = st.number_input("Order (Transaction Order)", value=2)
        PID = st.number_input("PID", value=5287)
    with col2:
        MS_Subclass = st.number_input("MS Subclass", value=20)
        MS_Zoning = st.selectbox("MS Zoning", ["RL", "RM", "FV", "RH", "C (all)"])
    with col3:
        Neighborhood = st.text_input("Neighborhood", "NAmes")

# ========== 2. Lot & Location ==========
with st.expander("📍 Lot & Location Details"):
    col1, col2, col3 = st.columns(3)
    with col1:
        Lot_Frontage = st.number_input("Lot Frontage", value=80.0)
        Lot_Area = st.number_input("Lot Area", value=9600)
        Street = st.selectbox("Street", ["Pave", "Grvl"])
    with col2:
        Alley = st.selectbox("Alley", [None, "Grvl", "Pave"])
        Lot_Shape = st.selectbox("Lot Shape", ["Reg", "IR1", "IR2", "IR3"])
        Land_Contour = st.selectbox("Land Contour", ["Lvl", "Bnk", "HLS", "Low"])
    with col3:
        Utilities = st.selectbox("Utilities", ["AllPub", "NoSewr", "NoSeWa", "ELO"])
        Lot_Config = st.selectbox("Lot Config", ["Inside", "Corner", "CulDSac", "FR2", "FR3"])
        Land_Slope = st.selectbox("Land Slope", ["Gtl", "Mod", "Sev"])
        Condition1 = st.text_input("Condition 1", "Norm")
        Condition2 = st.text_input("Condition 2", "Norm")

# ========== 3. Building Characteristics ==========
with st.expander("🏠 Building Characteristics"):
    col1, col2, col3 = st.columns(3)
    with col1:
        Bldg_Type = st.text_input("Bldg Type", "1Fam")
        House_Style = st.text_input("House Style", "2Story")
        Overall_Qual = st.slider("Overall Qual", 1, 10, 5)
    with col2:
        Overall_Cond = st.slider("Overall Cond", 1, 10, 7)
        Year_Built = st.number_input("Year Built", value=1961)
        Year_Remod_Add = st.number_input("Year Remod/Add", value=1961)
    with col3:
        Roof_Style = st.text_input("Roof Style", "Gable")
        Roof_Matl = st.text_input("Roof Matl", "CompShg")
        Foundation = st.text_input("Foundation", "CBlock")

# ========== 4. Exterior ==========
with st.expander("🏘️ Exterior Features"):
    col1, col2, col3 = st.columns(3)
    with col1:
        Exterior1st = st.text_input("Exterior 1st", "VinylSd")
        Exterior2nd = st.text_input("Exterior 2nd", "VinylSd")
    with col2:
        Mas_Vnr_Type = st.text_input("Mas Vnr Type", "None")
        Mas_Vnr_Area = st.number_input("Mas Vnr Area", value=0.0)
    with col3:
        Exter_Qual = st.text_input("Exter Qual", "TA")
        Exter_Cond = st.text_input("Exter Cond", "TA")

# ========== 5. Basement ==========
with st.expander("🏚️ Basement Details"):
    col1, col2, col3 = st.columns(3)
    with col1:
        Bsmt_Qual = st.text_input("Bsmt Qual", "TA")
        Bsmt_Cond = st.text_input("Bsmt Cond", "TA")
        Bsmt_Exposure = st.text_input("Bsmt Exposure", "No")
    with col2:
        BsmtFin_Type1 = st.text_input("BsmtFin Type 1", "Rec")
        BsmtFin_SF1 = st.number_input("BsmtFin SF 1", value=700.0)
        BsmtFin_Type2 = st.text_input("BsmtFin Type 2", "Unf")
        BsmtFin_SF2 = st.number_input("BsmtFin SF 2", value=0.0)
    with col3:
        Bsmt_Unf_SF = st.number_input("Bsmt Unf SF", value=150.0)
        Total_Bsmt_SF = st.number_input("Total Bsmt SF", value=850.0)

# ========== 6. Interior ==========
with st.expander("🛋️ Interior Rooms & Area"):
    col1, col2, col3 = st.columns(3)
    with col1:
        FirstFlrSF = st.number_input("1st Flr SF", value=856)
        SecondFlrSF = st.number_input("2nd Flr SF", value=854)
        LowQualFinSF = st.number_input("Low Qual Fin SF", value=0)
    with col2:
        Gr_Liv_Area = st.number_input("Gr Liv Area", value=1710.0)
        Bsmt_Full_Bath = st.number_input("Bsmt Full Bath", value=1)
        Bsmt_Half_Bath = st.number_input("Bsmt Half Bath", value=0)
    with col3:
        Full_Bath = st.number_input("Full Bath", value=1)
        Half_Bath = st.number_input("Half Bath", value=0)
        Bedroom_AbvGr = st.number_input("Bedroom AbvGr", value=3)
        Kitchen_AbvGr = st.number_input("Kitchen AbvGr", value=1)
        Kitchen_Qual = st.text_input("Kitchen Qual", "TA")
        TotRms_AbvGrd = st.number_input("TotRms AbvGrd", value=7)

# ========== 7. Utilities & Systems ==========
with st.expander("⚡ Utilities & Systems"):
    col1, col2, col3 = st.columns(3)
    with col1:
        Heating = st.text_input("Heating", "GasA")
        Heating_QC = st.text_input("Heating QC", "TA")
    with col2:
        Central_Air = st.selectbox("Central Air", ["Y", "N"])
        Electrical = st.text_input("Electrical", "SBrkr")
    with col3:
        Functional = st.text_input("Functional", "Typ")

# ========== 8. Fireplace ==========
with st.expander("🔥 Fireplaces"):
    Fireplaces = st.number_input("Fireplaces", value=2)
    Fireplace_Qu = st.text_input("Fireplace Qu", "TA")

# ========== 9. Garage ==========
with st.expander("🚗 Garage Details"):
    col1, col2, col3 = st.columns(3)
    with col1:
        Garage_Type = st.text_input("Garage Type", "Attchd")
        Garage_Yr_Blt = st.number_input("Garage Yr Blt", value=1961)
    with col2:
        Garage_Finish = st.text_input("Garage Finish", "Unf")
        Garage_Cars = st.number_input("Garage Cars", value=2)
        Garage_Area = st.number_input("Garage Area", value=500.0)
    with col3:
        Garage_Qual = st.text_input("Garage Qual", "TA")
        Garage_Cond = st.text_input("Garage Cond", "TA")
        Paved_Drive = st.selectbox("Paved Drive", ["Y", "N", "P"])

# ========== 10. Outdoor & Extra ==========
with st.expander("🌳 Outdoor & Additional Features"):
    col1, col2, col3 = st.columns(3)
    with col1:
        Wood_Deck_SF = st.number_input("Wood Deck SF", value=210.0)
        Open_Porch_SF = st.number_input("Open Porch SF", value=0)
    with col2:
        Enclosed_Porch = st.number_input("Enclosed Porch", value=0)
        ThreeSsn_Porch = st.number_input("3Ssn Porch", value=0)
        Screen_Porch = st.number_input("Screen Porch", value=0)
    with col3:
        Pool_Area = st.number_input("Pool Area", value=0)
        Pool_QC = st.selectbox("Pool QC", [None, "Ex", "Gd", "TA", "Fa"])
        Fence = st.selectbox("Fence", [None, "GdPrv", "MnPrv", "GdWo", "MnWw"])
        Misc_Val = st.number_input("Misc Val", value=0)
        Misc_Feature = st.selectbox("Misc Feature", [None, "Elev", "Gar2", "Othr", "Shed", "TenC"])

# ========== 11. Sale Info ==========
with st.expander("📑 Sale Information"):
    col1, col2, col3 = st.columns(3)
    with col1:
        Mo_Sold = st.number_input("Mo Sold", value=5)
    with col2:
        Yr_Sold = st.number_input("Yr Sold", value=2010)
    with col3:
        Sale_Type = st.text_input("Sale Type", "WD")
        Sale_Condition = st.text_input("Sale Condition", "Normal")

# --- Prediction button ---
if st.button("Predict Price"):
    input_data = {
        "dataframe_records": [
            {
                "Order": Order,
                "PID": PID,
                "MS SubClass": MS_Subclass,
                "MS Zoning": MS_Zoning,
                "Lot Frontage": Lot_Frontage,
                "Lot Area": Lot_Area,
                "Street": Street,
                "Alley": Alley,
                "Lot Shape": Lot_Shape,
                "Land Contour": Land_Contour,
                "Utilities": Utilities,
                "Lot Config": Lot_Config,
                "Land Slope": Land_Slope,
                "Neighborhood": Neighborhood,
                "Condition 1": Condition1,
                "Condition 2": Condition2,
                "Bldg Type": Bldg_Type,
                "House Style": House_Style,
                "Overall Qual": Overall_Qual,
                "Overall Cond": Overall_Cond,
                "Year Built": Year_Built,
                "Year Remod/Add": Year_Remod_Add,
                "Roof Style": Roof_Style,
                "Roof Matl": Roof_Matl,
                "Exterior 1st": Exterior1st,
                "Exterior 2nd": Exterior2nd,
                "Mas Vnr Type": Mas_Vnr_Type,
                "Mas Vnr Area": Mas_Vnr_Area,
                "Exter Qual": Exter_Qual,
                "Exter Cond": Exter_Cond,
                "Foundation": Foundation,
                "Bsmt Qual": Bsmt_Qual,
                "Bsmt Cond": Bsmt_Cond,
                "Bsmt Exposure": Bsmt_Exposure,
                "BsmtFin Type 1": BsmtFin_Type1,
                "BsmtFin SF 1": BsmtFin_SF1,
                "BsmtFin Type 2": BsmtFin_Type2,
                "BsmtFin SF 2": BsmtFin_SF2,
                "Bsmt Unf SF": Bsmt_Unf_SF,
                "Total Bsmt SF": Total_Bsmt_SF,
                "Heating": Heating,
                "Heating QC": Heating_QC,
                "Central Air": Central_Air,
                "Electrical": Electrical,
                "1st Flr SF": FirstFlrSF,
                "2nd Flr SF": SecondFlrSF,
                "Low Qual Fin SF": LowQualFinSF,
                "Gr Liv Area": Gr_Liv_Area,
                "Bsmt Full Bath": Bsmt_Full_Bath,
                "Bsmt Half Bath": Bsmt_Half_Bath,
                "Full Bath": Full_Bath,
                "Half Bath": Half_Bath,
                "Bedroom AbvGr": Bedroom_AbvGr,
                "Kitchen AbvGr": Kitchen_AbvGr,
                "Kitchen Qual": Kitchen_Qual,
                "TotRms AbvGrd": TotRms_AbvGrd,
                "Functional": Functional,
                "Fireplaces": Fireplaces,
                "Fireplace Qu": Fireplace_Qu,
                "Garage Type": Garage_Type,
                "Garage Yr Blt": Garage_Yr_Blt,
                "Garage Finish": Garage_Finish,
                "Garage Cars": Garage_Cars,
                "Garage Area": Garage_Area,
                "Garage Qual": Garage_Qual,
                "Garage Cond": Garage_Cond,
                "Paved Drive": Paved_Drive,
                "Wood Deck SF": Wood_Deck_SF,
                "Open Porch SF": Open_Porch_SF,
                "Enclosed Porch": Enclosed_Porch,
                "3Ssn Porch": ThreeSsn_Porch,
                "Screen Porch": Screen_Porch,
                "Pool Area": Pool_Area,
                "Pool QC": Pool_QC,
                "Fence": Fence,
                "Misc Val": Misc_Val,
                "Misc Feature": Misc_Feature,
                "Mo Sold": Mo_Sold,
                "Yr Sold": Yr_Sold,
                "Sale Type": Sale_Type,
                "Sale Condition": Sale_Condition
            }
        ]
    }

   
    json_data = json.dumps(input_data)
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=json_data)

    if response.status_code == 200:
        prediction = response.json()
        predicted_price = prediction["predictions"][0]  # extract the number
        st.success(f"🏠 Predicted House Price: ${predicted_price:,.2f}")
    else:
        st.error(f"Error {response.status_code}: {response.text}")
