#20 Aggregate the total capacity and cost
total_capacity = projects_df["Capacity (MW)"].sum()
total_cost = projects_df["Cost (Million $)"].sum()

print(f"\nTotal Capacity of all projects: {total_capacity} MW")
print(f"Total Cost of all projects: ${total_cost} million")
