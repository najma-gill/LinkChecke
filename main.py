import os
from pathlib import Path
from tracking_url import TrackingUrl
import json
url_list = ["https://lp.alpecin.com/de-de/grey-attack/index.html?utm_source\u003dOBB\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dCH_OBB%7CPR_Alp-GreyAtt%7CKZ_Conv%7CLA_DE%7CID_751%7CST_Test%7CTM_Hamburg5%7CTR_Prosp%7CGS_ConvMax%7CDE_Mob%7C\u0026utm_content\u003d00c7eb45b74b4e3a5dbfe423e7eac5b5b9utm_term\u003dZur%C3%BCck+zu+dunkleren+Haaren+ohne+F%C3%A4rben%3F+Es+ist+so+leicht%21\u0026dicbo\u003dv4-kssHhze-1080633691-1",
  "https://www.vagisan.net/de-de/milchsaeure/scheideninfektionen/?utm_source\u003dfacebook\u0026utm_medium\u003dprospecting\u0026utm_campaign\u003dCH_FB%7CPR_Vag-Milchs%7CFL_01%7CKZ_Conv%7CLA_DE%7CID_357%7C\u0026utm_content\u003dTR_Prosp%7CTG_Fem%7CTA_18-65Plus%7CGS_ConvMax%7CV_01%7C\u0026utm_term\u003dCR_phWert%7CCUA_Stat%7CC_FloraPinkPackStat%7C\u0026fbclid\u003dIwZXh0bgNhZW0BMABhZGlkAasXp8SYt54BHeW9lIpYe7tCs_flI26wFgXIuY07kCtMqpvqPDGR_lA-mbOqykxo4pwazQ_aem_WjJayITltGkWIA2kvaU6Ag\u0026utm_id\u003d23856128477950205",
"https://lp.alpecin.com/de-de/grey-attack/index.html?utm_source\u003dOBB\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dCH_OBB%7CPR_Alp-GreyAtt%7CKZ_Conv%7CLA_DE%7CID_751%7CST_Test%7CTM_Hamburg5%7CTR_Prosp%7CGS_ConvMax%7CDE_Mob%7C\u0026utm_content\u003d002bf80f5675b644fd7364fab0851e0d3cutm_term\u003dSchluss+mit+F%C3%A4rben%21+Dieses+M%C3%A4nnershampoo+ist+eine+echte+Alternative+gegen+Grau.\u0026dicbo\u003dv4-ixYceGa-1080633691-0",
"https://lp.alpecin.com/de-de/grey-attack/index.html?utm_source\u003dOBB\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dCH_OBB%7CPR_Alp-GreyAtt%7CKZ_Conv%7CLA_DE%7CID_751%7CST_Test%7CTM_Hamburg5%7CTR_Prosp%7CGS_ConvMax%7CDE_Mob%7C\u0026utm_content\u003d00c7eb45b74b4e3a5dbfe423e7eac5b5b9utm_term\u003dZur%C3%BCck+zu+dunkleren+Haaren+ohne+F%C3%A4rben%3F+Es+ist+so+leicht%21\u0026dicbo\u003dv4-kssHhze-1080633691-1",
"https://lp.vagisan.com/de-de/feuchtcreme/feucht/index.html?utm_source\u003doutbrain\u0026utm_medium\u003dadvertorial\u0026utm_campaign\u003dCH_OBB%7CPR_Vag-Feuchtcreme%7CFL_01%7CTR_Prosp%7CDE_Mob%7CCR_Scheidentrockenheit%7CKZ_Conv%7CLA_DE%7CID_358%7CCUA_Nati%7CGS_niedKost%7C\u0026utm_term\u003dPflege+f%C3%BCr+die+Scheide%3F+Mit+dieser+Creme+einfach+feucht+bleiben.\u0026utm_content\u003d0023a715c7c2b46c21c37c8fcef36a86d1\u0026dicbo\u003dv4-n4UHL8s-1131364175-1",
"https://lp.plantur39.com/en-gb/shampoo/index.html?utm_source\u003doutbrain\u0026utm_medium\u003dadvertorial\u0026utm_campaign\u003dCH_OBB%7CPR_P39-Green%7CFL_01%7CDE_Mob%7CKZ_Conv%7CLA_GB%7CID_686%7CTR_Prosp%7CGS_ConvMax%7CCR_Tonic%7CCUA_Nati%7C\u0026utm_term\u003dMiss+having+thick+and+full+hair%3F+Try+this+Leave-In+Caffeine+Tonic\u0026utm_content\u003d00dd456431b19f9ad25e830bed5e4e5a3e\u0026dicbo\u003dv4-LwrFSCw-1081011249-1",
"https://www.plantur39.com/es-es/champus-tonicos-co/anti-grey-effect-shampoo?%3Futm_source\u003dFacebook\u0026utm_medium\u003dprospecting\u0026utm_campaign\u003dCH_FB%7CPR_P39-AntiGrau%7CFL_01%7CKZ_Conv%7CLA_ES%7CID_689%7C\u0026utm_term\u003dTR_Prosp%7CTG_Fem%7CTA_35-64%7CGS_ConvMax%7C\u0026utm_content\u003dCR_GreyRoots%7CCUA_UGC%7CC_EmiUGC%7C\u0026fbclid\u003dPAZXh0bgNhZW0BMABhZGlkAasYOUT9QYUBpu896K4gxEDpAdwAiSXvnOpYFTfCxiPjUuoKel2kExxSUCYwgt5qgmvfZg_aem_mGiybdCQ6TR7D3PnPk-CEQ\u0026utm_source\u003dfacebook\u0026campaign_id\u003d120213776580540677\u0026ad_id\u003d120213848808780677",
"https://www.vagisan.net/de-de/milchsaeure/scheideninfektionen/?utm_source\u003dfacebook\u0026utm_medium\u003dprospecting\u0026utm_campaign\u003dCH_FB%7CPR_Vag-Milchs%7CFL_01%7CKZ_Conv%7CLA_DE%7CID_357%7C\u0026utm_content\u003dTR_Prosp%7CTG_Fem%7CTA_18-65Plus%7CGS_ConvMax%7CV_01%7C\u0026utm_term\u003dCR_phWert%7CCUA_Stat%7CC_FloraPinkPackStat%7C\u0026fbclid\u003dIwZXh0bgNhZW0BMABhZGlkAasXp8SYt54BHeW9lIpYe7tCs_flI26wFgXIuY07kCtMqpvqPDGR_lA-mbOqykxo4pwazQ_aem_WjJayITltGkWIA2kvaU6Ag\u0026utm_id\u003d23856128477950205",
"https://www.alpecin.com/it-it/prodotti/dettagli/product/grey-attack-caffeine-colour-shampoo?utm_source\u003dFacebook\u0026utm_medium\u003dprospecting\u0026utm_campaign\u003dCH_FB%7CPR_Alp-GreyAtt%7CFL_01%7CKZ_Conv%7CLA_IT%7CID_685%7C\u0026utm_term\u003dTR_Prosp%7CTG_M%7CTA_18-65Plus%7CGS_ConvMax%7C\u0026utm_content\u003dCR_CoveringGreyHair%7CCUA_Stat%7CC_LessMoreStat%7C\u0026fbclid\u003dIwZXh0bgNhZW0BMABhZGlkAasYYiIcRmcBHejZl1rWpuHgABqH8iL8G-mxG5AeBT47ONIxtiXLa40dKwg23zDhyGEbfw_aem_O069rerIJfRor7noP_vxTA\u0026campaign_id\u003d120216414799680119\u0026ad_id\u003d120216415299180119\u0026utm_id\u003d120216414799680119",
"https://www.vagisan.com/sk-sk/lp/prijemnejsi?%3Futm_source\u003dFacebook\u0026utm_medium\u003dlookalike\u0026utm_campaign\u003dCH_FB%7CPR_Vag-Feuchtcreme%7CFL_03%7CKZ_Conv%7CLA_SK%7CID_700%7C\u0026utm_term\u003dTR_Prosp-LL1%7CTG_Fem%7CTA_18-65Plus%7CGS_ConvMax%7C\u0026utm_content\u003dCR_Dryness%7CCUA_Stat%7CC_Dryness1Stat%7C\u0026utm_id\u003d120215384415860476\u0026fbclid\u003dPAZXh0bgNhZW0BMABhZGlkAasXQZhMJewBpm9HtQi_kmTZWOPvwtSyqjn8cz3Vs90x7HYKSelrK3kNR-_Q1p4Jwd7RbQ_aem_rFIdIb5l-Ho9vEFaKFjoYw\u0026utm_source\u003dfacebook\u0026campaign_id\u003d120215384415860476\u0026ad_id\u003d120215384415920476",
]

url_list2 = ["https://www.alpecin.com/es-es/productos/details/product/grey-attack-coffein-color-shampoo?utm_source=elmundo&utm_medium=oadv&utm_medium=reter&utm_campaign=CH_OADV%7CPR_Alp-GreyAtt%7CFL_01%7CKZ_Conv%7CLA_ES%7CID_741%7CNW_ElMundo%7C&utm_content=TG_Male%7CTA_35-64%7C&utm_term=C_AlpecinGreyAttack%7CV_12%7C",
"https://www.alpecin.com/es-es/productos/details/product/grey-attack-coffein-color-shampoo?utm_source=marca&utm_medium=oadv&utm_campaign=CH_OADV%7CPR_Alp-GreyAtt%7CFL_01%7CKZ_Conv%7CLA_ES%7CID_741%7CNW_Marca%7C&utm_content=TG_Male%7CTA_35-64%7C&utm_term=C_AlpecinGreyAttack%7CV_14%7C"
             
             ]
#url_list = ["https://lp.plantur39.com/en-gb/shampoo/index.html?utm_source=outbrain&utm_medium=advertorial&utm_campaign=CH_OBB%7CPR_P39-Green%7CFL_01%7CDE_Mob%7CKZ_Conv%7CLA_GB%7CID_686%7CTR_Prosp%7CGS_ConvMax%7CCR_Tonic%7CCUA_Nati%7C&utm_term=Miss+having+thick+and+full+hair%3F+Try+this+Leave-In+Caffeine+Tonic&utm_content=00dd456431b19f9ad25e830bed5e4e5a3e&dicbo=v4-LwrFSCw-1081011249-1",]
url = ["https://www.alpecin.com/es-es/productos/details/product/grey-attack-coffein-color-shampoo?utm_source=elmundo&utm_medium=oadv&utm_medium=reter&utm_campaign=CH_OADV%7CPR_Alp-GreyAtt%7CFL_01%7CKZ_Conv%7CLA_ES%7CID_741%7CNW_ElMundo%7C&utm_content=TG_Male%7CTA_35-64%7C&utm_term=C_AlpecinGreyAttack%7CV_12%7C"]
#tracking.validate_tracking_url(url)
tracking = TrackingUrl()
for url in url:
    print(f"\nURL: {url}\n")
    if " " in url:
        print("Space found in url")
    tracking.reset()
    tracking.validate_tracking_url(url)


# Specify path components
#base_path = Path('documents/tracking/')
#file_name = 'urlStrings.json'

# Construct the path to the file at the root directory
#root_directory = Path(os.sep)
#file_path = os.path.join(root_directory, file_name)

#file_path = base_path / file_name
#print(os.path.realpath)
#print(file_path)


"""try:
    with open(file_name, 'r') as file:
        #line = file.readline()
        data = json.load(file)
        for urlStr in data:
            url = urlStr['page_url']
            #print(f"URL: {url}")
            res = tracking.validate_tracking_url(url)
            print(f"Result: {res}")
            print(f"Source: {tracking.get_utm_source()}")
            print(f"Medium: {tracking.get_utm_medium()}")
            print(f"Campaign: {tracking.get_utm_campaign()}")
            print(f"Content: {tracking.get_utm_content()}")
            print(f"Content: {tracking.get_utm_term()}")
            
except FileNotFoundError:
    print(f"File: '{file_name}' not found")"""


    
# Print the extracted UTM parameters
"""print(f"Source: {tracking.get_utm_source()}")
print(f"Medium: {tracking.get_utm_medium()}")
print(f"Campaign: {tracking.get_utm_campaign()}")
print(f"Content: {tracking.get_utm_content()}")
print(f"Term: {tracking.get_utm_term()}")"""

