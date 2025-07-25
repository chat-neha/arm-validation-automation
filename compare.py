import json
import urllib.request

def load_parameters_from_url(url):
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8-sig')
        template = json.loads(data)
    return set(k.upper() for k in template.get('parameters', {}).keys())

def compare_parameters(maps_template_url, quickstart_template_url): 
    maps_params = load_parameters_from_url(maps_template_url)
    quickstart_params = load_parameters_from_url(quickstart_template_url)

    additional_params = quickstart_params - maps_params

    print ("Custom params:", sorted(maps_params))
    print ("QS params:", sorted(quickstart_params))
    print ("Suggested params:", sorted(additional_params))

# Call the function with URLs
compare_parameters(
    "https://raw.githubusercontent.com/neha-c23/arm_validation/refs/heads/main/templates/azuredeploy.json",
    "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/4b98edf26a59f311fe599bef4e48850d55e5fb50/quickstarts/microsoft.web/web-app-asp-app-on-asev3-create/azuredeploy.json"
)
