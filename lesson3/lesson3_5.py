import json
from pprint import pprint
import argparse  # 新增

class Site:
    def __init__(self,
                 sitename,
                 county,
                 aqi,
                 pollutant,
                 status,
                 pm2_5,
                 pm2_5_avg,
                 latitude,
                 longitude,
                 datacreationdate):      # ← 修正參數名稱
        self.sitename = sitename
        self.county = county
        self.aqi = aqi
        self.pollutant = pollutant
        self.status = status
        self.pm2_5 = pm2_5
        self.pm2_5_avg = pm2_5_avg
        self.latitude = latitude
        self.longitude = longitude
        self.datacreationdate = datacreationdate


def parse_sites_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    site_list = []
    for sitename in data['records']:
        site = Site(
            sitename=sitename['sitename'],
            county=sitename['county'],
            aqi=sitename['aqi'],
            pollutant=sitename['pollutant'],
            status=sitename['status'],
            pm2_5=sitename['pm2.5'],
            pm2_5_avg=sitename['pm2.5_avg'],
            latitude=sitename['latitude'],
            longitude=sitename['longitude'],
            datacreationdate=sitename['datacreationdate']
        )
        site_list.append(site)
    return site_list

def show_sites_by_county(site_list, county_name):
    found = False
    for site in site_list:
        if site.county == county_name:
            pprint(vars(site))
            found = True
    if not found:
        print(f"找不到縣市：{county_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="查詢指定縣市的空氣品質監測資料")
    parser.add_argument("json_file", help="JSON 檔案路徑")
    parser.add_argument("county", help="縣市名稱")
    args = parser.parse_args()

    sites = parse_sites_from_json(args.json_file)
    show_sites_by_county(sites, args.county)