import pandas as pd

data=pd.read_csv("pandas/titanic.csv")

print(data.head().to_string())
print(data.info()) #showing data info before fixing or filling missed values

data["Age"]=data["Age"].fillna(data["Age"].median()) #Fill missing values in the 'Age' column with the median age

data["Embarked"]=data["Embarked"].fillna(data["Embarked"].mode()[0])#Fill missing values in 'Embarked' with the most common value (mode )

data.drop(columns=["Cabin"],inplace=True)

print(data.info())  # showing data info after data cleaning 


# Create a filter for: Age > 30 AND Survived == 1
survivors_over_30 = data[(data['Age'] > 30) & (data['Survived'] == 1)]

# Print the first few rows of this filtered group
print("Passengers over 30 who survived:")
print(survivors_over_30.head().to_string())

# To count how many people are in this group:
print(f"\nTotal number of survivors over 30: {len(survivors_over_30)}")


print("//////////////////////////////////////////////////")
##############################
# Create a filter for: WOMEN AND Survived == 1
survivors_women = data[(data['Sex'] =="female") & (data['Survived'] == 1)]
print(survivors_women.to_string())


print(f"\nTotal no of women surv: {len(survivors_women)}")
####



# Group by 'Sex' and find the average of 'Survived' (then multiply by 100 for percentage)
survival_by_sex = data.groupby('Sex')['Survived'].mean() * 100

print("Survival Percentage by Gender:")
print(survival_by_sex)


# survival rate by class 
print("Survival Rate by Passenger Class:")
print(data.groupby('Pclass')['Survived'].mean() * 100, "\n")


# survival rate by age
data['AgeGroup'] = pd.cut(data['Age'], 
                          bins=[0, 12, 18, 60, 100], 
                          labels=['Child (0-12)', 'Teenager (13-18)', 'Adult (19-60)', 'Senior (60+)'])

#  Group by 'AgeGroup' and find the average 'Survived' (then multiply by 100)
print("Survival Percentage by Age Group:")
print(data.groupby('AgeGroup')['Survived'].mean() * 100)