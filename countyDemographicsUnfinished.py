import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print("Highest income counties:")
    print(high_income_counties(counties))
    print("\nAlphabetically first county:")
    print(alphabetically_first_county(counties))
    print("\nCounty with most under 18:")
    print(county_most_under_18(counties))
    print("\nPercent under 18:")
    print(percent_most_under_18(counties))
    print("\nLowest median income county:")
    print(lowest_median_income(counties))
    print("\nState with most counties:")
    print(state_with_most_counties(counties))
    print("\nNational average commute time:")
    print(your_interesting_demographic_function(counties))


def high_income_counties(counties):
    """Return a LIST of the counties with a median household income over $90,000."""
    toReturn = []
    for county in counties:
        if county['Income']['Median Household Income'] > 90000:
            toReturn.append(county['County'])
    return toReturn

    

def lowest_median_income(counties):
    """Return a name of a county with the lowest median household income"""
    tempLowest = counties[0]
    for county in counties:
        if county['Income']['Median Household Income']< tempLowest['Income']['Median Household Income']:
            tempLowest = county
    return tempLowest['County']

    

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    #Hint: you can use < to compare strings in Python. ex) "cat" < "dog" gives the value True
    tempFirst = counties[0]
    for county in counties:
        if county['County'] < tempFirst['County']:
            tempFirst = county
    return tempFirst['County']


    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""    
    tempHighest = counties[0]
    for county in counties:
        if county['Age']['Percent Under 18 Years'] > tempHighest['Age']['Percent Under 18 Years']:
            tempHighest = county
    return tempHighest['Age']['Percent Under 18 Years']      
    
    

def county_most_under_18(counties):
    """Return the name a county with the highest percent of under 18 year olds."""
    tempHighest = counties[0]
    for county in counties:
        if county['Age']['Percent Under 18 Years'] > tempHighest['Age']['Percent Under 18 Years']:
            tempHighest = county
    return tempHighest['County']    
    
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #1. Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    
    #2. Find the state in the dictionary with the most counties
    
    #3. Return the state with the most counties

    allStates={}
    for county in counties:
        if county['State'] not in allStates:
            allStates[county['State']]=0  
        allStates[county['State']]+=1

    highest = 'VT'
    for state in allStates:
        if allStates[state] > allStates[highest]:
            highest = state
    return highest

    
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    """Average Commute Time"""
    total = 0
    for county in counties:
        total += county['Miscellaneous']['Mean Travel Time to Work']
    total=total/len(counties)
    return round(total,2)
    
    
if __name__ == '__main__':
    main()
