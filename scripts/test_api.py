from github_api import get_contributions

USERNAME = "Kavyanjali-Korrapati"

weeks = get_contributions(USERNAME)

print("Weeks:", len(weeks))

print("Days in first week:")

for day in weeks[0]["contributionDays"]:
    print(day)