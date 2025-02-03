import datetime, requests, os
#from IGNORE import credentials

STATE_LIST = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
    'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
    'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
    'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
    'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
    'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
    'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
]

MISSING_STATES = {
    'Arkansas': [
        "Arkansas", "Ashley", "Baxter", "Benton", "Boone", "Bradley", "Calhoun", "Carroll",
        "Chicot", "Clark", "Clay", "Cleburne", "Cleveland", "Columbia", "Conway", "Craighead",
        "Crawford", "Crittenden", "Cross", "Dallas", "Desha", "Drew", "Faulkner", "Franklin",
        "Fulton", "Garland", "Grant", "Greene", "Hempstead", "Hot Spring", "Howard", "Independence",
        "Izard", "Jackson", "Jefferson", "Johnson", "Lafayette", "Lawrence", "Lee", "Lincoln",
        "Little River", "Logan", "Lonoke", "Madison", "Marion", "Miller", "Mississippi",
        "Monroe", "Montgomery", "Nevada", "Newton", "Ouachita", "Perry", "Phillips", "Pike",
        "Poinsett", "Polk", "Pope", "Prairie", "Pulaski", "Randolph", "St. Francis", "Saline",
        "Scott", "Searcy", "Sebastian", "Sevier", "Sharp", "Stone", "Union", "Van Buren",
        "Washington", "White", "Woodruff", "Yell"
    ],
    'Alaska': [
        "Aleutians East Borough", "Aleutians West Census Area", "Anchorage Municipality",
        "Bethel Census Area", "Bristol Bay Borough", "Denali Borough", "Dillingham Census Area",
        "Fairbanks North Star Borough", "Haines Borough", "Hoonah-Angoon Census Area",
        "Juneau City and Borough", "Kenai Peninsula Borough", "Ketchikan Gateway Borough",
        "Kodiak Island Borough", "Kusilvak Census Area", "Lake and Peninsula Borough",
        "Matanuska-Susitna Borough", "Nome Census Area", "North Slope Borough", "Northwest Arctic Borough",
        "Petersburg Borough", "Prince of Wales-Hyder Census Area", "Sitka City and Borough",
        "Skagway Municipality", "Southeast Fairbanks Census Area", "Wrangell City and Borough",
        "Yakutat City and Borough", "Yukon-Koyukuk Census Area"
    ],
    'Georgia': [
        "Appling", "Atkinson", "Bacon", "Baker", "Baldwin", "Banks", "Barrow", "Bartow", "Ben Hill",
        "Berrien", "Bibb", "Bleckley", "Brantley", "Brooks", "Bryan", "Bulloch", "Burke", "Butts",
        "Calhoun", "Camden", "Candler", "Carroll", "Catoosa", "Charlton", "Chatham", "Chattahoochee",
        "Chattooga", "Cherokee", "Clarke", "Clay", "Clayton", "Clinch", "Cobb", "Coffee", "Colquitt",
        "Columbia", "Cook", "Coweta", "Crawford", "Crisp", "Dade", "Dawson", "Decatur", "DeKalb",
        "Dodge", "Dooly", "Dougherty", "Douglas", "Early", "Echols", "Effingham", "Elbert", "Emanuel",
        "Evans", "Fannin", "Fayette", "Floyd", "Forsyth", "Franklin", "Fulton", "Gilmer", "Glascock",
        "Glynn", "Gordon", "Grady", "Greene", "Gwinnett", "Habersham", "Hall", "Hancock", "Haralson",
        "Harris", "Hart", "Heard", "Henry", "Houston", "Irwin", "Jackson", "Jasper", "Jeff Davis",
        "Jefferson", "Jenkins", "Johnson", "Jones", "Lamar", "Lanier", "Laurens", "Lee", "Liberty",
        "Lincoln", "Long", "Lowndes", "Lumpkin", "McDuffie", "McIntosh", "Macon", "Madison",
        "Marion", "Meriwether", "Miller", "Mitchell", "Monroe", "Montgomery", "Morgan", "Murray",
        "Muscogee", "Newton", "Oconee", "Oglethorpe", "Paulding", "Peach", "Pickens", "Pierce",
        "Pike", "Polk", "Pulaski", "Putnam", "Quitman", "Rabun", "Randolph", "Richmond", "Rockdale",
        "Schley", "Screven", "Seminole", "Spalding", "Stephens", "Stewart", "Sumter", "Talbot",
        "Taliaferro", "Tattnall", "Taylor", "Telfair", "Terrell", "Thomas", "Tift", "Toombs",
        "Towns", "Treutlen", "Troup", "Turner", "Twiggs", "Union", "Upson", "Walker", "Walton",
        "Ware", "Warren", "Washington", "Wayne", "Webster", "Wheeler", "White", "Whitfield",
        "Wilcox", "Wilkes", "Wilkinson", "Worth"
    ],
    'Illinois': [
        "Adams", "Alexander", "Bond", "Boone", "Brown", "Bureau", "Calhoun", "Carroll", "Cass",
        "Champaign", "Christian", "Clark", "Clay", "Clinton", "Coles", "Cook", "Crawford", "Cumberland",
        "DeKalb", "De Witt", "Douglas", "DuPage", "Edgar", "Edwards", "Effingham", "Fayette", "Ford",
        "Franklin", "Fulton", "Gallatin", "Greene", "Grundy", "Hamilton", "Hancock", "Hardin",
        "Henderson", "Henry", "Iroquois", "Jackson", "Jasper", "Jefferson", "Jersey", "Jo Daviess",
        "Johnson", "Kane", "Kankakee", "Kendall", "Knox", "Lake", "LaSalle", "Lawrence", "Lee",
        "Livingston", "Logan", "Macon", "Macoupin", "Madison", "Marion", "Marshall", "Mason",
        "Massac", "McDonough", "McHenry", "McLean", "Menard", "Mercer", "Monroe", "Montgomery",
        "Morgan", "Moultrie", "Ogle", "Peoria", "Perry", "Piatt", "Pike", "Pope", "Pulaski", "Putnam",
        "Randolph", "Richland", "Rock Island", "St. Clair", "Saline", "Sangamon", "Schuyler",
        "Scott", "Shelby", "Stark", "Stephenson", "Tazewell", "Union", "Vermilion", "Wabash",
        "Warren", "Washington", "Wayne", "White", "Whiteside", "Will", "Williamson", "Winnebago",
        "Woodford"
    ],
    'Louisiana': [
        "Acadia", "Allen", "Ascension", "Assumption", "Avoyelles", "Beauregard", "Bienville",
        "Bossier", "Caddo", "Calcasieu", "Caldwell", "Cameron", "Catahoula", "Claiborne",
        "Concordia", "De Soto", "East Baton Rouge", "East Carroll", "East Feliciana", "Evangeline",
        "Franklin", "Grant", "Iberia", "Iberville", "Jackson", "Jefferson", "Jefferson Davis",
        "Lafayette", "Lafourche", "LaSalle", "Lincoln", "Livingston", "Madison", "Morehouse",
        "Natchitoches", "Orleans", "Ouachita", "Plaquemines", "Pointe Coupee", "Rapides",
        "Red River", "Richland", "Sabine", "St. Bernard", "St. Charles", "St. Helena", "St. James",
        "St. John the Baptist", "St. Landry", "St. Martin", "St. Mary", "St. Tammany",
        "Tangipahoa", "Tensas", "Terrebonne", "Union", "Vermilion", "Vernon", "Washington",
        "Webster", "West Baton Rouge", "West Carroll", "West Feliciana", "Winn"
    ],
    'Massachusetts': [
        "Barnstable", "Berkshire", "Bristol", "Dukes", "Essex", "Franklin", "Hampden",
        "Hampshire", "Middlesex", "Nantucket", "Norfolk", "Plymouth", "Suffolk", "Worcester"
    ],
    'Mississippi': [
        "Adams", "Alcorn", "Amite", "Attala", "Benton", "Bolivar", "Calhoun", "Carroll",
        "Chickasaw", "Choctaw", "Claiborne", "Clarke", "Clay", "Coahoma", "Copiah", "Covington",
        "DeSoto", "Forrest", "Franklin", "George", "Greene", "Grenada", "Hancock", "Harrison",
        "Hinds", "Holmes", "Humphreys", "Issaquena", "Itawamba", "Jackson", "Jasper", "Jefferson",
        "Jefferson Davis", "Jones", "Kemper", "Lafayette", "Lamar", "Lauderdale", "Lawrence",
        "Leake", "Lee", "Leflore", "Lincoln", "Lowndes", "Madison", "Marion", "Marshall",
        "Monroe", "Montgomery", "Neshoba", "Newton", "Noxubee", "Oktibbeha", "Panola", "Pearl River",
        "Perry", "Pike", "Pontotoc", "Prentiss", "Quitman", "Rankin", "Scott", "Sharkey", "Simpson",
        "Smith", "Stone", "Sunflower", "Tallahatchie", "Tate", "Tippah", "Tishomingo", "Tunica",
        "Union", "Walthall", "Warren", "Washington", "Wayne", "Webster", "Wilkinson", "Winston",
        "Yalobusha", "Yazoo"
    ],
    'Missouri': [
        "Adair", "Andrew", "Atchison", "Audrain", "Barry", "Barton", "Bates", "Benton",
        "Bollinger", "Boone", "Buchanan", "Butler", "Caldwell", "Callaway", "Camden", "Cape Girardeau",
        "Carroll", "Carter", "Cass", "Cedar", "Chariton", "Christian", "Clark", "Clay", "Clinton",
        "Cole", "Cooper", "Crawford", "Dade", "Dallas", "Daviess", "DeKalb", "Dent", "Douglas",
        "Dunklin", "Franklin", "Gasconade", "Gentry", "Greene", "Grundy", "Harrison", "Henry",
        "Hickory", "Holt", "Howard", "Howell", "Iron", "Jackson", "Jasper", "Jefferson", "Johnson",
        "Knox", "Laclede", "Lafayette", "Lawrence", "Lewis", "Lincoln", "Linn", "Livingston",
        "McDonald", "Macon", "Madison", "Maries", "Marion", "Mercer", "Miller", "Mississippi",
        "Moniteau", "Monroe", "Montgomery", "Morgan", "New Madrid", "Newton", "Nodaway", "Oregon",
        "Osage", "Ozark", "Pemiscot", "Perry", "Pettis", "Phelps", "Pike", "Platte", "Polk",
        "Pulaski", "Putnam", "Ralls", "Randolph", "Ray", "Reynolds", "Ripley", "Saline", "Schuyler",
        "Scotland", "Scott", "Shannon", "Shelby", "St. Charles", "St. Clair", "St. Francois",
        "St. Louis", "Ste. Genevieve", "Stoddard", "Stone", "Sullivan", "Taney", "Texas", "Vernon",
        "Warren", "Washington", "Wayne", "Webster", "Worth", "Wright", "City of St. Louis"
    ],
    'Montana': [
        "Beaverhead", "Big Horn", "Blaine", "Broadwater", "Carbon", "Carter", "Cascade", "Chouteau",
        "Custer", "Daniels", "Dawson", "Deer Lodge", "Fallon", "Fergus", "Flathead", "Gallatin",
        "Garfield", "Glacier", "Golden Valley", "Granite", "Hill", "Jefferson", "Judith Basin",
        "Lake", "Lewis and Clark", "Liberty", "Lincoln", "Madison", "McCone", "Meagher",
        "Mineral", "Missoula", "Musselshell", "Park", "Petroleum", "Phillips", "Pondera",
        "Powder River", "Powell", "Prairie", "Ravalli", "Richland", "Roosevelt", "Rosebud",
        "Sanders", "Sheridan", "Silver Bow", "Stillwater", "Sweet Grass", "Teton", "Toole",
        "Treasure", "Valley", "Wheatland", "Wibaux", "Yellowstone"
    ],
    'Pennsylvania': [
        "Adams", "Allegheny", "Armstrong", "Beaver", "Bedford", "Berks", "Blair", "Bradford",
        "Bucks", "Butler", "Cambria", "Cameron", "Carbon", "Centre", "Chester", "Clarion",
        "Clearfield", "Clinton", "Columbia", "Crawford", "Cumberland", "Dauphin", "Delaware",
        "Elk", "Erie", "Fayette", "Forest", "Franklin", "Fulton", "Greene", "Huntingdon",
        "Indiana", "Jefferson", "Juniata", "Lackawanna", "Lancaster", "Lawrence", "Lebanon",
        "Lehigh", "Luzerne", "Lycoming", "McKean", "Mercer", "Mifflin", "Monroe", "Montgomery",
        "Montour", "Northampton", "Northumberland", "Perry", "Philadelphia", "Pike", "Potter",
        "Schuylkill", "Snyder", "Somerset", "Sullivan", "Susquehanna", "Tioga", "Union",
        "Venango", "Warren", "Washington", "Wayne", "Westmoreland", "Wyoming", "York"
    ],
    'Utah': [
        "Beaver", "Box Elder", "Cache", "Carbon", "Daggett", "Davis", "Duchesne", "Emery",
        "Garfield", "Grand", "Iron", "Juab", "Kane", "Millard", "Morgan", "Piute",
        "Rich", "Salt Lake", "San Juan", "Sanpete", "Sevier", "Summit", "Tooele",
        "Uintah", "Utah", "Wasatch", "Washington", "Wayne", "Weber"
    ],
    'Virginia': [
        "Accomack", "Albemarle", "Alleghany", "Amelia", "Amherst", "Appomattox", "Arlington",
        "Augusta", "Bath", "Bedford", "Bland", "Botetourt", "Brunswick", "Buchanan", "Buckingham",
        "Campbell", "Caroline", "Carroll", "Charles City", "Charlotte", "Chesterfield",
        "Clarke", "Craig", "Culpeper", "Cumberland", "Dickenson", "Dinwiddie", "Essex",
        "Fairfax", "Fauquier", "Floyd", "Fluvanna", "Franklin", "Frederick", "Giles",
        "Gloucester", "Goochland", "Grayson", "Greene", "Greensville", "Halifax", "Hanover",
        "Henrico", "Henry", "Highland", "Isle of Wight", "James City", "King and Queen",
        "King George", "King William", "Lancaster", "Lee", "Loudoun", "Louisa", "Lunenburg",
        "Madison", "Mathews", "Mecklenburg", "Middlesex", "Montgomery", "Nelson", "New Kent",
        "Northampton", "Northumberland", "Nottoway", "Orange", "Page", "Patrick", "Pittsylvania",
        "Powhatan", "Prince Edward", "Prince George", "Prince William", "Pulaski", "Rappahannock",
        "Richmond", "Roanoke", "Rockbridge", "Rockingham", "Russell", "Scott", "Shenandoah",
        "Smyth", "Southampton", "Spotsylvania", "Stafford", "Surry", "Sussex", "Tazewell",
        "Warren", "Washington", "Westmoreland", "Wise", "Wythe", "York"
    ],
    'West Virginia': [
        "Barbour", "Berkeley", "Boone", "Braxton", "Brooke", "Cabell", "Calhoun", "Clay",
        "Doddridge", "Fayette", "Gilmer", "Grant", "Greenbrier", "Hampshire", "Hancock",
        "Hardy", "Harrison", "Jackson", "Jefferson", "Kanawha", "Lewis", "Lincoln", "Logan",
        "Marion", "Marshall", "Mason", "McDowell", "Mercer", "Mineral", "Mingo", "Monongalia",
        "Monroe", "Morgan", "Nicholas", "Ohio", "Pendleton", "Pleasants", "Pocahontas",
        "Preston", "Putnam", "Raleigh", "Randolph", "Ritchie", "Roane", "Summers", "Taylor",
        "Tucker", "Tyler", "Upshur", "Wayne", "Webster", "Wetzel", "Wirt", "Wood", "Wyoming"
    ]
}

def makeStateFile(stateName):
    print(stateName)
    modifiedStateName = stateName.replace(' ', '_')
    if stateName in MISSING_STATES.keys():
        with open('raw/'+modifiedStateName+'.txt', "w") as file:
            for item in MISSING_STATES[stateName]:
                file.write(f"{item}\n")
        print('pulled from local\n')
    else:
        os.system('./fetchCountyNames.sh -k $WIKI_ACCESS_TOKEN -e https://api.wikimedia.org/core/v1/wikipedia/en/page/List_of_counties_in_'+modifiedStateName+' > raw/'+modifiedStateName+'.txt')
        print('fetched via api\n')

if __name__ == '__main__':
    for state in STATE_LIST:
        makeStateFile(state)

# today = datetime.datetime.now()
# date = today.strftime('%Y/%m/%d')
#
# url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/featured/' + date
#
# headers = {
#   'Authorization': 'Bearer '+WIKIMEDIA_KEY['Access token'],
#   'User-Agent': WIKIMEDIA_KEY['App name']+' ('+WIKIMEDIA_KEY['Email']+')'
# }
#
# response = requests.get(url, headers=headers)
# data = response.json()
