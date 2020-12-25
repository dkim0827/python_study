for i in range(1, 51):
    with open("week"+str(i), "w", encoding="utf8") as report_file:
        report_file.write(f"week {i} report")
        report_file.write("\norganization :")
        report_file.write("\nname :")
        report_file.write("\ndescription :")