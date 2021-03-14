import pandas as pd

###########################
# google mobility reports #
###########################

gmr_full = pd.read_csv("/home/alex/PycharmProjects/GoogleMobilityCovid/data/2020_BR_Region_Mobility_Report.csv")
gmr_rs = gmr_full[gmr_full['sub_region_1'] == 'State of Rio Grande do Sul']

###########################
# brasil.io COVID dataset #
###########################

brio_full = pd.read_csv("/home/alex/PycharmProjects/GoogleMobilityCovid/data/caso_full.csv")
brio_rs = brio_full[brio_full['state'] == 'RS']
brio_rs.info()