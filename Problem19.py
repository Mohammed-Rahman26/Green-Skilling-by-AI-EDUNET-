#19 Add a new column for cost per MW
projects_df["Cost per MW"] = projects_df["Cost (Million $)"] / projects_df["Capacity (MW)"]

print("\nDataFrame with Cost per MW:")
print(projects_df)
