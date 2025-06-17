def life_in_weeks(age):    
    total_weeks_90_years = 4680
    weeks_by_age = age * 52
    total_weeks = total_weeks_90_years - weeks_by_age
    print(f"You have {total_weeks} weeks left.")


life_in_weeks(27)

