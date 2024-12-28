import pandas as pd
import numpy as np
import math
import re


def round_down_age(age):
    if math.isnan(age):
        return "-"
    return math.floor(age)


def round_fare(fare):
    return round(fare, 2)


def survived_transformation(survived):
    return "survived" if survived else "died"


def remove_nicknames(name):
    name = re.sub(r'\([^)]*\)', '', name)
    name = re.sub(r'\s[^\s]+(?="")', '', name)
    name = re.sub(r'\s"', ' ', name)
    name = name.replace('"', '')
    return name.rstrip()


def extract_surenames(name):
    return name.split(',')[0].strip() if ',' in name else ""


def load_and_transform_data():
    # Reading the raw csv-file into a pandas dataframe
    titanic_data = pd.read_csv(r"Titanic.csv", low_memory=False)

    # Analyzing data quality
    missing_values_count = titanic_data.isnull().sum()
    percent_missing = round(((missing_values_count.sum() / np.prod(titanic_data.shape)) * 100), 2)
    # Counting and printing the amount of missing values
    print("Count of missing values", "\n", missing_values_count)
    # Printing the percentage of missing values
    print("Percent of missing data:", percent_missing)

    # Removing duplicates considering the column "Name"
    titanic_data_without_duplicates = titanic_data.drop_duplicates(subset=['Name'])

    # Beginning with necessary transformation operations
    # Drop "Cabin-column" because it contains too much missing data
    # Drop "Parch-column" because it is not needed in the final dataframe
    titanic_data_dropped = titanic_data_without_duplicates.drop(['Cabin', 'Parch'], axis=1)
    # Round down .50 age values and handle "NaN" values in "Age-column"
    titanic_data_dropped['Age_Trans'] = titanic_data_dropped['Age'].apply(round_down_age)
    # round number of "Fare-column" to two decimals
    titanic_data_dropped['Fare_Trans'] = titanic_data_dropped['Fare'].apply(round_fare)
    # Transform values of column "Survived"
    titanic_data_dropped['Survived_Trans'] = titanic_data_dropped['Survived'].apply(survived_transformation)
    # Removing nicknames from the name column
    titanic_data_dropped['Name_Trans'] = titanic_data_dropped['Name'].apply(remove_nicknames)
    # Splitting names column to extract the surnames and adding them to a new column
    titanic_data_dropped["Surename_Trans"] = titanic_data_dropped["Name_Trans"].apply(extract_surenames)
    # Extracting titles from the name column and adding them to a new column
    titanic_data_dropped["Title_Trans"] = titanic_data_dropped["Name_Trans"].str.extract(r"(\w+\.)")
    # Extracting first names from tne name column and adding them to a new column
    titanic_data_dropped["First_Name_Trans"] = titanic_data_dropped["Name_Trans"].str.extract(r"\.\s*(\w+)")
    # Drop the original columns which have been transformed
    titanic_data_final = titanic_data_dropped.drop(["Name", "Age", "Survived", "Fare"], axis=1)
    # Reorder columns
    reordered_cols = ["PassengerId", "Name_Trans", "Title_Trans", "First_Name_Trans", "Surename_Trans", "Sex", "Age_Trans", "Survived_Trans", "Pclass", "SibSp", "Embarked", "Ticket", "Fare_Trans"]
    titanic_data_final = titanic_data_final[reordered_cols]

    # Writing the final dataframe to a file
    titanic_data_final.to_csv("titanic_transformed.csv", sep=',', index=False, encoding='utf-8')
    return titanic_data_final


def main():
    transformed_data = load_and_transform_data()
    # Printing the final dataframe
    print(transformed_data.to_string())


if __name__ == "__main__":
    main()
