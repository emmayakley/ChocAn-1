import json
import datetime

class report:
    def __init__(self):
        pass

    def create_member_weekly_reports(self):
        today = datetime.date.today()
        with open("Member/MemberDirectory.json", mode="r") as memberFile:
            all_members = json.load(memberFile)
        for member in all_members["members"]:
            name = member["MemberName"]
            with open(f"Member/{name}/{name}_profile.json", "r") as aMemberFile:
                aMember = json.load(aMemberFile)
            with open(f"Member/{name}/{name}_{today}", "w") as f:
                json.dump(aMember, f,indent=4)
            aMember['Services'] = []
            with open(f"Member/{name}/{name}_profile.json", "w") as file:
                json.dump(aMember,file,indent=4)
    
    def create_provider_weekly_reports(self):
        today = datetime.date.today()
        with open("Provider/ProviderList.json", mode="r") as providerFile:
            all_providers = json.load(providerFile)
        for provider in all_providers["providers"]:
            name = provider["ProviderName"]
            with open(f"Provider/{name}/{name}_profile.json", "r") as aProviderFile:
                aProvider = json.load(aProviderFile)
            with open(f"Provider/{name}/{name}_{today}", "w") as f:
                json.dump(aProvider, f, indent=4)
            aProvider['Services'] = []
            with open(f"Provider/{name}/{name}_profile.json", "w") as file:
                json.dump(aProvider,file, indent=4)
