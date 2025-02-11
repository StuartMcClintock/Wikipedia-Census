# https://www2.census.gov/programs-surveys/decennial/2020/program-management/glance_data_products.pdf
# https://data.census.gov/table/DECENNIALPL2020.P1?q=Coal%20county,%20Oklahoma
# https://api.census.gov/data/2019/acs/acs1/examples.html
# https://api.wikimedia.org/wiki/Core_REST_API/Reference/Pages/Edit_page
# https://www.census.gov/data/academy/courses/intro-to-the-census-bureau-data-api.html
from census import Census
from us import states
from credentials import *

def getText(dataObj):
    return '''As of the [[2010 United States Census]], there were 5,295 people, 2,350 households, and 1,604 families residing in the county.<ref name="Census-2010-DP-1">United States Census Bureau. [http://factfinder.census.gov/bkmk/table/1.0/en/DEC/10_DP/DPDP1/0500000US40029 "DP-1 Profile of General Population and Housing Characteristics: 2010 - 2010 Demographic Profile Data - Coal County, Oklahoma,"] {{Webarchive|url=https://archive.today/20200213023140/http://factfinder.census.gov/bkmk/table/1.0/en/DEC/10_DP/DPDP1/0500000US40029 |date=February 13, 2020 }} ''American Fact Finder'', Accessed July 5, 2015.</ref> There were 2,810 housing units.<ref name="Census-2010-DP-1"/> The racial makeup of the county was 74.3% [[Race (United States Census)|White]], 0.5% [[Race (United States Census)|Black]] or [[Race (United States Census)|African American]], 16.7% [[Race (United States Census)|Native American]], 0.2% [[Race (United States Census)|Asian]], 0.5% from [[Race (United States Census)|other races]], and 7.8% from two or more races.<ref name="Census-2010-DP-1"/> 2.6% of the population were [[Race (United States Census)|Hispanic]] or [[Race (United States Census)|Latino]] of any race.<ref name="Census-2010-DP-1"/>

    There were 2,350 households, out of which 27.7% had children under the age of 18 living with them, 50.8% were [[Marriage|married couples]] living together, 12.1% had a female householder with no husband present, and 31.7% were non-families.<ref name="Census-2010-DP-1"/>  28.1% of all households were made up of individuals, and 14.6% had someone living alone who was 65 years of age or older.<ref name="Census-2010-DP-1"/>   The average household size was 2.50 and the average family size was 3.06.<ref name="Census-2010-DP-1"/>

    In the county, the population was spread out, with 25.5% under the age of 18, 7.2% from 18 to 24, 21.7% from 25 to 44, 27.8% from 45 to 64, and 17.8% who were 65 years of age or older.<ref name="Census-2010-QT-P1">United States Census Bureau. [http://factfinder.census.gov/bkmk/table/1.0/en/DEC/10_SF1/QTP1/0500000US40029 "QT-P1 Age Groups and Sex: 2010 2010 Census Summary File 1 - Coal County, Oklahoma,"] {{Webarchive|url=https://archive.today/20200213032912/http://factfinder.census.gov/bkmk/table/1.0/en/DEC/10_SF1/QTP1/0500000US40029 |date=February 13, 2020 }} ''American Fact Finder'', Accessed July 5, 2015.</ref> The median age was 41.0 years.<ref name="Census-2010-QT-P1"/> For every 100 females there were 97.7 males.<ref name="Census-2010-QT-P1"/> For every 100 females age 18 and over, there were 91.5 males.<ref name="Census-2010-QT-P1"/>

    According to the 2013 [[American Community Survey]], the median income for a household in the county was $34,867, and the median income for a family was $44,888.<ref name="ACS-2013">United States Census Bureau. [http://factfinder.census.gov/bkmk/table/1.0/en/ACS/13_5YR/DP03/0500000US40029 "DP03 Selected Economic Characteristics: 2009-2013 American Community Survey 5-Year Estimates - Coal County, Oklahoma,"] {{Webarchive|url=https://archive.today/20200213014104/http://factfinder.census.gov/bkmk/table/1.0/en/ACS/13_5YR/DP03/0500000US40029 |date=February 13, 2020 }} ''American Fact Finder'', Accessed July 5, 2015.</ref> Male full-time, year round workers had a median income of $36,442 compared to $26,450 for female full-time, year round workers.<ref name="ACS-2013"/> The [[per capita income]] for the county was $19,752.<ref name="ACS-2013"/> About 15.8% of families and 21.6% of the population were below the [[poverty line]], including 35.9% of those under age 18 and 15.7% of those age 65 or over.<ref name="ACS-2013"/>

    According to the 2000 census, 94.6% spoke [[English language|English]], 3.0% [[Spanish language|Spanish]], 1.1% [[German language|German]] and 1.1% [[Choctaw language|Choctaw]] as their first language.
    '''

c = Census(CENSUS_KEY)
c.acs5.get(('NAME', 'B25034_010E'),
          {'for': 'state:{}'.format(states.MD.fips)})
