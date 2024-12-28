# Titanic Dataset Cleaner
#### Video Demo:  https://youtu.be/oFODPNmMjIc
#### Description: rest of the file

## 0. Information about the used Dataset
The dataset which will be used in this project is the "Titanic-Dataset". It is availible under this URL:
https://www.kaggle.com/datasets/brendan45774/test-file

The dataset uses the Creative Commons CC0 1.0 Universal license. This means that the dataset can be used for any purpose without any conditions. Therefore the dataset can be used for the pusposes of this project.
The exact defintiion of the CC0 1.0 Universal License can be found here:
https://creativecommons.org/publicdomain/zero/1.0/

The Titanic dataset, available on Kaggle, consists of data related to passengers aboard the RMS Titanic. It includes details like names, age, gender, ticket details, fare, cabin, and whether the passenger survived or not.


Column Name	    Pandas Data Type	Column Explained 			            Column value explained
PassengerId     int64			    Unique ID of the passenger 		        unique number
Survived        int64			    Information if the passenger survived 	0 = No; 1 = Yes
Pclass          int64			    Passenger class 			            1 = 1st; 2 = 2nd; 3 = 3rd
Name            object			    Name of the passenger 			        name
Sex             object			    Sex of the passenger 			        male/female
Age            	float64			    Age of the passenger 			        number of years
SibSp           int64			    Number of Siblings/Spouses aboard 	    number of
Parch           int64			    Number of Parents/Children aboard 	    number of
Ticket          object			    Ticket number 				            title of ticket
Fare           	float64			    Passenger fare 				            price of fare
Cabin           object			    Cabin embarked 				            number of cabin
Embarked        object			    Port of Embarkation 			        C = Cherbourg; Q = Queenstown; S = Southampton


## 1. Introduction: Importance of Data Quality and Reason for Final CS50 Project

Data quality plays a very important role when working with data. Good data quality is the basis for almost all data work, which leads to analytical and decision-making processes. Good data quality produces accurate and relevant results when it is being analyzed. 
Poor data quality instead can lead to several issues, such as Inaccurate Analysis which can lead to loss of trust in the data and analytical process as well as to operational inefficiencies which can increasing the time and resources required to achieve desired outcomes. 

Hence, it's vital to ensure that the data we work with is of high quality, accurate, and devoid of inconsistencies.
Therefore my Final Project at CS50 for the Introduction to Python Programming will be a Python script, which applies data transformations 
to the chosen titanic dataset in order to improve its data quality. 


## 2. A Data Cleaning Process

Data Cleaning is a science by itself and lots of articles and books are already written on it. 
I have chosen to apply the Process which is described on iteratorsHQ and which can be found here:
https://www.iteratorshq.com/blog/data-cleaning-in-5-easy-steps/

According to the article from Iterators, a standard data cleaning process comprises the following steps:

### Importing Data: Loading data from external sources into our environment.

### Merging Datasets: Integrating multiple datasets to form a consolidated dataset, if necessary.

### Rebuilding/Handling Missing Data: Handling missing or null values in the dataset.

### Standardization: Ensuring data follows a consistent format or structure.

### Normalization: Adjusting the values of numeric columns to a standard scale.

### Deduplication: Removing duplicate entries from the dataset.

### Verification & Enrichment: Validating the data's accuracy and adding supplementary data, if necessary.

### Exporting Data: Saving the cleaned dataset for further use or analysis.


## 3. Data Cleaning Process Applied to the Titanic Dataset

This section of the readme explains how each step of the data cleaning process from section two is applied to the Titanic Dataset. It also explains the code of the Python script.

### Importing Data: We use Pandas to read the original CSV file from kaggle. The data is being loaded into a Pandas DataFrame.
titanic_data = pd.read_csv(r"Titanic.csv", low_memory=False)

### Merging Datasets: As in this case only a single dataset is being processed, there is no need or opportunity to merge datasets. In fact the provided dataset is already a merged dataset, as descibed here: "I took the titanic test file and the gender_submission and put them together in excel to make a csv. This is great for making charts to help you visualize. This also will help you know who died or survived."
https://www.kaggle.com/datasets/brendan45774/test-file/data

### Rebuilding/Handling Missing Data: We identify and analyze columns with missing values and print the result to console.

#### Analyzing data quality
missing_values_count = titanic_data.isnull().sum()
percent_missing = (missing_values_count.sum() / np.prod(titanic_data.shape)) * 100
#### Counting and printing the amount of missing values
print("Count of missing values", "\n", missing_values_count)
Printing the percentage of missing values
print("Percent of missing data:", percent_missing)	

The result of missing values is:
Count of missing values 
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age             86
SibSp            0
Parch            0
Ticket           0
Fare             1
Cabin          327
Embarked         0
dtype: int64
Percent of missing data: 8.253588516746412

8.25% of values are missing. 
Most of the "Cabin"-column values are missing.
Some of the "Age"-column values are missing.
One "Fare"-column values is missing.
A look into the "Age"-column values also shows some values which are decimal numbers (e.g. "34.5") not full numbers. 

We handle the missing values of the "Cabin"-column by dropping this column alltogether. This of course asumes, the data isn't required for further analysis.
	    	
#### Drop "Cabin-column" because it contains too much missing data
titanic_data_dropped = titanic_data.drop(['Cabin', 'Parch'], axis=1)

We handle the missing values of the "Age"-column by replacing missing values with "-" as part of the function round_down_age().
#### Round down .50 age values and handle "NaN" values in "Age"-column
titanic_data_dropped['Age_Trans'] = titanic_data_dropped['Age'].apply(round_down_age)

    def round_down_age(age):
        if math.isnan(age):
            return "-"
        return math.floor(age)

### Standardization: We apply transformations to ensure standardized data. We remove unnecessary columns. Therefore we drop the "Parch"-column because we also asume, it is not required for further analysis. If this was a real life project we of course would check with the responsible Data-Scientists/Data-Analysts if the required Data is needed.

#### Drop "Parch-column" because it is not needed in the final dataframe
titanic_data_dropped = titanic_data.drop(['Cabin', 'Parch'], axis=1)
	
We are extracting titles, first names, and surnames from the "Name"-column. Thereby creating three new columns "Title_Trans", "First_Name_Trans" and "Surename_Trans".

#### Extracting titles from the name column and adding them to a new column
titanic_data_dropped["Title_Trans"] = titanic_data_dropped["Name_Trans"].str.extract(r"(\w+\.)")

#### Extracting first names from tne name column and adding them to a new column
titanic_data_dropped["First_Name_Trans"] = titanic_data_dropped["Name_Trans"].str.extract(r"\.\s*(\w+)") 

#### Splitting names column to extract the surnames and adding them to a new column
titanic_data_dropped["Surename_Trans"] = titanic_data_dropped["Name_Trans"].apply(extract_surenames)
    def extract_surenames(name):
        return name.split(',')[0].strip() if ',' in name else ""

We are rounding fare prices to two decimal places.
#### round number of "Fare-column" to two decimals
titanic_data_dropped['Fare_Trans'] = titanic_data_dropped['Fare'].apply(round_fare)

### Normalization: Normalization typically scales numerical data to a standard range. In our dataset we therefore round fare prices to two digits and round down age values to the next full digit.
    
#### Round down .50 age values and handle "NaN" values in "Age-column"
titanic_data_dropped['Age_Trans'] = titanic_data_dropped['Age'].apply(round_down_age)
    def round_down_age(age):
        if math.isnan(age):
            return "-"
        return math.floor(age)

#### round number of "Fare-column" to two decimals
titanic_data_dropped['Fare_Trans'] = titanic_data_dropped['Fare'].apply(round_fare)

    def round_fare(fare):
        return round(fare, 2)


### Deduplication: We want to remove double entries of data. Therefore we check on the original name column, if there are any duplicates and remove them.

#### Removing duplicates considering the column "Name"
titanic_data_without_duplicates = titanic_data.drop_duplicates(subset=['Name'])

Verification & Enrichment: We enrich the data by removing the nicknames in the name column. Also extracting surnames, titles, and first names to ensure they're correctly structured and saving the data in new columns which happened as part of the Standartization is also part of enriching the data. 

#### Removing nicknames from the name column
titanic_data_dropped['Name_Trans'] = titanic_data_dropped['Name'].apply(remove_nicknames)
    
    def remove_nicknames(name):
        name = re.sub(r'\([^)]*\)', '', name)
        name = re.sub(r'\s[^\s]+(?="")', '', name)
        name = re.sub(r'\s"', ' ', name)
        name = name.replace('"', '')
        return name.rstrip()

### Exporting Data: Finally the transformed and cleaned dataset is exported to a new CSV file.

# Writing the final dataframe to a file
titanic_data_final.to_csv("titanic_transformed.csv", sep=',', index=False, encoding='utf-8')

+++ END OF DOCUMENTATION +++