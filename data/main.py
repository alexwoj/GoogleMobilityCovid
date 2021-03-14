import pandas as pd

# Google Mobility Reports
gmr_full = pd.read_csv("/home/alex/PycharmProjects/GoogleMobilityCovid/data/2020_BR_Region_Mobility_Report.csv")
gmr_rs = gmr_full[gmr_full['sub_region_1'] == 'State of Rio Grande do Sul']

