from datapackage import Package

def teste():
    package = Package('https://datahub.io/core/s-and-p-500-companies/datapackage.json')

    print(package.resource_names)

    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            for x in resource.read():
                print(x)
            