#2 This data is encoded alerts from the City Hall energy sensor. Find the corrupted srtings and replace it by using string operations without using function and conditional statements.
encoded_alerts = [
    ("03:00", "e#co1_sav@e", (5, "High")),
    ("11:00", "gr33n#sk@1lls", (8, "Medium")),
    ("16:00", "en#ergy_leak!", (9, "Critical")),
    ("20:00", "norm@l_0ps", (4, "Low")),
]

del encoded_alerts[0]
encoded_alerts.append(("03:00", "eco_save", (5, "High")))
del encoded_alerts[0]
encoded_alerts.append(("11:00", "green_skills", (8, "Medium")))
del encoded_alerts[0]
encoded_alerts.append(("16:00", "energy_leak", (9, "Critical")))
del encoded_alerts[0]
encoded_alerts.append(("20:00", "normal_ops", (4, "Low")))
print(encoded_alerts)
