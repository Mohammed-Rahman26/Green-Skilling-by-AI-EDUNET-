#21 Group by 'Technology' and calculate total capacity for each type
grouped_data = projects_df.groupby("Technology")["Capacity (MW)"].sum()

print("\nTotal Capacity by Technology:")
print(grouped_data)
