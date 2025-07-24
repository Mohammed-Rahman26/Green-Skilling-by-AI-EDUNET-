#18 Filter projects with capacity greater than 100 MW
high_capacity_projects = projects_df[projects_df["Capacity (MW)"] > 100]

print("\nProjects with Capacity Greater than 100 MW:")
print(high_capacity_projects)
