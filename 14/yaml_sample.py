import yaml

with open("restaurant.yaml") as yaml_file:
    restaurant = yaml.safe_load(yaml_file)

print(restaurant)
