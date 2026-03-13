import sqlite3
import json

# 1. Setup SQLite Database
conn = sqlite3.connect('trail_data.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS waypoints')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS waypoints (
        id INTEGER PRIMARY KEY,
        name TEXT,
        loc TEXT,
        lat REAL,
        lng REAL,
        category TEXT,
        unesco BOOLEAN,
        katha TEXT
    )
''')

# 2. Insert Delhi Heritage Waypoints (174 ASI Monuments)
waypoints = [
    (1, "Bastion \u2014 Jahan Panah meets Rai Pithora Fort", "Adchini", 28.5265, 77.1885, "fort", False, "A historical fort located in Adchini, protected by the Archaeological Survey of India (ASI)."),
    (2, "Ramp and Gateway of Rai Pithora's Fort", "Adchini", 28.527, 77.1878, "fort", False, "A historical fort located in Adchini, protected by the Archaeological Survey of India (ASI)."),
    (3, "Marble Tomb of Nawab Bahadur Jawid Khan", "Aliganj", 28.635, 77.22, "tomb", False, "A historical tomb located in Aliganj, protected by the Archaeological Survey of India (ASI)."),
    (4, "Lal Bangla", "Babarpur (Kaka Nagar)", 28.631, 77.2385, "other", False, "A historical other located in Babarpur (Kaka Nagar), protected by the Archaeological Survey of India (ASI)."),
    (5, "Khair-ul-Manzil", "Kaka Nagar", 28.609, 77.243, "mosque", False, "A historical mosque located in Kaka Nagar, protected by the Archaeological Survey of India (ASI)."),
    (6, "Kos Minar \u2014 Mughal Mile Stone", "Kaka Nagar", 28.6305, 77.238, "pillar", False, "A historical pillar located in Kaka Nagar, protected by the Archaeological Survey of India (ASI)."),
    (7, "Moti Gate of Shershah", "Kaka Nagar", 28.6095, 77.2435, "gate", False, "A historical gate located in Kaka Nagar, protected by the Archaeological Survey of India (ASI)."),
    (8, "Begampuri Masjid", "Begampur", 28.5438, 77.2025, "mosque", False, "A historical mosque located in Begampur, protected by the Archaeological Survey of India (ASI)."),
    (9, "Phool Chadar Aqueduct near Najafgarh Jheel", "Chaukri Mubarakabad", 28.586, 76.972, "other", False, "A historical other located in Chaukri Mubarakabad, protected by the Archaeological Survey of India (ASI)."),
    (10, "Lal Gumbad", "Chirag Delhi", 28.536, 77.2105, "tomb", False, "A historical tomb located in Chirag Delhi, protected by the Archaeological Survey of India (ASI)."),
    (11, "Tomb of Bahlol Lodi", "Chirag Delhi", 28.5355, 77.211, "tomb", False, "A historical tomb located in Chirag Delhi, protected by the Archaeological Survey of India (ASI)."),
    (12, "Ajmeri Gate", "Bazar Ajmeri Gate", 28.643, 77.2175, "gate", False, "A historical gate located in Bazar Ajmeri Gate, protected by the Archaeological Survey of India (ASI)."),
    (13, "Alipur Cemetery", "Delhi\u2013Alipur", 28.7978, 77.1326, "other", False, "A historical other located in Delhi\u2013Alipur, protected by the Archaeological Survey of India (ASI)."),
    (14, "Ashoka's Pillar \u2014 Ferozabad", "Ferozshah Kila", 28.6486, 77.237, "pillar", False, "A historical pillar located in Ferozshah Kila, protected by the Archaeological Survey of India (ASI)."),
    (15, "Bara Khamba Cemetery", "Imperial City", 28.627, 77.219, "other", False, "A historical other located in Imperial City, protected by the Archaeological Survey of India (ASI)."),
    (16, "Chauburji", "Ridge near Hindu Rao Hospital", 28.68, 77.199, "other", False, "A historical other located in Ridge near Hindu Rao Hospital, protected by the Archaeological Survey of India (ASI)."),
    (17, "Eremo Cemetery", "Kishanaganj Railway Station", 28.661, 77.171, "other", False, "A historical other located in Kishanaganj Railway Station, protected by the Archaeological Survey of India (ASI)."),
    (18, "Delhi Fort / Lal Qila (Red Fort)", "Red Fort", 28.6562, 77.241, "fort", True, "Built by Shah Jahan in 1639, this massive red sandstone fortress served as the Mughal capital for nearly 200 years. Every Independence Day, India's Prime Minister hoists the flag from its ramparts."),
    (19, "Delhi Gate", "Daryaganj", 28.6408, 77.246, "gate", False, "A historical gate located in Daryaganj, protected by the Archaeological Survey of India (ASI)."),
    (20, "Enclosure \u2014 Grave of Lt. Edwards (1857)", "North Ridge, Civil Lines", 28.689, 77.2065, "other", False, "A historical other located in North Ridge, Civil Lines, protected by the Archaeological Survey of India (ASI)."),
    (21, "Enclosure Wall with Tomb of Najaf Khan", "Safdarjang Flyover", 28.5712, 77.2038, "tomb", False, "A historical tomb located in Safdarjang Flyover, protected by the Archaeological Survey of India (ASI)."),
    (22, "Flag Staff Tower", "Civil Lines Ridge", 28.685, 77.204, "other", False, "A historical other located in Civil Lines Ridge, protected by the Archaeological Survey of India (ASI)."),
    (23, "Jantar Mantar", "Connaught Place", 28.627, 77.2166, "other", False, "A historical other located in Connaught Place, protected by the Archaeological Survey of India (ASI)."),
    (24, "Kashmeri Gate and City Wall", "Kashmeri Gate", 28.6668, 77.2276, "gate", False, "A historical gate located in Kashmeri Gate, protected by the Archaeological Survey of India (ASI)."),
    (25, "Kotla Ferozabad \u2014 Walls, Mosque & Ruins", "Near Delhi Gate", 28.6486, 77.237, "fort", False, "A historical fort located in Near Delhi Gate, protected by the Archaeological Survey of India (ASI)."),
    (26, "Lal Darwaza \u2014 Northern Gate of Shershah's Delhi", "South of Delhi Gate", 28.6375, 77.247, "gate", False, "A historical gate located in South of Delhi Gate, protected by the Archaeological Survey of India (ASI)."),
    (27, "Lothian Road Cemetery", "Kashmeri Gate", 28.6655, 77.229, "other", False, "A historical other located in Kashmeri Gate, protected by the Archaeological Survey of India (ASI)."),
    (28, "The Mosque \u2014 Qudsia Garden", "Qudsia Garden", 28.673, 77.2198, "mosque", False, "A historical mosque located in Qudsia Garden, protected by the Archaeological Survey of India (ASI)."),
    (29, "Mutiny Telegraph Memorial", "Kashmeri Gate", 28.667, 77.227, "other", False, "A historical other located in Kashmeri Gate, protected by the Archaeological Survey of India (ASI)."),
    (30, "Nicholson Cemetery", "Kashmeri Gate", 28.666, 77.2265, "other", False, "A historical other located in Kashmeri Gate, protected by the Archaeological Survey of India (ASI)."),
    (31, "Nicholson Statue and Enclosure", "Outside Kashmeri Gate", 28.6675, 77.226, "other", False, "A historical other located in Outside Kashmeri Gate, protected by the Archaeological Survey of India (ASI)."),
    (32, "Old Baoli \u2014 West of Hindu Rao's House", "The Ridge, Delhi", 28.681, 77.198, "other", False, "A historical other located in The Ridge, Delhi, protected by the Archaeological Survey of India (ASI)."),
    (33, "Old Entrance Gateway of the Garden", "Qudsia Garden", 28.6725, 77.2195, "garden", False, "A historical garden located in Qudsia Garden, protected by the Archaeological Survey of India (ASI)."),
    (34, "Pirghaib \u2014 North of Hindu Rao's House", "The Ridge, Delhi", 28.682, 77.1975, "other", False, "A historical other located in The Ridge, Delhi, protected by the Archaeological Survey of India (ASI)."),
    (35, "Portion of City Wall \u2014 Nicholson Wound Site (1857)", "The Ridge, Delhi", 28.6815, 77.1985, "fort", False, "A historical fort located in The Ridge, Delhi, protected by the Archaeological Survey of India (ASI)."),
    (36, "Punjabi Gate \u2014 Roshanara Bagh", "Subzi Mandi", 28.673, 77.1955, "gate", False, "A historical gate located in Subzi Mandi, protected by the Archaeological Survey of India (ASI)."),
    (37, "Purana Qila (Inderpat) with Kila Kohna Masjid & Sher Mandal", "South of Delhi Gate", 28.6082, 77.2431, "fort", False, "A historical fort located in South of Delhi Gate, protected by the Archaeological Survey of India (ASI)."),
    (38, "Rajpur Mutiny Cemetery", "Old Rajpur Cantonment", 28.735, 77.18, "other", False, "A historical other located in Old Rajpur Cantonment, protected by the Archaeological Survey of India (ASI)."),
    (39, "Remaining Gateways of Old Magazira", "Near Post Office, Delhi", 28.65, 77.23, "gate", False, "A historical gate located in Near Post Office, Delhi, protected by the Archaeological Survey of India (ASI)."),
    (40, "Sher Shah's Gate with Curtain Walls", "Opposite Purana Qila", 28.61, 77.245, "fort", False, "A historical fort located in Opposite Purana Qila, protected by the Archaeological Survey of India (ASI)."),
    (41, "Site of Siege Battery \u2014 Sammy House Battery", "300 Yds East of Mutiny Memorial", 28.687, 77.207, "other", False, "A historical other located in 300 Yds East of Mutiny Memorial, protected by the Archaeological Survey of India (ASI)."),
    (42, "Site of Siege Battery \u2014 Hospital Police Lines", "Police Lines", 28.685, 77.206, "other", False, "A historical other located in Police Lines, protected by the Archaeological Survey of India (ASI)."),
    (43, "Site of Siege Battery \u2014 Curzon House", "Curzon House", 28.6855, 77.205, "other", False, "A historical other located in Curzon House, protected by the Archaeological Survey of India (ASI)."),
    (44, "Site of Siege Battery \u2014 Delhi Club Ground", "Delhi Club", 28.6845, 77.208, "other", False, "A historical other located in Delhi Club, protected by the Archaeological Survey of India (ASI)."),
    (45, "Sunehri Masjid near Delhi Fort", "Delhi Fort", 28.6557, 77.2415, "mosque", False, "A historical mosque located in Delhi Fort, protected by the Archaeological Survey of India (ASI)."),
    (46, "Tomb of Capt. Mac. Barnatt \u2014 Kishanganj", "Kishanganaj", 28.6615, 77.172, "tomb", False, "A historical tomb located in Kishanganaj, protected by the Archaeological Survey of India (ASI)."),
    (47, "Tomb of Ghiasuddin Khan", "Tughlaqabad", 28.5065, 77.2537, "tomb", False, "A historical tomb located in Tughlaqabad, protected by the Archaeological Survey of India (ASI)."),
    (48, "Tomb of Roshanara & Baradari", "Sabzi Mandi", 28.672, 77.196, "tomb", False, "A historical tomb located in Sabzi Mandi, protected by the Archaeological Survey of India (ASI)."),
    (49, "Tomb of Razia Begum \u2014 Bulbuli Khana", "Shahjahanabad", 28.647, 77.2285, "tomb", False, "A historical tomb located in Shahjahanabad, protected by the Archaeological Survey of India (ASI)."),
    (50, "Tomb of Safdarjang", "Lodhi Road", 28.5909, 77.2081, "tomb", False, "A historical tomb located in Lodhi Road, protected by the Archaeological Survey of India (ASI)."),
    (51, "Tripolia Gateways", "Delhi\u2013Karnal Road", 28.711, 77.17, "gate", False, "A historical gate located in Delhi\u2013Karnal Road, protected by the Archaeological Survey of India (ASI)."),
    (52, "Uggar Sain's Baoli", "Near Jantar Mantar", 28.6268, 77.2162, "other", False, "A historical other located in Near Jantar Mantar, protected by the Archaeological Survey of India (ASI)."),
    (53, "Tomb of Darya Khan", "Kidwai Nagar East", 28.572, 77.2065, "tomb", False, "A historical tomb located in Kidwai Nagar East, protected by the Archaeological Survey of India (ASI)."),
    (54, "Baoli at Ghiaspur", "Nizamuddin", 28.5928, 77.2494, "other", False, "A historical other located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (55, "Tomb of Mirza Muzaffer \u2014 Chota Batasha (Ghiaspur)", "Nizamuddin", 28.592, 77.2492, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (56, "Tomb of Amir Khusro \u2014 Ghiaspur", "Nizamuddin", 28.5934, 77.2498, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (57, "Tomb of Mirza Muzaffer \u2014 Bara Batasha (Ghiaspur)", "Nizamuddin", 28.5918, 77.249, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (58, "Tomb of Nizamuddin Aulia \u2014 Ghiaspur", "Nizamuddin", 28.5931, 77.2495, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (59, "Unknown Tomb \u2014 Ghiaspur", "Nizamuddin", 28.5926, 77.2488, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (60, "Tomb of Ferozshah & Complex \u2014 Hauz Khas", "Hauz Khas", 28.5496, 77.198, "tomb", False, "A historical tomb located in Hauz Khas, protected by the Archaeological Survey of India (ASI)."),
    (61, "Bag-i-Alam Gumbad with Mosque", "Humayunpur", 28.555, 77.207, "mosque", False, "A historical mosque located in Humayunpur, protected by the Archaeological Survey of India (ASI)."),
    (62, "Kali Gumti", "Humayunpur (Hauz Khas)", 28.5545, 77.206, "tomb", False, "A historical tomb located in Humayunpur (Hauz Khas), protected by the Archaeological Survey of India (ASI)."),
    (63, "Tefewala Gumbad", "Humayunpur Deer Park, Hauz Khas", 28.5535, 77.205, "tomb", False, "A historical tomb located in Humayunpur Deer Park, Hauz Khas, protected by the Archaeological Survey of India (ASI)."),
    (64, "Arab Sarai", "Near Humayun's Tomb", 28.5926, 77.2519, "other", False, "A historical other located in Near Humayun's Tomb, protected by the Archaeological Survey of India (ASI)."),
    (65, "Gateway of Arab Sarai \u2014 Facing North (Purana Qila)", "Arab Sarai Village", 28.5923, 77.2523, "gate", False, "A historical gate located in Arab Sarai Village, protected by the Archaeological Survey of India (ASI)."),
    (66, "Gateway of Arab Sarai \u2014 Facing East (Humayun's Tomb)", "Arab Sarai Village", 28.5921, 77.2521, "gate", False, "A historical gate located in Arab Sarai Village, protected by the Archaeological Survey of India (ASI)."),
    (67, "Remaining Gateways of Arab Sarai & Abadi-Bagh-Buhalima", "Arab Sarai Village", 28.5919, 77.252, "gate", False, "A historical gate located in Arab Sarai Village, protected by the Archaeological Survey of India (ASI)."),
    (68, "Lakharwal Gumbad (Tomb)", "Sunder Nursery, Nizamuddin", 28.596, 77.2505, "tomb", False, "A historical tomb located in Sunder Nursery, Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (69, "Sunderwala Burj", "Sunder Nursery", 28.5958, 77.2508, "other", False, "A historical other located in Sunder Nursery, protected by the Archaeological Survey of India (ASI)."),
    (70, "Sunderwala Mahal", "Sunder Nursery", 28.5956, 77.251, "other", False, "A historical other located in Sunder Nursery, protected by the Archaeological Survey of India (ASI)."),
    (71, "Bijay Mandal \u2014 Neighbouring Domes & Dalan", "Kalusarai (Sarvapriya Vihar)", 28.5478, 77.201, "fort", False, "A historical fort located in Kalusarai (Sarvapriya Vihar), protected by the Archaeological Survey of India (ASI)."),
    (72, "Old Lodi Bridge", "Near Sikander Lodi's Tomb, Khairpur", 28.592, 77.2211, "other", False, "A historical other located in Near Sikander Lodi's Tomb, Khairpur, protected by the Archaeological Survey of India (ASI)."),
    (73, "Mosque with Dalans, Courtyard & Bara Gumbaj", "Khairpur (Lodhi Garden)", 28.592, 77.2218, "mosque", False, "A historical mosque located in Khairpur (Lodhi Garden), protected by the Archaeological Survey of India (ASI)."),
    (74, "Tomb of Mohammed Shah \u2014 Mubarak Khan-ka-Gumbaz", "Khairpur (Lodhi Garden)", 28.591, 77.2215, "tomb", False, "A historical tomb located in Khairpur (Lodhi Garden), protected by the Archaeological Survey of India (ASI)."),
    (75, "Tomb of Sikander Lodi", "Lodhi Garden", 28.5936, 77.2198, "tomb", False, "A historical tomb located in Lodhi Garden, protected by the Archaeological Survey of India (ASI)."),
    (76, "Shisha Gumbad \u2014 Blue Tile Decorated Tomb", "Lodhi Garden", 28.5929, 77.2205, "tomb", False, "A historical tomb located in Lodhi Garden, protected by the Archaeological Survey of India (ASI)."),
    (77, "Bandi / Poti ka Gumbad", "Kharera Village", 28.537, 77.193, "tomb", False, "A historical tomb located in Kharera Village, protected by the Archaeological Survey of India (ASI)."),
    (78, "Biran-Ka-Gumbad", "Kharera Village", 28.5375, 77.1935, "tomb", False, "A historical tomb located in Kharera Village, protected by the Archaeological Survey of India (ASI)."),
    (79, "Biwi / Dadi-ka-Gumbad", "Kharera Village", 28.5368, 77.1925, "tomb", False, "A historical tomb located in Kharera Village, protected by the Archaeological Survey of India (ASI)."),
    (80, "Chor Minar", "Hauz Khas Enclave", 28.5495, 77.1962, "other", False, "A historical other located in Hauz Khas Enclave, protected by the Archaeological Survey of India (ASI)."),
    (81, "Choti Gunti", "Kharehra Village, Green Park", 28.549, 77.1958, "other", False, "A historical other located in Kharehra Village, Green Park, protected by the Archaeological Survey of India (ASI)."),
    (82, "Idgah of Kharehra", "Hauz Khas Enclave", 28.5492, 77.1965, "mosque", False, "A historical mosque located in Hauz Khas Enclave, protected by the Archaeological Survey of India (ASI)."),
    (83, "Nili Mosque", "Hauz Khas Enclave", 28.55, 77.197, "mosque", False, "A historical mosque located in Hauz Khas Enclave, protected by the Archaeological Survey of India (ASI)."),
    (84, "Sakri Gumti", "Kharehra Village, Green Park", 28.5488, 77.1955, "other", False, "A historical other located in Kharehra Village, Green Park, protected by the Archaeological Survey of India (ASI)."),
    (85, "Khirkee Masjid", "Village Khirkee", 28.54, 77.2025, "mosque", False, "A historical mosque located in Village Khirkee, protected by the Archaeological Survey of India (ASI)."),
    (86, "Satpula", "Village Khirkee", 28.5395, 77.202, "other", False, "A historical other located in Village Khirkee, protected by the Archaeological Survey of India (ASI)."),
    (87, "Tomb of Yusuf-Quttal", "Khirkee Village", 28.5405, 77.203, "tomb", False, "A historical tomb located in Khirkee Village, protected by the Archaeological Survey of India (ASI)."),
    (88, "Jahaz Mahal", "Mehrauli", 28.5207, 77.186, "other", False, "A historical other located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (89, "Shamsid Talab with Platform & Entrance Gates", "Mehrauli", 28.5215, 77.187, "other", False, "A historical other located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (90, "Moti Masjid", "Mehrauli", 28.521, 77.1865, "mosque", False, "A historical mosque located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (91, "Old Palace of Bahadur Shah II \u2014 Lal Mahal", "Mehrauli", 28.5205, 77.1855, "fort", False, "A historical fort located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (92, "Bara Khamba", "Kherera Village, Hauz Khas", 28.538, 77.194, "other", False, "A historical other located in Kherera Village, Hauz Khas, protected by the Archaeological Survey of India (ASI)."),
    (93, "Qutab Archaeological Area \u2014 Qutub Minar & Complex", "Mehrauli", 28.5244, 77.1855, "pillar", True, "Rising 73 metres, the Qutub Minar is the tallest brick minaret in the world. The complex also houses the mysterious Iron Pillar that has resisted rust for over 1,600 years."),
    (94, "Tomb of Adam Khan (Rest House)", "Mehrauli", 28.523, 77.1845, "tomb", False, "A historical tomb located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (95, "Tomb and Mosque of Maulana Jamali Kamali", "Mehrauli", 28.522, 77.185, "tomb", False, "A historical tomb located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (96, "Wall Mosque", "Mehrauli", 28.5225, 77.1858, "mosque", False, "A historical mosque located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (97, "Walls of Lal Kot and Rai Pithora's Fort \u2014 Sohan Gate to Adam Khan's Tomb", "Mehrauli", 28.5235, 77.188, "fort", False, "A historical fort located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (98, "Walls of Lal Kot \u2014 Junction with Rai Pithora's Fort", "Near Jamali Kamali, Mehrauli", 28.5222, 77.1848, "fort", False, "A historical fort located in Near Jamali Kamali, Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (99, "Wall of Rai Pithora's Fort \u2014 Gates & Bastions", "Mehrauli", 28.524, 77.189, "fort", False, "A historical fort located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (100, "Gates and Walls of Mubarakpur Kotla", "Village Mubarakpur Kotla", 28.576, 77.2155, "fort", False, "A historical fort located in Village Mubarakpur Kotla, protected by the Archaeological Survey of India (ASI)."),
    (101, "Moti-ki-Masjid", "South Extension Part II", 28.568, 77.2165, "mosque", False, "A historical mosque located in South Extension Part II, protected by the Archaeological Survey of India (ASI)."),
    (102, "Inchla Wali Gunti", "Village Mubarakpur Kotla", 28.5758, 77.2152, "other", False, "A historical other located in Village Mubarakpur Kotla, protected by the Archaeological Survey of India (ASI)."),
    (103, "Kala Gumbad", "Village Mubarakpur Kotla", 28.5762, 77.2158, "tomb", False, "A historical tomb located in Village Mubarakpur Kotla, protected by the Archaeological Survey of India (ASI)."),
    (104, "Tombs of Bade Khan \u2014 Mubarakpur Kotla", "Village Mubarakpur Kotla", 28.5765, 77.216, "tomb", False, "A historical tomb located in Village Mubarakpur Kotla, protected by the Archaeological Survey of India (ASI)."),
    (105, "Tombs of Chote Khan \u2014 Mubarakpur", "Kotla", 28.5763, 77.2162, "tomb", False, "A historical tomb located in Kotla, protected by the Archaeological Survey of India (ASI)."),
    (106, "Tomb of Mubarak \u2014 Mubarakpur Kotla", "Village Mubarakpur Kotla", 28.576, 77.2165, "tomb", False, "A historical tomb located in Village Mubarakpur Kotla, protected by the Archaeological Survey of India (ASI)."),
    (107, "Mosque attached to Mubarak Shah Tomb", "Village Mubarakpur Kotla", 28.5758, 77.2168, "mosque", False, "A historical mosque located in Village Mubarakpur Kotla, protected by the Archaeological Survey of India (ASI)."),
    (108, "Tomb of Bhura Khan", "Village Mubarakpur Kotla", 28.5756, 77.217, "tomb", False, "A historical tomb located in Village Mubarakpur Kotla, protected by the Archaeological Survey of India (ASI)."),
    (109, "Tin Burji Walla Gumbad", "Mohammadpur Village", 28.569, 77.207, "tomb", False, "A historical tomb located in Mohammadpur Village, protected by the Archaeological Survey of India (ASI)."),
    (110, "Unnamed Tomb", "Mohammadpur Village", 28.5692, 77.2072, "tomb", False, "A historical tomb located in Mohammadpur Village, protected by the Archaeological Survey of India (ASI)."),
    (111, "Baoli", "Munika", 28.5605, 77.183, "other", False, "A historical other located in Munika, protected by the Archaeological Survey of India (ASI)."),
    (112, "Munda Gumbad", "Munika", 28.56, 77.1825, "tomb", False, "A historical tomb located in Munika, protected by the Archaeological Survey of India (ASI)."),
    (113, "Unnamed Mosque", "Munika", 28.5598, 77.1828, "mosque", False, "A historical mosque located in Munika, protected by the Archaeological Survey of India (ASI)."),
    (114, "Unnamed Tomb", "Munika", 28.5595, 77.1822, "tomb", False, "A historical tomb located in Munika, protected by the Archaeological Survey of India (ASI)."),
    (115, "Unnamed Tomb (315)", "Munika", 28.5592, 77.1818, "tomb", False, "A historical tomb located in Munika, protected by the Archaeological Survey of India (ASI)."),
    (116, "Unnamed Tomb (316)", "Munika", 28.559, 77.1815, "tomb", False, "A historical tomb located in Munika, protected by the Archaeological Survey of India (ASI)."),
    (117, "Unnamed Tomb (317)", "Munika", 28.5588, 77.1812, "tomb", False, "A historical tomb located in Munika, protected by the Archaeological Survey of India (ASI)."),
    (118, "Unnamed Mosque & Tomb (321\u2013322)", "Munika", 28.5585, 77.1808, "mosque", False, "A historical mosque located in Munika, protected by the Archaeological Survey of India (ASI)."),
    (119, "Wajirpur-ki-Gumbad", "Munika", 28.5608, 77.1835, "tomb", False, "A historical tomb located in Munika, protected by the Archaeological Survey of India (ASI)."),
    (120, "Afsah-walla-ki-Masjid \u2014 West Gate of Humayun's Tomb", "Nizamuddin", 28.5937, 77.2498, "mosque", False, "A historical mosque located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (121, "Bara Khamba \u2014 North Entrance to Shrine", "Nizamuddin", 28.5928, 77.249, "other", False, "A historical other located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (122, "Bara Pulah Bridge near Nizamuddin", "South of Nizamuddin", 28.588, 77.2508, "other", False, "A historical other located in South of Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (123, "Chausath Khamba & Tomb of Mirza Aziz Kokaltash", "Nizamuddin", 28.5922, 77.2486, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (124, "Grave of Jahanara Begum", "Nizamuddin", 28.593, 77.2496, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (125, "Grave of Mohammed Shah", "Nizamuddin", 28.5932, 77.2497, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (126, "Grave of Mirza Jahangir", "Nizamuddin", 28.5929, 77.2495, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (127, "Humayun's Tomb", "Nizamuddin", 28.5933, 77.2507, "tomb", True, "Completed in 1572, this garden-tomb was the first grand Mughal mausoleum on the subcontinent. Its symmetry and charbagh layout became the blueprint for the Taj Mahal itself."),
    (128, "Nila Gumbad \u2014 South Corner of Humayun's Tomb", "Nizamuddin", 28.5928, 77.2503, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (129, "Nili Chhatri / Subz Burz", "Nizamuddin East", 28.585, 77.2498, "other", False, "A historical other located in Nizamuddin East, protected by the Archaeological Survey of India (ASI)."),
    (130, "Tomb of Afsar-wala", "Nizamuddin", 28.5935, 77.25, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (131, "Tomb of Atgah Khan", "Nizamuddin", 28.5936, 77.2492, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (132, "Tomb of Isa Khan \u2014 Enclosure, Garden & Mosque", "Nizamuddin", 28.593, 77.2505, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (133, "Tomb of Khan-i-Khana", "Nizamuddin", 28.5873, 77.2516, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (134, "Tomb with Three Domes near Railway Station", "Nizamuddin", 28.5886, 77.249, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
    (135, "Sikargah Kushak", "Old Kushak Village", 28.577, 77.1765, "fort", False, "A historical fort located in Old Kushak Village, protected by the Archaeological Survey of India (ASI)."),
    (136, "Gateways of Badli-ki-Sarai", "Village Pipalthala", 28.735, 77.14, "gate", False, "A historical gate located in Village Pipalthala, protected by the Archaeological Survey of India (ASI)."),
    (137, "Tomb of Sheikh Kaburuddin \u2014 Rakabwala Gumbad", "Malviya Nagar", 28.5345, 77.2142, "tomb", False, "A historical tomb located in Malviya Nagar, protected by the Archaeological Survey of India (ASI)."),
    (138, "Ruined Walls, Bastions & Gateways of Siri", "Shahpur Jat", 28.5578, 77.214, "fort", False, "A historical fort located in Shahpur Jat, protected by the Archaeological Survey of India (ASI)."),
    (139, "Internal Buildings of Siri \u2014 Mehammadi Wali, Baradari, Motiyan Dome", "Shahpur Jat", 28.558, 77.2145, "fort", False, "A historical fort located in Shahpur Jat, protected by the Archaeological Survey of India (ASI)."),
    (140, "Nai-ka-Kot", "Tughlaqabad Kotla", 28.505, 77.2528, "fort", False, "A historical fort located in Tughlaqabad Kotla, protected by the Archaeological Survey of India (ASI)."),
    (141, "Tomb of Ghiyasuddin Tughlaq \u2014 Walls, Bastions & Causeway", "Tughlaqabad", 28.5065, 77.254, "tomb", False, "A historical tomb located in Tughlaqabad, protected by the Archaeological Survey of India (ASI)."),
    (142, "Tomb of Mohammed Tughlaqabad Shah", "Badarpur Zail", 28.5058, 77.2532, "tomb", False, "A historical tomb located in Badarpur Zail, protected by the Archaeological Survey of India (ASI)."),
    (143, "Walls of Old City of Tughlaqabad", "Badarpur Zail", 28.5045, 77.252, "fort", False, "A historical fort located in Badarpur Zail, protected by the Archaeological Survey of India (ASI)."),
    (144, "Walls, Gateways, Bastions of Tughlaqabad Fort", "Tughlaqabad", 28.5055, 77.253, "fort", False, "A historical fort located in Tughlaqabad, protected by the Archaeological Survey of India (ASI)."),
    (145, "Walls, Gate and Bastions of Adilabad (Mohammadbad)", "Tughlaqabad", 28.504, 77.251, "fort", False, "A historical fort located in Tughlaqabad, protected by the Archaeological Survey of India (ASI)."),
    (146, "The Tomb", "Wazirabad", 28.729, 77.234, "tomb", False, "A historical tomb located in Wazirabad, protected by the Archaeological Survey of India (ASI)."),
    (147, "The Mosque", "Wazirabad", 28.7292, 77.2342, "mosque", False, "A historical mosque located in Wazirabad, protected by the Archaeological Survey of India (ASI)."),
    (148, "Neighbouring Bridge", "Wazirabad", 28.7295, 77.2338, "other", False, "A historical other located in Wazirabad, protected by the Archaeological Survey of India (ASI)."),
    (149, "Mound \u2014 Jaga Bai (Plot No. 167)", "Jamia Nagar", 28.562, 77.2802, "other", False, "A historical other located in Jamia Nagar, protected by the Archaeological Survey of India (ASI)."),
    (150, "Ashoka Rock Edict", "East of Kailash Colony", 28.549, 77.253, "pillar", False, "A historical pillar located in East of Kailash Colony, protected by the Archaeological Survey of India (ASI)."),
    (151, "Mandi Mosque", "Ladho Sarai", 28.5278, 77.189, "mosque", False, "A historical mosque located in Ladho Sarai, protected by the Archaeological Survey of India (ASI)."),
    (152, "Rajon-ki-Bain with Mosque and Chhatri", "Ladho Sarai", 28.5282, 77.1885, "other", False, "A historical other located in Ladho Sarai, protected by the Archaeological Survey of India (ASI)."),
    (153, "Badun Gate", "Ladho Sarai", 28.5275, 77.188, "gate", False, "A historical gate located in Ladho Sarai, protected by the Archaeological Survey of India (ASI)."),
    (154, "Gateway of Lal Kot", "Ladho Sarai", 28.527, 77.1875, "gate", False, "A historical gate located in Ladho Sarai, protected by the Archaeological Survey of India (ASI)."),
    (155, "Gateway of Rai Pithora's Fort", "Ladho Sarai", 28.5265, 77.187, "gate", False, "A historical gate located in Ladho Sarai, protected by the Archaeological Survey of India (ASI)."),
    (156, "Walls of Rai Pithora's Fort & Jahan Panah \u2014 Junction", "Hauz Rani & Lado Sarai", 28.5285, 77.1895, "fort", False, "A historical fort located in Hauz Rani & Lado Sarai, protected by the Archaeological Survey of India (ASI)."),
    (157, "Tomb of Sultan Ghari", "Nalikpur Kohi", 28.512, 77.1025, "tomb", False, "A historical tomb located in Nalikpur Kohi, protected by the Archaeological Survey of India (ASI)."),
    (158, "Baoli \u2014 Diving Wall (Chandak-ki-Baoli)", "Mehrauli", 28.5218, 77.1862, "other", False, "A historical other located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (159, "Enclosure \u2014 Tomb of Shah Alam Bahadur Shah, Akbar Shah II", "Mehrauli", 28.5208, 77.1858, "tomb", False, "A historical tomb located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (160, "Hauz Shamsi with Central Red Stone Pavilion", "Mehrauli", 28.52, 77.1855, "other", False, "A historical other located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (161, "Iron Pillar (Hindu)", "Mehrauli", 28.5244, 77.1855, "pillar", False, "A historical pillar located in Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (162, "Ancient Mosque", "Palam", 28.6022, 77.0878, "mosque", False, "A historical mosque located in Palam, protected by the Archaeological Survey of India (ASI)."),
    (163, "Sheesh Mahal", "Shalimar Garden, Village Hyderpur", 28.689, 77.1468, "other", False, "A historical other located in Shalimar Garden, Village Hyderpur, protected by the Archaeological Survey of India (ASI)."),
    (164, "Ashokan Pillar \u2014 The Ridge", "Near Hindu Rao Hospital", 28.6812, 77.1985, "pillar", False, "A historical pillar located in Near Hindu Rao Hospital, protected by the Archaeological Survey of India (ASI)."),
    (165, "Sarai Shahji", "Malviya Nagar", 28.535, 77.215, "other", False, "A historical other located in Malviya Nagar, protected by the Archaeological Survey of India (ASI)."),
    (166, "Azim Khan Tomb", "Lado Sarai", 28.5268, 77.1892, "tomb", False, "A historical tomb located in Lado Sarai, protected by the Archaeological Survey of India (ASI)."),
    (167, "Mazar of Sheikh Muhammad Ibrahim Zauq", "Kadam Sherif, Paharganj", 28.644, 77.199, "tomb", False, "A historical tomb located in Kadam Sherif, Paharganj, protected by the Archaeological Survey of India (ASI)."),
    (168, "Fortification Wall \u2014 Asad Burj, Water Gate, Delhi Gate, Lahori Gate, Baoli", "Red Fort", 28.656, 77.2405, "fort", False, "A historical fort located in Red Fort, protected by the Archaeological Survey of India (ASI)."),
    (169, "Fortification Walls & Buildings of Salimgarh Fort", "Bela Road", 28.658, 77.2425, "fort", False, "A historical fort located in Bela Road, protected by the Archaeological Survey of India (ASI)."),
    (170, "Portion of City Wall of Shahjahanabad", "Ansari Road", 28.649, 77.234, "fort", False, "A historical fort located in Ansari Road, protected by the Archaeological Survey of India (ASI)."),
    (171, "Sat Narain Bhawan", "Roshanara Road", 28.6695, 77.1938, "other", False, "A historical other located in Roshanara Road, protected by the Archaeological Survey of India (ASI)."),
    (172, "Balban Khan's Tomb & Jamali Kamali", "Lado Sarai, Mehrauli", 28.5225, 77.1852, "tomb", False, "A historical tomb located in Lado Sarai, Mehrauli, protected by the Archaeological Survey of India (ASI)."),
    (173, "Unknown Tomb \u2014 Near JLN Stadium", "Pragati Vihar", 28.5845, 77.2388, "tomb", False, "A historical tomb located in Pragati Vihar, protected by the Archaeological Survey of India (ASI)."),
    (174, "Mazar of Mirza Ghalib", "Nizamuddin", 28.594, 77.2502, "tomb", False, "A historical tomb located in Nizamuddin, protected by the Archaeological Survey of India (ASI)."),
]

cursor.executemany('INSERT INTO waypoints VALUES (?, ?, ?, ?, ?, ?, ?, ?)', waypoints)
conn.commit()

# 3. Export to GeoJSON for the Web Map
cursor.execute('SELECT * FROM waypoints')
rows = cursor.fetchall()

features: list[dict] = []
geojson = {
    "type": "FeatureCollection",
    "features": features
}

for row in rows:
    feature = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [row[4], row[3]]},  # Lng, Lat
        "properties": {
            "id": row[0], 
            "name": row[1], 
            "loc": row[2], 
            "category": row[5], 
            "unesco": bool(row[6]), 
            "katha": row[7]
        }
    }
    features.append(feature)

with open('trail_data.js', 'w', encoding='utf-8') as f:
    f.write('const trailData = ')
    json.dump(geojson, f, indent=4)
    f.write(';\n')

print(f"Database built with {len(waypoints)} heritage sites.")
print("trail_data.js exported successfully!")
conn.close()
