#Task 1
import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

try:
    deep_weekly_sales = copy.deepcopy(weekly_sales)
    deep_weekly_sales["Week 2"].update({"Electronics": 18000})
except:
    print("An error occured, please try again!")
print(weekly_sales)
print(deep_weekly_sales)