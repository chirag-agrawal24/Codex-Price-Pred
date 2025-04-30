import pandas as pd
import json
import joblib

with open("app/artifacts/column_datas.json") as json_file:
    columns_for_model = json.load(json_file)['columns']

model_path= "app/artifacts/LightGBM_best_model.joblib"
model=joblib.load(model_path)

encoder_path="app/artifacts/target_encoder.joblib"
target_encoder=joblib.load(encoder_path)


def feature_engineered(input_dict:dict):
    df = pd.DataFrame(input_dict,index=[0])


    # Age Group

    # why we write 17??? because in cut(right=True) means right value is included but not left 
    # so if we write 18 then it will not be included in 18-25
    age_bins = [17, 25, 35, 45, 55, 70, float('inf')]  # Define bins
    age_labels = ['18-25', '26-35', '36-45', '46-55', '56-70', '70+']  # Define labels
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=True)

    #cf_ab_score
    consume_frequency_mapping = {
    "0-2 times": 1,
    "3-4 times": 2,
    "5-7 times": 3
}

    awareness_mapping = {
    "0 to 1": 1,
    "2 to 4": 2,
    "above 4": 3
}

    df['frequency_score'] = df['consume_frequency(weekly)'].map(consume_frequency_mapping)
    df['awareness_score'] = df['awareness_of_other_brands'].map(awareness_mapping)

    df['cf_ab_score'] = df['frequency_score'] / (df['awareness_score'] + df['frequency_score'])

    df['cf_ab_score'] = df['cf_ab_score'].round(2)

    #zas score

    zone_mapping = {
    "Urban": 3,
    "Metro": 4,
    "Rural": 1,
    "Semi-Urban": 2
    }

    income_mapping = {
        "<10L": 1,
        "10L - 15L": 2,
        "16L - 25L": 3,
        "26L - 35L": 4,
        "> 35L": 5,
        "Not Reported": 0
    }

    df['zone_score'] = df['zone'].map(zone_mapping)
    df['income_score'] = df['income_levels'].map(income_mapping)
    df['zas_score'] = df['zone_score'] * df['income_score']

    condition1 = df['current_brand'] != "Established"  # Check if current_brand is not "Established"
    condition2 = df['reasons_for_choosing_brands'].isin(['Price', 'Quality'])  # Check if reasons are "Price" or "Quality"


    df['bsi'] = (condition1 & condition2).astype(int)  # Assign 1 if both conditions are true, else 0



    output_df=df[columns_for_model]
    return output_df

def calculate(input_dict:dict):
    
    df=feature_engineered(input_dict)
    encoded_result = model.predict(df)
    result=target_encoder.inverse_transform(encoded_result.reshape(-1, 1))[0,0]

    return result
